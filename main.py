from Crypto.Cipher import AES
import base64,os,uuid 
import time,hashlib

x = 0
dataVal = float(input("enter value upto 2 decimal places"))
class node:
  def __init__(self,gen):
    if gen is 0:
      global x,dataVal
      x = x + 1
      self.timeStamp = time.time()
      self.nodeId = uuid.uuid1().int>>32
      self.nodeNum = x
      self.refNodeId = None
      self.childRefNodeId = None
      self.genRefNodeId = None
      self.data = self.encrypt(val = dataVal)
      self.hashVal = hashlib.md5(str([self.timestamp, self.data, self.nodeNum, self.nodeId, self.refNodeId, self.childRefNodeId, self.genRefNodeId]))



  def encrypt(val):
    pass

  def get_secret_key():
    AES_key_length = 32
    secret_key = os.urandom(AES_key_length)
    encoded_secret_key = base64.b64encode(secret_key)
    return encoded_secret_key
  
  def create_node(self):
    self.nodeNum = x
    self.timeStamp = time.time()
    self.data = self.encrypt()
  
  