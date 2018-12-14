class Foo:
    def hello(self):
        print('hello world')

class Bar:
    def welcome(self):
        print('how are you??')

class FooBar(Foo, Bar):
    pass

if __name__ == '__main__':
    mm = FooBar()
    mm.welcome()
    mm.hello()
    
