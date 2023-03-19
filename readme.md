# Requiem
```commandline
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░███░░░░░░██░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█
█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░███░░▄▀░░██░░▄▀░░█░░░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░████░░▄▀░░███░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░█████████░░▄▀░░░░░░▄▀░░░░░░▄▀░░█
█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░██░░░░░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░█████████░░▄▀░░██████████░░▄▀░░█
█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██████████░░▄▀░░█
█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█
█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
```

Requiem is a web scraping tool built in Python using only the `requests` library. It allows you to easily scrape web pages and download files.

## Installation

To install Requiem, clone this repository and install the required dependencies:

```commandline
git clone https://github.com/yourusername/requiem.git
cd requiem
pip install -r requirements.txt
```
or
```commandline
pip install requiem-webscraper
```

## Usage

To use Requiem, run the `scraper.py` script and provide the URL you want to scrape as an argument:

```commandline
python scraper.py https://example.com
```

By default, Requiem will scrape up to a depth of 1. You can specify a greater depth by providing a second argument:

```commandline
python scraper.py https://example.com 2
```

To download files, Requiem looks for links that point to files with extensions such as `.jpg`, `.pdf`, or `.docx`. If a file is found, it will be downloaded to the directory where the script is running from.

## Contributing

If you would like to contribute to Requiem, please open a pull request or issue on the GitHub repository. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Just replace yourusername in the installation instructions with your actual GitHub username.