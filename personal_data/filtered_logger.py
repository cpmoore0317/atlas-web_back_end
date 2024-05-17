#!/usr/bin/env python3
"""filtered_logger.py"""
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): A list of strings representing fields to obfuscate.
        redaction (str): A string representing the value to replace the fields with.
        message (str): A string representing the log line.
        separator (str): A string representing the character separating fields in the log line.

    Returns:
        str: The obfuscated log message.
    """
    for field in fields:
        message = re.sub(f"{field}=[^;]+", f"{field}={redaction}", message)
    return message
