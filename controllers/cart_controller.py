from models.OrderItemCollection import OrderItemCollection
from models.GenresCollection import GenresCollection

# create objekt in function OrderItemCollection GenresCollection 

class CartController:

    def get_cart_page_action(self,  request, responce):
        order_item_collection = OrderItemCollection()
        genres = GenresCollection()

        parameters = request.get_parameters()

        if 'customer_id' in parameters:
            customer_id = parameters['customer_id']

            order_item_collection.set_where({'customer_id': customer_id, 'status': "inprocess"})
            order_item_collection.load()
            genres.load()

            responce.set_status(200)
            data = {}
            data["order_items"] = order_item_collection.to_dict()
            data["genre"] = genres.to_dict() 
            responce.set_json(data)

        return responce


