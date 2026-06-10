import sys

# Define the local app variable
local_app = None

if __name__ == "__main__":
    # Initialize the local application if not already defined
    if local_app is None:
        local_app = app()  # Create an instance of the application
    
    # Start the server with the configured host and port
    app.run(host="localhost", port=8080)