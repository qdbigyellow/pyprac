"""Name caching"""

# 技术： 使用 dis.dis(func) 来检查分解的函数执行。 

class config:
    """Global configuration"""
    factor = 7.3
    threshold = 12


def normalize(numbers):
    """Normalize list of numbers"""
    norm = []
    for num in numbers:
        if num > config.threshold:    # 这种操作可以减少函数的行数，但是在一个loop里面每次都要做一个dict的lookup。 
            num /= config.factor      # 同上
        norm.append(num)              # 同上
    return norm


if __name__ == '__main__':
    import random

    random.seed(353)
    numbers = [random.randint(5, 50) for _ in range(1000)]      #generate test data
