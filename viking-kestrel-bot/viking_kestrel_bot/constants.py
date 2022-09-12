# Phrase to remove from an edition/work title
TITLE_PHRASE = "(Viking Kestrel Picture Books)"
# Phrase to add to an edition series.
SERIES_PHRASE = "Viking Kestrel Picture Books"

BASE_SEARCH_URL = "https://testing.openlibrary.org/search.json?q="
QUERY = 'title%3A+"Viking+Kestrel+Picture+Books"&mode=everything&fields=key,title'

EDITION_PRE_PROCESSED = {
    "title": "Blinks (Viking Kestrel Picture Books)",
    "authors": [{"key": "/authors/OL23975A"}],
    "publish_date": "March 26, 1987",
    "publishers": ["Viking Children's Books"],
    "created": {"type": "/type/datetime", "value": "2008-04-30T09:38:13.731961"},
    "last_modified": {"type": "/type/datetime", "value": "2011-04-28T10:28:31.661255"},
    "type": {"key": "/type/edition"},
    "isbn_13": ["9780670808595"],
    "edition_name": "Open Market Ed edition",
    "physical_format": "Hardcover",
    "isbn_10": ["0670808598"],
    "latest_revision": 2,
    "oclc_numbers": ["16830585"],
    "contributions": ["R. Avitabile (Illustrator)"],
    "subjects": [
        "English literature: essays, letters & other non-fiction prose works",
        "English literature: literary criticism",
    ],
    "revision": 2,
    "key": "/books/OL11068833M",
    "number_of_pages": 28,
}

EDITION_POST_PROCESSED = {
    "title": "Blinks",
    "authors": [{"key": "/authors/OL23975A"}],
    "publish_date": "March 26, 1987",
    "publishers": ["Viking Children's Books"],
    "created": {"type": "/type/datetime", "value": "2008-04-30T09:38:13.731961"},
    "last_modified": {"type": "/type/datetime", "value": "2011-04-28T10:28:31.661255"},
    "type": {"key": "/type/edition"},
    "isbn_13": ["9780670808595"],
    "edition_name": "Open Market Ed edition",
    "physical_format": "Hardcover",
    "isbn_10": ["0670808598"],
    "latest_revision": 2,
    "oclc_numbers": ["16830585"],
    "contributions": ["R. Avitabile (Illustrator)"],
    "series": ["Viking Kestrel Picture Books"],
    "subjects": [
        "English literature: essays, letters & other non-fiction prose works",
        "English literature: literary criticism",
    ],
    "revision": 2,
    "key": "/books/OL11068833M",
    "number_of_pages": 28,
}

WORK_PRE_PROCESSED = {
    "title": "Big Cat Dreaming (Viking Kestrel Picture Books)",
    "covers": [8597282],
    "key": "/works/OL19793284W",
    "authors": [
        {"type": {"key": "/type/author_role"}, "author": {"key": "/authors/OL31891A"}}
    ],
    "type": {"key": "/type/work"},
    "latest_revision": 2,
    "revision": 2,
    "created": {"type": "/type/datetime", "value": "2019-06-15T03:34:16.319298"},
    "last_modified": {"type": "/type/datetime", "value": "2022-03-22T14:15:07.469343"},
}

WORK_POST_PROCESSED = {
    "title": "Big Cat Dreaming",
    "covers": [8597282],
    "key": "/works/OL19793284W",
    "authors": [
        {"type": {"key": "/type/author_role"}, "author": {"key": "/authors/OL31891A"}}
    ],
    "type": {"key": "/type/work"},
    "latest_revision": 2,
    "revision": 2,
    "created": {"type": "/type/datetime", "value": "2019-06-15T03:34:16.319298"},
    "last_modified": {"type": "/type/datetime", "value": "2022-03-22T14:15:07.469343"},
}


EDITION_DOES_NOT_NEED_UPDATING = {
    "title": "Essays",
    "subtitle": "first series and second series.",
    "authors": [{"key": "/authors/OL18405A"}],
    "publishers": ["T. Nelson"],
    "pagination": "2 v. in 1. :",
    "source_records": ["ia:essaysfirstserie00emer"],
    "series": ["New century library"],
    "created": {"type": "/type/datetime", "value": "2009-01-30T05:21:40.425425"},
    "covers": [6035911],
    "languages": [{"key": "/languages/eng"}],
    "last_modified": {"type": "/type/datetime", "value": "2010-08-12T08:23:44.949532"},
    "latest_revision": 4,
    "publish_country": "nyu",
    "ocaid": "essaysfirstserie00emer",
    "publish_places": ["New York"],
    "type": {"key": "/type/edition"},
    "revision": 4,
    "key": "/books/OL22879676M",
    "works": [{"key": "/works/OL62250W"}],
}

WORK_DOES_NOT_NEED_UPDATING = {
    "description": {
        "type": "/type/text",
        "value": 'Rhymed text and illustrations invite the reader to play "I Spy" with a variety of Mother Goose and other folklore characters',
    },
    "title": "Each Peach Pear Plum",
    "key": "/works/OL807816W",
    "authors": [
        {"author": {"key": "/authors/OL67988A"}, "type": {"key": "/type/author_role"}},
        {"author": {"key": "/authors/OL236925A"}, "type": {"key": "/type/author_role"}},
    ],
    "type": {"key": "/type/work"},
    "subjects": [
        "Children's fiction",
        "Stories in rhyme",
        "Literary recreations",
        "Juvenile fiction",
        "Rhyme",
        "English language",
        "Picture books for children",
        "Juvenile literature",
        "Nursery rhymes",
        "Children's stories",
        "Picture books",
    ],
    "covers": [5375131, 6950322, 6901384, 104680, 402262, 400957],
    "location": "/works/OL807816W",
    "first_sentence": {
        "type": "/type/text",
        "value": "Each Peach Pear Plum I spy Tom Thumb",
    },
    "first_publish_date": "September 1, 1999",
    "latest_revision": 5,
    "revision": 5,
    "created": {"type": "/type/datetime", "value": "2009-12-09T04:33:12.963882"},
    "last_modified": {"type": "/type/datetime", "value": "2022-06-02T16:58:40.919417"},
}
