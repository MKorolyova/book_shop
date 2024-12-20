from models.Order import Order
from models.OrderItem import OrderItem

# create objekt in function  Order OrderItem

class OrderItemController:

    def add_item_to_order_action(self,  request, responce):
        order = Order()
        order_item = OrderItem()

        parameters = request.get_parameters()

        if 'customer_id' and 'book_id' in parameters:

            customer_id = parameters['customer_id']
            book_id = parameters['book_id']

            order.load(customer_id)

            order_item.set_book(book_id)
            order_item.set_order_id(order.order_id)

            order_item.save()

        responce.set_status(200)
        responce.set_json(order_item.to_dict())
        return responce
    
    def del_item_from_order_action(self, request, responce):
        order_item = OrderItem()
        parameters = request.get_parameters()

        if 'order_item_id' in parameters:

            order_item_id = parameters['order_item_id']

            order_item.load(order_item_id)
            order_item.delete()
  
            

        responce.set_status(200)
        responce.set_json(order_item.to_dict())
        return responce



