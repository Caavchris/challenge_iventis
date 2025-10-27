import os
from dotenv import load_dotenv
from src.infrastructure.selenium_handler import SeleniumHandler
from src.infrastructure.csv_handler import CSVHandler
from src.domain.services.movie_scrapping_service import MovieScrapingService

load_dotenv()

def main():
    driver = SeleniumHandler()
    url = os.getenv("URL_SCRAPPING")

    service = MovieScrapingService(driver)
    movies = service.scrape_movies(url)

    print(f"Total de filmes encontrados: {len(movies)}")

    csv_handler = CSVHandler(filename="movies_scrapping.csv")
    csv_handler.write_csv(movies, headers=["title", "release_date"])

    for item in movies:
        print(f"Título: {item.title}")
        print(f"Data: {item.release_date}")
        print("-" * 40)

    driver.quit()

if __name__ == "__main__":
    main()