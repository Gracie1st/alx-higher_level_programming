Object Oriented Programming

In all the programs we wrote till now, we have designed our program around functions i.e. blocks of statements which manipulate data. This is called the procedure-oriented way of programming. There is another way of organizing your program which is to combine data and functionality and wrap it inside something called an object. This is called the object oriented programming paradigm. Most of the time you can use procedural programming, but when writing large programs or have a problem that is better suited to this method, you can use object oriented programming techniques.



Classes and objects are the two main aspects of object oriented programming. A class creates a new type where objects are instances of the class. An analogy is that you can have variables of type int which translates to saying that variables that store integers are variables which are instances (objects) of the int class.



Note for Static Language Programmers



Note that even integers are treated as objects (of the int class). This is unlike C++ and Java (before version 1.5) where integers are primitive native types.



See help(int) for more details on the class.



C# and Java 1.5 programmers will find this similar to the boxing and unboxing concept.



Objects can store data using ordinary variables that belong to the object. Variables that belong to an object or class are referred to as fields. Objects can also have functionality by using functions that belong to a class. Such functions are called methods of the class. This terminology is important because it helps us to differentiate between functions and variables which are independent and those which belong to a class or object. Collectively, the fields and methods can be referred to as the attributes of that class.



Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself. They are called instance variables and class variables respectively.



A class is created using the class keyword. The fields and methods of the class are listed in an indented block.



The self

Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to the beginning of the parameter list, but you do not give a value for this parameter when you call the method, Python will provide it. This particular variable refers to the object itself, and by convention, it is given the name self.



Although, you can give any name for this parameter, it is strongly recommended that you use the name self - any other name is definitely frowned upon. There are many advantages to using a standard name - any reader of your program will immediately recognize it and even specialized IDEs (Integrated Development Environments) can help you if you use self.



Note for C++/Java/C# Programmers



The self in Python is equivalent to the this pointer in C++ and the this reference in Java and C#.



You must be wondering how Python gives the value for self and why you don't need to give a value for it. An example will make this clear. Say you have a class called MyClass and an instance of this class called myobject. When you call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) - this is all the special self is about.



This also means that if you have a method which takes no arguments, then you still have to have one argument - the self.



Classes

The simplest class possible is shown in the following example (save as oop_simplestclass.py).



class Person:

    pass  # An empty block



p = Person()

print(p)

Output:



$ python oop_simplestclass.py

<__main__.Person instance at 0x10171f518>

How It Works



We create a new class using the class statement and the name of the class. This is followed by an indented block of statements which form the body of the class. In this case, we have an empty block which is indicated using the pass statement.



Next, we create an object/instance of this class using the name of the class followed by a pair of parentheses. (We will learn more about instantiation in the next section). For our verification, we confirm the type of the variable by simply printing it. It tells us that we have an instance of the Person class in the __main__ module.



Notice that the address of the computer memory where your object is stored is also printed. The address will have a different value on your computer since Python can store the object wherever it finds space.



Methods

We have already discussed that classes/objects can have methods just like functions except that we have an extra self variable. We will now see an example (save as oop_method.py).



class Person:

    def say_hi(self):

        print('Hello, how are you?')



p = Person()

p.say_hi()

# The previous 2 lines can also be written as

# Person().say_hi()

Output:



$ python oop_method.py

Hello, how are you?

How It Works



Here we see the self in action. Notice that the say_hi method takes no parameters but still has the self in the function definition.



The __init__ method

There are many method names which have special significance in Python classes. We will see the significance of the __init__ method now.



The __init__ method is run as soon as an object of a class is instantiated (i.e. created). The method is useful to do any initialization (i.e. passing initial values to your object) you want to do with your object. Notice the double underscores both at the beginning and at the end of the name.



Example (save as oop_init.py):



class Person:

    def __init__(self, name):

        self.name = name



    def say_hi(self):

        print('Hello, my name is', self.name)



p = Person('Swaroop')

p.say_hi()

# The previous 2 lines can also be written as

# Person('Swaroop').say_hi()

Output:



$ python oop_init.py

Hello, my name is Swaroop

How It Works



Here, we define the __init__ method as taking a parameter name (along with the usual self). Here, we just create a new field also called name. Notice these are two different variables even though they are both called 'name'. There is no problem because the dotted notation self.name means that there is something called "name" that is part of the object called "self" and the other name is a local variable. Since we explicitly indicate which name we are referring to, there is no confusion.



When creating new instance p, of the class Person, we do so by using the class name, followed by the arguments in the parentheses: p = Person('Swaroop').



We do not explicitly call the __init__ method. This is the special significance of this method.



Now, we are able to use the self.name field in our methods which is demonstrated in the say_hi method.
