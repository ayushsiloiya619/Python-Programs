##parent class
class employee:
    def __init__(self,name,base_pay):
        self.name=name
        self.base_pay=base_pay
    def get_pay(self):
        return self.base_pay
##modify actual parent class through child class calling.
class Sales(employee):
    def __init__(self, name , base_pay , sales_incentive):
        self.name=name
        self.base_pay=base_pay
        self.sales_incentive=sales_incentive
    def get_pay(self):
        return self.base_pay + self.sales_incentive
john=Sales('John Doe',30000,10000)
print("The Sales Employee Will Get",john.get_pay(),'INR')