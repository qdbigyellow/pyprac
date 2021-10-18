# https://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p13_using_mataclass_to_control_instance_creation.html
# https://mp.weixin.qq.com/s/2VhXC-Kfz2k827OxELG1pQ

def protect(*protected):
    """Returns a metaclass that protects all attributes given as strings"""
    class Protect(type):
        has_base = False
        def __new__(meta, name, bases, attrs):
            if meta.has_base:
                for attribute in attrs:
                    if attribute in protected:
                        raise AttributeError('Overriding of attribute "%s" not allowed.'%attribute)
            meta.has_base = True
            klass = super().__new__(meta, name, bases, attrs)
            return klass
    return Protect

class Animal(metaclass=protect('dead', 'eat')):
    def move(self):
        print('moving...')
        
    def dead(self):
        print('deading...')
        
    def eat(self):
        print('eating...')
        

class Dog(Animal):
    def move(self):
        print('moving with 4 leg')
    
    def dead(self):
        print('dead in 20 years')    
        

if __name__ == 'main':
    d = Dog()
    d.move()
    d.dead()
    
