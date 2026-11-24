```python
import re

def normalize_phone(raw: str) -> str | None:
    if not isinstance(raw, str):
        return None
    s = raw.strip()
    # 허용 문자 외(문자 등)가 섞이면 무효
    if not s or re.search(r"[^\d\s\-.()+]", s):
        return None
    digits = re.sub(r"\D", "", s)
    # 국가번호 처리: +82 / 82 → 0
    if s.startswith("+"):
        if not digits.startswith("82"):
            return None
        digits = "0" + digits[2:]
    if re.fullmatch(r"010\d{8}", digits):
        return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"
    if re.fullmatch(r"02\d{7,8}", digits):
        return f"02-{digits[2:-4]}-{digits[-4:]}"
    return None
```

```python
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
```

- `+82` 접두는 앞의 0을 복원해 처리하고, 허용되지 않는 문자·자리수 오류·비문자열 입력은 모두 `None`을 반환합니다.
- 휴대폰은 `010`+8자리만 허용하고, 서울(02)은 총 9~10자리(국번 3~4자리)만 허용합니다.
- 테스트는 정상 6건 + 비정상 7건이며, 코드는 `phone.py`에 있다고 가정했습니다(실행은 하지 않았습니다).
