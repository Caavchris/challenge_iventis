from src.infrastructure.api_movie_handler import APIMovieHandler
from src.infrastructure.csv_handler import CSVHandler
from src.domain.models.scrapping_settings import ScrappingSettings
from dotenv import load_dotenv
load_dotenv()


class APIMovieScrapper:
    def __init__(self):
        self.api_handler = APIMovieHandler()
    
    def get_trending_movies(self) -> list[ScrappingSettings]:
        """
        Obtém filmes/séries em tendência via API.
        
        Returns:
            Lista de ScrappingSettings com título e data de lançamento
        """
        trending_items = self.api_handler.get_trending_movies()
        
        results = []
        
        for item in trending_items:
            try:
                title = item.get("title") or item.get("name")
                release_date = item.get("release_date") or item.get("first_air_date")
                
                if title and release_date:
                    movie_data = ScrappingSettings(
                        title=title,
                        release_date=release_date
                    )
                    results.append(movie_data)
                
            except Exception:
                continue
        
        return results


if __name__ == "__main__":
    scrapper = APIMovieScrapper()
    result = scrapper.get_trending_movies()
    
    print(f"\nTotal de filmes encontrados: {len(result)}")
    
    csv_handler = CSVHandler(filename="movies_api.csv")
    csv_handler.write_csv(result, headers=["title", "release_date"])
    
    print("\n" + "="*50)
    for item in result:
        print(f"Título: {item.title}")
        print(f"Data: {item.release_date}")
        print("-" * 50)