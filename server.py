from http.server import HTTPServer, BaseHTTPRequestHandler
import json

tasks = [{"id": 1, "title": "Sample Task 1"}, {"id": 2, "title": "Sample Task 2"}]

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/tasks':
            # Logic to retrieve all tasks
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(json.dumps(tasks), "utf8"))
            # json.dumps(tasks) converts this list into a JSON-formatted string
            # bytes(..., "utf8") converts the string into bytes in UTF-8 encoding
            # self.wfile.write(...) sends this byte data back to the client.
        else:
            # Default response for other paths
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("Not Found", "utf8"))
            
            
    def do_POST(self):
        
        if self.path == '/tasks':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            task_data = json.loads(post_data)

            if 'title' in task_data:
                new_id = len(tasks) + 1
                task_data['id'] = new_id
                tasks.append(task_data)

                self.send_response(201)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(bytes(json.dumps({"message": "Task added", "id": new_id}), "utf8"))
            else:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(bytes(json.dumps({"message": "Missing title in request"}), "utf8"))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(json.dumps({"message": "Not Found"}), "utf8"))

if __name__ == '__main__':
    # Server settings
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    # Run the server
    print("Server started at http://localhost:8000")
    httpd.serve_forever()
