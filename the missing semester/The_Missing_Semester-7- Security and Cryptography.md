### Security and Cryptography
#### 加密哈希函数
- 哈希函数是一种将任意长度的数据转换为固定长度的输出值的函数。
- 哈希函数的输入可以是任意长度的消息，输出是一个固定长度的摘要。
- 哈希函数的输出值可以用来验证数据的完整性、标识数据源、（承诺机制）防止数据篡改、索引数据等。
- 常见的哈希函数有 MD5、SHA-1、SHA-256、SHA-384、SHA-512 等。
- 加密哈希函数的特性
    - 单向性：计算结果仅由输入数据决定，无法通过输出值反推出输入数据。
    - 确定性：相同的输入数据必定会得到相同的输出值。
    - 无碰撞性：对于不同的输入数据，输出值必定不同。
#### 密匙生成函数
- 密匙生成函数（Key-Derivation Function，KDF）是一种用于生成加密密钥的算法。
- 特性：
    - 具有加密哈希函数的单向性和确定性。
    - 输出作为另一个加密算法的密匙。
    - 算法较慢：防止暴力攻击。
#### 加密算法
##### 对称加密算法
- 对称加密算法（Symmetric-key algorithm）是指使用相同的密钥进行加密和解密的算法。
- 加密：将明文（plaintext）与密钥（key）一起输入加密算法，输出密文（ciphertext）.`encrypt(plaintext: array<byte>, key) -> array<byte> `
- 解密：将密文（ciphertext）与密钥（key）一起输入解密算法，输出明文（plaintext）。`decrypt(ciphertext: array<byte>, key) -> array<byte>`
- 性质：
    - 加密方法 encrypt() 输出的密文 ciphertext 很难在不知道 key 的情况下得出明文 plaintext。
    - 解密方法 decrypt() 有明显的正确性。因为功能要求给定密文及其密钥，解密方法必须输出明文：decrypt(encrypt(m, k), k) = m。
    - 加密和解密方法都需要同一密钥 key，密匙一般由密钥生成函数生成，且具有高熵性。
- 例子：openssl
    > `openssl ase-256-cbc -salt -in
    plaintext.txt -out ciphertext.txt -k secret` 这条命令使用 AES-256-CBC 加密 plaintext.txt，并使用 secret 作为密钥，输出密文 ciphertext.txt。
    > `openssl aes-256-cbc -d -in ciphertext.txt -out plaintext.txt -k secret` 这条命令使用 AES-256-CBC 解密 ciphertext.txt，并使用 secret 作为密钥，输出明文 plaintext.txt。
##### 非对称加密算法
- 非对称加密算法（Asymmetric-key algorithm）是指使用不同的密钥进行加密和解密的算法。
- 加密：将明文（plaintext）与公钥（public key）一起输入加密算法，输出密文（ciphertext）。`encrypt(plaintext: array<byte>, public_key) -> array<byte>`
- 解密：将密文（ciphertext）与私钥（private key）一起输入解密算法，输出明文（plaintext）。`decrypt(ciphertext: array<byte>, private_key) -> array<byte>`
- 性质：
   - 公钥可以被公开，任何人都可以通过公钥加密数据，但只有私钥可以解密数据。
- 应用:
    - 数字签名：使用私钥加密消息，使用公钥验证消息的完整性。
    - PGP 电子邮件加密：用户可以将所使用的公钥在线发布，比如：PGP 密钥服务器或 Keybase。任何人都可以向他们发送加密的电子邮件。


