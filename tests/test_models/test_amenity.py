#!/usr/bin/python3
"""
This script contains unittests for the Amenity subclass in the models package.
    file: AirBnB_clone/models/amenity.py

It tests various aspects of the Amenity class, including:
    - inheritance.
    - initialization.
    - methods.
    - instances.
    - edge cases.
    - comparisons between instances in different models.
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime


class TestAmenityInheritance(unittest.TestCase):
    """Test cases for inheritance from the BaseModel class"""

    def setUp(self):
        self.amenity = Amenity()

    def test_inheritance(self):
        self.assertIsInstance(self.amenity, BaseModel)


class TestAmenityInitialization(unittest.TestCase):
    """Test cases for initializing the Amenity class"""
    def setUp(self):
        self.amenity = Amenity()

    def test_id_generation(self):
        self.assertIsNotNone(self.amenity.id)
        self.assertIsInstance(self.amenity.id, str)

    def test_timestamps_initialized(self):
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            Amenity(created_at="2024-04-04 4:00:00")

    def test_name_initialization(self):
        self.assertIsInstance(self.amenity.name, str)


class TestAmenityMethods(unittest.TestCase):
    """Test cases for methods of the Amenity class"""

    def setUp(self):
        self.amenity = Amenity()

    def test_str_method(self):
        str_rep = "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), str_rep)

    def test_save_method(self):
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_save_method_with_none(self):
        with self.assertRaises(TypeError):
            self.amenity.save(None)

    def test_to_dict_method(self):
        obj_dict = self.amenity.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "Amenity")
        self.assertIsInstance(
            datetime.fromisoformat(obj_dict["created_at"]), datetime)
        self.assertIsInstance(
            datetime.fromisoformat(obj_dict["updated_at"]), datetime)

    def test_to_dict_with_none(self):
        with self.assertRaises(TypeError):
            self.amenity.to_dict(None)


class TestAmenityInstances(unittest.TestCase):
    """Test cases for instances of the Amenity class"""

    def setUp(self):
        self.first_model = Amenity()
        self.second_model = Amenity()

    def test_equality(self):
        self.assertEqual(self.first_model, self.first_model)
        self.assertNotEqual(self.first_model, self.second_model)

    def test_unused_args(self):
        mymodel = Amenity(None)
        self.assertNotIn(None, mymodel.__dict__.values())

    def test_with_args_and_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        mymodel = Amenity(
                "13", id="1307966120652",
                created_at=date_iso, updated_at=date_iso, name="Media Rooms"
                )
        self.assertEqual(mymodel.id, "1307966120652")
        self.assertEqual(mymodel.created_at, date)
        self.assertEqual(mymodel.updated_at, date)
        self.assertEqual(mymodel.name, "Media Rooms")

    def test_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(
                    id=None, created_at=None, updated_at=None, name=None
                    )

    def test_serialization_and_deserialization(self):
        obj_dict = self.first_model.to_dict()
        for key, value in obj_dict.items():
            self.assertIsInstance(value, str)
        new_model = Amenity(**obj_dict)
        self.assertEqual(new_model.to_dict(), obj_dict)


class TestAmenityEdgeCases(unittest.TestCase):
    """Test cases for edge cases of the Amenity class"""

    def test_empty_instance_creation(self):
        empty_amenity = Amenity()
        self.assertIsNotNone(empty_amenity.id)
        self.assertIsInstance(empty_amenity.created_at, datetime)
        self.assertIsInstance(empty_amenity.updated_at, datetime)

    def test_attribute_edge_cases(self):
        myamenity = Amenity(
            empty_string_attr="", none_attr=None,
            special_chars_attr="!@##^#$%^&*()"
            )
        self.assertEqual(myamenity.empty_string_attr, "")
        self.assertIsNone(myamenity.none_attr)
        self.assertEqual(myamenity.special_chars_attr, "!@##^#$%^&*()")


class TestAmenityDifferentModels(unittest.TestCase):
    """Test cases for unique instances in different Amenity class models"""

    def setUp(self):
        self.first_model = Amenity()
        self.second_model = Amenity()

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
