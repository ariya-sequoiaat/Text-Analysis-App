import pytest
import os
import pandas as pd
from appl_project.run_replace import replace_words
import logging

@pytest.fixture
def setup_files(tmp_path):
    """Sets up temporary mapping and input files for testing."""
    # Create a temporary mapping CSV file
    mapping_file = tmp_path / "mapping.csv"
    mapping_data = "hello,hi\nworld,earth"
    mapping_file.write_text(mapping_data)

    # Create a temporary input file
    input_file = tmp_path / "input.txt"
    input_text = "hello world! Welcome to the world of Python."
    input_file.write_text(input_text)

    # Define the output file path
    output_file = tmp_path / "output.txt"

    return str(mapping_file), str(input_file), str(output_file)

def test_replace_words(setup_files, caplog):
    """Tests that words are correctly replaced."""
    mapping_file, input_file, output_file = setup_files

    with caplog.at_level(logging.INFO):
        replace_words(mapping_file, input_file, output_file)

    # Read the modified output file
    with open(output_file, "r", encoding="utf-8") as file:
        output_text = file.read()

    # Check if replacements occurred correctly
    assert "hi earth! Welcome to the earth of Python." == output_text

    # Check log messages
    assert "Replaced 'hello' with 'hi' 1 times." in caplog.text
    assert "Replaced 'world' with 'earth' 2 times." in caplog.text
    assert f"Word replacements completed. Output saved as {output_file}" in caplog.text

def test_missing_mapping_file(tmp_path, caplog):
    """Tests error handling when the mapping file is missing."""
    input_file = tmp_path / "input.txt"
    input_file.write_text("hello world!")

    output_file = tmp_path / "output.txt"

    with caplog.at_level(logging.ERROR):
        replace_words("non_existent.csv", str(input_file), str(output_file))

    assert "Mapping file non_existent.csv not found!" in caplog.text

def test_missing_input_file(tmp_path, caplog):
    """Tests error handling when the input file is missing."""
    mapping_file = tmp_path / "mapping.csv"
    mapping_file.write_text("hello,hi\nworld,earth")

    output_file = tmp_path / "output.txt"

    with caplog.at_level(logging.ERROR):
        replace_words(str(mapping_file), "non_existent.txt", str(output_file))

    assert "Input file non_existent.txt not found!" in caplog.text
