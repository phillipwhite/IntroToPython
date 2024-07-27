class Loan:

    def __init__(self,
                 annualInterestRate: float = 2.5,
                 numberOfYears: int = 1,
                 loanAmount: float = 1000,
                 borrower: str = ""):
        self.annualInterestRate = annualInterestRate
        self.numberOfYears = numberOfYears
        self.loanAmount = loanAmount
        self.borrower = borrower

    def getAnnualInterestRate(self):
        return self.annualInterestRate

    def setAnnualInterestRate(self, annualInterestRate):
        if annualInterestRate > 0:
            self.annualInterestRate = annualInterestRate

    def getNumberOfYears(self):
        return self.numberOfYears

    def setNumberOfYears(self, numberOfYears):
        if numberOfYears > 0:
            self.numberOfYears = numberOfYears

    def getLoanAmount(self):
        return self.loanAmount

    def setLoanAmount(self, loanAmount):
        if loanAmount > 0:
            self.loanAmount = loanAmount

    def getBorrower(self):
        return self.borrower

    def setBorrower(self, borrower):
        self.borrower = borrower


