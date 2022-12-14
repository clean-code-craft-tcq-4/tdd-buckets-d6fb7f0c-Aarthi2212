import constants as const
INPUT = "INPUT"
OUTPUT = "OUTPUT"
BIT_READINGS = "BIT_READINGS"
NO_OF_BITS = "NO_OF_BITS"
AMPERE_READINGS = "AMPERE_READINGS"
IS_BI_DIRECTIONAL = "IS_BI_DIRECTIONAL"
REFERENCE = "REFERENCE"
INPUT_DATA_1 = [200, 199, 100, 101, 102, 103, 104, 78, 79, 80, 105, 45]
INPUT_DATA_2 = [1, 4, 4, 10, 5, 11, 12, 13, 14]
OUTPUT_MAP_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
OUTPUT_MAP_2 = [0, 1, 0, 0, 2, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
OUTPUT_MAP_3 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
    INPUT:[2],
    OUTPUT:([(2, 2)], OUTPUT_MAP_3)}
]

get_ampere_ranges_data = [
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

print_ampere_ranges_data = [
    {
    INPUT:["47-47, 1", "7-8, 3"], 
    OUTPUT: "47-47, 1\n7-8, 3\n"
    },
    {
    INPUT:["20-20, 2"], 
    OUTPUT: "20-20, 2\n"
    }
    
]

detect_display_readings_data = [
    {
    INPUT:[21, 22], 
    OUTPUT: "21-22, 2\n"
    },
    {
    INPUT:INPUT_DATA_2, 
    OUTPUT:"1-1, 1\n4-5, 3\n10-14, 5\n"
    }
    
]

error_index_data = [
    {
    INPUT:{
            BIT_READINGS: [2091, 4095, 1178, 1982, 4095, 4094, 4094],
            NO_OF_BITS: 12,
            IS_BI_DIRECTIONAL : False,
            REFERENCE: 10
        },
    OUTPUT:[2091, 1178, 1982, 4094, 4094]
    }
]

bits_data = [
    {
    INPUT:{
        BIT_READINGS: 1146,
        NO_OF_BITS: 12,
        IS_BI_DIRECTIONAL: False,
        REFERENCE: 10
    },
    OUTPUT:3
    }
]

absolute_conversion_data = [
    {
        INPUT: {
            AMPERE_READINGS: [-14, 13, 12, -20, 0, 11, -1, 10],
            NO_OF_BITS: 10,
            IS_BI_DIRECTIONAL: True,
            REFERENCE: 15
        },
        OUTPUT: [14, 13, 12, 20, 0, 11, 1, 10]
    }
]

conversion_data = [
    {
        INPUT: {
            BIT_READINGS: [0, 1123, 987, 1142, 1134, 1500, 3098, 4000],
            NO_OF_BITS: 12,
            IS_BI_DIRECTIONAL: False,
            REFERENCE: 10
        },
        OUTPUT: [0, 3, 2, 3, 3, 4, 8, 10]
    }
]

conversion_readings_data = [
    {
        INPUT: {
            BIT_READINGS: [0, 1123, 987, 1142, 1134, 1500, 3098, 4000],
            NO_OF_BITS: 12,
            IS_BI_DIRECTIONAL: False,
            REFERENCE: 10
        },
        OUTPUT: "0-0, 1\n2-4, 5\n8-8, 1\n10-10, 1\n"
    },
    {
        INPUT: {
            BIT_READINGS: [100, 103, 150, 200, 500, 400, 800, 1021],
            NO_OF_BITS: 10,
            IS_BI_DIRECTIONAL: True,
            REFERENCE: 15
        },
        OUTPUT: "0-0, 1\n3-3, 1\n8-9, 2\n11-12, 3\n15-15, 1\n"
    }
]