import math

def area_cubo(lado):
    return 6 * lado ** 2

def area_paralelogramo(base, altura):
    return base * altura

def area_piramide(base, altura):
    area_base = base ** 2
    area_lateral = base * math.sqrt((altura ** 2) + (base ** 2) / 4)
    return area_base + area_lateral


import unittest

class TestCalculoAreaCubo(unittest.TestCase):
    
    def test_area_cubo_positivo(self):
        lado = 5
        self.assertEqual(area_cubo(lado), 150)
    
    def test_area_cubo_negativo(self):
        lado = -3
        self.assertEqual(area_cubo(lado), 54)

if __name__ == '__main__':
    unittest.main()

import unittest
import csv

class TestCalculoAreaPiramide(unittest.TestCase):
    
    def test_area_piramide_csv(self):
        with open('test_values.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Pular cabeçalho
            for row in csv_reader:
                base = float(row[0])
                altura = float(row[1])
                result = float(row[2])
                self.assertEqual(area_piramide(base, altura), result)

if __name__ == '__main__':
    unittest.main()

