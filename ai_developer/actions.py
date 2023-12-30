import os
import random
import string
from typing import Any, Dict

from ftp.ftp_actions import FTPActions
from rich.console import Console
from rich.theme import Theme

from e2b import Sandbox  # You may want to modify this import to change functionality

REPO_DIRECTORY = "/home/user/repo"

custom_theme = Theme({
    "info": "dim cyan",
    "warning": "yellow",
    "error": "bold red",
    "success": "bold green",
})

console = Console(theme=custom_theme)


class ActionsAdapter:
    def __init__(self, use_ftp=False):
        self.use_ftp = use_ftp
        if use_ftp:
            self.ftp_actions = FTPActions('ftp.yourserver.com')  # Change host to your FTP server

    def create_directory(self, args):
        path = args.get('path')
        if self.use_ftp:
            self.ftp_actions.create_directory(path)
        else:
            sandbox = Sandbox()  # Initialize your sandbox or equivalent system here
            _dir = os.path.dirname(path)
            sandbox.filesystem.make_dir(_dir)

    def list_files(self, args):
        path = args.get('path')
        if self.use_ftp:
            files = self.ftp_actions.list_files(path)
        else:
            sandbox = Sandbox()  # Initialize your sandbox or equivalent system here
            files = sandbox.filesystem.list(path)

        response = "\n".join(
            [f"dir: {file.name}" if file.is_dir() else file.name for file in files]
        )
        return response

    def retrieve_file(self, args):
        remote_path = args.get('remote_path')
        local_path = args.get('local_path')

        if self.use_ftp:
            self.ftp_actions.retrieve_file(remote_path, local_path)
        else:
            # Logic for the equivalent GIT operation or sandbox retrieval
            pass

    def save_content_to_file(self, args):
        path = args.get('path')
        content = args.get('content')
        mode = args.get('mode', 'overwrite')

        if self.use_ftp:
            # FTP operation to save content to file goes here
            pass
        else:
            sandbox = Sandbox()  # Initialize your sandbox or equivalent system here
            sandbox.filesystem.write(path, content)

    def disconnect(self):
        if self.use_ftp:
            self.ftp_actions.disconnect()
        else:
            # If GIT operations or connections are done, disconnect or clean them up here
            pass

# You can add additional methods that perform the operations as required.
