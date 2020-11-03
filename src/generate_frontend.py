#!/usr/bin/env python3

import os
from distutils.dir_util import copy_tree
from jinja2 import Environment, select_autoescape, FileSystemLoader
from helper_functions import load_json_from_file, write_string_to_file

# jinja init
env = Environment(
    loader=FileSystemLoader(searchpath='./templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

# load people.json
schedule = load_json_from_file("../data/schedule.json")

# load jinja template
template = env.get_template('index.html')

# render outpat based on schedule dict
output = template.render(schedule=schedule)

if os.path.exists("../dist") is False:
    os.mkdir("../dist")
write_string_to_file(output, "../dist/index.html")
copy_tree("templates/static", "../dist/static") # copy static files
print("index.html successfully generated and put here: " + os.path.abspath("../dist/index.html"))
