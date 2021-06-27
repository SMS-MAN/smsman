import requests
from traceback import format_exc
from . import number
from . import error



class Smsman:
 def __init__(self,api_key,timeout=20,proxy=None):
  self.api_key = api_key
  self.timeout = timeout
  self.proxy = proxy
  self.__url = "http://api.sms-man.ru/stubs/handler_api.php"

 def get(self,action,**k):
  link = "null"
  rt = "null"
  try:
   link = self.__url+f"?action={action}&api_key={self.api_key}&"+"&".join([i+"="+k[i] for i in k.keys()])
   r = requests.get(link)
   rt = r.text
   return error.Error(True,{"link":link,"text":rt})
  except Exception as e:
   return error.Error(False,error=str(e),error_full=format_exc())

 def getBalance(self):
  r = self.get("getBalance")
  if r:
   try: return r.data["text"].split(":")[-1]
   except: return r.data["text"]
  else:
   return str(r)


 def getNumber(self,country,service,try_count=1,interval=5):
  rt = "BAD_API"
  for i in range(try_count):
   r = self.get("getNumber",service=service,country=country)
   if r:
    rt = r.data["text"]
    if rt == "NO_NUMBERS":
     pass
    elif rt.startswith("ACCESS_NUMBER"):
     n = rt.split(":")[1:]
     return number.Number(True,n[1],n[0],self,error.Error(True,error=rt,error_full=rt+"\n\n"+str(r.data)))
    else:
     return number.Number(False,None,None,None,error.Error(False,error=rt,error_full=rt+"\n\n"+str(r.data)))
   else:
    pass
   time.sleep(interval)
  
  return number.Number(False,None,None,None,error.Error(False,error=rt,error_full=rt+"\n\n"+str(r.data)))
  




