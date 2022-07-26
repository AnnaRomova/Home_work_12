import json
from os import path

def read_function(path_):
    if not path.exists(path_):
        print('путь указан неверно')
        return None
    file_extension = path.splitext(path_)[1]
    with open(path_, "r", encoding='utf8') as f:
        if file_extension == '.json':
            data = json.load(f)
        else:
            data = f.read()
    return data

def search_posts_by_word(word, path_) -> list:
    data = read_function(path_)
    result = []
    for item in data:
        if word in item["content"]:
            result.append(item)
    return result

