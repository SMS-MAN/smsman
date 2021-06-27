# smsman
sms-man.com module for buy virtual numbers



# Installing

### Linux:
```
sudo python3 setup.py install
```

### Windows:
```
py setup.py install
```


# Example:
```
>>> import smsman                                     #connecting module
>>> api = smsman.Smsman("your_api_key")               #connect to sms-man.com api
>>> print(api.getBalance())                           #checking balance
900.34
>>> numb = api.getNumber("0","tg")                    #buying number
>>> if numb:                                          #check if we buy number or not
...  print("Number:",str(numb))                       #if yes, print number and do with them anything what we need
...  #do anything
... else:
...  print("Error:",str(numb))                        #if no, print error
...
Number: 7916*******                                   
>>> code = numb.getCode(try_count=10,interval=6)      #if number buyed succesfull and code sended, calling this method and waiting
>>> if code:                                          #checking, code recieved or not
...  print("Code recived:",str(code))                 #if code recived, print it and complete registration
...  #complete registration
... else:
...  #cancel registration
...  print("Code not recieved, error:",str(code))     #if not, print error and cancel number
...  numb.endNumber()
...
Code recived: 34297
>>> numb.endNumber()                                  #after working with number, end it
```
