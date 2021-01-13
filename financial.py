#This file provides financial evaluation methods
##############################################################################

import os
import matplotlib.pyplot as plt

#0 - Sell
#1 - Buy
#2 - Hold
#Returns: count stock history, model amount history and buy and hold amount history

def financialEvaluation(prices, actions, brokerage, amount, defaultCount):
    brokerage = 0
    leftover = 0
    leftoverBH = 0
        
    actualCount = 0
    bhCount = 0
    
    historyBH = []
    historyROI = []
    historyCount = []
    
    for i in range(len(actions)):
        #Buy and hold strategy evaluation
        if(i == 0):
             amount = amount - brokerage
             possibleBuy = int(amount / prices[i])
             totalBought = possibleBuy - (possibleBuy % defaultCount)
             bhCount = totalBought
             totalCost = prices[i] * totalBought
             leftoverBH = amount - totalCost
             
             historyBH.append(round(totalCost + leftoverBH, 2))
        else:
             actualAmount = bhCount * prices[i]
             historyBH.append(round(actualAmount + leftoverBH, 2))
            
        #Model evaluation
        if(actions[i] == 1):      #Buy
            if(actualCount == 0):
                amount = amount - brokerage
                possibleBuy = int(amount / prices[i])
                totalBought = possibleBuy - (possibleBuy % defaultCount)
                
                actualCount = totalBought
                totalCost = prices[i] * totalBought
                leftover = amount - totalCost
                
                historyCount.append(totalBought)
                historyROI.append(round(totalCost + leftover, 2))
            else:
                actualAmount = actualCount * prices[i]
            
                historyCount.append(actualCount)
                historyROI.append(round(actualAmount + leftover, 2))
        elif(actions[i] == 0):      #Sell
            if(actualCount > 0):
                actualAmount = round(actualCount * prices[i])
                amount = actualAmount + leftover - brokerage
                leftover = 0
                actualCount = 0
                
                historyCount.append(0)
                historyROI.append(round(amount, 2))
            else:
                historyCount.append(0)
                historyROI.append(round(amount, 2))
        else:                       #Hold
            if(actualCount > 0):
                actualAmount = actualCount * prices[i]
                
                historyCount.append(actualCount)
                historyROI.append(round(actualAmount + leftover, 2))
            else:
                historyCount.append(0)
                historyROI.append(round(amount, 2))
            
    return historyCount, historyROI, historyBH
