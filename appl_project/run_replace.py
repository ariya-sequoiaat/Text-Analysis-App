import os
import sys
import logging
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def replace_words(mapping_file="/mnt/c/Users/SAT-1070/Desktop/mapping.csv", input_file="input.txt",
                  output_file="output.txt"):
    """Replaces words in input.txt based on mapping.csv and saves the result in output.txt.

    Args:
        mapping_file (str): Path to the CSV file containing word mappings.
        input_file (str): Path to the input text file.
        output_file (str): Path to save the output text file.
    """
    if not os.path.exists(mapping_file):
        logger.error(f"Mapping file {mapping_file} not found!")
        return

    if not os.path.exists(input_file):
        logger.error(f"Input file {input_file} not found!")
        return

    try:
        # Load mapping
        df = pd.read_csv(mapping_file, header=None, names=["old_word", "new_word"], dtype=str)

        # Read input file
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Replace words
        for _, row in df.iterrows():
            old_word, new_word = row["old_word"], row["new_word"]
            occurrences = text.count(old_word)
            if occurrences > 0:
                text = text.replace(old_word, new_word)
                logger.info(f"Replaced '{old_word}' with '{new_word}' {occurrences} times.")
            else:
                logger.info(f"'{old_word}' not found in the text.")

        # Save the modified text
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(text)

        logger.info(f"Word replacements completed. Output saved as {output_file}")
    except Exception as e:
        logger.exception("An error occurred during word replacement.")


if __name__ == "__main__":
    replace_words()
