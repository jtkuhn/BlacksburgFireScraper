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

        
    def test_dateParsing_returnsNone_WhenInvalid1(self):
        self.assertEqual(DateHelpers.getDatetime("5/5/5 5:5"), None)
    
    
    #TODO: Figure out how to moq the DateHelpers.getDatetime method to return None so these are independent of the above
    def test_weekdayNumericParsing_works1(self):
        self.assertEqual(DateHelpers.getWeekdayNumeric("8/9/2017 10:16"), 2)
        
        
    def test_weekdayNumericParsing_returnsNone_whenDateParsingFails(self):
        self.assertEqual(DateHelpers.getWeekdayNumeric("5/5/5 5:5"), None)
        
        
    def test_weekdayParsing_works1(self):
        self.assertEqual(DateHelpers.getWeekdayEnglish("8/9/2017 10:16"), "Wednesday")
        
        
    def test_weekdayParsing_works2(self):
        self.assertEqual(DateHelpers.getWeekdayEnglish("8/12/2017 10:16"), "Saturday")
    
    
    def test_weekdayParsing_returnsNone_whenDateParsingFails(self):
        self.assertEqual(DateHelpers.getWeekdayEnglish("5/5/5 5:5"), None)
        
if __name__ == "__main__":
    unittest.main() 