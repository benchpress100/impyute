"""test_random_imputation.py"""
import unittest
import numpy as np
from impy.imputations.cs import random_imputation
from impy.datasets import test_data


class TestRandomImputation(unittest.TestCase):
    """ Tests for Random Imputation """
    def setUp(self):
        """
        self.data_c: Complete dataset/No missing values
        self.data_m: Incommplete dataset/Has missing values
        """
        mask = np.zeros((3, 3), dtype=bool)
        self.data_c = test_data(mask)
        mask[0][0] = True
        self.data_m = test_data(mask)

    def test_return_type(self):
        """Random - Check if it returns np's n-dimensional array"""
        imputed = random_imputation(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_do_nothing(self):
        """ Random - Fill Complete Data(nothing should happen)"""
        actual = random_imputation(self.data_c)
        self.assertTrue(np.array_equal(actual, self.data_c))

    def test_fill(self):
        """ Random - After imputation, no NaN's should exist"""
        imputed = random_imputation(self.data_m)
        self.assertFalse(np.isnan(imputed).any())


if __name__ == "__main__":
    unittest.main()
