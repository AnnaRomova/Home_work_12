import logging

from flask import Blueprint, render_template, request, current_app
from .functions import search_posts_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logger = logging.getLogger()
@main_blueprint.route('/')
def main_page():
    return render_template("index.html")

@main_blueprint.route('/search/')
def seach_page():
    result = {}
    result["s"] = request.args.get("s").lower()
    logging.info(f"Поиск по слову \"{result['s']}\"")

    result["posts"] = search_posts_by_word(result["s"], current_app.config["POST_PATH"])
    return render_template('post_list1.html', result=result)
