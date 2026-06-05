from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process(self):
        pass

class QRISPayment(PaymentMethod):
    def process(self):
        return "QRIS Payment Sukses"

class DANAPayment(PaymentMethod):
    def process(self):
        return "DANA Payment Sukses"

class OVOPayment(PaymentMethod):
    def process(self):
        return "OVO Payment Sukses"
    
class GOPAYPayment(PaymentMethod):
    def process(self):
        return "GOPAY Payment Sukses"

class BankTransferPayment(PaymentMethod):
    def process(self):
        return "BANK Payment Sukses"

class PaymentFactory:
    @staticmethod
    def get_payment(method: str):
        method = method.upper()

        if method == "QRIS":
            return QRISPayment()
        elif method == "DANA":
            return DANAPayment()
        elif method == "OVO":
            return OVOPayment()
        elif method == "GOPAY":
            return GOPAYPayment()
        elif method == "BCA":
            return BankTransferPayment()
        else:
            return QRISPayment()