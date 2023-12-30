import ftplib
import os


class FTPActions:
    def __init__(self, host, port=21):
        self.host = host
        self.port = port
        self.ftp = ftplib.FTP()

    def connect(self, username, password):
        try:
            self.ftp.connect(self.host, self.port)
            self.ftp.login(username, password)
            print("Connected to FTP server.")
        except Exception as e:
            print(f"FTP connection failed: {e}")

    def list_files(self, path):
        try:
            file_list = self.ftp.nlst(path)
            return file_list
        except ftplib.error_perm as e:
            print(f"Error listing files: {e}")
            return []

    def create_directory(self, dirname):
        try:
            self.ftp.mkd(dirname)
            print(f"Created directory '{dirname}'.")
        except ftplib.error_perm as e:
            print(f"Error creating directory: {e}")

    def retrieve_file(self, remote_path, local_path):
        try:
            with open(local_path, 'wb') as f:
                self.ftp.retrbinary(f'RETR {remote_path}', f.write)
            print(f"Retrieved file '{remote_path}'.")
        except ftplib.error_perm as e:
            print(f"Error retrieving file: {e}")

    def disconnect(self):
        self.ftp.quit()
        print("Disconnected from FTP server.")
