def test_substring(full_string, substring):
    """Check if substring is in the full string."""

    assert full_string.find(substring) != -1, \
        f"expected '{substring}' to be substring of '{full_string}'"


if __name__ == '__main__':
    test_substring('1', '1')
    test_substring('fulltext', 'some_value')
