age = 20
country = "COL"
userHasDNI = True


if age >= 21 and country == "USA":
    print("you can buy alcogol in USA")
elif age >= 18 and country == "COL":
    print("you can buy alcohol in COL")
elif age >= 16 and country == "GER":
    print("you can buy alcohol un GER")
else:
    userHasDNI = False
    print("you can\ 't buy alcohol ")


for i in range(10):
    i +=1
    print(i)   

