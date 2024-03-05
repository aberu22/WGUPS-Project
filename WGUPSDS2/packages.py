class Packages:
    def __init__(self, packageID, address, city, state, zipcode, deadline, weight, status, notes):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departure_time = ''
        self.deliver_time = ''
        self.notes = notes  

    def __str__(self):
        return f"{self.packageID},{self.address},{self.city},{self.state},{self.zipcode},{self.deadline},{self.weight},{self.status},{self.deliver_time},{self.notes},{self.departure_time}"
    
    
    
