from dotenv import load_dotenv
from src.infrastructure.api_movie_handler import APIMovieHandler
from src.infrastructure.csv_handler import CSVHandler
from src.domain.services.movie_api_service import APIMovieService

load_dotenv()

def main():
    api_handler = APIMovieHandler()
    service = APIMovieService(api_handler)

    movies = service.get_trending_movies()

    print(f"Total de filmes encontrados: {len(movies)}")

    csv_handler = CSVHandler(filename="movies_api.csv")
    csv_handler.write_csv(movies, headers=["title", "release_date"])

    for item in movies:
        print(f"Título: {item.title}")
        print(f"Data: {item.release_date}")
        print("-" * 50)

if __name__ == "__main__":
    main()