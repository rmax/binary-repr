from binary_repr import binary_repr, integer_repr


def test_binary_repr():
    assert binary_repr(3) == b'11'
    assert binary_repr(-3) == b'-11'
    assert binary_repr(3, width=4) == b'0011'
    assert binary_repr(-3, width=4) == b'1101'


def test_integer_repr():
    assert integer_repr(b'11') == 3
    assert integer_repr(b'-11') == -3
    assert integer_repr(b'0011') == 3
    assert integer_repr(b'1101', fixed_width=True) == -3
    assert integer_repr(b'1101', fixed_width=False) == 13


def test_both_repr():
    test_nums = [x for x in range(10)]
    test_nums += [0, 12345, 3141590]
    for num in test_nums:
        assert integer_repr(binary_repr(num)) == num
        assert integer_repr(binary_repr(num, width=32), fixed_width=True) == num
        assert integer_repr(binary_repr(-num, width=32), fixed_width=True) == -num
