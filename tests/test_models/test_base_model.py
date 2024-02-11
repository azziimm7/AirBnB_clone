#!/usr/bin/python3
"""
This script contains unittests for the BaseModel class in the models package.
    file: AirBnB_clone/models/base_model.py

It tests various aspects of the BaseModel class, including:
    - initialization.
    - methods.
    - instances.
    - edge cases.
    - comparisons between instances in different models.
"""

import unittest
import models
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModelInitialization(unittest.TestCase):
    """Test cases for initializing the BaseModel class"""

    def setUp(self):
        self.base_model = BaseModel()

    def test_init_method(self):
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_generation(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)

    def test_timestamps_initialized(self):
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            BaseModel(created_at="2024-04-04 4:00:00")


class TestBaseModelMethods(unittest.TestCase):
    """Test cases for methods of the BaseModel class"""

    def setUp(self):
        self.base_model = BaseModel()

    def test_str_method(self):
        str_rep = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), str_rep)

    def test_str_representation(self):
        date = datetime.today()
        date_rep = repr(date)
        self.base_model.id = "12079912065"
        self.base_model.created_at = self.base_model.updated_at = date
        model_str = self.base_model.__str__()
        self.assertIn("[BaseModel] (12079912065)", model_str)
        self.assertIn("'id': '12079912065'", model_str)
        self.assertIn("'created_at': " + date_rep, model_str)
        self.assertIn("'updated_at': " + date_rep, model_str)

    def test_save_method(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_save_method_with_none(self):
        with self.assertRaises(TypeError):
            self.base_model.save(None)

    def test_save_method_with_arg(self):
        with self.assertRaises(TypeError):
            self.base_model.save(None)

    def test_save_method_updates_file(self):
        self.base_model.save()
        model_id = "BaseModel." + self.base_model.id
        with open("file.json", "r") as f:
            self.assertIn(model_id, f.read())

    def test_to_dict_method(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertIsInstance(
            datetime.fromisoformat(obj_dict["created_at"]), datetime)
        self.assertIsInstance(
            datetime.fromisoformat(obj_dict["updated_at"]), datetime)

    def test_to_dict_with_none(self):
        with self.assertRaises(TypeError):
            self.base_model.to_dict(None)


class TestBaseModelInstances(unittest.TestCase):
    """Test cases for instances of the BaseModel class"""

    def setUp(self):
        self.first_model = BaseModel()
        self.second_model = BaseModel()

    def test_equality(self):
        self.assertEqual(self.first_model, self.first_model)
        self.assertNotEqual(self.first_model, self.second_model)

    def test_unused_args(self):
        mymodel = BaseModel(None)
        self.assertNotIn(None, mymodel.__dict__.values())

    def test_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_with_args_and_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        mymodel = BaseModel(
                "14", id="1207966120652",
                created_at=date_iso, updated_at=date_iso
                )
        self.assertEqual(mymodel.id, "1207966120652")
        self.assertEqual(mymodel.created_at, date)
        self.assertEqual(mymodel.updated_at, date)

    def test_serialization_and_deserialization(self):
        obj_dict = self.first_model.to_dict()
        for key, value in obj_dict.items():
            self.assertIsInstance(value, str)
        new_model = BaseModel(**obj_dict)
        self.assertEqual(new_model.to_dict(), obj_dict)

    def test_to_dict_added_attributes(self):
        self.second_model.name = "Inception"
        self.second_model.number = 79
        self.assertIn("name", self.second_model.to_dict())
        self.assertIn("number", self.second_model.to_dict())


class TestBaseModelEdgeCases(unittest.TestCase):
    """Test cases for edge cases of the BaseModel class"""

    def test_empty_instance_creation(self):
        empty_base_model = BaseModel()
        self.assertIsNotNone(empty_base_model.id)
        self.assertIsInstance(empty_base_model.created_at, datetime)
        self.assertIsInstance(empty_base_model.updated_at, datetime)

    def test_attribute_edge_cases(self):
        base_model = BaseModel(
            empty_string_attr="", none_attr=None,
            special_chars_attr="!@##^#$%^&*()"
            )
        self.assertEqual(base_model.empty_string_attr, "")
        self.assertIsNone(base_model.none_attr)
        self.assertEqual(base_model.special_chars_attr, "!@##^#$%^&*()")


class TestBaseModelDifferentModels(unittest.TestCase):
    """Test cases for unique instances in different BaseModel class models"""

    def setUp(self):
        self.first_model = BaseModel()
        self.second_model = BaseModel()

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
