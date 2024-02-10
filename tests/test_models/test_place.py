#!/usr/bin/python3
"""
This script contains unittests for the Place subclass in the models package.
    file: AirBnB_clone/models/place.py

It tests various aspects of the Place class, including:
    - inheritance.
    - initialization.
    - methods.
    - instances.
    - edge cases.
    - comparisons between instances in different models.
"""

import unittest
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime


class TestPlaceInheritance(unittest.TestCase):
    """Test cases for inheritance from the BaseModel class"""

    def setUp(self):
        self.place = Place()

    def test_inheritance(self):
        self.assertIsInstance(self.place, BaseModel)


class TestPlaceInitialization(unittest.TestCase):
    """Test cases for initializing the Place class"""
    def setUp(self):
        self.place = Place()

    def test_id_generation(self):
        self.assertIsNotNone(self.place.id)
        self.assertIsInstance(self.place.id, str)

    def test_timestamps_initialized(self):
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            Place(created_at="2024-04-04 4:00:00")

    def test_city_id_initialization(self):
        self.assertIsInstance(self.place.city_id, str)

    def test_user_id_initialization(self):
        self.assertIsInstance(self.place.user_id, str)

    def test_name_initialization(self):
        self.assertIsInstance(self.place.name, str)

    def test_description_initialization(self):
        self.assertIsInstance(self.place.description, str)

    def test_number_rooms_initialization(self):
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms_initialization(self):
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest_initialization(self):
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night_initialization(self):
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude_initialization(self):
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude_initialization(self):
        self.assertIsInstance(self.place.longitude, float)

    def test_amenity_ids_initialization(self):
        self.assertIsInstance(self.place.amenity_ids, list)


class TestPlaceMethods(unittest.TestCase):
    """Test cases for methods of the Place class"""

    def setUp(self):
        self.place = Place()

    def test_str_method(self):
        str_rep = "[Place] ({}) {}".format(
            self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), str_rep)

    def test_save_method(self):
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old_updated_at, self.place.updated_at)

    def test_save_method_with_none(self):
        with self.assertRaises(TypeError):
            self.place.save(None)

    def test_to_dict_method(self):
        obj_dict = self.place.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "Place")
        self.assertIsInstance(
            datetime.fromisoformat(obj_dict["created_at"]), datetime)
        self.assertIsInstance(
            datetime.fromisoformat(obj_dict["updated_at"]), datetime)

    def test_to_dict_with_none(self):
        with self.assertRaises(TypeError):
            self.place.to_dict(None)


class TestPlaceInstances(unittest.TestCase):
    """Test cases for instances of the Place class"""

    def setUp(self):
        self.first_model = Place()
        self.second_model = Place()

    def test_equality(self):
        self.assertEqual(self.first_model, self.first_model)
        self.assertNotEqual(self.first_model, self.second_model)

    def test_unused_args(self):
        mymodel = Place(None)
        self.assertNotIn(None, mymodel.__dict__.values())

    def test_with_args_and_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        mymodel = Place(
                "13", id="1307966120652",
                created_at=date_iso, updated_at=date_iso,
                city_id="789", user_id="10922781", name="Hotel California",
                description="Elegant, broad and comfy", number_rooms=4,
                number_bathrooms=2, max_guest=8, price_by_night=350,
                latitude=14.4, longitude=33.9, amenity_ids=[7, 11, 13]
                )
        self.assertEqual(mymodel.id, "1307966120652")
        self.assertEqual(mymodel.created_at, date)
        self.assertEqual(mymodel.updated_at, date)
        self.assertEqual(mymodel.city_id, "789")
        self.assertEqual(mymodel.user_id, "10922781")
        self.assertEqual(mymodel.name, "Hotel California")
        self.assertEqual(mymodel.description, "Elegant, broad and comfy")
        self.assertEqual(mymodel.number_rooms, 4)
        self.assertEqual(mymodel.number_bathrooms, 2)
        self.assertEqual(mymodel.max_guest, 8)
        self.assertEqual(mymodel.price_by_night, 350)
        self.assertEqual(mymodel.latitude, 14.4)
        self.assertEqual(mymodel.longitude, 33.9)
        self.assertEqual(mymodel.amenity_ids, [7, 11, 13])

    def test_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(
                    id=None, created_at=None, updated_at=None,
                    city_id=None, user_id=None, name=None,
                    description=None, number_rooms=None,
                    number_bathrooms=None, max_guest=None,
                    price_by_night=None, latitude=None, longitude=None,
                    amenity_ids=None
                    )

    def test_serialization_and_deserialization(self):
        obj_dict = self.first_model.to_dict()
        for key, value in obj_dict.items():
            self.assertIsInstance(value, str)
        new_model = Place(**obj_dict)
        self.assertEqual(new_model.to_dict(), obj_dict)


class TestPlaceEdgeCases(unittest.TestCase):
    """Test cases for edge cases of the Place class"""

    def test_empty_instance_creation(self):
        empty_place = Place()
        self.assertIsNotNone(empty_place.id)
        self.assertIsInstance(empty_place.created_at, datetime)
        self.assertIsInstance(empty_place.updated_at, datetime)

    def test_attribute_edge_cases(self):
        myplace = Place(
            empty_string_attr="", none_attr=None,
            special_chars_attr="!@##^#$%^&*()"
            )
        self.assertEqual(myplace.empty_string_attr, "")
        self.assertIsNone(myplace.none_attr)
        self.assertEqual(myplace.special_chars_attr, "!@##^#$%^&*()")


class TestPlaceDifferentModels(unittest.TestCase):
    """Test cases for unique instances in different Place class models"""

    def setUp(self):
        self.first_model = Place()
        self.second_model = Place()

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
