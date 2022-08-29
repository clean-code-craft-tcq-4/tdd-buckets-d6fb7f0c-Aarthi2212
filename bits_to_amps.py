import constants as const
from ampere_range import detect_and_display_ampere_readings
class BitsToAmpsConverter:
    def __init__(self, number_of_bits) -> None:
        self.number_of_bits = number_of_bits

    def ignore_error_index(self, bit_readings):
        return [reading for reading in bit_readings if reading != const.ERROR_INDEXES.get(str(self.number_of_bits))]

    def convert_bit_to_amps(self, bit_reading):
        max_bit_value = (2 ** self.number_of_bits) - 1
        return round(10* (bit_reading/ max_bit_value))

    def convert(self, bit_readings):
        readings_in_bits = self.ignore_error_index(bit_readings)
        ampere_readings = [self.convert_bit_to_amps(reading) for reading in readings_in_bits]
        return ampere_readings

    def convert_display_ampere_ranges(self, readings_in_bits):
        ampere_readings = self.convert(readings_in_bits)
        detect_and_display_ampere_readings(ampere_readings)
