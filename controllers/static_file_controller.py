import os
import sass

class StaticFileController:
    path = None

    def send_static_file_action(self, request, response):


        parameters = request.get_parameters()

        if 'path' in parameters:
            path = parameters['path']

            if path == '/':
                path = '/index.html'

            file_path = f'./src{path}'
            content_type = self.get_content_type(file_path)

            if file_path.endswith('.jpg'):
                try:
                    with open(file_path, 'rb') as file:
                        file_content = file.read()
                        response.set_status(200)
                        response.set_header("Content-Type", "application/octet-stream")
                        response.set_binary_body(file_content) 
                        return
                except FileNotFoundError:
                    response.set_status(404)
                    response.set_body("File not found")
                    return

            if file_path.endswith('.scss'):
                css_output = self.compile_scss(file_path)
                response.set_status(200)
                response.set_header("Content-type", "text/css")
                response.set_body(css_output)
                return

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                    response.set_status(200)
                    response.set_header("Content-type", content_type)
                    response.set_body(file_content)
            except FileNotFoundError:
                response.set_status(404)
                response.set_body("File not found")


    def get_content_type(self, file_path):
        _, extension = os.path.splitext(file_path)
        return {
            '.html': 'text/html',
            '.js': 'application/javascript',
            '.css': 'text/css',
            '.scss': 'text/css',
            '.json': 'application/json',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.ico': 'image/x-icon'
        }.get(extension, 'application/octet-stream')
    


    def compile_scss(self, input_path):

        css = sass.compile(filename=input_path)
        return css




















