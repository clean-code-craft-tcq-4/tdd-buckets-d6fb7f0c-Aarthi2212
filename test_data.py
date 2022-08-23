import constants as const
INPUT = "INPUT"
OUTPUT = "OUTPUT"
INPUT_DATA_1 = [200, 199, 100, 101, 102, 103, 104, 78, 79, 80, 105, 45]
INPUT_DATA_2 = [1, 4, 4, 10, 5, 11, 12, 13, 14]
OUTPUT_MAP_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
OUTPUT_MAP_2 = [0, 1, 0, 0, 2, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
validation_test_data = [
    {
    INPUT:-1, 
    OUTPUT:False
    },
    {
    INPUT:1, 
    OUTPUT:True
    }
    
]
convert_readings_to_map_data = [
    {
    INPUT:INPUT_DATA_1, 
    OUTPUT: OUTPUT_MAP_1
    },
    {
    INPUT:INPUT_DATA_2, 
    OUTPUT:OUTPUT_MAP_2
    }
]
convert_readings_to_map_negative_data = [
    {
    INPUT: [200, 201],
    OUTPUT: const.INDEX_ERROR + "\n"
    },
    {
    INPUT: ["199.9", 199.9],
    OUTPUT: const.TYPE_ERROR + "\n"
    }]

get_ranges_data = [
    {
    INPUT:INPUT_DATA_1, 
    OUTPUT:([(45, 45), (78, 80), (100, 105), (199, 200)], OUTPUT_MAP_1)
    },
    {
    INPUT:INPUT_DATA_2, 
    OUTPUT:([(1, 1), (4, 5), (10, 14)], OUTPUT_MAP_2)
    },
    {
    INPUT:[1],
    OUTPUT:([(1, 1)], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])}
]

get_current_ranges_data = [
    {
    INPUT:INPUT_DATA_1, 
    OUTPUT:[[(45, 45), 1], [(78, 80), 3], [(100, 105), 6], [(199, 200), 2]]
    },
    {
    INPUT:INPUT_DATA_2, 
    OUTPUT:[[(1, 1), 1], [(4, 5), 3], [(10, 14), 5]]
    }
    
]

format_range_display_data = [
    {
    INPUT:[(44, 44), 1], 
    OUTPUT: "44-44, 1"
    },
    {
    INPUT:[(89, 90), 3], 
    OUTPUT:"89-90, 3"
    }
    
]

print_current_ranges_data = [
    {
    INPUT:["45-45, 1", "4-5, 3"], 
    OUTPUT: "45-45, 1\n4-5, 3\n"
    },
    {
    INPUT:["1-1, 2"], 
    OUTPUT: "1-1, 2\n"
    }
    
]

detect_display_readings_data = [
    {
    INPUT:[4, 5], 
    OUTPUT: "4-5, 2\n"
    },
    {
    INPUT:INPUT_DATA_2, 
    OUTPUT:"1-1, 1\n4-5, 3\n10-14, 5\n"
    }
    
]