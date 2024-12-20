from models.Order import Order

# create objekt in function  Order 

class OrderController:

    def complete_order_action(self,  request, responce):
        order = Order()
        new_order = Order()
        parameters = request.get_parameters()
        data = {}

        if 'customer_id' and 'first_name' and 'last_name' and 'postal_zip'and 'address'and 'city' and 'counry' in parameters:

            customer_id = parameters['customer_id']
            first_name = parameters['first_name']
            last_name = parameters['last_name']
            postal_zip = parameters['postal_zip']
            address = parameters['address']
            city = parameters['city']
            counry = parameters['counry']

            order.load(customer_id)
            order.save()

            if order.order_id:
                order.mark_as_complete(first_name, last_name, postal_zip, address, city, counry)
                data['completed_order'] = order.to_dict()

            new_order.load(customer_id)
            new_order.save()
            data['new_order'] = new_order.to_dict()
            

        responce.set_status(200)
        responce.set_json(data)
        return responce



