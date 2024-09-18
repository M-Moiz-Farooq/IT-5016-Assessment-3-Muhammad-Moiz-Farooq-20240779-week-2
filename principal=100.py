item1=float(input("enter value of first item:"))
item2=float(input("enter value of second item:"))
item3=float(input("enter value of third item:"))
taxpercentage= 0.15
totalvalueofitems= item1+item2+item3
salestax=totalvalueofitems*taxpercentage
total=salestax+totalvalueofitems
print("your purchase total is $",total,sep="")
