#Seatwork 1
from pyscript import display

#Personal Info

    #declare variable

name = 'Jacqueline Tian'  #string
age = 15 #integer
height1 = 160 #integer
my_countries = ['Switzerland', 'Italy', 'France'] #list
student_type = False
dct_color = {'fav_color':'yellow',}
dct_car = {'car_brand':'Toyota',}
dct_shoe ={'shoe_size':'7',}
dct_bsf = {'best_friend':'Julia',} 
fruits = set(['Mango','Mangosteen','Orange','Pomelo', 'Avocado']) #set
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') #tuple

#join the list to remove special characters when displayed
# mc1 = f" I want to visit {"".join(my_countries)}


display (f'Hello! Im {name}! Today, I am {age} years old.', target= "content")
display (f'I am {height1}cm tall', target="content")
display (f'{mc1}', target="content")
display (f'I am a new student...aaand that is {student_type}', target="content")
display (f'My favorite color as of now is {dct_color}, the car I have is a {dct_car}, and my best friend is {dct_bsf}', target="content")
display (f'My favorite fruits are {fruits}', target="content")
display (f'The seven days of the week are: {days}', target="content")


#Operations

    #declare variable

#for button pyclick
def compute(e):
    document.getElementById("results").innerHTML = ""

value1 = float(document.getElementById("value1").value)
value2 = float(document.getElementById("value2").value)
result = value1 + value2
display(result, target="results")




