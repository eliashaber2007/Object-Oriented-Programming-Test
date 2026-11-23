# ABCD Records: Level 2

## Task 2.1: Complete use case diagram

- `<<include>>` = always happens, arrow from the main use case to the included one.
- `<<extend>>` = only sometimes (e.g. only Royal members), arrow from the optional use case to the main one.

```mermaid
flowchart LR
    Member((Member))
    NonMember((Non-Member))
    Clerk((Order Processing Clerk))
    Collection((Collection Department Clerk))
    subgraph ABCD Records system
        PO([Place Order])
        VIA([Verify Item Availability])
        AD([Apply Discount])
        OUI([Order Unavailable Items])
        MP([Make Payment])
        VM([Verify Membership])
        PRO([Process Order])
        PI([Print Invoice])
        PSL([Print Shipping List])
        SMA([Send Membership Application])
    end
    Member --- PO
    Member --- MP
    NonMember --- SMA
    Clerk --- VM
    Clerk --- PRO
    Collection --- MP
    PO -. "<<include>>" .-> VIA
    AD -. "<<extend>>" .-> PO
    OUI -. "<<extend>>" .-> PO
    PRO -. "<<include>>" .-> PI
    PRO -. "<<include>>" .-> PSL
```

## Task 2.2: Complete class diagram

- 3 inheritance families: Member, Payment, Item.
- An Order is made of OrderLines (composition). An OrderLine is one row of the order: a quantity and the item it points to.
- Non-Member has no class, because the system stores nothing about non-members. The membership application is what turns them into a Member.

```mermaid
classDiagram
    class MembershipApplication {
        -int id
        -String name
        -String lastName
        -Date dateOfBirth
        -String address
        +print()
        +send()
    }
    class Member {
        -int id
        -String name
        -String password
        -String address
        +placeOrder()
        +makePayment()
    }
    class RoyalMember {
        -float discountRate
        +applyDiscount()
        +orderUnavailableItem()
    }
    class RegularMember
    class Order {
        -int id
        -Date date
        -float totalAmount
        -String status
        +addItem()
        +calculateTotal()
    }
    class OrderLine {
        -int quantity
        +calculateSubtotal()
    }
    class Item {
        -int id
        -String title
        -float price
        -int stockQuantity
        +checkAvailability()
    }
    class CD {
        -int trackCount
    }
    class Tape {
        -int duration
    }
    class OrderProcessingClerk {
        -int id
        -String name
        -String password
        +verifyMembership()
        +processOrder()
    }
    class Invoice {
        -int id
        -Date date
        -float amount
        +print()
    }
    class ShippingList {
        -int id
        -Date date
        -String shippingStatus
        +print()
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
    class BankDraft {
        -String draftNumber
        -String bankName
        +process()
    }

    MembershipApplication "1" -- "0..1" Member
    Member <|-- RoyalMember
    Member <|-- RegularMember
    Member "1" -- "0..*" Order
    Order "0..*" -- "1" OrderProcessingClerk
    Order "1" *-- "1..*" OrderLine
    OrderLine "0..*" -- "1" Item
    Item <|-- CD
    Item <|-- Tape
    Order "1" -- "1" Invoice
    Order "1" -- "1" ShippingList
    Invoice "1" -- "0..1" Payment
    Payment <|-- Cash
    Payment <|-- Check
    Payment <|-- BankDraft
```

**Scenario check (Royal member orders 2 CDs, one unavailable, pays by check):** one Order with 2 OrderLines, each pointing to a CD. The unavailable CD is allowed because RoyalMember has `orderUnavailableItem()`, and the order status stays pending for that line. The payment is a Check linked to the order's Invoice.
