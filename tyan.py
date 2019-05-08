import json
import re
import warnings
from pathlib import Path


def load_file(path):
    file = open(path, "r", encoding="utf-8")
    data = file.read()
    file.close()

    if Path(path).suffix == '.tyan':
        return loads(data)
    else:
        return json.loads(data)


def loads(data):
    return json.loads(convert_json_to_tyan(data))

    
def convert_json_to_tyan(data):
    data = re.sub(r'\s+', ' ', data)

    warnings.simplefilter(action='ignore', category=FutureWarning)
    reg = re.compile('([[] ?((["\'].+["\'])+ ?,? ?)+[]] ?: ?["\'].+["\'] ?,?)')

    if bool(reg.search(data)):
        data_list = reg.findall(data)
        for element in data_list:
            elm = element
            element = element[0]
            texts = re.findall('["\'](.+)["\']', element)
            result = ""
            for text in texts:
                result += "\"{0}\": \"{1}\",".format(text, texts[2])

            if data_list.index(elm) == int(len(data_list) - 1):
                result = result[:-1]
            data = data.replace(element, result)

    return data
