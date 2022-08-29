RANGE_DISPLAY_FORMAT = '{}-{}, {}'
INDEX_ERROR = "Current Reading out of range. Supported Range (0, 200)"
TYPE_ERROR = "Readings contain unsupported values."
ERROR_INDEXES = {
    "12" : 4095,
    "10" : 1023
}
BITS_TO_AMPS_CONVERSION = {
    "12": "round(10* ({}/ {}))",
    "10": "round(({} * (30/{}))-15)"
}