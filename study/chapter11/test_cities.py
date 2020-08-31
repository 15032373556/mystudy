import unittest
from study.study.chapter11.city_functions import city_country

class CityFunctionsTestCase(unittest.TestCase):
    """ 测试city_functions.py"""

    def test_city_country(self):
        """ 能正确处理类似'santiago','chile'这样的值吗"""
        city = city_country('santiago','chile')
        self.assertEqual(city,"Santiago,Chile")

    def test_city_country_population(self):
        """ 能正确处理类似'santiago','chile','population=5000000'这样的值吗"""
        city = city_country('santiago','chile',5000000)
        self.assertEqual(city,"Santiago,Chile - population 5000000")

unittest.main