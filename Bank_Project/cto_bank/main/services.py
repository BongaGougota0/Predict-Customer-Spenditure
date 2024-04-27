
class ServiceObj:
    def __init__(self, service_id):
        self.service_id = service_id
        self.description = ""

    def get_service_details(self):
        return 0

    def __repr__(self):
        return f" service_id = {self.service_id}, description = {self.description}"
