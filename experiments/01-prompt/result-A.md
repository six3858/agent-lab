한국 전화번호를 하이픈 형식으로 통일하는 코드입니다. 휴대폰, 서울(02), 지역번호, 대표번호(1588 등), `+82` 국제 형식도 처리합니다.

```python
import re


def normalize_phone(raw: str) -> str | None:
    """한국 전화번호를 하이픈 형식으로 정리. 유효하지 않으면 None 반환."""
    digits = re.sub(r"\D", "", raw)          # 숫자만 남김

    # 국제 형식 처리: +82 10-1234-5678 / 82-2-123-4567 -> 0으로 시작하게
    if digits.startswith("82"):
        digits = "0" + digits[2:]
    # "+82 (0)10..." 처럼 0이 중복된 경우
    if digits.startswith("00"):
        digits = digits[1:]

    # 대표번호: 1588-1234 (8자리)
    if re.fullmatch(r"1[5-9]\d{2}\d{4}", digits):
        return f"{digits[:4]}-{digits[4:]}"

    # 서울 (02)
    if digits.startswith("02"):
        if len(digits) == 9:      # 02-123-4567
            return f"{digits[:2]}-{digits[2:5]}-{digits[5:]}"
        if len(digits) == 10:     # 02-1234-5678
            return f"{digits[:2]}-{digits[2:6]}-{digits[6:]}"
        return None

    # 휴대폰 / 지역번호 / 050x / 070 등 (3자리 국번)
    if re.match(r"0\d{2}", digits):
        if len(digits) == 10:     # 010-123-4567, 031-123-4567
            return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
        if len(digits) == 11:     # 010-1234-5678, 031-1234-5678
            return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"

    return None


def clean_phone_list(numbers: list[str]) -> tuple[list[str], list[str]]:
    """목록을 정리하고 중복을 제거. (정상 목록, 오류 목록) 반환."""
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
        "+82 10-1234-5678",
        "(02) 123-4567",
        "0212345678",
        "031)123-4567",
        "1588-1234",
        "070-8888-9999",
        "010-1234-5678",   # 중복
        "12345",           # 오류
    ]

    ok, bad = clean_phone_list(samples)
    print("정상:")
    for n in ok:
        print("  ", n)
    print("오류:", bad)
```

**실행 결과 예상**
```
정상:
   010-1234-5678
   02-123-4567
   031-123-4567
   1588-1234
   070-8888-9999
오류: ['12345']
```

**동작 요약**
- 공백, 점, 괄호, 하이픈 등 숫자가 아닌 문자를 모두 제거한 뒤 자릿수로 형식을 판단합니다.
- 정리 후 같은 번호는 중복으로 보고 한 번만 남깁니다.
- 형식에 맞지 않는 번호는 `None`을 반환하고, 목록 함수에서는 오류 목록으로 따로 모읍니다.

CSV나 엑셀 파일의 전화번호 열을 일괄 정리하는 버전이 필요하면 말씀해 주세요.
