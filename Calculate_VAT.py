#Calculate VAT 

class Vat():
    def __init__(self,amount,VatRate = 20):
        self._amount = amount
        self._VatRate = VatRate        
        
    def __str__(self):
        return f"amount = {self._amount} and VAT'Rate: {self._VatRate}%\n"    
   
    def calculateVat(self):
        return f"VAT = {round(self._amount*(self._VatRate/100),2)} VAT "

    def GrossAmount(self):                      
        
        return f"Gross = {round(self._amount+ self._amount*(self._VatRate/100),2)} VAT included"
     
    def NetWithoutVat(self):
        return f"Net amount = {self._amount} VAT not included"

amount= Vat(float(input("Enter the amount :"'\n')))

print(amount)
print(amount.calculateVat())
print(amount.GrossAmount())               
print(amount.NetWithoutVat())


