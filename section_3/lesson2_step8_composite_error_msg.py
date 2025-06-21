def test_input_text(expected_result, actual_result):

    assert expected_result == actual_result, \
            f'expected {expected_result}, got {actual_result}'


if __name__ == '__main__':
    test_input_text(8, 11)
