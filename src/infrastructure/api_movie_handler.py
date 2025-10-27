import requests
import os


class APIMovieHandler:
    
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.base_url = os.getenv("API_URL")
        self.headers = {
            "accept": "application/json"
        }
    
    def get_trending_movies(self, time_window: str = "day", language: str = "pt-BR") -> list:
        endpoint = f"{self.base_url}/trending/movie/{time_window}"
        params = {
            "api_key": self.api_key,
            "language": language
        }
        
        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("results", [])
        except requests.exceptions.RequestException as e:
            print(f"✗ Erro ao buscar filmes em tendência: {e}")
            return []
    
if __name__ == "__main__":    
    handler = APIMovieHandler()
    
    movies = handler.get_trending_movies(time_window="day")
    print(f"Total de itens em tendência: {len(movies)}")
    
    for movie in movies[:20]:
        title = movie.get("title") or movie.get("name")
        release = movie.get("release_date") or movie.get("first_air_date")
        print(f"- {title} ({release})")