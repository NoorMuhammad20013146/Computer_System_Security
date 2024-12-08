import requests
import base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

#Class MaliciousKey Exchanger
class MaliciousKeyExchanger:
    def __init__(self):
        self.compromised_keys = {}
    
#Create RSA key Pair for malicious purpose
    def create_attack_keypair(self):
        attacker_private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        attacker_public_key = attacker_private_key.public_key()
        return attacker_private_key, attacker_public_key
    