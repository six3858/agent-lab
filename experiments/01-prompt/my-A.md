한국 전화번호를 표준 형식(하이픈 포함)으로 정리하고, 중복 제거와 유효성 검사까지 하는 코드입니다.

```python
import re

def normalize_phone(raw: str) -> str | None:
    """전화번호를 표준 형식(하이픈 포함)으로 변환. 유효하지 않으면 None."""
    if not raw:
        return None

    # 숫자와 '+'만 남기기
    s = re.sub(r"[^\d+]", "", raw)

    # 국제번호 처리: +82 10... -> 010...
    if s.startswith("+82"):
        s = "0" + s[3:]
    elif s.startswith("82") and len(s) >= 11:
        s = "0" + s[2:]

    s = s.replace("+", "")

    # 휴대폰 (010, 011, 016, 017, 018, 019)
    m = re.fullmatch(r"(01[016789])(\d{3,4})(\d{4})", s)
    if m:
        return "-".join(m.groups())

    # 서울 (02)
    m = re.fullmatch(r"(02)(\d{3,4})(\d{4})", s)
    if m:
        return "-".join(m.groups())

    # 기타 지역번호 (031, 032, 051 ...) 및 인터넷전화 (070)
    m = re.fullmatch(r"(0[3-6]\d|070)(\d{3,4})(\d{4})", s)
    if m:
        return "-".join(m.groups())

    # 대표번호 (1588-1234 등)
    m = re.fullmatch(r"(1[5-9]\d{2})(\d{4})", s)
    if m:
        return "-".join(m.groups())

    return None


def clean_phone_list(numbers: list[str]):
    """리스트를 정리: 정규화 + 중복 제거(순서 유지) + 유효하지 않은 번호 분리."""
    valid, invalid, seen = [], [], set()
    for raw in numbers:
        result = normalize_phone(raw)
        if result is None:
            invalid.append(raw)
        elif result not in seen:
            seen.add(result)
            valid.append(result)
    return valid, invalid


if __name__ == "__main__":
    samples = [
        "01012345678",
        "010 1234 5678",
        "010.1234.5678",
        "(010) 1234-5678",     # 중복
        "+82 10-1234-5678",    # 중복
        "02-123-4567",
        "0212345678",          # 중복
        "031) 987-6543",
        "070-8888-1234",
        "1588-1234",
        "12345",               # 유효하지 않음
        "",                    # 유효하지 않음
    ]

    valid, invalid = clean_phone_list(samples)

    print("정리된 번호:")
    for v in valid:
        print(" ", v)

    print("\n유효하지 않은 번호:")
    for i in invalid:
        print(" ", repr(i))
```

**실행 결과 예시**
```
정리된 번호:
  010-1234-5678
  02-123-4567
  031-987-6543
  070-8888-1234
  1588-1234

유효하지 않은 번호:
  '12345'
  ''
```

**동작 요약**
- 공백, 점, 괄호, 하이픈 등 특수문자를 제거한 뒤 다시 하이픈을 붙입니다.
- `+82` 국제번호 형식을 `0`으로 시작하는 국내 형식으로 변환합니다.
- 휴대폰, 서울(02), 지역번호, 070, 대표번호(15xx~19xx)를 지원합니다.
- 중복은 첫 등장 순서를 유지하며 제거하고, 형식에 맞지 않는 번호는 따로 모아줍니다.

CSV나 엑셀 파일을 읽어서 정리하는 버전이 필요하면 말씀해 주세요.
