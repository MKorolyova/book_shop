from models.Customer import Customer
from models.Order import Order

# create objekt in function Customer Order 

class CustomerController:

    def log_in_action(self,  request, responce):
        customer = Customer()
        parameters = request.get_parameters()

        if 'email' and 'password' in parameters:
            email = parameters['email']
            password = parameters['password']

            customer.load_by_email(email, password)
            data = {}

            if not customer.customer_id:
                customer.save()

            data['status'] = "success" if customer.password == password else "error"
            data['customer'] = customer.to_dict()

            
            order = Order()
            order.load(customer.customer_id)
            order.save()
            data['order'] = order.to_dict()

        responce.set_json(data)
        responce.set_status(200)
        return responce



