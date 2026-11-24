Python 예시입니다.

```python
def is_palindrome(s: str) -> bool:
    # 영문자와 숫자만 남기고 소문자로 변환 (공백·구두점·대소문자 무시)
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]
```

사용 예:

```python
print(is_palindrome("level"))                            # True
print(is_palindrome("A man, a plan, a canal: Panama"))   # True
print(is_palindrome("hello"))                            # False
print(is_palindrome(""))                                 # True
```

- 공백, 구두점, 대소문자는 무시합니다. 엄격하게 비교하려면 `s == s[::-1]`만 쓰면 됩니다.
- `isalnum()`은 한글도 문자로 인식하므로 "다시마시다" 같은 한글 팰린드롬도 동작합니다.
- 시간 복잡도는 O(n)입니다.

다른 언어(JavaScript, Java 등)로도 필요하시면 말씀해 주세요.
