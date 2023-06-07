class SimpleFramework:
    def __init__(self):
        self.routes = {}

    def route(self, path, methods=["GET"]):
        print("decorating...")

        def decorator(f):
            print("inside decorator...")
            self.routes[(path, tuple(methods))] = f
            return f

        print("decorating done...")
        return decorator

    def serve(self, path, method):
        key = (path, method)
        for route, methods in self.routes.keys():
            if route == path and method in methods:
                return self.routes[(route, methods)]()
        return "404 Not Found"


app = SimpleFramework()


@app.route("/", ["GET"])
def home():
    return "This is the home page."


print("routes created...")

# @app.route("/users", ["GET", "POST"])
# def users():
#     if request.method == "GET":
#         return "GET: Here are the users."
#     elif request.method == "POST":
#         return "POST: Creating a new user."


print(app.serve("/", "GET"))  # Outputs: This is the home page.
print(app.serve("/users", "GET"))  # Outputs: GET: Here are the users.
print(app.serve("/users", "POST"))  # Outputs: POST: Creating a new user.
print(app.serve("/notfound", "GET"))  # Outputs: 404 Not Found
