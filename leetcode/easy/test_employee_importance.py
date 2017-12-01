import unittest

from employee_importance import *

class EmployeeImportanceTest(unittest.TestCase):

    def test_employee_importance(self):
        data = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
        employee1 = Employee(data[0][0], data[0][1], data[0][2])
        employee2 = Employee(data[1][0], data[1][1], data[1][2])
        employee3 = Employee(data[2][0], data[2][1], data[2][2])

        solution = Solution()
        actual = solution.get_importance([employee1, employee2, employee3], 1)
        self.assertEqual(11, actual)
