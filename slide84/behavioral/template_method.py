import time
from abc import ABC, abstractmethod


class DataPipeline(ABC):
    """The workflow is fixed here once. Children only fill in the steps that differ."""

    def __init__(self, source: str):
        self.source = source
        self.data = None

    def run(self) -> str:
        """Template method: always the same order, no step can be skipped."""
        self.connect()
        self.extract()
        self.transform()
        self.validate()
        self.load()
        self.cleanup()
        return f"{self.name()} Pipeline finished"

    # Steps each pipeline must write
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def required_fields(self) -> list:
        pass

    # Shared steps, written once
    def connect(self):
        print(f"Connecting to {self.name()}: {self.source}")
        time.sleep(0.1)
        print(f"{self.name()} connection established")

    def validate(self):
        print("Validating data...")
        for record in self.data:
            for field in self.required_fields():
                if field not in record:
                    raise ValueError("Invalid record structure")
        print("Validation passed")

    def load(self):
        print("Loading data to destination...")
        time.sleep(0.1)
        print(f"Loaded {len(self.data)} records successfully")

    def cleanup(self):
        print("Cleaning up resources...")
        self.data = None
        print("Cleanup complete")


class CSVPipeline(DataPipeline):
    def name(self):
        return "CSV"

    def extract(self):
        print("Extracting data from CSV...")
        self.data = [{"id": 1, "name": "Alice", "age": 30}, {"id": 2, "name": "Bob", "age": 25}]

    def transform(self):
        for record in self.data:
            record["age"] = int(record["age"])
            record["name"] = record["name"].upper()

    def required_fields(self):
        return ["id", "name"]


class APIPipeline(DataPipeline):
    def name(self):
        return "API"

    def extract(self):
        print("Extracting data from API...")
        self.data = [
            {"user_id": 101, "username": "charlie", "score": 85},
            {"user_id": 102, "username": "diana", "score": 92},
        ]

    def transform(self):
        for record in self.data:
            record["score"] = int(record["score"])
            record["username"] = record["username"].lower()
            record["grade"] = "A" if record["score"] >= 90 else "B"

    def required_fields(self):
        return ["user_id", "username"]


class DatabasePipeline(DataPipeline):
    def name(self):
        return "Database"

    def extract(self):
        print("Extracting data from database...")
        self.data = [
            {"product_id": 501, "product_name": "laptop", "price": 1200},
            {"product_id": 502, "product_name": "mouse", "price": 25},
        ]

    def transform(self):
        for record in self.data:
            record["price"] = float(record["price"])
            record["product_name"] = record["product_name"].title()
            record["tax"] = record["price"] * 0.2

    def required_fields(self):
        return ["product_id", "price"]


# New pipeline added without changing the workflow
class XMLPipeline(DataPipeline):
    def name(self):
        return "XML"

    def extract(self):
        print("Extracting data from XML...")
        self.data = [{"order_id": 9001, "total": "49.90"}, {"order_id": 9002, "total": "15.00"}]

    def transform(self):
        for record in self.data:
            record["total"] = float(record["total"])

    def required_fields(self):
        return ["order_id", "total"]


if __name__ == "__main__":
    for pipeline in [
        CSVPipeline("data/users.csv"),
        APIPipeline("https://api.example.com/users"),
        DatabasePipeline("postgresql://localhost/mydb"),
        XMLPipeline("data/orders.xml"),
    ]:
        print(f"RUNNING {pipeline.name().upper()} PIPELINE")
        print("=" * 70)
        print(f"\n{pipeline.run()}\n")
