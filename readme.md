# my_module.py

def some_function():
    print("This is a function in my_module.")

if __name__ == "__main__":
    print("This code runs only when the script is executed directly.")
    some_function()
In this example, if you run my_module.py directly, it will execute the code inside the if __name__ == "__main__": block, including the call to some_function(). However, if you import my_module into another script, the code inside the if __name__ == "__main__": block will not be executed when the module is imported. This allows you to define reusable functions and classes in your modules while also providing a way to include script-specific code that should only run when the script is the main program.