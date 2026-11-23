from dataclasses import dataclass
from typing import Optional


@dataclass
class Employee:
    """The product: just holds the final record."""
    first_name: str
    last_name: str
    email: str
    department: str
    position: str
    salary: float
    start_date: Optional[str] = None
    manager_id: Optional[int] = None
    phone: Optional[str] = None
    has_parking: bool = False
    has_laptop: bool = False
    has_vpn_access: bool = False
    has_admin_rights: bool = False
    office_location: Optional[str] = None
    contract_type: str = "permanent"


class EmployeeBuilder:
    """Builds an Employee step by step. Each method returns self so calls can be chained."""

    def __init__(self):
        self._data = {}

    def with_name(self, first_name: str, last_name: str):
        self._data["first_name"] = first_name
        self._data["last_name"] = last_name
        return self

    def with_email(self, email: str):
        self._data["email"] = email
        return self

    def with_job(self, department: str, position: str, salary: float):
        self._data["department"] = department
        self._data["position"] = position
        self._data["salary"] = salary
        return self

    def with_contact(self, phone: str = None, manager_id: int = None):
        self._data["phone"] = phone
        self._data["manager_id"] = manager_id
        return self

    def with_equipment(self, laptop: bool = False, parking: bool = False):
        self._data["has_laptop"] = laptop
        self._data["has_parking"] = parking
        return self

    def with_access(self, vpn: bool = False, admin: bool = False):
        self._data["has_vpn_access"] = vpn
        self._data["has_admin_rights"] = admin
        return self

    def with_contract(self, contract_type: str, start_date: str, office: str = None):
        self._data["contract_type"] = contract_type
        self._data["start_date"] = start_date
        self._data["office_location"] = office
        return self

    def build(self) -> Employee:
        # All validation in one place
        if not self._data.get("first_name") or not self._data.get("last_name"):
            raise ValueError("Name is required")
        if "@" not in self._data.get("email", ""):
            raise ValueError("Valid email is required")
        if self._data.get("salary", 0) < 0:
            raise ValueError("Salary cannot be negative")
        return Employee(**self._data)


class DeveloperBuilder(EmployeeBuilder):
    """Preset: a developer always gets a laptop and VPN access."""

    def __init__(self, first_name: str, last_name: str, email: str):
        super().__init__()
        self.with_name(first_name, last_name)
        self.with_email(email)
        self.with_job("Engineering", "Developer", 60000)
        self.with_equipment(laptop=True)
        self.with_access(vpn=True)


if __name__ == "__main__":
    employee = (
        EmployeeBuilder()
        .with_name("John", "Doe")
        .with_email("john.doe@company.com")
        .with_job("Engineering", "Senior Developer", 75000)
        .with_equipment(laptop=True, parking=False)
        .with_access(vpn=True, admin=True)
        .build()
    )
    print(employee)

    dev = DeveloperBuilder("John", "Doe", "john.doe@company.com").build()
    print(dev)
