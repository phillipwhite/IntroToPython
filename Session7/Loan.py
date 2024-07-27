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

    def getNumberOfYears(self):
        return self.numberOfYears

    def getLoanAmount(self):
        return self.loanAmount

    def getBorrower(self):
        return self.borrower


