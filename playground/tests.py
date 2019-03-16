import unittest


class TestPython(unittest.TestCase):
    def test_float_to_int_coercion(self):
        self.assertEqual(1, int(1.0))

    def test_get_empty_dict(self):
        self.assertIsNone({}.get('key'))

    def test_trueness(self):
        self.assertTrue(bool(10))

    def test_integer_division(self):
        self.assertIs(10 / 5, 2)

        """(venv) >python -m unittest tests.py
            ..F.
            ======================================================================
            FAIL: test_integer_division (tests.TestPython)
            ----------------------------------------------------------------------
            Traceback (most recent call last):
              File "tests.py", line 14, in test_integer_division
                self.assertIs(10 / 5, 2)
            AssertionError: 2.0 is not 2

            ----------------------------------------------------------------------
            Ran 4 tests in 0.001s

            FAILED (failures=1)
        """
