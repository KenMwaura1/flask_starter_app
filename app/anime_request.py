from jikanpy import Jikan
from .models import Anime

jikan = Jikan()


# print(jikan.top(type='anime'))
# print(jikan.season())
# top_anime_request = jikan.top(type='anime', page=2, subtype='')

# function to get top anime
def get_season_anime():
    """
    function to get the top anime from My anime list
    :return: list of anime
    """
    season_anime_request = jikan.season()
    season_anime = []
    if season_anime_request['anime']:
        response = season_anime_request['anime']

        for anime in response:
            mal_id = anime.get('mal_id')
            url = anime.get('url')
            title = anime.get('title')
            image_url = anime.get('image_url')
            synopsis = anime.get('synopsis')
            type = anime.get('type')
            airing_start = anime.get('airing_start')
            episodes = anime.get('episodes')
            members = anime.get('members')

            new_anime = Anime(mal_id, url, title, image_url, synopsis, type, airing_start, episodes, members)
            season_anime.append(new_anime)

    return season_anime
