import unittest
from gedcomParser import *
from datetime import *
from dateutil.parser import parse

class TestGedcome(unittest.TestCase):

    def test_before_current_date(self):
        self.assertEqual(before_current_date("01-01-2040", "Julie", "I01", "Birth", "1"),
                         "Error US01: Birth date of Julie(I01) occurs before the current date on line 1.")
    def test_marriage_before_birth(self):
        self.assertEqual(marriage_before_birth("01-01-1900", "01-01-2000", "Julie", "I01", "2"),
                         "Error US02: Marriage date of Julie(I01) occurs before their birth date on line 2.")
    def test_death_before_birth(self):
        self.assertEqual(death_before_birth("01-01-1999", "01-01-2000", "Sam", "I02", "3"),
                         "Error US03: Death date of Sam(I02) occurs before their birth date on line 3.")
    def test_divorce_before_marriage(self):
        self.assertEqual(divorce_before_marriage("01-01-1999", "01-01-2000", "Jack", "I02", "4"),
                         "Error US04: Divorce date of Jack(I02) occurs before their marriage date on line 4.")                     
    def test_death_before_marriage(self):
        self.assertEqual(death_before_marriage("01-01-2000", "01-01-2001", "John", "I07", "11"),
                         "Error US05: Death date of John(I07) occurs before their marriage date on line 11.")
    def test_death_before_divorce(self):
        self.assertEqual(death_before_divorce("01-01-2000", "01-01-2002", "John", "I07", "12"),
                         "Error US06: Death date of John(I07) occurs before their divorce date on line 12.")
    def test_greater_than_150(self):
        self.assertEqual(greater_than_150("150", "Jill", "I09", "5"), "Error US07: Age of Jill(I09) is not less than 150 on line 5.")
    def test_birth_before_marriage(self):
        self.assertEqual(birth_before_marriage("01-01-1999", "01-01-2000", "N/A", "Jim Beam", "I03", "F04", "6"), "Anomaly US08: Birth date of Jim Beam(I03) occurs before the marriage date of their parents in Family F04 on line 6.")
    def test_birth_before_marriage_divorce(self):
        self.assertEqual(birth_before_marriage("01-01-1999", "01-01-1990", "01-01-1998", "Jim Beam", "I03", "F04", "7"), "Anomaly US08: Birth date of Jim Beam(I03) occurs after 9 months from the divorce date of their parents in Family F04 on line 7.")
    def test_no_bigamy(self):
        self.assertEqual(no_bigamy("01-01-1990", "01-01-1999", "01-01-2000", "Steel", "I11", "16"), 
                        "Anomaly US11: Marriage of Steel(I11) occurred during another marriage on line 16 (there is bigamy).")
    def test_parent_too_old(self):
        self.assertEqual(parent_too_old("02-02-2000", "01-01-1900", "Jackie", "I12", "F", "17"), 
                        "Anomaly US12: Jackie(I12) is a mother who is 100 (more than 60) years older than her child on line 17.")
    def test_parent_too_old(self):
        self.assertEqual(parent_too_old("02-02-2000", "01-01-1900", "Jacob", "I12", "M", "17"), 
                        "Anomaly US12: Jacob(I12) is a father who is 100 (more than 80) years older than his child on line 17.")

if __name__ == '__main__':
    unittest.main()
