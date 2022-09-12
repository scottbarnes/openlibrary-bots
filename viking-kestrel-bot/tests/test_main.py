import json
from pathlib import Path

import pytest
import requests
from olclient.openlibrary import OpenLibrary
from viking_kestrel_bot.constants import (
    EDITION_DOES_NOT_NEED_UPDATING,
    EDITION_POST_PROCESSED,
    SERIES_PHRASE,
    TITLE_PHRASE,
    WORK_DOES_NOT_NEED_UPDATING,
    WORK_POST_PROCESSED,
)
from viking_kestrel_bot.main import (
    get_ol_ids_from_dict,
    has_title_phrase,
    process_edition,
    process_work,
    remove_title_phrase_from_title,
)


@pytest.fixture(scope="session")
def setup_ol():
    """Get an OpenLibrary connection to use as necessary. Yes, this isn't a mock."""
    ol = OpenLibrary(base_url="https://testing.openlibrary.org")
    yield ol


# def test_can_probably_get_json():
#     """Just looks for a response < 400. Doesn't actually verify JSON"""
#     response = requests.get(BASE_SEARCH_URL + QUERY)
#     assert response.ok is True


def test_get_ol_ids_from_dict():
    file = Path("./tests/sample_query_response.json")
    with file.open(mode="r") as fp:
        data = json.load(fp)
        # Nominal works are read first, then nominal editions.
        assert list(get_ol_ids_from_dict(data)) == [
            "OL807816W",
            "OL11068833M",
            "OL19793284W",
            "OL106035W",
            "OL9688593M",
            "OL11068833M",
            "OL27004810M",
            "OL11069040M",
        ]


def test_has_title_phrase_finds_the_title_phrase():
    title = "Blinks (Viking Kestrel Picture Books)"
    title_phrase = "(Viking Kestrel Picture Books)"
    assert has_title_phrase(title, title_phrase) is True


def test_has_title_phrase_ignores_non_matching_titles():
    title = "Blinks Viking Kestrel Picture Books"
    title_phrase = "(Viking Kestrel Picture Books)"
    assert has_title_phrase(title, title_phrase) is False


def test_remove_title_phrase_from_title_removes_the_title_phrase():
    title = "Blinks (Viking Kestrel Picture Books)"
    title_phrase = "(Viking Kestrel Picture Books)"
    parsed_title = "Blinks"
    assert remove_title_phrase_from_title(title, title_phrase) == parsed_title


def test_remove_title_phrase_from_title_ignores_non_matching_titles():
    title = "Blinks Viking Kestrel Picture Books"
    title_phrase = "(Viking Kestrel Picture Books)"
    assert remove_title_phrase_from_title(title, title_phrase) == title


# TODO: This should be mocked. Dumb to use testing.openlibrary.org.
def test_process_edition_that_needs_updating(setup_ol):
    ol = setup_ol
    book = ol.Edition.get("OL11068833M")
    processed_book, needs_updating = process_edition(book, TITLE_PHRASE, SERIES_PHRASE)
    print(processed_book.json())
    assert processed_book.json() == EDITION_POST_PROCESSED
    assert needs_updating is True


def test_process_edition_that_does_not_need_updating(setup_ol):
    ol = setup_ol
    book = ol.Edition.get("OL22879676M")
    processed_edition, needs_updating = process_edition(
        book, TITLE_PHRASE, SERIES_PHRASE
    )
    assert needs_updating is False
    assert processed_edition.json() == EDITION_DOES_NOT_NEED_UPDATING


def test_process_work_that_needs_updating(setup_ol):
    ol = setup_ol
    work = ol.Work.get("OL19793284W")
    processed_work, needs_updating = process_work(work, TITLE_PHRASE)
    print(processed_work.json())
    assert processed_work.json() == WORK_POST_PROCESSED
    assert needs_updating is True


def test_process_work_that_does_not_need_updating(setup_ol):
    ol = setup_ol
    work = ol.Work.get("OL807816W")
    processed_work, needs_updating = process_work(work, TITLE_PHRASE)
    print(processed_work.json())
    assert processed_work.json() == WORK_DOES_NOT_NEED_UPDATING
    assert needs_updating is False
