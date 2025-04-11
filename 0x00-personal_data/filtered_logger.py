#!/usr/bin/env python3
""" filter logger"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscate specified fields in a log message.
    Args:
        fields: List of field names to obfuscate
        redaction: String to replace field values with
        message: The log message to process
        separator: Character separating fields in the log message
    Returns:
        The obfuscated log message
    """

    pattern = f'({"|".join(fields)})=[^{separator}]*'
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
