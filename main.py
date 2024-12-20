from controllers.book_controller import BookController
from controllers.cart_controller import CartController
from controllers.customer_controller import CustomerController
from controllers.order_controller import OrderController
from controllers.order_item_controller  import  OrderItemController
from controllers.static_file_controller import StaticFileController
from http.server import BaseHTTPRequestHandler, HTTPServer
from collections import deque
import json
import webbrowser
import threading

class Response:
    def __init__(self):
        self.status = 404
        self.headers = {}
        self.body = ""

    def set_status(self, status):
        self.status = status

    def set_body(self, data):
        self.body = data.encode('utf-8')
        return self
    
    def set_binary_body(self, data):
        self.body = data
        return self

    def set_header(self, name, value):
        self.headers[name] = value 
        return self
    
    def get_status(self):
        return self.status

    def get_headers(self):
        return self.headers
    
    def get_body(self):
        return self.body
    
    
    def set_json(self, data):
        self.set_header("Content-type", "application/json")
        self.set_body(json.dumps(data))
        return self

    
class Request:

    def __init__(self, path):
        path_list = deque(path.split('/'))
        path_list.popleft()
        data = path_list.popleft()

        if path_list and data == 'data':
            self.controller_name = self.to_pascal_case(path_list.popleft()) if path_list else None
            self.action_name = self.to_snake_case(path_list.popleft()) if path_list else None
            self.parameters = self.to_parameters_map(path_list) if path_list else {}
        else:
            self.controller_name = 'StaticFileController'
            self.action_name = 'send_static_file_action'
            self.parameters = {'path': path}

    def to_pascal_case(self, string):
        parts = string.split('-')
        pascal_case = ''.join(word.capitalize() for word in parts)
        pascal_case += 'Controller'
        return pascal_case
    
    def to_snake_case(self, string):
        snake_case = string.replace('-', '_').lower()
        snake_case += '_action'
        return snake_case
    
    def to_parameters_map(self, path_list):
        parameters = {}
        while path_list:
            key = path_list.popleft() if path_list else None
            value = path_list.popleft() if path_list else None
            if key is not None and value is not None:
                parameters[key] = value
        return parameters

    def get_controller_name(self):
        return self.controller_name
    
    def get_action_name(self):
        return self.action_name
    
    def get_parameters(self):
        return self.parameters


class HTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        response = self.process_request()
        self.send_response(response.get_status())
        for key, value  in response.get_headers().items():
            self.send_header(key, value) 
        self.end_headers()

        self.wfile.write(response.get_body()) 


    def process_request(self):
        path = self.path
        request = Request(path)
        controller_name = request.get_controller_name() 
        action_name = request.get_action_name()

        response = Response()
        if controller_name in globals():
            if hasattr(globals()[controller_name], action_name): 
                controller = globals()[controller_name]()
                action = getattr(controller, action_name)  
                data = action(request, response)
        return response


def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, HTTP)
    print("Server is running on http://localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':

    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    webbrowser.open('http://localhost:8000')