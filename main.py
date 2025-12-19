class cifraCesar(str):
    def __init__(self):
        self.ALFABETH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encode(self, text) -> list:
        text = text.upper()
        indices = []
        for char in text:
            if char in self.ALFABETH:
                indices.append(self.ALFABETH.index(char))
            else:
                indices.append(char) # keep spaces and punctuation
        return indices

    def decode(self, indices)->str:
        text =""
        for item in indices:
            if isinstance(item, int):
                text += self.ALFABETH[item]
            else:
                text += item
        return text

    def encrypt(self, enc_text:list, key):
        cipher_text= []
        for enc_char in enc_text:
            if isinstance(enc_char, int):
                cipher_text.append((enc_char + key) % 26)
            else:
                cipher_text.append(enc_char)
        return cipher_text

    def decrypt (self, cipher_text:list, key):
        dec_text = []
        for char in cipher_text:
            if isinstance(char, int):
                dec_text.append((char - key)% 26)
            else:
                dec_text += char
        return dec_text

    def full_encrypt(self, text: str, key: int) -> str:
        encoded = self.encode(text)
        encrypted = self.encrypt(encoded, key)
        fully_encrypter_text = self.decode(encrypted)
        return fully_encrypter_text

    def full_decrypt(self, text:str, key:int) -> str:
        encoded =self.encode(text)
        decrypted = self.decrypt(encoded, key)
        fully_decrypted_text = self.decode(decrypted)
        return fully_decrypted_text

a =cifraCesar()

operacao = input("Digite 'c' para criptografar ou 'd' para descriptografar: ").lower()
texto = input("Digite o texto: ")
chave = int(input("Digite a chave (número inteiro): "))

if operacao== 'c':
    resultado = a.full_encrypt(texto, chave)
    print("Texto criptografado:", resultado)
elif operacao == 'd':
    resultado = a.full_decrypt(texto, chave)
    print("Texto descriptografado:", resultado)
else:
    print("Operação inválida. Digite 'c' ou 'd'.")