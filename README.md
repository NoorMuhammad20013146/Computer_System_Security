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
I have added a code file of exchange_key folder in the github for this process.
