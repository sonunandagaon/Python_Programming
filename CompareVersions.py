class Utility:
  #constructor
   def __init__(self,version1,version2):
     self.version1=version1
     self.version2=version2

     #CompareVersion method
   def compareVersion(self):     
      versions1 = [int(v) for v in self.version1.split(".")]
      versions2 = [int(v) for v in self.version2.split(".")]
      for i in range(max(len(versions1),len(versions2))):
         v1 = versions1[i] if i < len(versions1) else 0
         v2 = versions2[i] if i < len(versions2) else 0
         if v1 > v2:
            return 1
         elif v1 <v2:
            return -1
      return 0



#creating parameters 
ver1="1.2.9.9.9.9"    # verified this feature for various inputs 
ver2="1.3"

#creating object of class Utility    
compareversionsobj = Utility(ver1,ver2)
#calling the function
print(compareversionsobj.compareVersion())