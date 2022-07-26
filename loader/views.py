import logging

from flask import Blueprint, render_template, request

from lesson12_project_source_v3.loader.utils import save_picture
from lesson12_project_source_v3.main.functions import add_post

ALLOWED_EXTENSIONS = {'png','jpeg'}

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

@loader_blueprint.route('/post')
def post_page():
    return render_template("post_form.html")

@loader_blueprint.route('/post', methods = ['POST'])
def add_post_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    extension = picture.filename.split('.')[-1]
    if extension in ALLOWED_EXTENSIONS:
        if not picture or not content:
            if not picture:
                logging.error("ошибка при загрузке файла")
            return 'Нет картинки или текста. Ошибка загрузки'

        picture_path = '/' + save_picture(picture)
        post = add_post({'pic':picture_path, 'content': content })
        return render_template('post_uploaded.html', post=post)
    else:
        logging.info("загруженный файл - не картинка")
        return f"Тип файлов {extension} не поддерживается"