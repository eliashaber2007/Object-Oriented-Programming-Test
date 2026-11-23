# Design patterns (slide 84)

Each exercise takes the "spaghetti" code from the course and refactors it with one pattern. The UML diagram for each solution is below, drawn before coding.

Run any file with `python3 <file>.py`.

| Family | Pattern | File | Problem it fixes |
| --- | --- | --- | --- |
| Creational | Factory Method | `creational/factory.py` | long if/elif on payment type |
| Creational | Builder | `creational/builder.py` | function with 17 parameters |
| Creational | Singleton | `creational/singleton.py` | config file loaded 4 times |
| Structural | Adapter | `structural/adapter.py` | legacy XML vs dashboard expecting JSON |
| Structural | Decorator | `structural/decorator.py` | boolean flags for order options |
| Behavioral | Strategy | `behavioral/strategy.py` | if/elif on report format |
| Behavioral | Template Method | `behavioral/template_method.py` | 3 pipelines with copy-pasted steps |

## Factory Method

```mermaid
classDiagram
    class PaymentProcessor {
        <<abstract>>
        +validate(details) bool
        +process(amount, details) dict
    }
    class PaymentFactory {
        -dict _processors
        +get_processor(payment_type) PaymentProcessor
    }
    PaymentProcessor <|-- CreditCardProcessor
    PaymentProcessor <|-- BankTransferProcessor
    PaymentProcessor <|-- PayPalProcessor
    PaymentFactory ..> PaymentProcessor : creates
```

## Builder

```mermaid
classDiagram
    class Employee {
        <<dataclass>>
        +first_name
        +last_name
        +email
        +department
        +position
        +salary
    }
    class EmployeeBuilder {
        -dict _data
        +with_name(first, last) EmployeeBuilder
        +with_email(email) EmployeeBuilder
        +with_job(department, position, salary) EmployeeBuilder
        +with_equipment(laptop, parking) EmployeeBuilder
        +with_access(vpn, admin) EmployeeBuilder
        +build() Employee
    }
    EmployeeBuilder <|-- DeveloperBuilder
    EmployeeBuilder ..> Employee : builds
```

## Singleton

```mermaid
classDiagram
    class ConfigManager {
        -ConfigManager _instance$
        -dict _config
        +get_instance()$ ConfigManager
        +get(key) any
    }
```

## Adapter

```mermaid
classDiagram
    class ReportGeneratorInterface {
        <<interface>>
        +generate(data) str
    }
    class LegacyReportGenerator {
        +generate_report(data) str
    }
    class LegacyReportAdapter {
        -LegacyReportGenerator _legacy
        +generate(data) str
    }
    ReportGeneratorInterface <|-- LegacyReportAdapter
    LegacyReportAdapter o-- LegacyReportGenerator : wraps
    AnalyticsDashboard ..> ReportGeneratorInterface : uses JSON from
```

## Decorator

```mermaid
classDiagram
    class OrderComponent {
        <<interface>>
        +get_cost() float
        +get_description() str
    }
    class OrderDecorator {
        -OrderComponent _order
    }
    OrderComponent <|-- BaseOrder
    OrderComponent <|-- OrderDecorator
    OrderDecorator o-- OrderComponent : wraps
    OrderDecorator <|-- ExpressShippingDecorator
    OrderDecorator <|-- InsuranceDecorator
    OrderDecorator <|-- GiftWrapDecorator
    OrderDecorator <|-- DiscountDecorator
    OrderDecorator <|-- PremiumMemberDecorator
```

## Strategy

Problems with the original code: adding a format means editing `generate_report` and `save_report` (breaks Open/Closed), every format is tested through one big function, formats can't be switched cleanly at runtime, and the if/elif is duplicated in two methods.

```mermaid
classDiagram
    class FormatStrategy {
        <<interface>>
        +format(data) str
        +extension() str
    }
    class ReportGenerator {
        -list data
        -FormatStrategy _strategy
        +set_strategy(strategy)
        +generate_report() str
        +save_report(filename)
    }
    ReportGenerator o-- FormatStrategy
    FormatStrategy <|-- PDFFormatStrategy
    FormatStrategy <|-- ExcelFormatStrategy
    FormatStrategy <|-- CSVFormatStrategy
    FormatStrategy <|-- JSONFormatStrategy
    FormatStrategy <|-- HTMLFormatStrategy
```

## Template Method

Problems with the original code: validation, loading and cleanup were copied 3 times, adding logging means editing 3 classes, and nothing stopped a pipeline from skipping a step.

```mermaid
classDiagram
    class DataPipeline {
        <<abstract>>
        #str source
        #list data
        +run() str
        +connect()
        +validate()
        +load()
        +cleanup()
        +name()* str
        +extract()*
        +transform()*
        +required_fields()* list
    }
    DataPipeline <|-- CSVPipeline
    DataPipeline <|-- APIPipeline
    DataPipeline <|-- DatabasePipeline
    DataPipeline <|-- XMLPipeline
```
