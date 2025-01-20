# CardEncryptor 🔒💳

## 🔐 Overview

**CardEncryptor** is a Python class that replicates the encryption mechanism of FirstData V1 using single-line public keys. It securely encrypts credit card data for safe transmission, ensuring compliance with high-security standards.

## 🌟 Features

- **Single-Line Public Key**: Supports public keys in single-line format, converting them to PEM format automatically.
    
-   **Secure Encryption**: Utilizes RSA encryption with OAEP padding and SHA-256 hashing.
    
-   **Metadata Generation**: Includes field length metadata for added validation.
    
-   **Ease of Use**: Minimal setup required; simply pass your public key and card data.
    

----------

## 🚀 Usage Example

```python
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import logging

# Initialize the payload
payload = {
    "pk": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxU0Lvv1kDJsu3zH8hHe2bB14r3pDzeLR5/WUG54Ftpp9PHDwIjrjWRMSYYO0KhJP6R8/0dq5KGI7W01+Fk9O3omk8TI4hIZOlNZVXFVE9yfjB/hwp3pehWOGM7YJwMes1FCA/N23lV77l9zlJNYxAUdtY73KsBJhB6rBDDVTAIF7ko3xlbBKeZEqQH6NktS3k7YOYQ68mgvYuBts3GxpcBFRjelCzodK1turp/K9aK6NZCsMsq0tt4YcYiEpCVCzzYMhZ7R62/e8WBVT825QmxZq6TIjbuD/mSgBH/zePMgfIbnW8HuZVZu8WbZTOFowj2JBv9LjHnvR2O9nzcOS0QIDAQAB",
    "data": {
        "card": "4111111111111111",
        "cvv": "123",
        "exp": "0125",
        "name": "John Doe"
    }
}

# Initialize the encryptor
encryptor = CardEncryptor()

try:
    result = encryptor.encrypt_card_data(payload)
    encrypted_block = result['encryptedCard']['encryption_block']
    fields = result['encryptedCard']['encryption_block_fields']
    print(f"\ud83d\udd10 Encrypted Block: {encrypted_block}\n\ud83d\udcca Metadata: {fields}")
except ValueError as e:
    print(f"Encryption Failed: {str(e)}")
```

----------

## ⚙️ Installation

1.  **Clone the Repository**:
    
    ```bash
    git clone https://github.com/your-repo/CardEncryptor.git
    ```
    
2.  **Install Dependencies**:
    
    ```
    pip install pycryptodome
    ```
    

----------

## 📚 API Documentation

### `set_public_key(key_string: str) -> bool`

Converts a single-line public key to PEM format and sets it for encryption.

-   **Parameters**:
    
    -   `key_string`: Public key in single-line format.
        
-   **Returns**: `True` if the key is successfully set, `False` otherwise.
    

----------

### `encrypt_card_data(payload: dict) -> dict`

Encrypts credit card data using RSA and returns the encrypted block with metadata.

-   **Parameters**:
    
    -   `payload`: A dictionary containing `pk` (public key) and `data` (card details).
        
        -   `data` fields:
            
            -   `card`: Card number.
                
            -   `cvv`: Security code (optional).
                
            -   `exp`: Expiration date.
                
            -   `name`: Cardholder name.
                
-   **Returns**: A dictionary with the encrypted block and metadata.
    

----------

## 🌐 Connect with Us

📩 Questions? Reach out via Telegram for instant support.

🌟 Star us on [GitHub](https://github.com/Taiinyyy/CardEncryptor) to show your appreciation!

----------

## 🛠️ Built With

-   Python 3.8+
    
-   [PyCryptodome](https://www.pycryptodome.org/)
    
-   RSA Encryption
    

----------

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

----------

### Made with by [Taiinyy](t.me/Taiinyyy)