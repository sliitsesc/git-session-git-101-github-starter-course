import os
import pytest


def any_markdown_file_exists(directory):
    for file_name in os.listdir(directory):
        if file_name.endswith(".md"):
            print(f"Markdown file found: {file_name}")
            return True
    print("No Markdown file found.")
    return False


def test_any_markdown_file_exists():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    assert any_markdown_file_exists(root_dir) == True


if __name__ == "__main__":
    pytest.main()
