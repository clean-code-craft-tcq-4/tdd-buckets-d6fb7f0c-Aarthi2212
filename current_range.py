import constants as const

# def get_ranges(nums):
#     nums = sorted(set(nums))
#     gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
#     edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
#     return list(zip(edges, edges))

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

def convert_readings_to_map(current_data):
    reading_map = [0]*201
    try:
        reading_map = map_reading(reading_map, current_data)
    except IndexError:
        print(const.INDEX_ERROR)
    except TypeError:
        print(const.TYPE_ERROR)
    return reading_map
    
def get_ranges(current_data):
    reading_map = convert_readings_to_map(current_data)
    current_reading_index = [i for i, e in enumerate(reading_map) if e != 0]
    gaps = [[s, e] for s, e in zip(current_reading_index, current_reading_index[1:]) if s+1 < e]
    edges = iter(current_reading_index[:1] + sum(gaps, []) + current_reading_index[-1:])
    return list(zip(edges, edges)), reading_map

def get_current_ranges(data):
    current_ranges = []
    range_data, total_reading_map = get_ranges(data)
    for _range in range_data:
        total_readings = sum(list(map(total_reading_map.__getitem__, range(_range[0], _range[-1]+1))))
        current_ranges.append([_range, total_readings])
    return current_ranges

def format_range_display(range, reading):
    return const.RANGE_DISPLAY_FORMAT.format(range[0], range[-1], reading)

def print_current_ranges(range_display):
    for range in range_display:
        print(range)

def detect_and_display_current_readings(data):
    current_ranges = get_current_ranges(data)
    range_display = []
    for _range in current_ranges:
        range_data, reading = _range
        formatted_range = format_range_display(range_data, reading)
        range_display.append(formatted_range)
    print_current_ranges(range_display)
