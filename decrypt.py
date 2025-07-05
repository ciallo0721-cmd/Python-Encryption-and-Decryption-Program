# 凯撒解密（密钥3）
def caesar_decrypt(text, shift=3):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

# 英文单词转数字
def english_to_number(text):
    word_map = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    result = []
    words = text.split()
    for word in words:
        result.append(word_map.get(word, word))
    return ''.join(result)

# 主解密函数
def decrypt_text(encrypted_hex, user_key):
    # 用户密钥异或解密
    key_bytes = user_key.encode()
    encrypted_bytes = bytes.fromhex(encrypted_hex)
    decrypted_bytes = bytearray()
    for idx, byte in enumerate(encrypted_bytes):
        decrypted_bytes.append(byte ^ key_bytes[idx % len(key_bytes)])
    processed = decrypted_bytes.decode()
    
    # 删除中文（非ASCII字符）
    cleaned = ''.join(char for char in processed if char.isascii())
    # 凯撒解密
    cleaned = caesar_decrypt(cleaned)
    # 英文数字单词转回数字
    return english_to_number(cleaned)

if __name__ == "__main__":
    user_key = input("请输入用户密钥: ")
    encrypted_hex = input("请输入加密文本: ")
    decrypted = decrypt_text(encrypted_hex, user_key)
    print("解密结果:", decrypted)