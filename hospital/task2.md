# Task 2: Complete class diagram + sequence diagram

## Class diagram

The patient's problem is no longer an attribute of Patient. It has its own details (description, date), so it becomes its own class.

- Patient owns its health problems (composition): if the patient is deleted, their problems go too.
- A health problem owns its prescription (composition).
- Doctor writes prescriptions (plain association): a prescription still exists if the doctor leaves.
- Payment types use inheritance. Each child rewrites `process()`.

```mermaid
classDiagram
    class Patient {
        -int id
        -String name
        -String password
        +login()
        +postProblem()
        +pay()
    }
    class Organizer {
        -int id
        -String name
        -String password
        +login()
        +readProblem()
        +consultDoctor()
        +sendPrescription()
        +forwardPayment()
        +createMember()
        +maintainSystem()
    }
    class Doctor {
        -int id
        -String name
        -String password
        -String department
        +login()
        +providePrescription()
        +receivePayment()
    }
    class HealthProblem {
        -int id
        -String description
        -Date date
    }
    class Prescription {
        -int id
        -String medication
        -Date date
    }
    class Payment {
        -int id
        -float amount
        -Date date
        +process()
    }
    class Cash {
        +process()
    }
    class Check {
        -String checkNumber
        -String bankName
        +process()
    }
    class CreditCard {
        -String cardNumber
        -String expiryDate
        +process()
    }

    Patient "0..*" -- "1" Organizer
    Organizer "1" -- "1..*" Doctor
    Patient "1" *-- "0..*" HealthProblem
    HealthProblem "1" *-- "0..1" Prescription
    Doctor "1" -- "0..*" Prescription
    Patient "1" -- "0..*" Payment
    Payment <|-- Cash
    Payment <|-- Check
    Payment <|-- CreditCard
```

## Sequence diagram: a patient submits a problem, receives a prescription and pays

Only arrow 3 is dashed, because it is the doctor's direct reply to request 2.

```mermaid
sequenceDiagram
    actor Patient
    participant Organizer
    participant Doctor
    Patient->>Organizer: postProblem(problem)
    Organizer->>Doctor: consultDoctor(problem)
    Doctor-->>Organizer: prescription
    Organizer->>Patient: sendPrescription(prescription)
    Patient->>Organizer: pay(amount)
    Organizer->>Doctor: forwardPayment(amount)
```
