from abc import ABC, abstractmethod


class OrderComponent(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


class BaseOrder(OrderComponent):
    def __init__(self, base_price: float):
        self._base_price = base_price

    def get_cost(self) -> float:
        return self._base_price

    def get_description(self) -> str:
        return f"Base order ({self._base_price}€)"


class OrderDecorator(OrderComponent):
    """Wraps another order and passes calls through to it."""

    def __init__(self, order: OrderComponent):
        self._order = order

    def get_cost(self) -> float:
        return self._order.get_cost()

    def get_description(self) -> str:
        return self._order.get_description()


class ExpressShippingDecorator(OrderDecorator):
    def get_cost(self) -> float:
        return self._order.get_cost() + 15.00

    def get_description(self) -> str:
        return self._order.get_description() + " + express shipping (15€)"


class InsuranceDecorator(OrderDecorator):
    def get_cost(self) -> float:
        cost = self._order.get_cost()
        return cost + cost * 0.05

    def get_description(self) -> str:
        return self._order.get_description() + " + insurance (5%)"


class GiftWrapDecorator(OrderDecorator):
    def get_cost(self) -> float:
        return self._order.get_cost() + 5.00

    def get_description(self) -> str:
        return self._order.get_description() + " + gift wrap (5€)"


class DiscountDecorator(OrderDecorator):
    def __init__(self, order: OrderComponent, percent: float):
        super().__init__(order)
        self._percent = percent

    def get_cost(self) -> float:
        cost = self._order.get_cost()
        return cost - cost * self._percent / 100

    def get_description(self) -> str:
        return self._order.get_description() + f" - discount ({self._percent}%)"


class PremiumMemberDecorator(OrderDecorator):
    def get_cost(self) -> float:
        cost = self._order.get_cost()
        return cost - cost * 0.10

    def get_description(self) -> str:
        return self._order.get_description() + " - premium member (10%)"


if __name__ == "__main__":
    simple = BaseOrder(100.00)
    print(simple.get_description())
    print(f"Total: {simple.get_cost():.2f}€")

    print("\n---\n")

    order = BaseOrder(100.00)
    order = ExpressShippingDecorator(order)
    order = InsuranceDecorator(order)
    order = GiftWrapDecorator(order)
    order = DiscountDecorator(order, percent=15)
    order = PremiumMemberDecorator(order)
    print(order.get_description())
    print(f"Total: {order.get_cost():.2f}€")
