from src.infrastructure.selenium_handler import SeleniumHandler
from src.infrastructure.csv_handler import CSVHandler
from selenium.webdriver.common.by import By
from src.domain.models.scrapping_settings import ScrappingSettings
import os
import time
from dotenv import load_dotenv
load_dotenv()
driver = SeleniumHandler()

class ScrappingMovie:
    def __init__(self, url: str):
        self.url = url

    def scrapping_movie(self) -> list[ScrappingSettings]:
        driver.open_url(self.url)
        time.sleep(5)
        
        try:
            scroller = driver.find_element(By.ID, "trending_scroller")
            driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scroller)
            time.sleep(2)
            driver.execute_script("arguments[0].scrollLeft = 0", scroller)
            time.sleep(2)
        except Exception as e:
            print(f"Scroller error: {e}")
        
        cards = driver.find_elements(By.CSS_SELECTOR, ".card.style_1")
        
        results = []
        
        for card in cards:
            try:
                h2_elements = card.find_elements(By.TAG_NAME, "h2")
                p_elements = card.find_elements(By.TAG_NAME, "p")
                
                if not h2_elements or not p_elements:
                    continue
                
                title = h2_elements[0].text.strip()
                release_date = p_elements[0].text.strip()
                
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
    url = os.getenv("URL_SCRAPPING")
    scrapper = ScrappingMovie(url)
    result = scrapper.scrapping_movie()

    print(f"\nTotal de filmes encontrados: {len(result)}")
    
    csv_handler = CSVHandler(filename="movies_scrapping.csv")
    csv_handler.write_csv(result, headers=["title", "release_date"])
    
    print("\n" + "="*50)
    for item in result:
        print(f"Título: {item.title}")
        print(f"Data: {item.release_date}")
        print("-" * 50)

    driver.quit()