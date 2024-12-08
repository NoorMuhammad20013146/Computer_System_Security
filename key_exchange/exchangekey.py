import requests
import base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

#Class MaliciousKey Exchanger
class MaliciousKeyExchanger:
    def __init__(self):
        self.compromised_keys = {}
    
#Create RSA key Pair for malicious purpose
