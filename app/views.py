from flask import render_template
from .anime_request import get_season_anime

from . import app


@app.route('/')
def index():
    """
    root page view that returns the index page and its data
    :return: index template
    """
    season_anime = get_season_anime()
    print(season_anime)
    return render_template('index.html', season_anime=season_anime)
