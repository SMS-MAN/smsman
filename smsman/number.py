from . import error
from . import code

class Number:
 def __init__(self,status,number,id,api,error=None):
  self.status = status
  self.number = number
  self.id = id
  self.api = api
  self.error = error

 def __bool__(self):
  return self.status

 def __str__(self):
  if self.status:
   return str(self.number)
  else:
   return str(self.error)

 def getCode(self, try_count=1, interval=5, auto_end=True):
  rt = "BAD_API"
  for i in range(try_count):
   r = self.api.get("getStatus",id=self.id)
   if r:
    rt = r.data["text"]
    if rt == "STATUS_WAIT_CODE":
     pass
    elif rt.startswith("STATUS_OK"):
     code_ = ":".join(rt.split(":")[1:])
     if auto_end:
      self.endNumber()
     return code.Code(True,code_,self,error.Error(True,error=rt,error_full=rt+"\n\n"+str(r.data)))
    else:
     if auto_end:
      self.endNumber()
     return code.Code(False,None,None,error.Error(False,error=rt,error_full=rt+"\n\n"+str(r.data)))
   else:
    pass
   time.sleep(interval)
  
  if auto_end:
   self.endNumber()
  return code.Code(False,None,None,error.Error(False,error=rt,error_full=rt+"\n\n"+str(r.data)))
  

 def endNumber(self):
  r = self.api.get("setStatus",id = self.id)
  return r