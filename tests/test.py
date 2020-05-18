import unittest

from markov_algorithm import interpret, parse


class Test(unittest.TestCase):
    def test_increment_7(self):
        code = """
        $1:1$
        $0:0$
        $:+
        0+::1
        1+:+0
        +::1
        :$
        """
        data = "1010101110111"
        expected = "1010101111000"
        self.assertEqual(interpret(code, data), expected)

    def test_min_digit_14(self):
        code = """
        5<:<
        4<:<
        >5:>
        >4:>
        <:
        >::
        1:544444444444444445
        2:5444444444444444445
        3:54444444444444444445
        544444444444444445:<1>
        5444444444444444445:<2>
        54444444444444444445:<3>
        4:<4>
        5:<5>
        """
        data = "5434543524"
        expected = "2"
        self.assertEqual(interpret(code, data), expected)
