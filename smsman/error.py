class Error:
 def __init__(self,status=False,data=None,error=None,error_full=None):
  self.status = status
  self.data = data
  self.error = error
  self.error_full = error_full

 def __bool__(self):
  return self.status

 def __str__(self):
  if self.status:
   return str(self.data)
  else:
   return str(self.error)