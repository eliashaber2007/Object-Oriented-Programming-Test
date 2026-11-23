from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    """Every processor promises to have these two methods."""

    @abstractmethod
    def validate(self, details: dict) -> bool:
        pass

    @abstractmethod
    def process(self, amount: float, details: dict) -> dict:
        pass


class CreditCardProcessor(PaymentProcessor):
    def validate(self, details: dict) -> bool:
        card_number = details.get("card_number", "")
        cvv = details.get("cvv", "")
        return len(card_number) == 16 and len(cvv) == 3

    def process(self, amount: float, details: dict) -> dict:
        if not self.validate(details):
            return {"success": False, "error": "Invalid card details"}
        fee = amount * 0.029
        return {"success": True, "method": "credit_card", "amount": amount + fee, "fee": fee}


class BankTransferProcessor(PaymentProcessor):
    def validate(self, details: dict) -> bool:
        return len(details.get("iban", "")) >= 15

    def process(self, amount: float, details: dict) -> dict:
        if not self.validate(details):
            return {"success": False, "error": "Invalid IBAN"}
        fee = 1.50
        return {"success": True, "method": "bank_transfer", "amount": amount + fee, "fee": fee}


class PayPalProcessor(PaymentProcessor):
    def validate(self, details: dict) -> bool:
        return "@" in details.get("email", "")

    def process(self, amount: float, details: dict) -> dict:
        if not self.validate(details):
            return {"success": False, "error": "Invalid PayPal email"}
        fee = amount * 0.034 + 0.30
        return {"success": True, "method": "paypal", "amount": amount + fee, "fee": fee}


class PaymentFactory:
    """The middleman: takes a string, returns the right processor."""

    _processors = {
        "credit_card": CreditCardProcessor,
        "bank_transfer": BankTransferProcessor,
        "paypal": PayPalProcessor,
    }

    def get_processor(self, payment_type: str) -> PaymentProcessor:
        processor_class = self._processors.get(payment_type)
        if processor_class is None:
            raise ValueError(f"Unknown payment type: {payment_type}")
        return processor_class()


if __name__ == "__main__":
    factory = PaymentFactory()

    processor = factory.get_processor("credit_card")
    print(processor.process(100.0, {"card_number": "1234567890123456", "cvv": "123"}))

    processor = factory.get_processor("bank_transfer")
    print(processor.process(100.0, {"iban": "FR7630006000011234567890189"}))

    processor = factory.get_processor("paypal")
    print(processor.process(100.0, {"email": "elias@example.com"}))
