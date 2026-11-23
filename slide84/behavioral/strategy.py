import json
from abc import ABC, abstractmethod


class FormatStrategy(ABC):
    """Every format must know how to build its report and its file extension."""

    @abstractmethod
    def format(self, data: list) -> str:
        pass

    @abstractmethod
    def extension(self) -> str:
        pass


class PDFFormatStrategy(FormatStrategy):
    def format(self, data: list) -> str:
        report = "PDF REPORT\n" + "=" * 50 + "\n"
        for item in data:
            report += f"| {item['name']:20} | {item['value']:10} |\n"
        return report + "=" * 50 + "\nEnd of PDF Report"

    def extension(self) -> str:
        return ".pdf"


class ExcelFormatStrategy(FormatStrategy):
    def format(self, data: list) -> str:
        report = "EXCEL REPORT\n" + "-" * 50 + "\nName\tValue\n"
        for item in data:
            report += f"{item['name']}\t{item['value']}\n"
        return report + "-" * 50 + "\n"

    def extension(self) -> str:
        return ".xlsx"


class CSVFormatStrategy(FormatStrategy):
    def format(self, data: list) -> str:
        report = "name,value\n"
        for item in data:
            report += f"{item['name']},{item['value']}\n"
        return report

    def extension(self) -> str:
        return ".csv"


class JSONFormatStrategy(FormatStrategy):
    def format(self, data: list) -> str:
        return json.dumps(data, indent=2)

    def extension(self) -> str:
        return ".json"


# Added later WITHOUT touching any class above (Open/Closed)
class HTMLFormatStrategy(FormatStrategy):
    def format(self, data: list) -> str:
        rows = "".join(f"<tr><td>{item['name']}</td><td>{item['value']}</td></tr>" for item in data)
        return f"<table><tr><th>Name</th><th>Value</th></tr>{rows}</table>"

    def extension(self) -> str:
        return ".html"


class ReportGenerator:
    """The context: uses whichever strategy it is given."""

    def __init__(self, data: list, strategy: FormatStrategy = None):
        self.data = data
        self._strategy = strategy

    def set_strategy(self, strategy: FormatStrategy):
        self._strategy = strategy

    def generate_report(self) -> str:
        return self._strategy.format(self.data)

    def save_report(self, filename: str):
        with open(filename + self._strategy.extension(), "w") as f:
            f.write(self.generate_report())


if __name__ == "__main__":
    data = [
        {"name": "Sales Q1", "value": 15000},
        {"name": "Sales Q2", "value": 18000},
        {"name": "Sales Q3", "value": 22000},
        {"name": "Sales Q4", "value": 25000},
    ]
    generator = ReportGenerator(data)

    for title, strategy in [
        ("PDF", PDFFormatStrategy()),
        ("CSV", CSVFormatStrategy()),
        ("JSON", JSONFormatStrategy()),
        ("HTML (NEW!)", HTMLFormatStrategy()),
    ]:
        print(f"=== {title} FORMAT ===")
        generator.set_strategy(strategy)
        print(generator.generate_report())
        print("\n" + "=" * 60 + "\n")
