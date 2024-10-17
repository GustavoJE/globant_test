import pytest
from helpers.functions import validate_csv
from fastapi import HTTPException

# Mock file class for testing
class MockFile:
    def __init__(self, filename):
        self.filename = filename

# Test cases
def test_valid_csv_file():
    valid_file = MockFile("data.csv")
    # Assert no exception is raised
    validate_csv(valid_file)

def test_invalid_csv_file():
    invalid_file = MockFile("data.txt")
    # Assert that the HTTPException is raised
    with pytest.raises(HTTPException) as exc_info:
        validate_csv(invalid_file)
    
    # Assert the status code and detail of the exception
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "File must be a CSV."