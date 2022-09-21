from filestack import Client


class FileSharer:
    def __init__(self, filepath, api_key='AViVqp7suSQWWEdr16hf9z'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url