import unittest
from unittest.mock import patch
from io import StringIO
import sys
import test_data
from current_range import detect_and_display_current_readings, \
  convert_readings_to_map, format_range_display, \
  get_current_ranges, get_ranges, print_current_ranges, \
  validate_reading

STD_OUT = 'sys.stdout'

class CurrentRangeTest(unittest.TestCase):

  def test_validate_reading(self):
    for test in test_data.validation_test_data:
      self.assertEqual(validate_reading(test.get(test_data.INPUT)), test.get(test_data.OUTPUT))

  def test_convert_readings_to_map(self):
    for test in test_data.convert_readings_to_map_data:
      self.assertEqual(convert_readings_to_map(test.get(test_data.INPUT)), test.get(test_data.OUTPUT))

  def test_convert_readings_to_map_negative(self):
    for test in test_data.convert_readings_to_map_negative_data:
      with patch(STD_OUT, new = StringIO()) as fake_out:
        convert_readings_to_map(test.get(test_data.INPUT))
        self.assertEqual(fake_out.getvalue(), test.get(test_data.OUTPUT))
  
  def test_get_ranges(self):
    for test in test_data.get_ranges_data:
      self.assertEqual(get_ranges(test.get(test_data.INPUT)), test.get(test_data.OUTPUT))


  def test_get_current_ranges(self):
    for test in test_data.get_current_ranges_data:
      self.assertEqual(get_current_ranges(test.get(test_data.INPUT)), test.get(test_data.OUTPUT))

  def test_format_range_display(self):
    for test in test_data.format_range_display_data:
      self.assertEqual(format_range_display(*test.get(test_data.INPUT)), test.get(test_data.OUTPUT))

  def test_print_current_ranges(self):
    for test in test_data.print_current_ranges_data:
      with patch(STD_OUT, new = StringIO()) as fake_out:
        print_current_ranges(test.get(test_data.INPUT))
        self.assertEqual(fake_out.getvalue(), test.get(test_data.OUTPUT))

  def test_detect_display_readings(self):
    for test in test_data.detect_display_readings_data:
      with patch(STD_OUT, new = StringIO()) as fake_out:
        detect_and_display_current_readings(test.get(test_data.INPUT))
        self.assertEqual(fake_out.getvalue(), test.get(test_data.OUTPUT))
        
if __name__ == '__main__':
  sys.exit(unittest.main()) # pragma: no cover
