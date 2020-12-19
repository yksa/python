class User:
    def log(self):
        print(self)

class Teacher(User):
    def log(self):
        print("I'm a teacher!")

class Customer(User):

    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def update_membership(self, new_membership):
        print("Calculatin costs")
        self.membership_type = new_membership

    # convert object location to object data
    def __str__(self):
        return self.name + " " + self.membership_type

    # original method is compare with memory location 
    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    __repr__ = __str__

    __hash__ = None


users = [Customer("Jame", "Gold"), Customer("Smith", "Gold"), Teacher()]

# Static method invoke
# Customer.print_all_customers(customers)

# print(customers[0] == customers[1])
# print(id(customers[0]), id(customers[1]))

for user in users:
    user.log()