#Seatwork 1
from pyscript import display, document

#Personal Info

    #declare variable

name = 'Jacqueline Tian'  #string
age = 15 #integer
height1 = 160 #integer
my_countries = ['Switzerland', 'Italy', 'France'] #list
student_type = False #Boolean
dct_color = {'fav_color':'yellow',}
dct_car = {'car_brand':'Toyota',}
dct_shoe ={'shoe_size':'7',}
dct_bsf = {'best_friend':'Julia',} 
fruits = set(['Mango','Mangosteen','Orange','Pomelo', 'Avocado']) #set
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') #tuple

#join the list to remove special characters when displayed by:{", ".join(listvariable)}



display (f'Hello! Im {name}! I am {age} years old.', target= "content")

display (f'I am {height1}cm tall.', target="content")
display (f'I am a new student. (That is {student_type}).', target="content")
display (f'My favorite color as of now is {dct_color["fav_color"]}, the car I have is a {dct_car["car_brand"]}, and my best friend is {dct_bsf["best_friend"]}.', target="content")
display (f'My favorite fruits are {", ".join(fruits)}.', target="content")
display (f'The seven days of the week are: {", ".join(days)}.', target="content")


#Operations

    #declare variable

#for button pyclick

def add(e):
    document.getElementById("output").innerHTML = ""
    value1 = float(document.getElementById("value1").value)
    value2 = float(document.getElementById("value2").value)
    added = value1 + value2
    display (added, target="output")

def subtract(e):
    document.getElementById("output").innerHTML = ""
    value1 = float(document.getElementById("value1").value)
    value2 = float(document.getElementById("value2").value)
    subtracted = value1 - value2
    display (subtracted, target="output")

def multiply(e):
    document.getElementById("output").innerHTML = ""
    value1 = float(document.getElementById("value1").value)
    value2 = float(document.getElementById("value2").value)
    multiplied = value1 * value2
    display (multiplied, target="output")

def divide(e):
    document.getElementById("output").innerHTML = ""
    value1 = float(document.getElementById("value1").value)
    value2 = float(document.getElementById("value2").value)
    divided = value1 / value2
    display (divided, target="output")









