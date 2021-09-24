import pytest
class TestTuple:

    @pytest.mark.parametrize(
        'test_input, expected',
        [
            ([False, True, False], (0, 1, 0)),
            ([[1,3,4,7],' '.join(['Hello','World']),2,6], ([1,3,4,7],'Hello World',2,6))
        ]
    )
    def test_creation_tuples_with_different_input_data(self, test_input, expected):
        assert tuple(test_input) == expected

    def test_add_element_to_tuple(self):
        tuple_ = tuple([[1], 1000, '3'])
        try:
            tuple_[3] = 'Python'
        except TypeError:
            assert tuple_ == ([1], 1000, '3')

    def test_importance_of_order(self):
        tuple_one = (True, 'tuple', 5, [1,2,3,4])
        tuple_two = (5, 'tuple', [1,2,3,4], True)
        assert tuple_one != tuple_two