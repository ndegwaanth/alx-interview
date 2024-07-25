#!/usr/bin/env python3
"""0-validate_utf8.py"""


def validUTF8(data):
    """
     determines if a given data set represents
     a valid UTF-8 encoding.
     parameters:
     data: this is the list represents the string
    """
    def is_valid_byte(byte, pattern):
        """
        This check if the byte match the pattern
        parameters:
        byte: bytes that are being checked
        pattern: the paradigm tha it must follow
        return: a boolean either True or False
        """
        return (byte & pattern[0]) == pattern[1]

    # Patterns for UTF-8 encoding:
    # 0xxxxxxx for 1-byte (ASCII)
    # 110xxxxx for 2-byte start
    # 11110xxx for 4-byte start
    # 10xxxxxx for continuation
    patterns = [
        (0b10000000, 0b00000000),
        (0b11100000, 0b11000000),
        (0b11110000, 0b11100000),
        (0b11111000, 0b11110000),
        (0b11000000, 0b10000000)
    ]

    n = len(data)
    i = 0

    while i < n:
        byte = data[i]
        if byte > 255:
            return False

        # Determine the number of bytes in the character
        if is_valid_byte(byte, patterns[0]):
            i += 1
            continue
        elif is_valid_byte(byte, patterns[1]):
            num_bytes = 2
        elif is_valid_byte(byte, patterns[2]):
            num_bytes = 3
        elif is_valid_byte(byte, patterns[3]):
            num_bytes = 4
        else:
            return False

        for j in range(1, num_bytes):
            if i + j >= n or not is_valid_byte(data[i + j], patterns[4]):
                return False

        i += num_bytes

    return True
