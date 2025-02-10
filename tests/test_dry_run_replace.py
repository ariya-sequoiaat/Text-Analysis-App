import sys
import os
import pytest
import logging
from collections import Counter
from appl_project.dry_run_replace import analyze_text

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def create_test_file(filename, content):
    """Creates a test file with given content."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def test_analyze_text(caplog):
    """Tests the analyze_text function for correct word analysis."""
    test_filename = "test_input.txt"
    test_content = "hello world hello pytest pytest pytest"

    # Create a test input file
    create_test_file(test_filename, test_content)

    with caplog.at_level(logging.INFO):
        analyze_text(test_filename)

    # Check if word count and frequency are logged correctly
    assert "Total number of words in the text: 6" in caplog.text
    assert "Total unique words: 3" in caplog.text
    assert "hello: 2 times" in caplog.text
    assert "pytest: 3 times" in caplog.text
    assert "world: 1 times" in caplog.text

    # Cleanup test file
    os.remove(test_filename)


if __name__ == "__main__":
    pytest.main()