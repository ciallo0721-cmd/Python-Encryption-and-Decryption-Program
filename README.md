# Caesar Cipher with Chinese Support

这是一个支持中文的凯撒密码加密/解密工具。该工具可以将中文转换为拼音后加密，处理数字，并添加二次加密层增强安全性。

## 功能特点
- 中文转拼音后加密
- 数字转英文单词后加密
- 凯撒密码加密（密钥3）
- 添加随机中文干扰
- 用户自定义密钥二次加密
- 解密功能还原原始内容

## 安装

```bash
git clone https://github.com/yourusername/caesar-cipher-chinese.git
cd caesar-cipher-chinese
pip install -r requirements.txt
```

## 使用方法

### 加密文本
```bash
python encrypt.py
```
输入要加密的文本和用户密钥

### 解密文本
```bash
python decrypt.py
```
输入用户密钥和加密后的文本

## 注意事项
1. **密钥安全**：加密和解密必须使用相同的密钥
2. **中文处理**：解密后中文显示为拼音（如"你好" → "ni hao"）
3. **数字处理**：数字会转换为英文单词加密（123 → "one two three"）
4. **依赖库**：需要安装pypinyin库（`pip install pypinyin`）
5. **字符集**：支持标准ASCII字符和中文字符

---

# 中文対応シーザー暗号ツール

このツールは、中国語をサポートしたシーザー暗号の暗号化/復号化ツールです。中国語をピンインに変換して暗号化し、数字を処理し、セキュリティを強化するための二重暗号化層を追加します。

## 特徴
- 中国語をピンインに変換して暗号化
- 数字を英単語に変換して暗号化
- シーザー暗号暗号化（キー3）
- ランダムな中国語文字を追加して妨害
- ユーザー定義キーによる二重暗号化
- 復号化機能で元の内容を復元

## インストール

```bash
git clone https://github.com/yourusername/caesar-cipher-chinese.git
cd caesar-cipher-chinese
pip install -r requirements.txt
```

## 使用方法

### テキストの暗号化
```bash
python encrypt.py
```
暗号化するテキストとユーザーキーを入力

### テキストの復号化
```bash
python decrypt.py
```
ユーザーキーと暗号化されたテキストを入力

## 注意事項
1. **キーの安全性**：暗号化と復号化には同じキーを使用する必要があります
2. **中国語処理**：復号化後、中国語はピンインで表示されます（例："你好" → "ni hao"）
3. **数字処理**：数字は英単語に変換されて暗号化されます（123 → "one two three"）
4. **依存ライブラリ**：pypinyinライブラリが必要です（`pip install pypinyin`）
5. **文字セット**：標準ASCII文字と中国語文字をサポート

---

# Caesar Cipher with Chinese Support

This tool provides Caesar cipher encryption/decryption with support for Chinese characters. It converts Chinese to Pinyin before encryption, handles numbers, and adds a secondary encryption layer for enhanced security.

## Features
- Encrypt Chinese by converting to Pinyin
- Convert numbers to English words before encryption
- Caesar cipher encryption (key 3)
- Add random Chinese characters as noise
- Secondary encryption with user-defined key
- Decryption function to recover original content

## Installation

```bash
git clone https://github.com/yourusername/caesar-cipher-chinese.git
cd caesar-cipher-chinese
pip install -r requirements.txt
```

## Usage

### Encrypt text
```bash
python encrypt.py
```
Enter text to encrypt and user key

### Decrypt text
```bash
python decrypt.py
```
Enter user key and encrypted text

## Important Notes
1. **Key Security**: The same key must be used for encryption and decryption
2. **Chinese Handling**: Decrypted Chinese appears as Pinyin (e.g., "你好" → "ni hao")
3. **Number Handling**: Numbers are converted to English words (123 → "one two three")
4. **Dependencies**: Requires pypinyin library (`pip install pypinyin`)
5. **Character Set**: Supports standard ASCII characters and Chinese characters

## Contribution
Contributions are welcome! Please open an issue or pull request for any improvements.

## License
This project is licensed under the MIT License.
