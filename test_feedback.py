import os
import pytest


def file_exists(file_path):
    print(f"Checking if {file_path} exists: {os.path.isfile(file_path)}")
    return os.path.isfile(file_path)


def test_feedback_file_exists():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(root_dir, "feedback.txt")
    assert file_exists(file_path) == True


if __name__ == "__main__":
    pytest.main()
