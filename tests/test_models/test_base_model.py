#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instatiation(unittest.TestCase):
    """Test for instatiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        """
        Test for instances with no args
        """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        """
        Test for instances stored in objects
        """
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        """
        Test if id is public string
        """
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        """
        created_at is public date time
        """
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        """
        updated_at is public timestamp
        """
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        """
        Test if instances are unique
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        """
        diffrent instances have diffrent creation timestamp
        """
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        """
        Two instances have diffrent update timestamp
        """
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_instantiation_with_kwargs(self):
        """
        Test if args are unused
        """
        dt = datetime.now()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """instantiation with none kwargs test method"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        """instantiation with kwargs test method"""
        dt = datetime.now()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


if __name__ == "__main__":
    unittest.main()
