seeds = []
soil_mapping = {}
fertilizer_mapping = {}
water_mapping = {}
light_mapping = {}
temperature_mapping = {}
humidity_mapping = {}
location_mapping = {}
states = ['seeds','soil','fertilizer','water','light','temperature','humidity','location']
soil_list = []
fertilizer_list = []
water_list = []
light_list = []
temperature_list = []
humidity_list = []
location_list = []
# Both functions are bad because it brute forces. Test input too large. Crashy crashy 
def get_location(seed):
    translation = seed
    #print("Seed:", seed)
    if translation in soil_mapping.keys():
        translation = soil_mapping[translation]
    #print("Soil:", translation)
    if translation in fertilizer_mapping.keys():
        translation = fertilizer_mapping[translation]
    #print("Fertilizer:", translation)
    if translation in water_mapping.keys():
        translation = water_mapping[translation]
    #print("Water:", translation)
    if translation in light_mapping.keys():
        translation = light_mapping[translation]
    #print("Light:", translation)
    if translation in temperature_mapping.keys():
        translation = temperature_mapping[translation]
    #print("Temperature:", translation)
    if translation in humidity_mapping.keys():
        translation = humidity_mapping[translation]
    #print("Humidity:", translation)
    if translation in location_mapping.keys():
        translation = location_mapping[translation]
    #print("Location:", translation)
    return translation

def part1_bad(data):
    state = 0
    for line, e in enumerate(data):
        if e == "\n":
            print("new state")
            state += 1
            print(states[state])
        elif state == 0:
            print("gathering seeds")
            colon = e.find(":")
            nums = e[colon+2:].strip("\n").split(" ")
            for each in nums:
                seeds.append(int(each))
        else:
            if not e[0].isdigit():
                continue
            else:
                temp = e.strip("\n").split(" ")
                target_number = int(temp[0])
                source_number = int(temp[1])
                range_length = int(temp[2])
                for i in range(range_length):
                    if state == 1:
                        soil_mapping[source_number+i] = target_number+i
                    if state == 2:
                        fertilizer_mapping[source_number+i] = target_number+i
                    if state == 3:
                        water_mapping[source_number+i] = target_number+i
                    if state == 4:
                        light_mapping[source_number+i] = target_number+i
                    if state == 5:
                        temperature_mapping[source_number+i] = target_number+i
                    if state == 6:
                        humidity_mapping[source_number+i] = target_number+i
                    if state == 7:
                        location_mapping[source_number+i] = target_number+i
    locations = []
    for each in seeds:
        locations.append(get_location(each))
    return min(locations)

def translate(seed):
    translation = seed
    #print("Seed:", translation)
    for each in soil_list:
        source = each['source']
        target = each['target']
        # see if the seed is inside of the source range
        if translation >= source[0] and translation <= source[1]:
            # if so translate it using this rule
            translation = target[0] - source[0] + translation
            break
    #print("Soil:",translation)
    for each in fertilizer_list:
        source = each['source']
        target = each['target']
        # see if the seed is inside of the source range
        if translation >= source[0] and translation <= source[1]:
            # if so translate it using this rule
            translation = target[0] - source[0] + translation
            break
    #print("Fertilizer:",translation)
    for each in water_list:
        source = each['source']
        target = each['target']
        # see if the seed is inside of the source range
        if translation >= source[0] and translation <= source[1]:
            # if so translate it using this rule
            translation = target[0] - source[0] + translation
            break
    #print("Water:",translation)
    for each in light_list:
        source = each['source']
        target = each['target']
        # see if the seed is inside of the source range
        if translation >= source[0] and translation <= source[1]:
            # if so translate it using this rule
            translation = target[0] - source[0] + translation
            break
    #print("Light:",translation)
    for each in temperature_list:
        source = each['source']
        target = each['target']
        # see if the seed is inside of the source range
        if translation >= source[0] and translation <= source[1]:
            # if so translate it using this rule
            translation = target[0] - source[0] + translation
            break
    #print("Temperature:",translation)
    for each in humidity_list:
        source = each['source']
        target = each['target']
        # see if the seed is inside of the source range
        if translation >= source[0] and translation <= source[1]:
            # if so translate it using this rule
            translation = target[0] - source[0] + translation
            break
    #print("Humidity:",translation)
    for each in location_list:
        source = each['source']
        target = each['target']
        # see if the seed is inside of the source range
        if translation >= source[0] and translation <= source[1]:
            # if so translate it using this rule
            translation = target[0] - source[0] + translation
            break
    #print("Location:",translation)
    return translation


def part1(data):
    global soil_list, fertilizer_list, water_list, light_list, temperature_list, humidity_list, location_list
    soil_list, fertilizer_list, water_list, light_list, temperature_list, humidity_list, location_list = [], [], [], [], [], [], []
    state = 0
    for line, e in enumerate(data):
        if e == "\n":
            print("new state")
            state += 1
            print(states[state])
        elif state == 0:
            print("gathering seeds")
            colon = e.find(":")
            nums = e[colon+2:].strip("\n").split(" ")
            for each in nums:
                seeds.append(int(each))
        else:
            if not e[0].isdigit():
                continue
            else:
                temp = e.strip("\n").split(" ")
                target_number = int(temp[0])
                source_number = int(temp[1])
                range_length = int(temp[2])
                min_target = target_number
                min_source = source_number
                max_target = min_target + range_length - 1
                max_source = min_source + range_length - 1
                if state == 1:
                    soil_list.append({"source":[min_source, max_source], "target":[min_target, max_target]})
                if state == 2:
                    fertilizer_list.append({"source":[min_source, max_source], "target":[min_target, max_target]})
                if state == 3:
                    water_list.append({"source":[min_source, max_source], "target":[min_target, max_target]})
                if state == 4:
                    light_list.append({"source":[min_source, max_source], "target":[min_target, max_target]})
                if state == 5:
                    temperature_list.append({"source":[min_source, max_source], "target":[min_target, max_target]})
                if state == 6:
                    humidity_list.append({"source":[min_source, max_source], "target":[min_target, max_target]})
                if state == 7:
                    location_list.append({"source":[min_source, max_source], "target":[min_target, max_target]})
    locations = []
    for each in seeds:
        locations.append(translate(each))

    return min(locations)

