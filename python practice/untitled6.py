def announce(f):
    def wrapper():
        print('Abot to print the function ')
        f()
        print('done with the function')

@announce
def hello():
    print('hello world')

hello()