import os
import logging
from collections import Counter

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Get the absolute path of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

def analyze_text(filename=file_path):
    """Analyzes the text file for word count and occurrences of a user-specified word.

    Args:
        filename (str): The name of the file to analyze.
    """
    if not os.path.exists(filename):
        logger.error(f"File {filename} not found!")
        return

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        words = text.split()
        total_words = len(words)
        word_freq = Counter(words)

        logger.info(f"Total number of words in the text: {total_words}")

        search_word = input("Enter the word you want to check occurrences for: ").strip()
        occurrences = word_freq.get(search_word, 0)
        logger.info(f"The word '{search_word}' occurs {occurrences} times in the text.")

        # Additional statistics
        unique_words = len(word_freq)
        most_common = word_freq.most_common(10)

        logger.info(f"Total unique words: {unique_words}")
        logger.info("Top 10 most common words:")
        for word, count in most_common:
            logger.info(f"{word}: {count} times")

    except Exception as e:
        logger.exception("An error occurred while analyzing the text.")


if __name__ == "__main__":
    analyze_text()
