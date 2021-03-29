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
    def test_no_bigamy1(self):
        self.assertEqual(no_bigamy("01-01-1990", "01-01-1999", "01-01-2000", "Steel", "I11", "16"), 
                        "Anomaly US11: Marriage of Steel(I11) occurred during another marriage (there is bigamy) on line 16.")
    def test_no_bigamy2(self):
        self.assertEqual(no_bigamy("01-01-1990", "01-01-1999", "N/A", "Manny", "I18", "19"), 
                        "Anomaly US11: Marriage of Manny(I18) occurred during another marriage (there is bigamy) on line 19.")
    def test_parent_too_old1(self):
        self.assertEqual(parent_too_old("01-02-2000", "01-01-1900", "Jackie", "I12", "F", "17"), 
                        "Anomaly US12: Jackie(I12) is a mother who is 100 (more than 60) years older than her child on line 17.")
    def test_parent_too_old2(self):
        self.assertEqual(parent_too_old("02-02-2000", "01-01-1919", "Jacob", "I12", "M", "17"), 
                        "Anomaly US12: Jacob(I12) is a father who is 81 (more than 80) years older than his child on line 17.")
    def test_more_than_15_siblings(self):
        self.assertEqual(more_than_15_siblings(16, "F06", "128"), "Anomaly US15: Family (F06) has more than 15 siblings on line 128.")
    def test_different_last_names(self):
        self.assertEqual(different_last_names("Altenburg", "Chasnov", "I09", "128"), "Anomaly US16: Chasnov (I09) does not have the same name as their father (Altenburg) on line 128.")
    def test_birth_before_parents_death_mother(self):
        self.assertEqual(birth_before_parents_death("02-02-2000", "Suzy Smith", "I02", "01-01-2000", True, "128"), "Error US09: Birth of Suzy Smith(I02) is after the death of their mother on line 128.")
    def test_birth_before_parents_death_father(self):
        self.assertEqual(birth_before_parents_death("11-11-2000", "Suzy Smith", "I02", "01-01-2000", False, "128"), "Error US09: Birth of Suzy Smith(I02) is after 9 months after the death of their father on line 128.")
    def test_marriage_after_14(self):
        self.assertEqual(marriage_after_14("I02", "Suzy Smith", "01-01-2005", "02-02-2000", "128"),
                         "Error US10: Birth of Suzy Smith(I02) is less than 14 years before their marriage date on line 128.")
        
if __name__ == '__main__':
    unittest.main()
