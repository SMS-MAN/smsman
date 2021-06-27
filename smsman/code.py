class Code:
 def __init__(self,status,code,number,error):
  self.status = status
  self.code = code
  self.number = number
  self.error = error

 def __bool__(self):
  return self.status

 def __str__(self):
  if self.status:
   return str(self.code)
  else:
   return str(self.error)