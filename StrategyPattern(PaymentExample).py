# PaymentStrategy Interface
class PaymentStrategy:
    def process_payment(self):
        pass

# Concrete Strategy: PaymentByCard
class PaymentByCard(PaymentStrategy):
    def process_payment(self):
        print("Payment is done by Card")

# Concrete Strategy: PaymentByUPI
class PaymentByUPI(PaymentStrategy):
    def process_payment(self):
        print("Payment is done by UPI")

# PaymentService Class
class PaymentService:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def process_order(self):
        self.payment_strategy.process_payment()

# Usage
if __name__ == "__main__":
    first = PaymentService(PaymentByUPI())
    second = PaymentService(PaymentByCard())

    first.process_order()

"""
PaymentStrategy Interface: Defines the contract for different payment strategies.
Concrete Payment Strategies: PaymentByCard and PaymentByUPI classes implement specific payment methods.
PaymentService Class: Uses the PaymentStrategy interface to handle payment processing without knowing the specific payment method 
                    at initialization. The process_order method utilizes the injected payment strategy to execute the payment.
"""