import unittest
from unittest.mock import patch
from io import StringIO
import sys
import mock
from current_range import detect_and_display_current_readings

STD_OUT = 'sys.stdout'

class CurrentRangeTest(unittest.TestCase):
  def test_detect_display_readings(self):
    with patch(STD_OUT, new = StringIO()) as fake_out:
      detect_and_display_current_readings([4, 5])
      self.assertEqual(fake_out.getvalue(), "4-5, 2\n")
          
  

class Test(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    with mock.patch.object(unittest, "main", return_value=42):
      with mock.patch.object(unittest, "__name__", "__main__"):
        with mock.patch.object(sys,'exit') as mock_exit:
          init()         
          assert mock_exit.call_args[0][0] == 42
        
def init():
  if __name__ == '__main__':
    sys.exit(unittest.main())

init()