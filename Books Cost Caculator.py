'''
Books Cost Calculator
Author: Muhammad Moiz Farooq/20240779
WhiteCliffe College, AKL

'''
numberofcopies=int(input("enter the number of copies you need:"))
coverpriceofbook=24.95
bookstorediscount=.40
shippingcostforfirstcopy=3
shippingcostforadditionalcost=0.75
discount=24.95*0.40
priceofcopyafterdiscount=coverpriceofbook-discount
numberofcopieswithdeliveryprice75=numberofcopies-1
shippingofcopies=(numberofcopieswithdeliveryprice75*shippingcostforadditionalcost)+shippingcostforfirstcopy
totalpriceofcopies=numberofcopies*priceofcopyafterdiscount
totalcost=totalpriceofcopies+shippingofcopies
print("The total cost of copies with shipping is $",totalcost,sep="")