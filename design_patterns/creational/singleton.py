import json
import os


class ConfigManager:
    """Loads config.json once, then everyone shares the same instance."""

    _instance = None

    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), "config.json")
        print("Loading config file...")
        with open(path, "r") as f:
            self._config = json.load(f)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def get(self, key: str):
        """Reads nested values with dots, e.g. get('database.host')."""
        value = self._config
        for part in key.split("."):
            value = value[part]
        return value


def start_application():
    config = ConfigManager.get_instance()
    print(f"Starting {config.get('app.name')} (debug={config.get('app.debug')})")


def connect_database():
    config = ConfigManager.get_instance()
    print(f"Connecting to database at {config.get('database.host')}:{config.get('database.port')}")


def send_email(to: str, subject: str):
    config = ConfigManager.get_instance()
    print(f"Sending email from {config.get('email.sender')} via {config.get('email.smtp_host')}")


def process_payment(amount: float):
    config = ConfigManager.get_instance()
    print(f"Processing {amount}€ in {config.get('payment.environment')} mode")


if __name__ == "__main__":
    start_application()
    connect_database()
    send_email("user@test.com", "Welcome")
    process_payment(99.99)

    # Same object every time: the file was only read once
    print(ConfigManager.get_instance() is ConfigManager.get_instance())
