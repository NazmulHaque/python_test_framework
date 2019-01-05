from tests.base import FunctionalTest


class SampleTest(FunctionalTest):

    def test_number_equality(self):
        '''
        Test equality of two numbers
        :return:
        '''
        assert 3 == 3, 'this is a message is assertion fails'

    def assert_uppercase(self, _str):
        assert _str.isupper(), _str

    def test_string_case(self):
        '''
        Test if string is in upper case
        :return:
        '''
        test_strings = ['NAZMUL', 'RASHED', 'MARIFA']

        for s in test_strings:
            self.assert_uppercase(s)
