#ID CARD, CSE110, by Herendira Gomez, Sep 20,2022
print("Please enter the following information:")
first_name=input("First name: ")
last_name=input("Last name: ")
email=input("Email address: ")
phone=input("Phone number: ")
job_title=input("Job title: ")
id_number=input("ID Number: ")
hair=input("Hair color: ")
eyes=input("Eyes color: ")
month=input("Month: ")
training=input("Did you have training? yes or not? ")
print("\n\nThe ID Card is: ")
print("\n-----------------------------------------\n")
print(last_name.upper()+ ", "+first_name.capitalize())
print(job_title.capitalize())
print("ID:   "+id_number+"\n\n")
print(email)
print(phone+"\n\n")
print("Hair: "+hair.capitalize().ljust(20)+"Eyes: "+eyes.capitalize().center(20)+"\n")
print("Month: "+month.capitalize().ljust(20)+"Training: "+training.capitalize().center(9)+"\n")
print("-----------------------------------------")




