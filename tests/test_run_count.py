import pytest
import sys
import io
from appl_project.run_count import analyze_text

def test_analyze_text(monkeypatch, caplog, tmp_path):
    """Tests analyze_text function using monkeypatch for input and tmp_path for test files."""

    # Create a temporary test file
    test_file = tmp_path / "test_input.txt"
    test_file.write_text("python is great. python is powerful. python is easy.")

    # Mock input function to simulate user entering 'python'
    monkeypatch.setattr("builtins.input", lambda _: "python")

    # Capture logs
    with caplog.at_level("INFO"):
        analyze_text(str(test_file))

    # Assertions to check expected log messages
    assert "Total number of words in the text: 9" in caplog.text
    assert "The word 'python' occurs 3 times in the text." in caplog.text
