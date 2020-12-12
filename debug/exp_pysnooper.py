import pysnooper

@pysnooper.snoop()
def demo_func():
    profile = {}
    profile["name"] = "写代码的明哥"
    profile["age"] = 27
    profile["gender"] = "male"

    return profile

@pysnooper.snoop(output='debug.log', prefix="demo_func: ")
def demo_func2():
    profile = {}
    profile["name"] = "写代码的明哥"
    profile["age"] = 27
    profile["gender"] = "male"

    return profile
   
@pysnooper.snoop(watch=("counter"))
def demo_func3():
    for i in range(1, 10):
       counter = i * i
    return counter

@pysnooper.snoop(max_variable_length=200, thread_info=True)
def demo_func4():
    pass

def main():
    profile = demo_func()
    profile2 = demo_func2()
    profile3 = demo_func3()

main()