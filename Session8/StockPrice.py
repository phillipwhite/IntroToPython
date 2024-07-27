class Stock:

    def __init__(self, symbol: str, name: str,
                 previousClosingPrice: float = 0,
                 currentPrice: float = 0):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getSymbol(self):
        return self.__symbol

    def getName(self):
        return self.__name

    def getPreviousPrice(self):
        return self.__previousClosingPrice

    def setPreviousPrice(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice

    def getCurrentPrice(self):
        return self.__currentPrice

    def setCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice

    def getChangePercent(self):
        return ((self.__currentPrice - self.__previousClosingPrice) \
            / self.__previousClosingPrice) * 100


intelStock = Stock("INTC", "Intel Corporation",
                   20.5, 20.35)

print(intelStock.getChangePercent())
