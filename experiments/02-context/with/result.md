[확인] 문자열이 팰린드롬인지 확인하는 함수를 파일 없이 답변으로만 보여달라는 요청입니다.

```python
import re
import pytest


def is_palindrome(text: str) -> bool:
    """영문자와 숫자만 비교해 대소문자 무시 팰린드롬 여부를 반환한다."""
    cleaned: str = re.sub(r"[^0-9a-zA-Z가-힣]", "", text).lower()
    return cleaned == cleaned[::-1]


@pytest.mark.parametrize(
    "text, expected",
    [
        ("level", True),
        ("A man, a plan, a canal: Panama", True),
        ("hello", False),
        ("", True),
        ("기러기", True),
    ],
)
def test_is_palindrome(text: str, expected: bool) -> None:
    """is_palindrome이 다양한 입력에서 기대값을 반환하는지 검증한다."""
    assert is_palindrome(text) is expected
```

공백·구두점·대소문자를 무시하고 앞뒤로 뒤집어 비교하며, 한글도 처리합니다. 표준 라이브러리(`re`)만 사용했고 테스트는 pytest 형식입니다.

다음 단계 제안: 유니코드 정규화(`unicodedata`)나 투 포인터 방식으로 메모리를 줄인 버전을 추가해 볼까요?
