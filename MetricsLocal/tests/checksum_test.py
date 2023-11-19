import pytest
from checksum import generate_checksum, validate_checksum

def test_generate_checksum():
    data = "Hello, World!"
    expected_checksum = "65a8e27d8879283831b664bd8b7f0ad4"  # Precomputed MD5 checksum of "Hello, World!"
    assert generate_checksum(data) == expected_checksum

def test_validate_checksum():
    data = "Hello, World!"
    valid_checksum = "65a8e27d8879283831b664bd8b7f0ad4"
    invalid_checksum = "1234567890abcdef1234567890abcdef"
    assert validate_checksum(data, valid_checksum)
    assert not validate_checksum(data, invalid_checksum)