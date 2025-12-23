from flask import send_from_directory

class StorageController:
    def public(self, path, filename):
        return send_from_directory(f'static/{path}', filename)
