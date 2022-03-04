# we can also mark the arguments of function as keyword only. that way while calling the function, the user will be forced to use correct keyword for each parameter

def hello(*, name='User'):
    print("Hello %s" % name)

    print (hello('vignesh')) 
