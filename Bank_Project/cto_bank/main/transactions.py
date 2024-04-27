from cto_bank.models import Transaction, Service

class TransactionObj:
    def __init__(self, transaction_obj, service_id):
        self.transaction_obj = transaction_obj
        self.service_id = service_id
        self.description = ""

    def get_transaction_details(self):
        service = Service.query.get(id = self.service_id)
        return 0
    
    def __repr__(self):
        return f"service_id = {self.service_id}, transaction_object_id = {self.transaction_obj}"