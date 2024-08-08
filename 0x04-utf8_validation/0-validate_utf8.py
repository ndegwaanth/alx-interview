#!/usr/bin/python3
'''utf-8validation
'''
import re
from typing import List


def to_binary(n: int) -> str:
    '''Converts an integer to its 8-bit binary representation'''
    bin_rep = bin(n)[2:]
    if len(bin_rep) > 8:
        bin_rep = bin_rep[-8:]
    return bin_rep.zfill(8)


def determine_type(bin_str: str) -> int:
    '''Determines the type of UTF-8 encoding based on binary string'''
    if re.match(r"^0[01]{7}$", bin_str):
        return 1
    elif re.match(r"^110[01]{5}$", bin_str):
        return 2
    elif re.match(r"^1110[01]{4}$", bin_str):
        return 3
    elif re.match(r"^11110[01]{3}$", bin_str):
        return 4
    return -1


def validate_continuation_byte(data: List[int]) -> bool:
    '''Validates that the next byte is a valid continuation byte'''
    if not data:
        return False
    byte = data.pop(0)
    return re.match(r"^10[01]{6}$", to_binary(byte)) is not None


def validUTF8(data: List[int]) -> bool:
    '''
    Determines if a given data set represents a valid UTF-8 encoding'''
    while data:
        byte = data.pop(0)
        if byte > 255:
            return False
        bin_byte = to_binary(byte)
        byte_type = determine_type(bin_byte)
        if byte_type == 1:
            continue
        elif byte_type > 1:
            for _ in range(byte_type - 1):
                if not validate_continuation_byte(data):
                    return False
        else:
            return False
    return True
