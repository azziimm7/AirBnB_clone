#!/usr/bin/python3
"""
This script contains unittests for the State subclass in the models package.
    file: AirBnB_clone/models/state.py

It tests various aspects of the State class, including:
    - inheritance.
    - initialization.
    - methods.
    - instances.
    - edge cases.
    - comparisons between instances in different models.
"""

import unittest
from models.base_model import BaseModel
from models.state import State
from datetime import datetime


class TestStateInheritance(unittest.TestCase):
    """Test cases for inheritance from the BaseModel class"""

    def setUp(self):
        self.state = State()

    def test_inheritance(self):
        self.assertIsInstance(self.state, BaseModel)


class TestStateInitialization(unittest.TestCase):
    """Test cases for initializing the State class"""
    def setUp(self):
        self.state = State()

    def test_id_generation(self):
        self.assertIsNotNone(self.state.id)
        self.assertIsInstance(self.state.id, str)

    def test_timestamps_initialized(self):
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            State(created_at="2024-04-04 4:00:00")

    def test_name_initialization(self):
        self.assertIsInstance(self.state.name, str)


class TestStateMethods(unittest.TestCase):
    """Test cases for methods of the State class"""

    def setUp(self):
        self.state = State()

    def test_str_method(self):
        str_rep = "[State] ({}) {}".format(
            self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), str_rep)

    def test_save_method(self):
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)

    def test_save_method_with_none(self):
        with self.assertRaises(TypeError):
            self.state.save(None)

    def test_to_dict_method(self):
        obj_dict = self.state.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "State")
        self.assertIsInstance(
            datetime.fromisoformat(obj_dict["created_at"]), datetime)
        self.assertIsInstance(
            datetime.fromisoformat(obj_dict["updated_at"]), datetime)

    def test_to_dict_with_none(self):
        with self.assertRaises(TypeError):
            self.state.to_dict(None)


class TestStateInstances(unittest.TestCase):
    """Test cases for instances of the State class"""

    def setUp(self):
        self.first_model = State()
        self.second_model = State()

    def test_equality(self):
        self.assertEqual(self.first_model, self.first_model)
        self.assertNotEqual(self.first_model, self.second_model)

    def test_unused_args(self):
        mymodel = State(None)
        self.assertNotIn(None, mymodel.__dict__.values())

    def test_with_args_and_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        mymodel = State(
                "13", id="1307966120652",
                created_at=date_iso, updated_at=date_iso, name="Khartoum"
                )
        self.assertEqual(mymodel.id, "1307966120652")
        self.assertEqual(mymodel.created_at, date)
        self.assertEqual(mymodel.updated_at, date)
        self.assertEqual(mymodel.name, "Khartoum")

    def test_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(
                    id=None, created_at=None, updated_at=None, name=None
                    )

    def test_serialization_and_deserialization(self):
        obj_dict = self.first_model.to_dict()
        for key, value in obj_dict.items():
            self.assertIsInstance(value, str)
        new_model = State(**obj_dict)
        self.assertEqual(new_model.to_dict(), obj_dict)


class TestStateEdgeCases(unittest.TestCase):
    """Test cases for edge cases of the State class"""

    def test_empty_instance_creation(self):
        empty_state = State()
        self.assertIsNotNone(empty_state.id)
        self.assertIsInstance(empty_state.created_at, datetime)
        self.assertIsInstance(empty_state.updated_at, datetime)

    def test_attribute_edge_cases(self):
        mystate = State(
            empty_string_attr="", none_attr=None,
            special_chars_attr="!@##^#$%^&*()"
            )
        self.assertEqual(mystate.empty_string_attr, "")
        self.assertIsNone(mystate.none_attr)
        self.assertEqual(mystate.special_chars_attr, "!@##^#$%^&*()")


class TestStateDifferentModels(unittest.TestCase):
    """Test cases for unique instances in different State class models"""

    def setUp(self):
        self.first_model = State()
        self.second_model = State()

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
