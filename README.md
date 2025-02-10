Word Replacement & Text Analysis Project


Overview


This Python project automates downloading a text file from a GitHub repository, performs word replacements based on a CSV file (mapping.csv), and generates a modified text file (output.txt). Additionally, it provides text analysis, including word count and frequency statistics.



Features


Downloads a text file from a GitHub repository.



Replaces words in input.txt based on mapping.csv (mapping.csv file should be in Desktop).


Saves the modified content in output.txt.


Logs details of replacements, including occurrences.


Provides word count statistics.


Allows users to check occurrences of a specific word in the text.


Handles missing files and errors gracefully with logging.



Project Structure



Appl-project/                               # Root directory of the project



│── Dockerfile                              # Instructions to build a Docker container for the project


│── Makefile                                # Makefile with predefined commands for running, testing, etc.


│── README.md                               # Project documentation


│── docker-compose.yml                      # Docker Compose configuration file for managing multi-container setup


│── pyproject.toml                          # Project configuration and dependencies (for modern Python projects)


│── requirements.txt                        # List of required Python packages


│


│── appl_project/                           # Main application directory


│   │── __init__.py                         # Marks this directory as a Python package


│   │── dry_run_replace.py                  # Script for a dry-run version of text replacement logic


│   │── run_count.py                        # Script to analyze text from input.txt


│   │── run_replace.py                      # Script to perform actual text replacement


│   │── sync_data.py                        # Script to fetch and save data as input.txt


│


│── tests/                                  # Directory containing unit tests


│   │── __init__.py                         # Marks this directory as a test package


│   │── test_dry_run_replace.py             # Tests for dry_run_replace.py


│   │── test_run_count.py                   # Tests for run_count.py


│   │── test_run_replace.py                 # Tests for run_replace.py


│   │── test_sync_data.py                   # Tests for sync_data.py





Prerequisites



Ensure you have Python 3.11+ installed. You also need pandas:


pip install pandas



Usage


1.Downloading the Input Text File


Run the script to fetch the file from GitHub and save it as input.txt:


python sync_data.py


2. Performing Word Replacement


Run the script to replace words and generate output.txt:

python run_replace.py


3. Analyzing Word Statistics


Run the script to analyze word count and check specific word occurrences:


python run_count.py


Example: mapping.csv


old_word,new_word
Harry,Sujit
Ron,Jerry
Hermione,Ariya




Error Handling


If mapping.csv or input.txt is missing, an error is logged.


If a word in mapping.csv is not found in input.txt, a log entry is created.


If the GitHub link is incorrect, an error is logged.





Steps to run smoothly



Running with python

Appl-project/appl_project$ python sync_data.py

Appl-project/appl_project$ python dry_run_replace.py

Appl-project/appl_project$ python run_count.py

Appl-project/appl_project$ python run_replace.py



Running Pytest without make and docker

Appl-project$ pytest



Running with Docker

sudo apt update -y

sudo apt install docker.io -y

docker build -t appl-project .

docker run --rm appl-project



Using docker compose

docker-compose up



Using Makefile

make install  # Install dependencies

make test     # Run tests

make run      # Download file and analyze it

make build    # Package the project

make clean    # Remove generated files


