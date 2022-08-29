import constants as const

def validate_reading(reading):
    result = True
    if reading < 0:
        result = False
    return result

def map_reading(reading_map, current_data):
    for item in current_data:
        result = validate_reading(item)
        if result:
            reading_map[item] = reading_map[item]+1
    return reading_map

def convert_readings_to_map(ampere_data):
    reading_map = [0]*201
    try:
        reading_map = map_reading(reading_map, ampere_data)
    except IndexError:
        print(const.INDEX_ERROR)
    except TypeError:
        print(const.TYPE_ERROR)
    return reading_map
    
def get_ranges(ampere_data):
    reading_map = convert_readings_to_map(ampere_data)
    ampere_reading_index = [i for i, e in enumerate(reading_map) if e != 0]
    gaps = [[s, e] for s, e in zip(ampere_reading_index, ampere_reading_index[1:]) if s+1 < e]
    edges = iter(ampere_reading_index[:1] + sum(gaps, []) + ampere_reading_index[-1:])
    return list(zip(edges, edges)), reading_map

def get_ampere_ranges(data):
    ampere_ranges = []
    range_data, total_reading_map = get_ranges(data)
    for _range in range_data:
        total_readings = sum(list(map(total_reading_map.__getitem__, range(_range[0], _range[-1]+1))))
        ampere_ranges.append([_range, total_readings])
    return ampere_ranges

def format_range_display(range, reading):
    return const.RANGE_DISPLAY_FORMAT.format(range[0], range[-1], reading)

def print_ampere_ranges(range_display):
    for range in range_display:
        print(range)

def detect_and_display_ampere_readings(data):
    ampere_ranges = get_ampere_ranges(data)
    range_display = []
    for _range in ampere_ranges:
        range_data, reading = _range
        formatted_range = format_range_display(range_data, reading)
        range_display.append(formatted_range)
    print_ampere_ranges(range_display)
