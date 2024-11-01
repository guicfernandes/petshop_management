import os
import re
import sys


def format_phone_number(phone: str) -> str:
    """Format a phone number to (XX)XXXXX-XXXX or (XX)9XXXX-XXXX

    Args:
        phone (str): Phone number to be formatted

    Returns:
        str: Formatted phone number
    """
    # Remove all non-digit characters
    digits = re.sub(r"\D", "", phone)
    # Format the number to (XX)XXXXX-XXXX
    if len(digits) == 11:
        return f"({digits[:2]}){digits[2:7]}-{digits[7:]}"
    # Format the number to (XX)9XXXX-XXXX
    if len(digits) == 10:
        return f"({digits[:2]})9{digits[2:6]}-{digits[6:]}"
    return phone  # Return the original if it doesn't match the expected length
