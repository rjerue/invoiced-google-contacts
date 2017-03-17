import invoiced
import json
import gdata.data
import gdata.contacts.client
import gdata.contacts.data

#invoiced-161823

client = invoiced.Client("")

customers, metadata = client.Customer.list()

# print(json.dumps(customers))

customerNameAndPhone = [] #customers[0]
# print(customerNameAndPhone["name"] + " " + customerNameAndPhone["phone"])

for customer in customers:
    #print(customer["name"])
    customerNameAndPhone.append(
    {
        'name': customer["name"],
        'phone': customer["phone"]
    })
    print(len(customerNameAndPhone))
print(customerNameAndPhone)
