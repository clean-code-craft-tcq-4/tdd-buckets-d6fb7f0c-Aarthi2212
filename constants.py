RANGE_DISPLAY_FORMAT = '{}-{}, {}'
INDEX_ERROR = "Current Reading out of range. Supported Range (0, 200)"
TYPE_ERROR = "Readings contain unsupported values."
ERROR_INDEXES = {
    "12" : 4095,
    "10" : 1023
}
BITS_TO_AMPS_CONVERSION_UNI = "round({2}* ({0}/ {1}))"

BITS_TO_AMPS_CONVERSION_BI = "round(({0} * (2*{2}/{1}))-{2})"