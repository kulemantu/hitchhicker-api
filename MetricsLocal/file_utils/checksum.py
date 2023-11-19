"""
checksum.py
-----------
This module provides functions to generate and validate MD5 checksums.

Example Usage:
--------------
from checksum import generate_checksum, validate_checksum

data = "Hello, World!"
checksum = generate_checksum(data)

print("Checksum:", checksum)
print("Is valid:", validate_checksum(data, checksum))
"""

import hashlib

def generate_checksum(data):
    """
    Generate an MD5 checksum for a given string.

    Parameters:
    data (str): The string for which the checksum is to be generated.

    Returns:
    str: The generated hexadecimal MD5 checksum.
    """
    return hashlib.md5(data.encode()).hexdigest()

def validate_checksum(data, checksum):
    """
    Validate a string against an MD5 checksum.

    Parameters:
    data (str): The string to validate.
    checksum (str): The MD5 checksum to validate against.

    Returns:
    bool: True if the generated checksum of the data matches the provided checksum, False otherwise.
    """
    return generate_checksum(data) == checksum
