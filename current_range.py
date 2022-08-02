import constants as const

def get_ranges(nums):
    nums = sorted(set(nums))
    gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
    edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
    return list(zip(edges, edges))

def format_range_display(range, length):
    return const.RANGE_DISPLAY_FORMAT.format(range[0], range[-1], length)


def get_current_range(data):
    range_display = []
    range_data = get_ranges(data)
    for datum in range_data:
        range_display.append(format_range_display(datum, len(list(x for x in data if x in datum))))
    return range_display

def print_current_ranges(range_display):
    for item in range_display:
        print(item)

def detect_and_display_current_readings(data):
    range_display = get_current_range(data)
    print_current_ranges(range_display)

