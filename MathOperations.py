class mathOperation:
  #constructor
  def __init__(self,quantifier,listofNumbers):
    self.q=quantifier
    self.listofNumbers=listofNumbers

  #finding min values from the list
  def findMinNumbers(self):
    from heapq import nsmallest
    return nsmallest(self.q,self.listofNumbers)

  #finding max values from the list
  def findMaxNumbers(self):
    from heapq import nlargest
    return nlargest(self.q,self.listofNumbers)

  #calculate average value
  def calculateAverage(self):
    average=sum(self.listofNumbers)/len(self.listofNumbers)
    return "%.2f" %average

  #calculate median
  def calculateMedian(self):
    self.listofNumbers.sort()
    mid = len(self.listofNumbers) // 2
    return (self.listofNumbers[mid] + self.listofNumbers[~mid]) / 2

  #calculate qth percentile using nearest rank approach
  def calculatePercentile(self):
    import numpy as np
    datalist=self.listofNumbers
    datalist = np.array(datalist)
    datalist = np.sort(datalist)
    n = len(datalist)
    rank = (self.q/100) * (n + 1)
    frac, whole = np.modf(rank)
    if frac == 0:
        return datalist[int(rank) - 1]
    else:
        low = datalist[int(whole - 1)]
        high = datalist[int(whole)]
        return low + frac * (high - low)






#verified the feature for various inputs
#parameters
q=3
listOfNumbers=[1,2,3,4,5]
#creating object
calcobject=mathOperation(q,listOfNumbers)

#calling the functions 
print("Min values :",calcobject.findMinNumbers())
print("Max values :",calcobject.findMaxNumbers())
print("Average value :",calcobject.calculateAverage())
print("Median :",calcobject.calculateMedian())
print("Percentile",calcobject.calculatePercentile())