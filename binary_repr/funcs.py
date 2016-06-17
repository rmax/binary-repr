"""Functions to convert integers to binary strings and viceversa."""

_lookup = {
    b'0': b'0000',
    b'1': b'0001',
    b'2': b'0010',
    b'3': b'0011',
    b'4': b'0100',
    b'5': b'0101',
    b'6': b'0110',
    b'7': b'0111',
    b'8': b'1000',
    b'9': b'1001',
    b'a': b'1010',
    b'b': b'1011',
    b'c': b'1100',
    b'd': b'1101',
    b'e': b'1110',
    b'f': b'1111',
    b'A': b'1010',
    b'B': b'1011',
    b'C': b'1100',
    b'D': b'1101',
    b'E': b'1110',
    b'F': b'1111',
    b'L': b'',
}


def binary_repr(num, width=None):
    """binary_repr(num, width=None)

    Converts an integer number to its binary representation.

    For negative numbers, if width is not given, a minus sign is added to the
    front. If width is given, the two's complement of the number is
    returned, with respect to that width.

    Parameters
    ----------
    num : int
        Only an integer decimal number can be used.
    width : int, optional
        The length of the returned string if `num` is positive, the length of
        the two's complement if `num` is negative.

    Returns
    -------
    out : str
        Binary representation of `num` or two's complement of `num`.

    Examples
    --------

    >>> binary_repr(3)
    '11'
    >>> binary_repr(-3)
    '-11'
    >>> binary_repr(3, width=4)
    '0011'

    The two's complement is returned when the input number is negative and
    width is specified:

    >>> binary_repr(-3, width=4)
    '1101'

    """
    # ' <-- unbreak Emacs fontification
    sign = b''
    if num < 0:
        if width is None:
            sign = '-'
            num = -num
        else:
            # replace num with its 2-complement
            num = 2**width + num
    elif num == 0:
        return b'0'*(width or 1)
    ostr = hex(num)
    out = b''.join([_lookup[ch] for ch in ostr[2:]])
    out = out.lstrip(b'0')
    if width is not None:
        out = out.zfill(width)
    return sign + out


def integer_repr(bin_str, fixed_width=False):
    """integer_repr(bin_str, fixed_width=False)

    Converts a binary representation to its integer number.

    Examples
    --------

    >>> integer_repr(b'11')
    3
    >>> integer_repr(b'-11')
    -3
    >>> integer_repr(b'0011')
    3

    The two's complement is returned when negative number with fixed width
    representation is given:

    >>> integer_repr(b'1101', fixed_width=True)
    -3
    >>> integer_repr(b'1101', fixed_width=False)
    13

    """
    # TODO: In C use strtol strtoll
    if fixed_width:
        assert bin_str[0] != '-', "invalid fixed-width binary representation"
        num = int(bin_str, 2)
        if bin_str[0] == '1':
            num -= 2**len(bin_str)
        return num
    else:
        return int(bin_str, 2)
