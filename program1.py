class Program(object):
    def Inflation(self,price):
        years=int(input("enter no of years of inflation:"))
        rate=float(input("enter the rate of inflation:"))
        for i in range(years):
            price=price+(price*(rate/100))
        print("price after",i+1 ,"years with a rate of", str(rate)+str("%"),"inflation will be:",round(price,2))   
object=Program()
price=int(input("enter the price of the product:"))
object.Inflation(price)




    
