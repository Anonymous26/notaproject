from Crypto.Cipher import AES
from Crypto import Random
import base64,os,uuid 
import time,hashlib

x = 0
dataVal = float(input("enter value upto 2 decimal places"))
ownerName = input("enter the name of the owner")
prOwnerId = 500
class node:
  def __init__(self,gen):
    if gen is 0:
      global x,dataVal,ownerName
      x = x + 1
      self.timeStamp = time.time()
      self.nodeId = uuid.uuid1().int>>32
      self.nodeNum = x
      self.refNodeId = None
      self.childRefNodeId = ''
      self.genRefNodeId = ''
      self.data = self.encrypt(val = dataVal, owner = ownerName, ownerId = prOwnerId)
      self.hashVal = hashlib.md5(str([self.timeStamp, self.data, self.nodeNum, self.nodeId, self.refNodeId, self.childRefNodeId, self.genRefNodeId]))



  def encrypt(self, val, owner, ownerId):
    hashId = hashlib.md5(str([owner, val, ownerId, self.nodeId]).encode()).hexdigest()

    if self.refNodeId is not None:
      parentId = self.refNodeId

    msg = str([owner, val, ownerId, hashId])
    secret_key = base64.b64decode(ownerId)
    cipher = AES.new(secret_key)
    # pad the private_msg
	  # because AES encryption requires the length of the msg to be a multiple of 16
    padded_private_msg = msg + ("-" * ((16-len(msg)) % 16))
	  # use the cipher to encrypt the padded message
    encrypted_msg = cipher.encrypt(padded_private_msg)
	  # encode the encrypted msg for storing safely in the database
    encode_encrypt_msg = base64.b64encode(encrypted_msg)
    return encode_encrypt_msg




  def get_secret_key(self):
    AES_key_length = 32
    secret_key = os.urandom(AES_key_length)
    encoded_secret_key = base64.b64encode(secret_key)
    return encoded_secret_key
  
  def create_node(self):
    self.nodeNum = x
    self.timeStamp = time.time()
    self.data = self.encrypt()
  
genesisNode = node(0)

def new_user():
  global prOwnerId
  name = input("enter name")
  ownerId = prOwnerId + 1
  prOwnerId += 1

#rest of the logic not created
