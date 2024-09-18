'''
Australian Dollars to NewZealand Dollars and vice versa converter
Author: Muhammad Moiz Farooq/20240779
Whitecliffe College, AKL

'''

ammounttoconvert=float(input("Enter the ammount you want to convert:"))
nzdtoaudrate=0.95
audtonzdrate=1.0526
nzdtoaud=ammounttoconvert*nzdtoaudrate
audtonzd=ammounttoconvert*audtonzdrate
print("The converted ammount from AU$ to NZ$ is $",audtonzd,sep="")
print("The converted ammount from NZ$ to AU$ is $",nzdtoaud,sep="")
