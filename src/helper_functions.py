import json
import random
from datetime import datetime
from typing import List, Dict

# split people into random sets of people of length 3-4
def construct_day_groups(dt: datetime, people: List[Dict]):
    # TODO: Some form of uniform distribution would make sense, but I am lazy
    random.shuffle(people)
    return {
        "ISO": dt.isoformat(),
        "data_dk": dt.strftime("%d/%m/%Y"),
        "groups": list(chunks(people, 3))
    }

# Thanks SO
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        if i + n >= len(lst): # if at last iteration, just return all remaining, so one poor person is not drinking alone or something
            yield lst[i:]
        else:
            yield lst[i:i + n]

def load_json_from_file(filename):
    with open(filename, encoding='utf-8') as f_in:
        return json.load(f_in)

def save_json_file_from_dict(d, filename):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(d, fp, ensure_ascii=False)
