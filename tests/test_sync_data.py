import pytest
import os
import requests
from unittest.mock import patch, MagicMock
from appl_project.sync_data import download_story
import logging

@pytest.fixture
def temp_directory(tmp_path):
    """Creates a temporary directory for testing."""
    return str(tmp_path)

@patch("requests.get")
def test_download_story_success(mock_get, temp_directory, caplog):
    """Tests successful file download and saving."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = "Mocked story content."
    mock_get.return_value = mock_response

    test_file = os.path.join(temp_directory, "test_input.txt")

    with caplog.at_level(logging.INFO):
        download_story(filename=test_file)

    # Check if the file was created
    assert os.path.exists(test_file)

    # Check file content
    with open(test_file, "r", encoding="utf-8") as file:
        content = file.read()
    assert content == "Mocked story content."

    # Check log messages
    assert f"Story saved successfully as {test_file}" in caplog.text

@patch("requests.get")
def test_download_story_http_error(mock_get, caplog):
    """Tests handling of HTTP error during download."""
    mock_get.side_effect = requests.exceptions.RequestException("HTTP Error")

    with caplog.at_level(logging.ERROR):
        download_story()

    assert "Failed to download the story: HTTP Error" in caplog.text
