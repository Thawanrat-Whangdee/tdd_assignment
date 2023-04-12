from function import amount_of_vehicle 
from function import validate_number
import sys

input_number = input("Enter number of people ==>")


try:
    # int(input_number)
    try:
        input_number = int(input_number)
    except:
        input_number = float(input_number)
    
except:
    input_number = str(input_number)

result = amount_of_vehicle(input_number)
print("Number of vehicles used: "+result)