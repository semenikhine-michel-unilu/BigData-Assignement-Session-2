# Scrapy Books Spider - SEMENIKHINE MICHEL

## Project Overview

This project is a web scraping tool built using the Scrapy framework. It scrapes book data from a target e-commerce website (e.g., "Books to Scrape") and extracts useful information such as book titles, prices, and availability. The data can be output in multiple formats such as JSON, CSV, or directly stored in a database (MongoDB or SQL).

## Features

- Extracts book data (title, price, and availability) from the website.
- Handles pagination to scrape multiple pages.
- Supports output in various formats (e.g., JSON, CSV).
- Includes a pipeline to store data in MongoDB (optional).

## Prerequisites

Before running the project, ensure that you have the following installed :

1. Python 3.7 or higher
2. Scrapy (can be installed via pip)
3. MongoDB (optional, only needed for database integration)

## Installation

### Step 1: Clone the repository

Clone this project to your local machine using the following command :

```bash
git clone https://github.com/semenikhine-michel-unilu/BigData-Assignement-Session-2.git
cd BigData-Assignement-Session-2
```

### Step 2: Set up the environment

Install the necessary Python dependencies. It is recommended to use a virtual environment :

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install Scrapy and dependencies
pip install scrapy
```

### Step 3: Project Structure

```bash
book_scraper_folder/
├──scrapy.cfg
├──books.json
|                     # List of scraped books
└──book_scraper/
│   ├── __pycache__/ 
│   |
│   ├──__init__.py
│   ├──items.py               # Defines the data fields for book items
│   ├──middlewares.py         # Middlewares for processing requests and responses
│   ├──pipelines.py           # Data processing and storage logic (MongoDB, etc.)
│   ├──settings.py            # Configuration for the Scrapy project
|   |
│   └──spiders/
|      ├──__pycache__/
|      |
│      ├──__init__.py
│      └──books_spider.py   # Spider that scrapes the target website
│   
├──scrapy_env/                # Scrapy environment
└──README.md                  # Project documentation
```

## How the Spider Works
### Spider Logic
The spider, located in the books_spider.py file, performs the following tasks:

1. Target URL : The spider starts at the main page of the website.
2. Data Extraction : It extracts book details such as:
    - Title
    - Price
    - Availability
3. Pagination : The spider navigates through multiple pages to scrape all available books.
4. Output: Data is output to a file (e.g., JSON or CSV) or stored in MongoDB via the pipeline.


### Core Spider Code
Here’s a simplified breakdown of how the spider operates:

- Start Requests : The spider starts by making a request to the base URL.

- Parse Method : For each page, the spider identifies and extracts the required information (book title, price, and availability).

- Pagination : After processing the current page, it looks for a "next" button to continue scraping subsequent pages.

### Fields

The spider extracts the following fields from each book:

- title: The title of the book.
- price: The price of the book (e.g., "£45.00").
- availability: Availability status (e.g., "In stock").



## How to Run the Project
### Step 1: Run the Spider
Navigate to the project directory and run the spider using the following command :
```bash
scrapy crawl books -o books.json --loglevel=DEBUG
```

This will run the "books" spider and output the scraped data into a books.json file.

-> You can change the output format by specifying the desired file format (e.g., CSV, JSON) as shown below :
```bash
# Output as CSV
scrapy crawl books -o books.csv

# Output as JSON
scrapy crawl books -o books.json
```

### Step 3: Running in Debug Mode
To see detailed log output while the spider runs, you can use :
```bash
scrapy crawl books --loglevel=DEBUG
```