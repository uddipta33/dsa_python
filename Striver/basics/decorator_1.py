def display_info(func):
    greeting = "Hello..."
    def inner():
        print(greeting)
        func()
        print("Done...")
    return inner

@display_info
def printer():
    print("Using printer")

# res_func = display_info(printer)
# res_func()
printer()
