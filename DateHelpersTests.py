import DateHelpers
import unittest
from datetime import datetime

class DateHelpersTests(unittest.TestCase):
    
    
    def test_dateParsing_works1(self):
        self.assertEqual(DateHelpers.getDatetime("5/2/17 8:03am"), datetime(2017, 5, 2, 8, 3))
        
        
    def test_dateParsing_works2(self):
        self.assertEqual(DateHelpers.getDatetime("5/2/17 8:03pm"), datetime(2017, 5, 2, 20, 3))

        
    def test_dateParsing_works3(self):
        self.assertEqual(DateHelpers.getDatetime("05/02/17 20:03"), datetime(2017, 5, 2, 20, 3))
        
        
    def test_dateParsing_works4(self):
        self.assertEqual(DateHelpers.getDatetime("5/2/2017 20:03"), datetime(2017, 5, 2, 20, 3))

    
    def test_weekdayParsing_works1(self):
        self.assertEqual(DateHelpers.getWeekdayEnglish("8/9/2017 10:16"), "Wednesday")
        
        
    def test_weekdayParsing_works2(self):
        self.assertEqual(DateHelpers.getWeekdayEnglish("8/12/2017 10:16"), "Saturday")
        
        
if __name__ == "__main__":
    unittest.main() 