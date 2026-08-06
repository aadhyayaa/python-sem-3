# Payment Methods (Strategies)
class CreditCard:
    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")

class DebitCard:
    def pay(self, amount):
        print("Paid ₹", amount, "using Debit Card")

class UPI:
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")

# Context Class
class PaymentProcessor:
    def __init__(self, method):
        self.method = method

    def process(self, amount):
        self.method.pay(amount)

# Main Program
processor = PaymentProcessor(CreditCard())
processor.process(1000)

processor = PaymentProcessor(DebitCard())
processor.process(2000)

processor = PaymentProcessor(UPI())
processor.process(500)
