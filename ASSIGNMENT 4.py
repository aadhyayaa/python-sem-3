from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

# Concrete Strategy 2
class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Debit Card.")

# Concrete Strategy 3
class UpiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

# Context Class
class PaymentProcessor:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if self.strategy:
            self.strategy.pay(amount)
        else:
            print("No payment method selected.")

# Driver Code
processor = PaymentProcessor()

# Credit Card Payment
processor.set_strategy(CreditCardPayment())
processor.process_payment(2500)

# Debit Card Payment
processor.set_strategy(DebitCardPayment())
processor.process_payment(1800)

# UPI Payment
processor.set_strategy(UpiPayment())
processor.process_payment(950)