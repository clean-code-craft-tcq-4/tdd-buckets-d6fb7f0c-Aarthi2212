import unittest
from unittest.mock import patch
from io import StringIO
import sys
from current_range import detect_and_display_current_readings

STD_OUT = 'sys.stdout'

class CurrentRangeTest(unittest.TestCase):
  def test_detect_display_readings(self):
    with patch(STD_OUT, new = StringIO()) as fake_out:
      detect_and_display_current_readings([4, 5])
      self.assertEqual(fake_out.getvalue(), "4-5, 2\n")
          
  


        
if __name__ == '__main__':
  sys.exit(unittest.main())
