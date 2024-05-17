#!/usr/bin/env python3
"""filtered_logger.py"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Returns the log message with specified fields obfuscated.

    Args:
        fields (List[str]): Fields to obfuscate.
        redaction (str): String to replace the field values.
        message (str): The log line to process.
        separator (str): Character that separates fields in the log line.

    Returns:
        str: The obfuscated log message.
    """
    pattern = '|'.join(f"{field}=[^\\{separator}]*" for field in fields)
    return re.sub(pattern, lambda m: m.group().split('=')[0] + '=' + redaction,
                  message)
