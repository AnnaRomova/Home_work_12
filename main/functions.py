import json
from os import path
from flask import current_app



def read_function(path_):
    """The common function to read files. For json-files return the function python instances either list or dictionary"""
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
    """The function finds posts by a word"""
    data = read_function(path_)
    result = []
    for item in data:
        if word in item["content"]:
            result.append(item)
    return result

def add_post(post:dict) -> dict:
    """"""
    path_ = current_app.config["POST_PATH"]
    posts = read_function(path_)
    posts.append(post)
    with open(path_, "w", encoding='utf8') as file:
        json.dump(posts, file)
    return post


