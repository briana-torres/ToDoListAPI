### To-Do List API Project

**Project Overview:**
Create a basic RESTful API to manage a To-Do list, where you can add, view, and delete tasks. Each task will have an `id` and `title`.

**Tools Required:**
- Python (with the `http.server` module)
- Postman for testing the API

**Key Concepts to Learn:**
- HTTP methods and status codes
- JSON handling in Python
- Basic routing and handling HTTP requests in Python

**Project Steps:**

1. **Set Up a Basic HTTP Server:**
   - Use Python’s `http.server` module to set up a basic server.
   - Implement basic request handling to respond to HTTP requests.

2. **Implement RESTful Endpoints:**
   - **GET** to retrieve the list of tasks or a specific task.
   - **POST** to add a new task.
   - **DELETE** to remove a task.

3. **Manage In-Memory Data:**
   - Use a simple Python dictionary or list to store tasks.
   - This avoids the complexity of database management.

4. **Handle JSON Data:**
   - Parse JSON data from POST requests to add tasks.
   - Send task data as JSON in response to GET requests.

5. **Test API with Postman:**
   - Test each endpoint (GET, POST, DELETE) with Postman.
   - Ensure the API responds with correct status codes and JSON data.

6. **Basic Error Handling:**
   - Implement simple error handling (e.g., for not found or bad requests).

**Focus Areas:**
- Understanding how HTTP methods are handled in Python.
- Learning how JSON is used in the request and response cycle.
- Getting comfortable with testing APIs using Postman.

