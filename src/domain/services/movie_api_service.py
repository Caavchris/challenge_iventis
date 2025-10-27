from src.domain.models.scrapping_settings import ScrappingSettings

class APIMovieService:
    def __init__(self, api_handler):
        self.api_handler = api_handler

    def get_trending_movies(self) -> list[ScrappingSettings]:
        trending_items = self.api_handler.get_trending_movies()
        results = []

        for item in trending_items:
            try:
                title = item.get("title") or item.get("name")
                release_date = item.get("release_date") or item.get("first_air_date")

                if title and release_date:
                    results.append(ScrappingSettings(title=title, release_date=release_date))
            except Exception:
                continue

        return results