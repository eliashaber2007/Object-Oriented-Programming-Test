# ABCD Records: Level 1

## Task 1.1: Use case diagram

```mermaid
flowchart LR
    Member((Member))
    Clerk((Order Processing Clerk))
    subgraph ABCD Records system
        PO([Place Order])
        MP([Make Payment])
        VM([Verify Membership])
        PRO([Process Order])
    end
    Member --- PO
    Member --- MP
    Clerk --- VM
    Clerk --- PRO
```

## Task 1.2: Class diagram

People classes take their methods from the use case diagram. Order is a thing, so its methods manage its own data (`calculateTotal()` fills in `totalAmount`).

```mermaid
classDiagram
    class Member {
        -int id
        -String name
        -String password
        -String address
        +placeOrder()
        +makePayment()
    }
    class Order {
        -int id
        -Date date
        -float totalAmount
        -String status
        +addItem()
        +calculateTotal()
    }
    class OrderProcessingClerk {
        -int id
        -String name
        -String password
        +verifyMembership()
        +processOrder()
    }
    Member "1" -- "0..*" Order
    Order "0..*" -- "1" OrderProcessingClerk
```
