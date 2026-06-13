import os
os.chdir(os.path.dirname(__file__))
from datetime import datetime
import time

# main function
def find_root():
    # Find the current directory
    dir_name = os.getcwd()
    
    # Check if there are any files in this directory
    found = False
    for filename in os.listdir(dir_name):
        if os.path.isfile(os.path.join(dir_name, filename)):
            # Check if it's a file with version information
            if "version" in filename:
                # Open the file to read its content
                try:
                    with open(os.path.join(dir_name, filename), 'r') as f:
                        data = f.read()
                        
                        # Extract the root hash from the file contents
                        root_hash = ""
                        for line in data.split('\n'):
                            if line.startswith("hash"):
                                root_hash = line[10:23]
                        if len(root_hash) > 0:
                            # Create a timestamp and compare to the current time
                            now_time = datetime.now().timestamp()
                            current_time = int(time.strftime("%Y%m%dH%M%S"))
                            
                            # Compare timestamps for correctness
                            if root_hash != f"{now_time:06d}{current_time:03d}":
                                print("The hash is incorrect. Please check the version information.")
                                return
                        else:
                            print("No root hash found in this directory. The solution cannot be verified.")
                except Exception as