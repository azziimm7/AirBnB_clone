#!/usr/bin/python3
"""
This script contains unittests for the User subclass in the models package.
    file: AirBnB_clone/models/user.py

It tests various aspects of the User class, including:
    - inheritance.
    - initialization.
    - methods.
    - instances.
    - edge cases.
    - comparisons between instances in different models.
"""

import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class TestUserInheritance(unittest.TestCase):
    """Test cases for inheritance from the BaseModel class"""

    def setUp(self):
        self.user = User()

    def test_inheritance(self):
        self.assertIsInstance(self.user, BaseModel)


class TestUserInitialization(unittest.TestCase):
    """Test cases for initializing the User class"""

    def setUp(self):
        self.user = User()

    def test_id_generation(self):
        self.assertIsNotNone(self.user.id)
        self.assertIsInstance(self.user.id, str)

    def test_timestamps_initialized(self):
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            User(created_at="2024-04-04 4:00:00")

    def test_email_initialization(self):
        self.assertIsInstance(self.user.email, str)

    def test_password_initialization(self):
        self.assertIsInstance(self.user.password, str)

    def test_first_name_initialization(self):
        self.assertIsInstance(self.user.first_name, str)

    def test_last_name_initialization(self):
        self.assertIsInstance(self.user.last_name, str)


class TestUserMethods(unittest.TestCase):
    """Test cases for methods of the User class"""

    def setUp(self):
        self.user = User()

    def test_str_method(self):
        str_rep = "[User] ({}) {}".format(
            self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), str_rep)

    def test_save_method(self):
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)

    def test_save_method_with_none(self):
        with self.assertRaises(TypeError):
            self.user.save(None)

    def test_to_dict_method(self):
        obj_dict = self.user.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "User")
        self.assertIsInstance(
            datetime.fromisoformat(obj_dict["created_at"]), datetime)
        self.assertIsInstance(
            datetime.fromisoformat(obj_dict["updated_at"]), datetime)

    def test_to_dict_with_none(self):
        with self.assertRaises(TypeError):
            self.user.to_dict(None)


class TestUserInstances(unittest.TestCase):
    """Test cases for instances of the User class"""

    def setUp(self):
        self.first_model = User()
        self.second_model = User()

    def test_equality(self):
        self.assertEqual(self.first_model, self.first_model)
        self.assertNotEqual(self.first_model, self.second_model)

    def test_unused_args(self):
        mymodel = User(None)
        self.assertNotIn(None, mymodel.__dict__.values())

    def test_with_args_and_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        mymodel = User(
                "13", id="1307966120652",
                created_at=date_iso, updated_at=date_iso,
                email="brad@gmail.com", password="zeronine$@1",
                first_name="Grand", last_name="Child"
                )
        self.assertEqual(mymodel.id, "1307966120652")
        self.assertEqual(mymodel.created_at, date)
        self.assertEqual(mymodel.updated_at, date)
        self.assertEqual(mymodel.email, "brad@gmail.com")
        self.assertEqual(mymodel.password, "zeronine$@1")
        self.assertEqual(mymodel.first_name, "Grand")
        self.assertEqual(mymodel.last_name, "Child")

    def test_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(
                    id=None, created_at=None, updated_at=None,
                    email=None, password=None,
                    first_name=None, last_name=None
                    )

    def test_serialization_and_deserialization(self):
        obj_dict = self.first_model.to_dict()
        for key, value in obj_dict.items():
            self.assertIsInstance(value, str)
        new_model = User(**obj_dict)
        self.assertEqual(new_model.to_dict(), obj_dict)


class TestUserEdgeCases(unittest.TestCase):
    """Test cases for edge cases of the User class"""

    def test_empty_instance_creation(self):
        empty_user = User()
        self.assertIsNotNone(empty_user.id)
        self.assertIsInstance(empty_user.created_at, datetime)
        self.assertIsInstance(empty_user.updated_at, datetime)

    def test_attribute_edge_cases(self):
        myuser = User(
            empty_string_attr="", none_attr=None,
            special_chars_attr="!@##^#$%^&*()"
            )
        self.assertEqual(myuser.empty_string_attr, "")
        self.assertIsNone(myuser.none_attr)
        self.assertEqual(myuser.special_chars_attr, "!@##^#$%^&*()")


class TestUserDifferentModels(unittest.TestCase):
    """Test cases for unique instances in different User class models"""

    def setUp(self):
        self.first_model = User()
        self.second_model = User()

    def test_unique_ids(self):
        self.assertNotEqual(self.first_model.id, self.second_model.id)

    def test_different_created_at(self):
        self.assertLess(
                self.first_model.created_at, self.second_model.created_at
                )

    def test_different_updated_at(self):
        self.assertLess(
                self.first_model.updated_at, self.second_model.updated_at
                )


if __name__ == '__main__':
    unittest.main()
