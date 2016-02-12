import json
import sys
import cc_data
import cc_dat_utils

def make_LevelPack_from_json(json_data):
    level_pack = cc_data.CCDataFile()
    for json_levels in json_data:
        level_number = json_levels["level_number"]
        time = json_levels["time"]
        num_chips = json_levels["num_chips"]
        upper_layer = json_levels["upper_layer"]
        lower_layer = json_levels["lower_layer"]
        optional_fields = json_levels["optional_fields"]

        real_level = cc_data.CCLevel()
        real_level.level_number = level_number
        real_level.time = time
        real_level.num_chips = num_chips
        real_level.upper_layer = upper_layer
        real_level.lower_layer = lower_layer
        real_level.optional_fields = optional_fields

        for json_field in json_levels:
            if json_field["type"] == 3:
                field_title = json_field["title"]
                cc_field = cc_data.CCMapTitleField(field_title)


        #look through fields in list figure out what kind of field  for /if statement based on type make new field and add to level
        #get type print type of field
        #if type print blah
        #fill in with what makes that field type

        level_pack.add_level(real_level)
    return level_pack

default_input_json_file = "data/cc_data.json"
default_output_dat_file = "data/cc_dat.dat"

if len(sys.argv) == 3:
    input_json_file = sys.argv[1]
    output_dat_file = sys.argv[2]
    print("Using command line args:", input_json_file, output_dat_file)
else:
    input_json_file = default_input_json_file
    output_dat_file = default_output_dat_file
    print("Unknown command line options. Using default values:", input_json_file, output_dat_file)

json_reader = open(input_json_file, "r")
json_data = json.load(json_reader)
json_reader.close()

level_pack = make_LevelPack_from_json(json_data)


output_dat_filename="data/cc_dat.dat"
cc_dat_utils.write_cc_data_to_dat(level_pack, output_dat_filename)

make_cc_data_from_json(json_data)