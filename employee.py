"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name,contractType,commissionType):
        self.name = name
        self.contractType = contractType
        self.commissionType = commissionType

        self.totalPayment =0        
        
        self.contractHours = 0
        self.HourlyPay =0
        self.MonthlyPay =0
        self.contractPayment = 0

        
        self.CommissionPayment = 0
        self.ContractCommission = 0
        self.NoContracts = 0

       

    def set__contract_pay(self,contractHours,HourlyPay,MonthlyPay):
        if self.contractType == "monthly":
            self.contractPayment = MonthlyPay
            self.MonthlyPay =MonthlyPay
        else:
            self.contractPayment = HourlyPay * contractHours
            self.HourlyPay =HourlyPay
            self.contractHours =contractHours

    def set__commission_pay(self,fixedBonus,ContractCommission,NoContracts):
        if self.commissionType == 'fixed':
            self.CommissionPayment = fixedBonus
            
        elif self.commissionType == "contract":
            self.CommissionPayment = ContractCommission * NoContracts
            self.ContractCommission = ContractCommission
            self.NoContracts = NoContracts

        else:
            self.CommissionPayment = 0
            
    
    def get_pay(self):
        if self.CommissionPayment > 0:
            self.totalPayment =  self.contractPayment + self.CommissionPayment
        else:
            self.totalPayment = self.contractPayment
        return self.totalPayment
        
       

    def __str__(self):
        totalPayString = "Their total pay is " + str(self.totalPayment)+ "."
        contractInfoString = ""
        if self.contractType == "monthly":
            contractInfoString = "monthly salary of " + str(self.MonthlyPay)
        else:
            contractInfoString = "contract of " +  str(self.contractHours) + " hours at " + str(self.HourlyPay) + "/hour"

        
        if self.CommissionPayment > 0:
            if self.commissionType == 'fixed':
                commissionInfoString = " and receives a bonus commission of " + str(self.CommissionPayment)
            else:
                commissionInfoString = " and receives a commission for "+str(self.NoContracts)+" contract(s) at "+str(self.ContractCommission)+"/contract"

            return self.name + " works on a "+ contractInfoString + commissionInfoString+ ". "+ totalPayString

        else:
            return self.name + " works on a " + contractInfoString +  ". " + totalPayString




# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie','monthly','none')
billie.set__contract_pay(0,0,4000)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie','hourly','none')
charlie.set__contract_pay(100,25,0)


# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee','monthly','contract')
renee.set__contract_pay(0,0,3000)
renee.set__commission_pay(0,200,4)


# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan','hourly','contract')
jan.set__contract_pay(150,25,0)
jan.set__commission_pay(0,220,3)


# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie','monthly','fixed')
robbie.set__contract_pay(0,0,2000)
robbie.set__commission_pay(1500,0,0)


# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel','hourly','fixed')
ariel.set__contract_pay(120,30,0)
ariel.set__commission_pay(600,0,0)

