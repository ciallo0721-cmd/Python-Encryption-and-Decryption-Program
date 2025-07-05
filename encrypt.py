import random
from pypinyin import pinyin, Style

# 中文转拼音
def chinese_to_pinyin(text):
    pinyin_list = pinyin(text, style=Style.NORMAL)
    return ' '.join([item[0] for item in pinyin_list])

# 数字转英文单词
def number_to_english(num_str):
    num_map = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    return ' '.join([num_map[char] for char in num_str])

# 凯撒加密（密钥3）
def caesar_encrypt(text, shift=3):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

# 混入随机中文和数字
def add_random_chars(text):
    chinese_chars = "你好世界Python编程"
    result = list(text)
    # 随机插入3-5个中文或数字
    for _ in range(random.randint(3, 5)):
        pos = random.randint(0, len(result))
        result.insert(pos, random.choice(chinese_chars))
    return ''.join(result)

# 主加密函数
def encrypt_text(input_text, user_key):
    # 处理数字
    processed = []
    i = 0
    while i < len(input_text):
        if input_text[i].isdigit():
            num_str = ''
            while i < len(input_text) and input_text[i].isdigit():
                num_str += input_text[i]
                i += 1
            processed.append(number_to_english(num_str))
        else:
            processed.append(input_text[i])
            i += 1
    
    processed = ''.join(processed)
    # 中文转拼音
    processed = chinese_to_pinyin(processed)
    # 凯撒加密
    processed = caesar_encrypt(processed)
    # 混入随机字符
    processed = add_random_chars(processed)
    # 添加用户密钥（异或加密）
    key_bytes = user_key.encode()
    text_bytes = processed.encode()
    encrypted_bytes = bytearray()
    for idx, byte in enumerate(text_bytes):
        encrypted_bytes.append(byte ^ key_bytes[idx % len(key_bytes)])
    return encrypted_bytes.hex()

if __name__ == "__main__":
    input_text = input("请输入要加密的文本: ")
    user_key = input("请输入用户密钥: ")
    encrypted = encrypt_text(input_text, user_key)
    print("加密结果:", encrypted)