'''
*
**
***
****
*****

'''
for i in range(1, 6):
    for j in range(0, i):
        print("*", end="")
    print()
    
print("----------------")
for i in range(5):
    print("*" * (i + 1))
print("----------------")

'''
*****
****
***
**
*
'''
for i in range(5, 0, -1):
    print("*"*i)
print("----------------")
    
'''
    *
   **
  ***
 ****
*****
'''
for i in range(5):
    print(" "*(4 - i),end="")
    print("*"*(i + 1))
    
print("----------------")    

'''
*****
 ****
  ***
   **
    *
'''
for i in range(5):
    print(" "*i,end="")
    print("*"*(5-i))
print("----------------")    
'''
    *
   ***
  *****
 *******
*********
'''
for i in range(5):
    print(" " * (4-i),end="")
    print("*" *(2*(i+1)-1))
    
