import ssl
import json
import re
from deep_translator import GoogleTranslator
ssl._create_unverified_context()


# Free Proxy
# https://geonode.com/free-proxy-list
proxies_example = {
    "http": "95.216.78.205:3128",
    "http": "213.165.248.42:3128",
    "http": "23.88.23.123:80",
    "http": "188.132.150.87:8080",
    "http": "168.119.141.135:80"
}

def translate(text):
    return GoogleTranslator(source='russian', target='english', proxies=proxies_example).translate(text)

def contains_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))

def process_json(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                process_json(value)
            elif isinstance(value, str):
                try:
                    nested_data = json.loads(value)
                    process_json(nested_data)
                    data[key] = json.dumps(nested_data, ensure_ascii=False)
                except json.JSONDecodeError:
                    if contains_cyrillic(value):
                        tt = translate(data[key])
                        print(f"{data[key]} -> {tt}")
                        data[key] = tt

    elif isinstance(data, list):
        for i, item in enumerate(data):
            if isinstance(item, (dict, list)):
                process_json(item)
            elif isinstance(item, str):
                try:
                    nested_data = json.loads(item)
                    process_json(nested_data)
                    data[i] = json.dumps(nested_data, ensure_ascii=False)
                except json.JSONDecodeError:
                    if contains_cyrillic(item):
                        tt = translate(data[i])
                        print(f"\n----------\n{data[i]} -> {tt}\n----------\n")
                        data[i] = tt

def process_json_string(json_str):
    data = json.loads(json_str)
    process_json(data)
    return json.dumps(data, ensure_ascii=False)

def process_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    process_json(data)
    with open(file_path+"processed.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

# Add full path of JSON file with cyrillic symbols
file_path = 'c:/Users/boris/Downloads/Community-Pack-CorrelationRules_RU_dec.json'
process_json_file(file_path)
print(f"Processed JSON file saved to {file_path+'processed.json'}")