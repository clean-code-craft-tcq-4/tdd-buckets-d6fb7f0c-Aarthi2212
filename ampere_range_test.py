import unittest
from unittest.mock import patch
from io import StringIO
import sys
import test_data
from ampere_range import detect_and_display_ampere_readings, \
  convert_readings_to_map, format_range_display, \
  get_ampere_ranges, get_ranges, print_ampere_ranges, \
  validate_reading

from bits_to_amps import BitsToAmpsConverter

STD_OUT = 'sys.stdout'

class AmpereRangeTest(unittest.TestCase):

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


  def test_get_ampere_ranges(self):
    for test in test_data.get_ampere_ranges_data:
      self.assertEqual(get_ampere_ranges(test.get(test_data.INPUT)), test.get(test_data.OUTPUT))

  def test_format_range_display(self):
    for test in test_data.format_range_display_data:
      self.assertEqual(format_range_display(*test.get(test_data.INPUT)), test.get(test_data.OUTPUT))

  def test_print_ampere_ranges(self):
    for test in test_data.print_ampere_ranges_data:
      with patch(STD_OUT, new = StringIO()) as fake_out:
        print_ampere_ranges(test.get(test_data.INPUT))
        self.assertEqual(fake_out.getvalue(), test.get(test_data.OUTPUT))

  def test_detect_display_readings(self):
    for test in test_data.detect_display_readings_data:
      with patch(STD_OUT, new = StringIO()) as fake_out:
        detect_and_display_ampere_readings(test.get(test_data.INPUT))
        self.assertEqual(fake_out.getvalue(), test.get(test_data.OUTPUT))

class BitsToAmpsTest(unittest.TestCase):
  def test_ignore_error_index(self):
    for test in test_data.error_index_data:
      self.assertEqual(BitsToAmpsConverter(
        test.get(test_data.INPUT).get(test_data.NO_OF_BITS),
        test.get(test_data.INPUT).get(test_data.IS_BI_DIRECTIONAL),
        test.get(test_data.INPUT).get(test_data.REFERENCE)
        ).ignore_error_index(test.get(test_data.INPUT).get(test_data.BIT_READINGS)), test.get(test_data.OUTPUT))

  def test_bits_to_amps_conversion(self):
    for test in test_data.bits_data:
      self.assertEqual(BitsToAmpsConverter(
        test.get(test_data.INPUT).get(test_data.NO_OF_BITS),
        test.get(test_data.INPUT).get(test_data.IS_BI_DIRECTIONAL),
        test.get(test_data.INPUT).get(test_data.REFERENCE)).convert_bit_to_amps(test.get(test_data.INPUT).get(test_data.BIT_READINGS)), test.get(test_data.OUTPUT))   

  def test_convert(self):
    for test in test_data.conversion_data:
      self.assertEqual(BitsToAmpsConverter(
        test.get(test_data.INPUT).get(test_data.NO_OF_BITS),
        test.get(test_data.INPUT).get(test_data.IS_BI_DIRECTIONAL),
        test.get(test_data.INPUT).get(test_data.REFERENCE)).convert(test.get(test_data.INPUT).get(test_data.BIT_READINGS)), test.get(test_data.OUTPUT))   
  
  def test_absolute_conversion(self):
    for test in test_data.absolute_conversion_data:
      self.assertEqual(BitsToAmpsConverter(
        test.get(test_data.INPUT).get(test_data.NO_OF_BITS),
        test.get(test_data.INPUT).get(test_data.IS_BI_DIRECTIONAL),
        test.get(test_data.INPUT).get(test_data.REFERENCE)).get_absolute_readings(test.get(test_data.INPUT).get(test_data.AMPERE_READINGS)), test.get(test_data.OUTPUT))   
  
  def test_convert_display_ampere_ranges(self):
    for test in test_data.conversion_readings_data:
      with patch(STD_OUT, new = StringIO()) as fake_out:
        BitsToAmpsConverter(
          test.get(test_data.INPUT).get(test_data.NO_OF_BITS),
          test.get(test_data.INPUT).get(test_data.IS_BI_DIRECTIONAL),
          test.get(test_data.INPUT).get(test_data.REFERENCE)).convert_display_ampere_ranges(test.get(test_data.INPUT).get(test_data.BIT_READINGS))
        self.assertEqual(fake_out.getvalue(), test.get(test_data.OUTPUT))

if __name__ == '__main__':
  sys.exit(unittest.main()) # pragma: no cover
