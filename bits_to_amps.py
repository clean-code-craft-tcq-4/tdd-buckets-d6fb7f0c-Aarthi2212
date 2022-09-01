import constants as const
from ampere_range import detect_and_display_ampere_readings
class BitsToAmpsConverter:
    def __init__(self, number_of_bits, is_bidirectional, reference) -> None:
        self.number_of_bits = number_of_bits
        self.is_birectional = is_bidirectional
        self.reference_value = reference

    def ignore_error_index(self, bit_readings):
        return [reading for reading in bit_readings if reading != const.ERROR_INDEXES.get(str(self.number_of_bits))]

    def convert_bit_to_amps(self, bit_reading):
        amp_output = None
        max_bit_value = (2 ** self.number_of_bits) - 1
        if self.is_birectional is True:
            amp_output = eval(const.BITS_TO_AMPS_CONVERSION_BI.format(bit_reading, max_bit_value, self.reference_value))
        else:
            amp_output = eval(const.BITS_TO_AMPS_CONVERSION_UNI.format(bit_reading, max_bit_value, self.reference_value))
        return amp_output

    def get_absolute_readings(self, ampere_readings):
        return list(map(abs, ampere_readings))

    def convert(self, bit_readings):
        readings_in_bits = self.ignore_error_index(bit_readings)
        ampere_readings = [self.convert_bit_to_amps(reading) for reading in readings_in_bits]
        ampere_readings = self.get_absolute_readings(ampere_readings)
        return ampere_readings

    def convert_display_ampere_ranges(self, readings_in_bits):
        ampere_readings = self.convert(readings_in_bits)
        detect_and_display_ampere_readings(ampere_readings)
