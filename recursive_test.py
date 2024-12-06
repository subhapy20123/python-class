def tri_recursion(k):
  if(k > 0):
    print("value ",k)    
    result = k + tri_recursion(k-1)
    print(k,result)
  else:
    result = 0
  print("result",result)  
  return result

print("\n\nRecursion Example Results")
# print('dddd',tri_recursion(6))
def factorial(n): 
     
    # Checking the number
    # is 1 or 0 then
    # return 1
    # other wise return
    # factorial
    if (n==1 or n==0):
         
        return 1
     
    else:
        # Final response 
        return (n * factorial(n - 1))
    

print("factrial",factorial(1))    
                

class animal():
   def __init__(self,name,type):
      self.name=name
      self.type = type
   def show(self):
      print("Animal name is "+self.name)   


Obj_animal= animal("Tiger","king")
Obj_animal.show()
