import math
print(math.sqrt(16))  # This will compute the square root of 16

#also check the other built-in modules in pyhton     

import mymodule
mymodule.hello()  # This will call the hello function from mymodule

#example of external module usage just use pip install requests in terminal

import requests
response = requests.get("https://www.google.com")
print(response.text)  # This will print the HTTP status code of the response
