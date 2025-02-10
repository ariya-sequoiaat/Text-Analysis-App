import requests
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define the GitHub raw file URL
GITHUB_RAW_URL = "https://raw.githubusercontent.com/amephraim/nlp/master/texts/J.%20K.%20Rowling%20-%20Harry%20Potter%201%20-%20Sorcerer's%20Stone.txt"


def download_story(github_raw_url=GITHUB_RAW_URL, filename="input.txt"):
    """Downloads the story from the given GitHub raw URL and saves it as input.txt in the script directory.

    Args:
        github_raw_url (str): The raw URL of the GitHub file to download.
        filename (str): The name of the file to save the content in.
    """
    try:
        response = requests.get(github_raw_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        # Get the current directory where the script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)

        # Save content to file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(response.text)

        logger.info(f"Story saved successfully as {filename} in {script_dir}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to download the story: {e}")


if __name__ == "__main__":
    try:
        download_story()
    except Exception as e:
        logger.exception("An unexpected error occurred.")
