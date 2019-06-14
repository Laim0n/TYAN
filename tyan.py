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
    return json.loads(convert_tyan_to_json(data))


def convert_tyan_to_json(data):
    warnings.simplefilter(action='ignore', category=FutureWarning)
    reg = re.compile('([[] ?((["\'].+["\'])+ ?,? ?)+[]] ?: ?["\'].+["\'] ?,?)')

    if bool(reg.search(data)):
        data_list = reg.findall(data)
        for element in data_list:
            element = element[0]
            texts = re.findall('["\']([^:,]+)["\']', element)
            result = ""
            for text in texts:
                if text == texts[-1]:
                    continue
                result += "\"{0}\": \"{1}\",".format(text, texts[-1])

            if element[-1:] != ",":
                result = result[:-1]
            data = data.replace(element, result)

    return data
