파일 쓰기와 실행 권한이 승인되지 않아 `phone.py`를 만들지 못했고, 코드는 실행해 보지 못했습니다. 아래 코드를 `D:\agent-lab\experiments\01-prompt\phone.py`로 저장해 주세요. 권한을 허용해 주시면 제가 직접 저장하고 테스트하겠습니다.

```python
import re


def normalize_phone(raw: str) -> str | None:
    """한국 전화번호를 하이픈 형식(010-1234-5678)으로 정규화한다. 유효하지 않으면 None."""
    if not isinstance(raw, str):
        return None
    s = raw.strip()
    if not s or not re.fullmatch(r"[+\d\s\-().]+", s):
        return None

    digits = re.sub(r"\D", "", s)
    if s.startswith("+"):
        if not digits.startswith("82"):
            return None
        digits = "0" + digits[2:].lstrip("0")   # +82 (0)10... 도 허용
    elif digits.startswith("82") and len(digits) >= 11:
        digits = "0" + digits[2:]

    for pat in (r"(01[016789])(\d{3,4})(\d{4})",       # 휴대폰
                r"(02)(\d{3,4})(\d{4})",               # 서울
                r"(0[3-6]\d|070)(\d{3,4})(\d{4})"):    # 지역번호/인터넷전화
        m = re.fullmatch(pat, digits)
        if m:
            return "-".join(m.groups())
    return None
```

기대 결과는 다음과 같습니다. 실행해서 확인한 값은 아닙니다.
- `010-1234-5678`은 `010-1234-5678`이 됩니다.
- `01012345678`은 `010-1234-5678`이 됩니다.
- `+82 10-1234-5678`은 `010-1234-5678`이 됩니다.
- `+82`처럼 번호 없이 국가번호만 있는 입력, 빈 문자열, 문자가 섞인 입력은 `None`이 됩니다.

확인이 필요한 가정은 다음과 같습니다.
1. **표준 형식**: 하이픈 포함 국내 형식(`010-1234-5678`)으로 정했습니다. E.164(`+821012345678`)나 숫자만 남기는 형식이 필요하면 알려 주세요.
2. **`+82` 입력**: 요구사항이 잘려 있어 국가번호 표기로 해석했습니다. 다른 의도였다면 알려 주세요.
3. **검증 범위**: 국내 번호(휴대폰, 서울, 지역번호, 070)만 인정합니다.
