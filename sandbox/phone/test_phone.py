import pytest
from phone import normalize_phone


@pytest.mark.parametrize("raw, expected", [
    ("010-1234-5678", "010-1234-5678"),
    ("01012345678", "010-1234-5678"),
    ("+82 10 1234 5678", "010-1234-5678"),
    ("010.1234.5678", "010-1234-5678"),
    ("02-123-4567", "02-123-4567"),
    ("02-1234-5678", "02-1234-5678"),
])
def test_valid(raw, expected):
    assert normalize_phone(raw) == expected


@pytest.mark.parametrize("raw", ["", "abc", "010-1234-567", "010-1234-56789", "02-12-345", "+1 010 1234 5678", None])
def test_invalid_returns_none(raw):
    assert normalize_phone(raw) is None
