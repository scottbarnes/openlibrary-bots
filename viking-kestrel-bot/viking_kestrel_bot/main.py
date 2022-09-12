from __future__ import annotations

import json
import re
from collections.abc import Iterator
from itertools import chain, islice
from pathlib import Path
from typing import Any

import requests
from jsondiff import diff
from olclient.openlibrary import OpenLibrary
from viking_kestrel_bot.constants import (
    BASE_SEARCH_URL,
    QUERY,
    SERIES_PHRASE,
    TITLE_PHRASE,
)


def get_ol_ids_from_dict(query_dict: dict) -> Iterator[str]:
    """
    Extract Open Library Edition IDs from a dictionary as created from a JSON blob as
    returned by a title search for everything with the fields key and title. E.g.
    https://testing.openlibrary.org/search.json?q=title%3A+%22Viking%22&mode=everything&fields=key,title  # noqa E501
    """

    docs: list[dict] = query_dict.get("docs", None)
    if docs is None:
        raise TypeError(f"The 'docs' key is None: {query_dict}")

    # Perhaps this is better to do with glom: https://glom.readthedocs.io/en/latest/
    def get_nested_editions(docs: list[dict]) -> Iterator[str]:
        """
        Pull Open Library IDs out of nested dictionaries and lists. The data is
        quite nested. For an example of the data schema, see:
        `tests/sample_query_response.json`

        Returns an iterator similar to iter(['OL9688593M', ..., 'OL27004810M'])
        """
        works: Iterator[dict] = (work for work in docs if work is not None)
        editions: Iterator = (
            work.get("editions") for work in works if work is not None
        )
        edition_docs: Iterator = (
            edition.get("docs") for edition in editions if edition is not None
        )
        flattened_edition_docs: Iterator = chain.from_iterable(edition_docs)
        nominal_edition_ids: Iterator = (
            doc.get("key", "").split("/")[-1]
            for doc in flattened_edition_docs
            if doc.get("key", "") != ""
        )

        return nominal_edition_ids

    nominal_edition_ids = get_nested_editions(docs)

    # This reads the JSON a second time, but it seemed cleaner to read than a loop that
    # does both simultaneously.
    nominal_work_ids: Iterator[str] = (
        item.get("key", "").split("/")[-1] for item in docs if item.get("key", "") != ""
    )

    return chain(nominal_work_ids, nominal_edition_ids)


def has_title_phrase(title: str, title_phrase: str) -> bool:
    """Returns True if {title} has {title_phrase} and False otherwise."""
    pattern = re.escape(title_phrase)
    pattern = re.compile(pattern, re.IGNORECASE)
    return re.search(pattern, title) is not None


def remove_title_phrase_from_title(title: str, title_phrase: str) -> str:
    """
    If {title_phrase} is present in {title}, return {title} stripped and without
    {title_phrase}. Otherwise just return the original title.
    """
    pattern = re.escape(title_phrase)
    pattern = re.compile(pattern, re.IGNORECASE)
    sub = re.sub(pattern, "", title)
    return sub.strip()


# TODO: Type 'Edition' properly.
def process_edition(
    edition: Any, title_phrase: str, series_phrase: str
) -> tuple[Any, bool]:  # Returns an Edition.
    """
    If necessary, remove {tile_phrase} from {edition}'s title and add {series_phrase}
    to the edition's series.
    """
    needs_updating = False
    before = edition.json()

    if has_title_phrase(edition.title, title_phrase):
        edition.title = remove_title_phrase_from_title(edition.title, title_phrase)

        # Only update the series if the title is updated.
        try:
            edition.series
        except AttributeError:
            edition.series = []

        if series_phrase not in edition.series:
            edition.series.append(series_phrase)

        needs_updating = True

    after = edition.json()
    if changes := diff(before, after):
        print(f'Changing {edition.olid} from "{before.get("title")}" to {changes}')

    return (edition, needs_updating)


def process_work(work: Any, title_phrase: str) -> tuple[Any, bool]:  # Returns a work.
    """
    Remove {title_phrase} from {work}'s title if necessary.
    """
    needs_updating = False
    before = work.json()

    if has_title_phrase(work.title, title_phrase):
        work.title = remove_title_phrase_from_title(work.title, title_phrase)
        needs_updating = True

    after = work.json()
    if changes := diff(before, after):
        print(f'Changing {work.olid} from "{before.get("title")}" to {changes}')

    return (work, needs_updating)


def main(
    title_phrase: str, series_phrase: str, live: bool = False, end: int | None = 1
) -> None:
    """Run everything."""

    ol = OpenLibrary(base_url="https://testing.openlibrary.org")
    # sample_query_response = Path("./tests/sample_query_response.json")
    # query_dict = {}
    # with sample_query_response.open(mode="r") as fp:
    #     query_dict = json.load(fp)

    r = requests.get(BASE_SEARCH_URL + QUERY)
    query_dict = r.json()

    # Update the title/series as needed.
    for openlibrary_id in islice(set(get_ol_ids_from_dict(query_dict)), end):

        # Editions
        if openlibrary_id.endswith("M"):
            edition = ol.Edition.get(openlibrary_id)
            if not edition:
                raise TypeError(f"Edition {openlibrary_id} returned None.")

            edition, needs_saving = process_edition(
                edition, title_phrase, series_phrase
            )
            if needs_saving and live:
                # edition.save()
                pass

        # Works
        elif openlibrary_id.endswith("W"):
            work = ol.Work.get(openlibrary_id)
            if not work:
                raise TypeError(f"Work {openlibrary_id} returned None.")

            work, needs_saving = process_work(work, title_phrase)
            if needs_saving and live:
                # work.save()
                pass


# only main() is used in collab.
if __name__ == "__main__":
    main(TITLE_PHRASE, SERIES_PHRASE, live=False, end=None)
