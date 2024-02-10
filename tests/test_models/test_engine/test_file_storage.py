#!/usr/bin/python3
"""
This script contains unittests for the FileStorage class in the engine package
    file: AirBnB_clone/models/engine/file_storage.py

It tests various aspects of the FileStorage class, including:
    - initialization
    - methods
"""

import unittest
import os
import json
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorageInitialization(unittest.TestCase):
    """Test cases for initializing the FileStorage class"""

    def setUp(self):
        self.file_storage = FileStorage()
        self.file_path = self.file_storage._FileStorage__file_path
        self.objects = self.file_storage._FileStorage__objects
        self.allclass = self.file_storage._FileStorage__allclass

    def test_initialization(self):
        self.assertEqual(self.file_path, "file.json")
        self.assertEqual(self.objects, {})
        self.assertEqual(
            self.allclass,
            {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
            }
        )

    def test_file_path_type(self):
        self.assertEqual(str, type(self.file_path))

    def test_objects_type(self):
        self.assertEqual(dict, type(self.objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class"""

    def setUp(self):
        self.file_storage = FileStorage()

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        my_basemodel = BaseModel()
        my_user = User()
        my_state = State()
        my_city = City()
        my_place = Place()
        my_amenity = Amenity()
        my_review = Review()
        models.storage.new(my_basemodel)
        models.storage.new(my_user)
        models.storage.new(my_state)
        models.storage.new(my_city)
        models.storage.new(my_place)
        models.storage.new(my_amenity)
        models.storage.new(my_review)
        self.assertIn(
                "BaseModel." + my_basemodel.id, models.storage.all().keys()
                )
        self.assertIn(my_basemodel, models.storage.all().values())
        self.assertIn("User." + my_user.id, models.storage.all().keys())
        self.assertIn(my_user, models.storage.all().values())
        self.assertIn("State." + my_state.id, models.storage.all().keys())
        self.assertIn(my_state, models.storage.all().values())
        self.assertIn("City." + my_city.id, models.storage.all().keys())
        self.assertIn(my_city, models.storage.all().values())
        self.assertIn("Place." + my_place.id, models.storage.all().keys())
        self.assertIn(my_place, models.storage.all().values())
        self.assertIn("Amenity." + my_amenity.id, models.storage.all().keys())
        self.assertIn(my_amenity, models.storage.all().values())
        self.assertIn("Review." + my_review.id, models.storage.all().keys())
        self.assertIn(my_review, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        my_basemodel = BaseModel()
        my_user = User()
        my_state = State()
        my_city = City()
        my_place = Place()
        my_amenity = Amenity()
        my_review = Review()
        models.storage.new(my_basemodel)
        models.storage.new(my_user)
        models.storage.new(my_state)
        models.storage.new(my_city)
        models.storage.new(my_place)
        models.storage.new(my_amenity)
        models.storage.new(my_review)

        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + my_basemodel.id, save_text)
            self.assertIn("User." + my_user.id, save_text)
            self.assertIn("State." + my_state.id, save_text)
            self.assertIn("City." + my_city.id, save_text)
            self.assertIn("Place." + my_place.id, save_text)
            self.assertIn("Amenity." + my_amenity.id, save_text)
            self.assertIn("Review." + my_review.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        my_basemodel = BaseModel()
        my_user = User()
        my_state = State()
        my_city = City()
        my_place = Place()
        my_amenity = Amenity()
        my_review = Review()
        models.storage.new(my_basemodel)
        models.storage.new(my_user)
        models.storage.new(my_state)
        models.storage.new(my_city)
        models.storage.new(my_place)
        models.storage.new(my_amenity)
        models.storage.new(my_review)

        models.storage.save()
        models.storage.reload()
        objs = models.storage.all()
        self.assertIn("BaseModel." + my_basemodel.id, objs)
        self.assertIn("User." + my_user.id, objs)
        self.assertIn("State." + my_state.id, objs)
        self.assertIn("City." + my_city.id, objs)
        self.assertIn("Place." + my_place.id, objs)
        self.assertIn("Amenity." + my_amenity.id, objs)
        self.assertIn("Review." + my_review.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


class TestFileStorageInstances(unittest.TestCase):
    """Unittests for testing instances of the FileStorage class"""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)


class TestFileStorageEdgeCases(unittest.TestCase):
    """Unittests for testing edge cases of the FileStorage class"""

    def test_save_empty(self):
        """Test saving when there are no objects"""
        models.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_nonexistent_file(self):
        """Test reloading from a non-existent file"""
        os.remove("file.json")
        models.storage.reload()
        self.assertFalse(os.path.exists("file.json"))

    def test_new_with_invalid_object(self):
        """Test adding an invalid object"""
        with self.assertRaises(AttributeError):
            models.storage.new(123)

    def test_reload_corrupted_json(self):
        """Test reloading from a corrupted JSON file"""
        with open("file.json", "w") as f:
            f.write("Invalid JSON content")
        with self.assertRaises(ValueError):
            models.storage.reload()


if __name__ == '__main__':
    unittest.main()
