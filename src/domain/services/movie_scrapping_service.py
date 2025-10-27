import time
from selenium.webdriver.common.by import By
from src.domain.models.scrapping_settings import ScrappingSettings

class MovieScrapingService:
    def __init__(self, selenium_handler):
        self.driver = selenium_handler

    def scrape_movies(self, url: str) -> list[ScrappingSettings]:
        self.driver.open_url(url)
        time.sleep(5)
        try:
            scroller = self.driver.find_element(By.ID, "trending_scroller")
            self.driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scroller)
            time.sleep(2)
            self.driver.execute_script("arguments[0].scrollLeft = 0", scroller)
            time.sleep(2)
        except Exception as e:
            print(f"Scroller error: {e}")

        cards = self.driver.find_elements(By.CSS_SELECTOR, ".card.style_1")
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
                    results.append(ScrappingSettings(title=title, release_date=release_date))
            except Exception:
                continue

        return results