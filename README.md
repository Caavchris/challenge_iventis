# Movies Search

A simple Python project to fetch trending movies and using:
- TMDb API
- Web scraping

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with:
```env
API_KEY="34d00162b775b382e621499b550cc14d"  # Shared API key for testing
API_URL="https://api.themoviedb.org/3"
URL_SCRAPPING="https://www.themoviedb.org/"
```

Note: A TMDb API key is already provided for testing purposes. If you want to use your own key, you can get one by signing up at [TMDb website](https://www.themoviedb.org/signup).

## Usage

### API Method
```bash
python -m src.main_api
```
Results will be saved to `output/movies_api.csv`

### Web Scraping Method
```bash
python -m src.main_scrapping
```
Results will be saved to `output/movies_scrapping.csv`

Both methods will save the movie titles and release dates to CSV files and display the results in the console.