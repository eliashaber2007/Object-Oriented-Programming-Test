import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


# Legacy reporting system (can't modify - external library)
class LegacyReportGenerator:
    def generate_report(self, data: dict) -> str:
        """Returns XML format - old system"""
        xml = "<report>\n"
        for key, value in data.items():
            xml += f"  <{key}>{value}</{key}>\n"
        xml += "</report>"
        return xml


# New analytics dashboard expects JSON
class AnalyticsDashboard:
    def display(self, json_data: str):
        data = json.loads(json_data)
        print("=== Analytics Dashboard ===")
        for key, value in data.items():
            print(f"  {key}: {value}")


class ReportGeneratorInterface(ABC):
    """What the dashboard expects: something that returns JSON."""

    @abstractmethod
    def generate(self, data: dict) -> str:
        pass


class LegacyReportAdapter(ReportGeneratorInterface):
    """Wraps the legacy XML generator and converts its output to JSON."""

    def __init__(self, legacy: LegacyReportGenerator):
        self._legacy = legacy

    def generate(self, data: dict) -> str:
        xml_report = self._legacy.generate_report(data)
        root = ET.fromstring(xml_report)
        result = {}
        for child in root:
            result[child.tag] = self._convert(child.text)
        return json.dumps(result)

    @staticmethod
    def _convert(text: str):
        # XML only stores text, so turn numbers back into numbers
        try:
            return int(text)
        except ValueError:
            try:
                return float(text)
            except ValueError:
                return text


def show_sales_report(report_generator, dashboard):
    json_report = report_generator.generate({"total_sales": 150000, "orders": 1234, "avg_order": 121.55})
    dashboard.display(json_report)


def show_inventory_report(report_generator, dashboard):
    json_report = report_generator.generate({"total_items": 5000, "low_stock": 45, "out_of_stock": 12})
    dashboard.display(json_report)


if __name__ == "__main__":
    report_generator = LegacyReportAdapter(LegacyReportGenerator())
    dashboard = AnalyticsDashboard()

    show_sales_report(report_generator, dashboard)
    show_inventory_report(report_generator, dashboard)
