from abc import ABC, abstractmethod


class BaseCDR(ABC):
    """Base class for scanning different types of models."""

    def __init__(self, model_path, model_type):
        self._path = model_path
        self._type = model_type
        self._anomaly = False
        self._result = {
            "bad_locations": [],
            "bad_calls": [],
            "bad_signals": [],
            "bad_files": [],
            "bad_shell_cmds": [],
            "bad_chars": [],
            "bad_cmds": [],
            "bad_modules": [],
            "bad_imports": []
        }

    @abstractmethod
    def scan(self):
        """Implement scanning logic in subclasses."""
        pass

    @abstractmethod
    def analyze(self):
        """Implement analysis logic in subclasses."""
        pass

    @abstractmethod
    def disarm(self):
        """Implement disarming logic in subclasses."""
        pass

    @abstractmethod
    def save_as_new_file(self, path):
        """Save the cleaned or modified file as a new file."""
        pass

    @staticmethod
    def create_instance(path, model_type):
        if model_type == "h5":
            return H5_CDR(path)
        elif model_type == "dill":
            return Dill_CDR(path)
        else:
            raise ValueError(f"Unsupported model type: {model_type}")

