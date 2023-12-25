import os
from dotenv import load_dotenv
from e2b import Sandbox
import openai
import time
from ai_github_developer.actions import (
    create_directory,
    read_file,
    save_content_to_file,
    list_files,
    commit,
    make_pull_request,
    REPO_DIRECTORY,
)

import pyperclip

from rich import print
from rich.console import Console
from rich.theme import Theme
from rich.prompt import Prompt

class MyPrompt(Prompt):
    prompt_suffix = ""


custom_theme = Theme(
    {
        "theme": "bold #666666",
    }
)
console = Console(theme=custom_theme)


load_dotenv()
client = openai.Client()

AI_ASSISTANT_ID = os.getenv("AI_ASSISTANT_ID")
USER_GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

assistant = client.beta.assistants.retrieve(AI_ASSISTANT_ID)

def main():
    # Prompt the user to select an option to work with: repository, ftp, or local folder
    work_option = console.input(
        "Select an option to work with [repository/ftp/local]: "
    ).strip().lower()

    if work_option == 'repository':
        # Existing functionality to work with repository
        pass  # This will be replaced with the existing code
    elif work_option == 'ftp':
        # Placeholder for future FTP functionality
        print("FTP option is not implemented yet.")
    elif work_option == 'local':
        # Implementation of local folder functionality with pyperclip support
        path = console.input("Enter the path of the local file to paste content into: ")
        clipboard_content = pyperclip.paste()
        with open(path, 'w') as file:
            file.write(clipboard_content)
        print("Content pasted into", path)
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()