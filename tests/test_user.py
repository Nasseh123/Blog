import unittest
from app import db
from app.models import User, Post, Comment, Subscribers


class UserModelTest(unittest.TestCase):
     """
    Test class to test the behaviour of the user class
    """

    def setUp(self):
        """
        Set up password method that will run before every test
        """
        self.new_user = User(password = 'koko')


    def test_password_setter(self):
        """
        Test that makes sure that when generating password the 
        password field is not blank
        """
        self.assertTrue(self.new_user.password is not None)
    
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        """
        Test to make sure that password_hash_checker works
        """
        self.assertTrue(self.new_user.verify_password('koko'))