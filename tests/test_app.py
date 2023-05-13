import pytest

from app import TRIGGER_WORDS, do_i_care


@pytest.mark.parametrize(
    "test_message, expected_response",
    [(trigger_word, True) for trigger_word in TRIGGER_WORDS]
    + [
        ("sources is cool", True),
        ("the sources is cool", True),
        ("bront is this in the sources", True),
        ("resources", False),
        ("resources is cool", False),
        ("the resources is cool", False),
        ("bront is this in the resources", False),
        (None, False),
        ("", False),
        (" ", False),
    ],
)
def test_do_i_care(test_message, expected_response):
    assert do_i_care(test_message) is expected_response
