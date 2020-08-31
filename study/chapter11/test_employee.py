import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """针对Employee类的测试"""

    def setUp(self):
        """创建雇员实例，供使用的测试方法使用"""
        self.employee = Employee('janis','joplin',5000)

    def test_give_default_raise(self):
        """测试年薪增加默认值"""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary,10000)

    def test_give_custom_raise(self):
        """测试年薪增加给定值"""
        self.employee.give_raise(raise_salary=300)
        self.assertEqual(self.employee.annual_salary,5300)

