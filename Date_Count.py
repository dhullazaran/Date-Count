from datetime import date

#get today's date
today = date.today()
print("Today: "+today.strftime('%A, %d %b %Y'))
print()

#Input Date of Birth:
dob_str = input("What is your Date of Birth? dd/mm/yyy : ")

#covert user input into a date
dob_date = dob_str.split("/")
dob_day = int(dob_date[0])
dob_month = int(dob_date[1])
dob_year = int(dob_date[2])
dob = date(dob_year,dob_month,dob_day)
print()
print("Your Date of Birth is : "+dob.strftime('%A, %d %b %Y'))
print()

#Calculate number of days
numberofdays = (today-dob).days

#converter this into whole years to display the age
age = numberofdays//365
print("You are "+str(age) + " years old.")
print()

#Retrieve the day of the week (Monday to Sunday) correspoding to
day = dob.strftime("%A")
print("You were born on a "+day+".")
print()

#days on earth
print("You have spent "+str(numberofdays)+" days on Earth.")
print()

#Calculating the number of days until next birthday
this_year = today.year
nextbirthday = date(this_year,dob_month,dob_day)
if today<nextbirthday:
    gap = (nextbirthday-today).days
    print("Your birthday is in "+str(gap)+" days.")
elif today == nextbirthday:
    print("Hey! Today is your birthday! Happy Birthday!")
else:
    nextbirthday = date(this_year+1,dob_month,dob_day)
    gap = (nextbirthday-today).days
    print("Your birthday is in "+str(gap)+" days.")

print()
print()
