#!/usr/bin/python3
"""
This script contains unittests for the Review subclass in the models package.
    file: AirBnB_clone/models/review.py

It tests various aspects of the Review class, including:
    - inheritance.
    - initialization.
    - methods.
    - instances.
    - edge cases.
    - comparisons between instances in different models.
"""

import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime


class TestReviewInheritance(unittest.TestCase):
    """Test cases for inheritance from the BaseModel class"""

    def setUp(self):
        self.review = Review()

    def test_inheritance(self):
        self.assertIsInstance(self.review, BaseModel)


class TestReviewInitialization(unittest.TestCase):
    """Test cases for initializing the Review class"""
    def setUp(self):
        self.review = Review()

    def test_id_generation(self):
        self.assertIsNotNone(self.review.id)
        self.assertIsInstance(self.review.id, str)

    def test_timestamps_initialized(self):
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            Review(created_at="2024-04-04 4:00:00")

    def test_place_id_initialization(self):
        self.assertIsInstance(self.review.place_id, str)

    def test_user_id_initialization(self):
        self.assertIsInstance(self.review.user_id, str)

    def test_text_initialization(self):
        self.assertIsInstance(self.review.text, str)


class TestReviewMethods(unittest.TestCase):
    """Test cases for methods of the Review class"""

    def setUp(self):
        self.review = Review()

    def test_str_method(self):
        str_rep = "[Review] ({}) {}".format(
            self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), str_rep)

    def test_save_method(self):
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated_at, self.review.updated_at)

    def test_save_method_with_none(self):
        with self.assertRaises(TypeError):
            self.review.save(None)

    def test_to_dict_method(self):
        obj_dict = self.review.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "Review")
        self.assertIsInstance(
            datetime.fromisoformat(obj_dict["created_at"]), datetime)
        self.assertIsInstance(
            datetime.fromisoformat(obj_dict["updated_at"]), datetime)

    def test_to_dict_with_none(self):
        with self.assertRaises(TypeError):
            self.review.to_dict(None)


class TestReviewInstances(unittest.TestCase):
    """Test cases for instances of the Review class"""

    def setUp(self):
        self.first_model = Review()
        self.second_model = Review()

    def test_equality(self):
        self.assertEqual(self.first_model, self.first_model)
        self.assertNotEqual(self.first_model, self.second_model)

    def test_unused_args(self):
        mymodel = Review(None)
        self.assertNotIn(None, mymodel.__dict__.values())

    def test_with_args_and_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        mymodel = Review(
                "13", id="1307966120652",
                created_at=date_iso, updated_at=date_iso,
                place_id="479", user_id="120977", text="very nice"
                )
        self.assertEqual(mymodel.id, "1307966120652")
        self.assertEqual(mymodel.created_at, date)
        self.assertEqual(mymodel.updated_at, date)
        self.assertEqual(mymodel.place_id, "479")
        self.assertEqual(mymodel.user_id, "120977")
        self.assertEqual(mymodel.text, "very nice")

    def test_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(
                    id=None, created_at=None, updated_at=None,
                    place_id=None, user_id=None, text=None
                    )

    def test_serialization_and_deserialization(self):
        obj_dict = self.first_model.to_dict()
        for key, value in obj_dict.items():
            self.assertIsInstance(value, str)
        new_model = Review(**obj_dict)
        self.assertEqual(new_model.to_dict(), obj_dict)


class TestReviewEdgeCases(unittest.TestCase):
    """Test cases for edge cases of the Review class"""

    def test_empty_instance_creation(self):
        empty_review = Review()
        self.assertIsNotNone(empty_review.id)
        self.assertIsInstance(empty_review.created_at, datetime)
        self.assertIsInstance(empty_review.updated_at, datetime)

    def test_attribute_edge_cases(self):
        myreview = Review(
            empty_string_attr="", none_attr=None,
            special_chars_attr="!@##^#$%^&*()"
            )
        self.assertEqual(myreview.empty_string_attr, "")
        self.assertIsNone(myreview.none_attr)
        self.assertEqual(myreview.special_chars_attr, "!@##^#$%^&*()")


class TestReviewDifferentModels(unittest.TestCase):
    """Test cases for unique instances in different Review class models"""

    def setUp(self):
        self.first_model = Review()
        self.second_model = Review()

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
