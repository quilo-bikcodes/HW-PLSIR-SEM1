class Dict2Class(object):
      
    def __init__(self, my_dict):
          
        for key in my_dict:
            setattr(self, key, my_dict[key])
  
# Driver Code
if __name__ == "__main__":
      

    my_dict = {"Name": "Geeks",
               "Rank": "1223",
               "Subject": "Python"}
      
    result = Dict2Class(my_dict)
      

    print("After Converting Dictionary to Class : ")
    print(result.Name, result.Rank, result.Subject)
    print(type(result))