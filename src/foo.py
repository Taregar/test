a = 1
print("Hello World")

def start():
    bar()

def bar():
    return test()
def test():
    return bar()

start()
