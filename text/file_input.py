# fileinput 这个模块只专注于输入（读）而不是输出（写）
# https://mp.weixin.qq.com/s/_PeJqraeMgTm6NQSEgX4Iw

import fileinput

# 当Python 脚本没有传入任何参数时，fileinput 默认会以 stdin 作为输入源
# for line in fileinput.input():
#     print(line)
#     break
    

# 默认使用 mode='r' 的模式读取文件，如果你的文件是二进制的，可以使用mode='rb' 模式
with fileinput.input(files=("text/demo.txt", )) as file:
    for line in file:
        print(f'{fileinput.filename()} 第{fileinput.lineno()}行: {line}', end='')
        
# files accept "set" or "list"  for multiple files  
# in this case, "demo1.txt" and "demo2.txt" are combined to one file in memory    
# notice the diff of lineno(), and filelineno()
with fileinput.input(files=("text/demo.txt", "text/demo2.txt" )) as file:
    for line in file:
        print(f'{fileinput.filename()} 第{fileinput.lineno()}行: {line}', end='')        
        print(f'{fileinput.filename()} 第{fileinput.filelineno()}行: {line}', end='') 
        

# Together with glob
import glob

for line in fileinput.input(glob.glob("*.txt")):
    if fileinput.isfirstline():
        print('-'*20, f'Reading {fileinput.filename()}...', '-'*20)
    print(str(fileinput.lineno()) + ': ' + line.upper(), end="")
    
    
# fileinput.input 有一个 backup 参数，你可以指定备份的后缀名，比如 .bak
with fileinput.input(files=("text/demo.txt",), backup=".bak") as file:
    for line in file:
        print(f'{fileinput.filename()} 第{fileinput.lineno()}行: {line}', end='') 

# fileinput.input 有一个 inplace 参数，表示是否将标准输出的结果写回文件，默认不取代
with fileinput.input(files=("a.txt",), inplace=True) as file:
    print("[INFO] task is started...") 
    for line in file:
        print(f'{fileinput.filename()} 第{fileinput.lineno()}行: {line}', end='') 
    print("[INFO] task is closed...") 
    
# 实现文本替换    
import sys

for line in fileinput.input(files=('a.txt', ), inplace=True):
    #将Windows/DOS格式下的文本文件转为Linux的文件
    if line[-2:] == "\r\n":  
        line = line + "\n"
    sys.stdout.write(line)
    
