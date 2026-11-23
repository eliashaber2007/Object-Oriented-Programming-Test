# ABCD Records: Level 3 sequence diagrams

Solid arrow = a request. Dashed arrow = the immediate reply.

## 1. Complete order processing flow

```mermaid
sequenceDiagram
    actor Member
    participant Clerk as OrderProcessingClerk
    participant Order
    participant Item
    participant Invoice
    participant ShippingList
    Member->>Clerk: placeOrder(items)
    Clerk->>Clerk: verifyMembership(member)
    Clerk->>Order: create(member)
    loop for each item
        Clerk->>Item: checkAvailability()
        Item-->>Clerk: available
        Clerk->>Order: addItem(item, quantity)
    end
    Clerk->>Order: calculateTotal()
    Order-->>Clerk: totalAmount
    Clerk->>Invoice: print()
    Clerk->>ShippingList: print()
    Clerk-->>Member: order confirmed
```

## 2. Membership verification

```mermaid
sequenceDiagram
    actor Person
    participant Clerk as OrderProcessingClerk
    participant System as MemberRecords
    Person->>Clerk: placeOrder(memberId)
    Clerk->>System: verifyMembership(memberId)
    alt member found
        System-->>Clerk: valid member
        Clerk-->>Person: order accepted
    else not a member
        System-->>Clerk: not found
        Clerk->>Person: sendMembershipApplication()
    end
```

## 3. Payment processing (all types)

Each payment type rewrites `process()`, so the collection clerk calls the same method whatever the type (polymorphism).

```mermaid
sequenceDiagram
    actor Member
    participant Collection as CollectionDepartmentClerk
    participant Payment
    participant Invoice
    Member->>Collection: makePayment(invoiceId, method)
    alt cash
        Collection->>Payment: process() on Cash
    else check
        Collection->>Payment: process() on Check
    else bank draft
        Collection->>Payment: process() on BankDraft
    end
    Payment-->>Collection: payment accepted
    Collection->>Invoice: markPaid()
    Collection-->>Member: receipt
```

## 4. Item reordering for Royal members

```mermaid
sequenceDiagram
    actor Royal as RoyalMember
    participant Clerk as OrderProcessingClerk
    participant Item
    participant Order
    Royal->>Clerk: placeOrder(item)
    Clerk->>Item: checkAvailability()
    Item-->>Clerk: unavailable
    Clerk->>Royal: offer to order unavailable item
    Royal->>Clerk: orderUnavailableItem(item)
    Clerk->>Order: addItem(item) with status PENDING
    Clerk-->>Royal: item reserved, shipped when back in stock
```
