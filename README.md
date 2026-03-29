# Weather CLI 

A simple command-line weather app built with Python, using the OpenWeatherMap API and `rich` for terminal formatting.

## Features

- Current temperature with feels-like
- Weather description
- Humidity
- Wind speed
- Color-coded output based on temperature and wind intensity
- Multi-language support

## Installation

```bash
git clone https://github.com/kaysba/Weather-CLI.git
cd Weather-CLI
pip install -r requirements.txt
```

Create a `.env` file at the root of the project:

```
API_KEY=your_openweathermap_api_key
```

> Get a free API key at [openweathermap.org](https://openweathermap.org/api)

## Usage

```bash
python main.py --city Nice
python main.py --city Paris --lang fr
python main.py --city London --lang en
```

### Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--city` | City name (required) | — |
| `--lang` | Language code (`en`, `fr`, `ar`...) | `en` |

## Project Structure

```
Weather-CLI/
├── api.py        # Fetches data from OpenWeatherMap
├── display.py    # Handles terminal output with rich
├── main.py       # Entry point, argument parsing
├── .env          # API key (not committed)
└── README.md
```

## Requirements

- Python 3.x
- `requests`
- `python-dotenv`
- `rich`

Installation using command line :
```bash
pip install -r requirements.txt
```