def reverse_dictionaries():
    global soil_list, fertilizer_list, water_list, light_list, temperature_list,humidity_list, location_list

    temp = []
    for each in soil_list:
        temp.append({'source':each['target'], 'target':each['source']})
    soil_list = temp 
    temp = []
    for each in fertilizer_list:
        temp.append({'source':each['target'], 'target':each['source']})
    fertilizer_list = temp 
    temp = []
    for each in water_list:
        temp.append({'source':each['target'], 'target':each['source']})
    water_list = temp 
    temp = []
    for each in light_list:
        temp.append({'source':each['target'], 'target':each['source']})
    light_list = temp 
    temp = []
    for each in temperature_list:
        temp.append({'source':each['target'], 'target':each['source']})
    temperature_list = temp 
    temp = []
    for each in humidity_list:
        temp.append({'source':each['target'], 'target':each['source']})
    humidity_list = temp 
    temp = []
    for each in location_list:
        temp.append({'source':each['target'], 'target':each['source']})
    location_list = temp 

def reverse_translate(location):
    translation = location
#    print("location:",location)
    for each in location_list:
        source = each['source']
        target = each['target']
        # see if the seed is inside of the source range
        if translation >= source[0] and translation <= source[1]:
            # if so translate it using this rule
            translation = target[0] - source[0] + translation
            break
#    print("humidity: ", translation)
    for each in humidity_list:
        source = each['source']
        target = each['target']
        # see if the seed is inside of the source range
        if translation >= source[0] and translation <= source[1]:
            # if so translate it using this rule
            translation = target[0] - source[0] + translation
            break
#    print("temperature: ", translation)
    for each in temperature_list:
        source = each['source']
        target = each['target']
        # see if the seed is inside of the source range
        if translation >= source[0] and translation <= source[1]:
            # if so translate it using this rule
            translation = target[0] - source[0] + translation
            break
#    print("light: ", translation)
    for each in light_list:
        source = each['source']
        target = each['target']
        # see if the seed is inside of the source range
        if translation >= source[0] and translation <= source[1]:
            # if so translate it using this rule
            translation = target[0] - source[0] + translation
            break
#    print("water: ", translation)
    for each in water_list:
        source = each['source']
        target = each['target']
        # see if the seed is inside of the source range
        if translation >= source[0] and translation <= source[1]:
            # if so translate it using this rule
            translation = target[0] - source[0] + translation
            break
#    print("fertilizer: ", translation)
    for each in fertilizer_list:
        source = each['source']
        target = each['target']
        # see if the seed is inside of the source range
        if translation >= source[0] and translation <= source[1]:
            # if so translate it using this rule
            translation = target[0] - source[0] + translation
            break
#    print("soil: ", translation)
    for each in soil_list:
        source = each['source']
        target = each['target']
        # see if the seed is inside of the source range
        if translation >= source[0] and translation <= source[1]:
            # if so translate it using this rule
            translation = target[0] - source[0] + translation
            break
#    print("seed: ", translation)
    return translation
def return_min_location(start, stop):
    minimum = 99999999999
    for i in range(start, stop):
        loc = translate(i)
        minimum = min(minimum, loc)
        print(minimum)
    return minimum


    
def part2(data):
    global seeds
    seeds = []
    state = 0
    for line, e in enumerate(data):
        if e == "\n":
            print("new state")
            state += 1
            print(states[state])
        elif state == 0:
            print("gathering seeds")
            colon = e.find(":")
            nums = e[colon+2:].strip("\n").split(" ")
            start = -99
            end = -99
            for each in nums:
                if start == -99:
                    start = int(each)
                elif end == -99:
                    end = int(each)
                    seeds.append([start, start+end])
                    
                    start = -99
                    end = -99
        else:
            continue
    #reverse_dictionaries()
    locations = 999999999999
    known = 157211394
    #for i in range(10000000):
    #    temp_seed = reverse_translate(i)
    #    print("temp seed: ", temp_seed)
    #    for each in seeds:
            
    #        if temp_seed >= each[0] and temp_seed <= each[1]:
    #            locations = min(locations, i)
  
    #for each in seeds:
    #    for i in range(each[0], each[0]+100000):
    #        loc = translate(i)
    #        locations = min(locations, loc)
    minimum_location_list = [999999999,999999999]
    for each in location_list:
        if each['target'][0] < minimum_location_list[0]:
            minimum_location_list = each['target']
    reverse_dictionaries()
    for i in range(minimum_location_list[0], minimum_location_list[1]):
        temp_seed = reverse_translate(i)
        for each in seeds:
            
            if temp_seed >= each[0] and temp_seed <= each[1]:
                locations = min(locations, i)
                print("Minimum: ", locations)

    return locations

file = "data/day5.txt"
# Get the file read in 
with open(file, 'r') as f:
    data = f.readlines()
    print("Part1: ",part1(data))
    print("Part2: ", part2(data))
