def validate_phone(phone: str) -> bool:
    return phone.isdigit() and 7 <= len(phone) <= 15