from http.server import HTTPServer, BaseHTTPRequestHandler
import json

tasks = []
next_id = 1

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
        global next_id
        
        if self.path == '/tasks':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            task_data = json.loads(post_data)

            if 'title' in task_data:
                task_data['id'] = next_id
                tasks.append(task_data)
                self.send_response(201) # 201 is the HTTP status code for "Created"
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(bytes(json.dumps({"message": "Task added", "id": next_id}), "utf8"))
                next_id += 1
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
            
    def do_DELETE(self):
        path_parts = self.path.split('/')
        if len(path_parts) == 3 and path_parts[1] == 'tasks':
            try:
                task_id = int(path_parts[2])
            except ValueError:
                self.send_response(400)
                self.end_headers()
                return

            task_found = False
            for i, task in enumerate(tasks):
                if task['id'] == task_id:
                    del tasks[i]
                    task_found = True
                    break

            if task_found:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(json.dumps({"message": "Task deleted", "id": task_id}), "utf8"))
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(bytes(json.dumps({"message": "Not Found"}), "utf8"))
        else:
            self.send_response(404)
            self.end_headers()
            
    def do_PUT(self):
        path_parts = self.path.split('/')
        if len(path_parts) == 3 and path_parts[1] == 'tasks':
            try:
                task_id = int(path_parts[2])
            except ValueError:
                self.send_response(400) # Bad Request
                self.end_headers()
                return

            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length)
            updated_task_data = json.loads(put_data)
            
            # Find and update the task
            task_found = False
            for task in tasks:
                if task['id'] == task_id:
                    if 'title' in updated_task_data:
                        task['title'] = updated_task_data['title']
                        task_found = True
                        break

            if task_found:
                self.send_response(200)  # OK
                self.end_headers()
            else:
                self.send_response(404)  # Not Found
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == '__main__':
    # Server settings
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    # Run the server
    print("Server started at http://localhost:8000")
    httpd.serve_forever()
