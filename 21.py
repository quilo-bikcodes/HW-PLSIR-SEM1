def func():
 
  
    a_variable = 0
 
  # for checking existence in locals() function
    if 'a_variable' in locals() or 'a_variable' in globals():
        return True
 

print(func())