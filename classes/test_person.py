import unittest
from unittest.mock import patch

from oop import Person


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        # before each test
        print("set up")
        self.person_1 = Person("Tony", "Stark", 64)

    def tearDown(self) -> None:
        # after each test
        print("tear down")

    @classmethod
    def setUpClass(cls) -> None:
        # before class
        print("set up class")

    @classmethod
    def tearDownClass(cls) -> None:
        # after class
        print("tear down class")

    def test_full_name(self):
        self.assertEqual(self.person_1.fullname, "Tony Stark")

        self.person_1.fullname = "Tony Potts"
        self.assertEqual(self.person_1.fullname, "Tony Potts")

    def test_social(self):
        with patch('oop.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            social = self.person_1.social()
            mocked_get.assert_called_once_with(f"http://youtube.com/Tony+Stark")
            self.assertEqual(social, "Success")

        with patch('oop.requests.get') as mocked_get:
            mocked_get.return_value.ok = False

            social = self.person_1.social()
            mocked_get.assert_called_once_with(f"http://youtube.com/Tony+Stark")
            self.assertEqual(social, "Bad Response!")
