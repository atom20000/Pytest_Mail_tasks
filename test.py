import pytest
class TestTuple:

    @pytest.mark.parametrize(
        'test_input, expected',
        [
            ([False, True, False], (0, 1, 0)),
            ([[1,3,4,7],' '.join(['Hello','World']),2,6], ([1,3,4,7],'Hello World',2,6)),
            ('Galaktionov',('G','a','l','a','k','t','i','o','n','o','v')) # Посто стеб над одногруппником 
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

class TestDictionary:

    def test_assigning_dictionary_and_accessing_non_existent_key(self):
        dict_one = {1 : 'Give', 2 : 'me', 3 : 'my', 4 : 'money'}
        dict_two = dict_one
        dict_one.pop(1)
        try:
             assert dict_two[1] == 'Give'
        except KeyError:
            assert dict_two == {2 : 'me', 3 : 'my', 4 : 'money'}
    
    def test_unimportance_of_order(self):
        dict_one = {
            'Цой': 'Жив!',
            3 : 76546,
            (1,2) : {1:1,2:2},
            "в наших сердцах" : 'Всегда'
        }
        dict_two = {
            'Цой': 'Жив!',
            "в наших сердцах" : 'Всегда',
            3 : 76546,
            (1,2) : {1:1,2:2}
        }
        assert dict_one == dict_two

    @pytest.mark.parametrize(
        'test_input, expected',
        [
            ([('python', '3'+'.9'), ('VS', 'Code')], {'VS' : 'Code', 'python': '3.9'}),
            (zip((1,2,3),('water','world','film')), {1 : 'water',2:'world', 3:'film'}),
            ([(1,1),(2,4),(3,9)], {i : i**2 for i in range(1,4)})
        ]
    )
    def test_creation_dict_with_different_input_data(self, test_input, expected):
        assert dict(test_input) == expected

    