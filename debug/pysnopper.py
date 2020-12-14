import pysnooper

# https://mp.weixin.qq.com/s/1a8Qcv5Tc4KcXFtk3koCqg

@pysnooper.snoop()
def demo_snoop():
    profile = {}
    profile["name"] = "写代码的明哥"
    profile["age"] = 27
    profile["gender"] = "male"

    return profile

@pysnooper.snoop(output='.\pysnooper_log.log')
def demo_snoop_trace_to_log():
    profile = {}
    profile["name"] = "写代码的明哥"
    profile["age"] = 27
    profile["gender"] = "male"

    return profile

# set prefix of the function in the log, in order to eaisily search in the log file
@pysnooper.snoop_with_func_prefix(output='.\pysnooper_log.log', prefix="demo_func: ")
def demo_snoop_trace_to_log():
    pass

# by default pysnoopyer only watch the local variable
# to watch global vairable, need use watch option.  
out = {'foo': 'bar'}
@pysnooper.snoop(watch=('out["foo"]'))
def demo_snoop_global_var():
    global out
    out['foo'] = 'newbar'
    profile = {}
    profile["name"] = "写代码的明哥"
    profile["age"] = 27
    profile["gender"] = "male"

    return profile

# watch multiple global varaiable
@pysnooper.snoop(watch=('out["foo"]', 'foo.bar', 'self.foo["bar"]'))
def demo_snoop_multi_global_vars():
    pass

# watch multiple global variable by excluding a few
@pysnooper.snoop(watch_explode=('out["foo"]'))
def demo_snoop_all_global_var_except():
    pass

# set the depth,  for nested function.  
@pysnooper.snoop(depth=2)
def demo_snoop_depth_for_nested_func():
    pass

# set max output length of each line
@pysnooper.snoop(max_variable_length=200)
def demo_snoop_depth_for_nested_func():
    pass

# set concurrency log
@pysnooper.snoop(thread_info=True)
def demo_snoop_on_multi_threads():
    pass

# snoop own class
class Person:
    def __init__(self):
        self.name = "name"
        self.age = "age"
        self.gender = "gender"

def snoop_person_obj(obj):
    return f"<Person {obj.name} {obj.age} {obj.gender}>

@pysnooper.snoop(custom_repr=(Person, snoop_person_obj))
def demo_snoop_own_class():
    person = Person()
    person.name = "写代码的明哥"
    person.age = 27
    person.gender = "male"
    return person
    
# snoop own classes.
@pysnooper.snoop(custom_repr=((Person, snoop_person_obj), (Animal, snoop_animal_obj)))
def demo_snoop_own_classes():  
    pass


def main():
    
    profile = demo_snoop_global_var()


if __name__ == "__main__":
    main()