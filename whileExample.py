#val = input("Do you want to format your hard drive (y/n)?")
#while val != "y" and val != "n":
#    val = input ("Please answer y/n. Do you want to format your hard drive (y/n)?")
# This probably is only useful if your doing a command line program

lst = ["Santiago", "Codes", "Please", "Get me out of Argentina"]

# i = 0
# while i < len(lst):
#     print(lst[i].upper())
#     i += 0

# for i in range(0,len(lst)):
#     print(lst[i].upper())

lst2 = [item.upper() for item in lst]
print(lst)
print(lst2)
