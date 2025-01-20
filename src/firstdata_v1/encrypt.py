import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import logging

class CardEncryptor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.public_key = None

    def set_public_key(self, key_string):
        try:
            # Format PEM key
            pem_lines = ['-----BEGIN PUBLIC KEY-----']
            pem_lines.extend([key_string[i:i+64] for i in range(0, len(key_string), 64)])
            pem_lines.append('-----END PUBLIC KEY-----')
            pem_key = '\n'.join(pem_lines)
            
            self.public_key = RSA.import_key(pem_key)
            return True
        except Exception as e:
            self.logger.error(f"Key import error: {str(e)}")
            return False
    def encrypt_card_data(self, payload):
        try:
            if 'pk' not in payload:
                raise ValueError('BAD_ENCRYPTION_KEY')
            
            self.set_public_key(payload['pk'])
            
            # Extract card data
            card_data = payload['data']
            if not card_data.get('card') or not card_data.get('exp') or not card_data.get('name'):
                raise ValueError('MISSING_REQUIRED_FIELDS')
            # Concatenate card data
            data_string = (
                card_data['card'] +
                card_data['name'] +
                card_data['exp'] +
                (card_data.get('cvv', '') or '')
            )

            # Create metadata
            metadata = [
                f"card.cardData:{len(card_data['card'])}",
                f"card.nameOnCard:{len(card_data['name'])}",
                f"card.expiration:{len(card_data['exp'])}"
            ]
            if 'cvv' in card_data:
                metadata.append(f"card.securityCode:{len(card_data['cvv'])}")
            metadata_string = ','.join(metadata)

            # Encrypt data
            cipher = PKCS1_OAEP.new(self.public_key, hashAlgo=SHA256)
            encrypted = cipher.encrypt(data_string.encode('utf-8'))
            encrypted_b64 = base64.b64encode(encrypted).decode('utf-8')

            return {
                'encryptedCard': {
                    'encryption_block': encrypted_b64,
                    'encryption_block_fields': metadata_string
                }
            }
            

        except Exception as e:
            error_msg = str(e)
            if 'key' in error_msg.lower():
                raise ValueError('BAD_ENCRYPTION_KEY')
            raise ValueError('ENCRYPTION_FAILED')

# Usage example
if __name__ == '__main__':
    payload = {
        "pk": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxU0Lvv1kDJsu3zH8hHe2bB14r3pDzeLR5/WUG54Ftpp9PHDwIjrjWRMSYYO0KhJP6R8/0dq5KGI7W01+Fk9O3omk8TI4hIZOlNZVXFVE9yfjB/hwp3pehWOGM7YJwMes1FCA/N23lV77l9zlJNYxAUdtY73KsBJhB6rBDDVTAIF7ko3xlbBKeZEqQH6NktS3k7YOYQ68mgvYuBts3GxpcBFRjelCzodK1turp/K9aK6NZCsMsq0tt4YcYiEpCVCzzYMhZ7R62/e8WBVT825QmxZq6TIjbuD/mSgBH/zePMgfIbnW8HuZVZu8WbZTOFowj2JBv9LjHnvR2O9nzcOS0QIDAQAB",
        "data": {
            "card": "4111111111111111",
            "cvv": "123",
            "exp": "0125",
            "name": "John Doe"
        }
    }

    encryptor = CardEncryptor()
    try:
        result = encryptor.encrypt_card_data(payload)
        EncryptedBlock = result['encryptedCard']['encryption_block']
        Fields = result['encryptedCard']['encryption_block_fields']
        print(EncryptedBlock, Fields)
    except ValueError as e:
        print('Final error:', str(e))