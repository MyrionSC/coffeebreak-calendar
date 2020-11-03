#!/usr/bin/env python3
from datetime import datetime, timedelta
from helper_functions import load_json_from_file, construct_day_groups, save_json_file_from_dict

# load people.json
people = load_json_from_file("../data/people.json")

# create list of 365 next days
today = datetime.today()
dateList = [today + timedelta(days=i) for i in range(365)]

# create groups for each day
schedule = list(map(lambda dt: construct_day_groups(dt, people), dateList))

# save groups into schedule.json file
save_json_file_from_dict(schedule, "../data/schedule.json")
