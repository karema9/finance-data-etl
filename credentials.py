
from polygon import RESTClient
# Read the api key from the text file
# NOTE!!! - Add the api key to the git ignore file
file = "api-key.txt"

try:
    with open(file, "r") as key:
        api_key = key.read()

except FileNotFoundError:
    print("File not found {file}")



