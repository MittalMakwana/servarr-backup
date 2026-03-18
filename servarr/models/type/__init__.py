from abc import ABC, abstractmethod
import os


class Server(ABC):
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

    def get_instance_prefix(self):
        return getattr(self, "instance_name", "").strip().strip("/")

    def build_backup_s3_key(self, backup_path):
        filename = os.path.basename(backup_path)
        instance_prefix = self.get_instance_prefix()
        return f"{instance_prefix}/{filename}" if instance_prefix else filename

    @abstractmethod
    def create_backup(self):
        raise NotImplementedError

    # @abstractmethod
    # def restore_backup(self):
    #     raise NotImplementedError
