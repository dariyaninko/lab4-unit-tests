import unittest
import rectangle

class TestRectangle(unittest.TestCase):
    """Тесты для функций из rectangle.py"""
    
    
    def test_area_normal(self):
        """Тест площади с нормальными значениями"""
        result = rectangle.area(5, 7)
        self.assertEqual(result, 35)
    
    def test_area_zero(self):
        """Тест площади с нулевыми значениями"""
        result = rectangle.area(0, 10)
        self.assertEqual(result, 0)
    
    def test_area_square(self):
        """Тест площади квадрата"""
        result = rectangle.area(10, 10)
        self.assertEqual(result, 100)
    
    def test_perimeter_normal(self):
        """Тест периметра с нормальными значениями"""
        result = rectangle.perimeter(5, 7)
        self.assertEqual(result, 24)
    
    def test_perimeter_zero(self):
        """Тест периметра с нулевыми значениями"""
        result = rectangle.perimeter(0, 0)
        self.assertEqual(result, 0)
    
    def test_perimeter_square(self):
        """Тест периметра квадрата"""
        result = rectangle.perimeter(10, 10)
        self.assertEqual(result, 40)

if __name__ == '__main__':
    unittest.main()