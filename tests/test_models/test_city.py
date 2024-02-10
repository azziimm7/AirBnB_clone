#!/usr/bin/python3
"""
This script contains unittests for the City subclass in the models package.
    file: AirBnB_clone/models/city.py

It tests various aspects of the City class, including:
    - inheritance.
    - initialization.
    - methods.
    - instances.
    - edge cases.
    - comparisons between instances in different models.
"""

import unittest
from models.base_model import BaseModel
from models.city import City
from datetime import datetime


class TestCityInheritance(unittest.TestCase):
    """Test cases for inheritance from the BaseModel class"""

    def setUp(self):
        self.city = City()

    def test_inheritance(self):
        self.assertIsInstance(self.city, BaseModel)


class TestCityInitialization(unittest.TestCase):
    """Test cases for initializing the City class"""
    def setUp(self):
        self.city = City()

    def test_id_generation(self):
        self.assertIsNotNone(self.city.id)
        self.assertIsInstance(self.city.id, str)

    def test_timestamps_initialized(self):
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            City(created_at="2024-04-04 4:00:00")

    def test_state_id_initialization(self):
        self.assertIsInstance(self.city.state_id, str)

    def test_name_initialization(self):
        self.assertIsInstance(self.city.name, str)


class TestCityMethods(unittest.TestCase):
    """Test cases for methods of the City class"""

    def setUp(self):
        self.city = City()

    def test_str_method(self):
        str_rep = "[City] ({}) {}".format(
            self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), str_rep)

    def test_save_method(self):
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)

    def test_save_method_with_none(self):
        with self.assertRaises(TypeError):
            self.city.save(None)

    def test_to_dict_method(self):
        obj_dict = self.city.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "City")
        self.assertIsInstance(
            datetime.fromisoformat(obj_dict["created_at"]), datetime)
        self.assertIsInstance(
            datetime.fromisoformat(obj_dict["updated_at"]), datetime)

    def test_to_dict_with_none(self):
        with self.assertRaises(TypeError):
            self.city.to_dict(None)


class TestCityInstances(unittest.TestCase):
    """Test cases for instances of the City class"""

    def setUp(self):
        self.first_model = City()
        self.second_model = City()

    def test_equality(self):
        self.assertEqual(self.first_model, self.first_model)
        self.assertNotEqual(self.first_model, self.second_model)

    def test_unused_args(self):
        mymodel = City(None)
        self.assertNotIn(None, mymodel.__dict__.values())

    def test_with_args_and_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        mymodel = City(
                "13", id="1307966120652",
                created_at=date_iso, updated_at=date_iso,
                state_id="217", name="Bahri"
                )
        self.assertEqual(mymodel.id, "1307966120652")
        self.assertEqual(mymodel.created_at, date)
        self.assertEqual(mymodel.updated_at, date)
        self.assertEqual(mymodel.state_id, "217")
        self.assertEqual(mymodel.name, "Bahri")

    def test_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(
                    id=None, created_at=None, updated_at=None,
                    state_id=None, name=None
                    )

    def test_serialization_and_deserialization(self):
        obj_dict = self.first_model.to_dict()
        for key, value in obj_dict.items():
            self.assertIsInstance(value, str)
        new_model = City(**obj_dict)
        self.assertEqual(new_model.to_dict(), obj_dict)


class TestCityEdgeCases(unittest.TestCase):
    """Test cases for edge cases of the City class"""

    def test_empty_instance_creation(self):
        empty_city = City()
        self.assertIsNotNone(empty_city.id)
        self.assertIsInstance(empty_city.created_at, datetime)
        self.assertIsInstance(empty_city.updated_at, datetime)

    def test_attribute_edge_cases(self):
        mycity = City(
            empty_string_attr="", none_attr=None,
            special_chars_attr="!@##^#$%^&*()"
            )
        self.assertEqual(mycity.empty_string_attr, "")
        self.assertIsNone(mycity.none_attr)
        self.assertEqual(mycity.special_chars_attr, "!@##^#$%^&*()")


class TestCityDifferentModels(unittest.TestCase):
    """Test cases for unique instances in different City class models"""

    def setUp(self):
        self.first_model = City()
        self.second_model = City()

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
