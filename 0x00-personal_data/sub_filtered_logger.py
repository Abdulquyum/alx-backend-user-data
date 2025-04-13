#!/usr/bin/env python3
""" filter logger"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Obfuscate specified fields in a log message.
    
    Args:
        fields: List of field names to obfuscate
        redaction: String to replace field values with
        message: The log message to process
        separator: Character separating fields in the log message
        
    Returns:
        The obfuscated log message
    """


    field_pattern = '|'.join(fields)
    pattern = f'({field_pattern})=[^{separator}]*'
        
    # Replace each matched field with the field name and redaction string
    def replace_match(match):
        field_name = match.group(1)  # Get the field name that was matched
        return f"{field_name}={redaction}"
        
    # Apply the replacement to the entire message
    return re.sub(pattern, replace_match, message) 