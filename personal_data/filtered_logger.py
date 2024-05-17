#!/usr/bin/env python3
"""filtered_logger.py"""
import re
from typing import List
import logging

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

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with the fields to redact.

        Args:
            fields (List[str]): List of fields to redact in log messages.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, redacting specified fields.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log message with specified fields redacted.
        """
        original_message = super().format(record)
        redacted_message = filter_datum(self.fields,
                                        self.REDACTION, original_message, self.SEPARATOR)
        return redacted_message
