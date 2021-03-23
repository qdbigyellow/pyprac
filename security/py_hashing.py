import hashlib

# https://mp.weixin.qq.com/s/Pr9_eH8wZRNOlu_lYsN1ug
#在Python中打印等效于MD5哈希的字节
result = hashlib.md5(b'Python Pool') 
print("Hash Value : ", end ="")
print(result)
print("Equivalent Byte : ", end ="") 
print(result.digest()) 

# 在Python中打印MD5哈希的十六进制等效项
result = hashlib.md5('Python Pool'.encode()) 
print("Hash Value : ", end ="")
print(result)
print("Hexadecimal Equivalent : ", end ="") 
print(result.hexdigest()) 

# Python MD5文件校验
import pathlib
curdir = pathlib.Path(__file__).parent.absolute()

md5_hash = hashlib.md5()
file = open(curdir.joinpath("hashing_test.txt"), "rb")
content = file.read()
md5_hash.update(content)
result = md5_hash.hexdigest()
print(result)

md5_hash_copy = hashlib.md5()
file = open(curdir.joinpath("hashing_test_copy.txt"), "rb")
content = file.read()
md5_hash_copy.update(content)
result = md5_hash_copy.hexdigest()
print(result)

# extra white space
md5_hash_xws = hashlib.md5()
file = open(curdir.joinpath("hashing_test_extraspace.txt"), "rb")
content = file.read()
md5_hash_xws.update(content)
result = md5_hash_xws.hexdigest()
print(result)

# 使用Python在MD5中编码字符串
string = "pythonpool.com"
encoded=string.encode()
result = hashlib.md5(encoded)
print("String : ", end ="")
print(string)
print("Hash Value : ", end ="")
print(result)
print("Hexadecimal equivalent: ",result.hexdigest())

# 在Python中计算文件的MD5哈希
with open(curdir.joinpath("hashing_test.txt"), "rb") as f:
    bytes = f.read()
    print("Bytes read from the file:",bytes)
    result = hashlib.md5(bytes)
    print("Hah Value: ",result)
    print("The hexadecimal equivalent: ")
    print(result.hexdigest())