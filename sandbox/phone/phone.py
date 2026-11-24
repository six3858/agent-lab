import re


def normalize_phone(raw: str) -> str | None:
    if not isinstance(raw, str):
        return None
    s = raw.strip()
    # 허용 문자 외(문자 등)가 섞이면 무효
    if not s or re.search(r"[^\d\s\-.()+]", s):
        return None
    digits = re.sub(r"\D", "", s)
    # 국가번호 처리: +82 / 82 -> 0
    if s.startswith("+"):
        if not digits.startswith("82"):
            return None
        digits = "0" + digits[2:]
    if re.fullmatch(r"010\d{8}", digits):
        return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"
    if re.fullmatch(r"02\d{7,8}", digits):
        return f"02-{digits[2:-4]}-{digits[-4:]}"
    return None


if __name__ == "__main__":
    import sys

    for arg in sys.argv[1:]:
        print(f"{arg!r} -> {normalize_phone(arg)!r}")
