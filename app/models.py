from dataclasses import dataclass


@dataclass
class Anime:
    """
    class to model anime data
    """
    all_anime = []
    mal_id: int
    url: str
    title: str
    image_url: str
    synopsis: str
    type: str
    airing_start: str
    episodes: int
    members: int

    @classmethod
    def save_anime(cls, self):
        self.all_anime.append(cls)

    @classmethod
    def clear_anime(cls, self):
        self.all_anime.clear()

    @classmethod
    def get_anime(cls, self):
        return self.all_anime
