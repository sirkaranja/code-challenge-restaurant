# Query the customers table
from Customer import Customer, Session



customers = Session.query(Customer).all()

# Print customer data
for customer in customers:
    print(customer.id, customer.given_name, customer.family_name)