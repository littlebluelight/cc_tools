import json
import sys
import cc_data

def make_LevelPack_from_json(json_data):
    level_pack= cc_data.CCDataFile()
    for json_levels in json_data:
        level_number=json_levels["level_number"]
        timer=json_levels["timer"]
        chip_number=json_levels["chip_number"]
        upper_layer=json_levels["upper_layer"]
        lower_layer=json_levels["lower_layer"]
        optional_field=json_levels["optional_field"]

        real_level = cc_data.CCLevel()
        real_level.level_number=level_number
        real_level.timer=timer
        real_level.chip_number=chip_number
        real_level.upper_layer=upper_layer
        real_level.lower_layer=lower_layer
        real_level.optional_fields=optional_field
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