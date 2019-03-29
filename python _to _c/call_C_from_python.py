Here, in this tutorial, I am going to tutor you a simple Python wrapper for C library. And how to call C functions from Python?

Before beginning this, let’s see…

Why do we need of Calling C Functions from Python?
Till now I have talked about many plus points about Python.

But…

There is One of the major disadvantages of the Python – its execution speed. 🙁  Python is slower than many of the competitive programming language like C, Java…

C and CPP is a very standard programming language. And there are so many libraries already available in C.

To enhance the speed of the Python and to make the reuse of existing C libraries, the concept of calling C functions from Python is useful.

So there are two advantages of using C libraries (or C functions):

As the library is compiled from C programming, it increases the spread of execution. (C program runs faster than Python program.)
There are many C libraries are already build. Reusing existing C libraries saves time and resource.
In fact, there are many Python inbuilt standard libraries are written in C. You may not have noticed it, but many times when you call inbuilt function, it executes C function internally.

So coming to our coding part…

How to create these C libraries?

In this tutorial, I am going to tell you, how to compile C program to create library and step by step procedure for calling C functions from Python code.

Creating C library and Calling C Functions from Python:
Steps…

Write a C program with function definition
Write a C program header file with all function declaration
Create C library that can be used in Python
Calling C functions from Python program
To understand this tutorial, we will create an arithmetic application where all the arithmetic definition are written in C. And we will write a wrapper using Python called calcithat will call the function written in C program.

Let’s begin…

Step 1: Write a C program with functions definition
First of all, write a simple C program with functions definition.

Even if you know the basic of C and C++ programming, you can write the function in C that performs the basic arithmetic operations.

Following is code in C.
#include <stdio.h>
#include <stdlib.h>
#include "arithmatic.h"
 
void connect()
{
    printf("Connected to C extension...\n");
}
 
//return random value in range of 0-50
int randNum()
{
        int nRand = rand() % 50; 
    return nRand;
}
 
//add two number and return value
int addNum(int a, int b)
{
    int nAdd = a + b;
    return nAdd;
}
Note: There is no function main() in above program. There are only function definitions that we are going to call them from Python program.

Save above program as arithmatic.c.

Step 2: Write a C Program Header File with all Function Declaration
We may have noticed in above C program as we have included header file as arithmatic.h.


void connect();
int randNum();
int addNum(int a, int b);
This header file contains declarations of all the arithmetic functions.

Save the file as aithmatic.h. in the same directory.

Step 3: Create C library that can be used in Python
You need gcc compiler to compile C program.

To use that C function in Python you need to compile and generate the shared object.

Now Compile C program Using gcc Compiler:

gcc -c -fPIC arithmatic.c -o arithmatic.o
It will generate .o file. Run below command to get shared object .so file from .o.

gcc hello.o -shared -o libcalci.so
It will create the file libcalci.so.

Another way using the Single Command:

We are only interested in file .so (shared object). So, we can skip creating .o file.

You can merge above two commands into one, that will give you shared object without getting .o object file.

gcc -shared -o libcalci.so -fPIC arithmatic.c
After running this command you see th file libcalci.so is generated in current directory.

Backend C library (libcalci.so) is ready to use. We can import it into our Python program to use it.

Note: You need to generate shared object .so file for Linux, OS X, etc. For the Window OS,  you need to generate .dll file.

Step 4: Calling C Functions from Python Program
As like Python programming, writing wrapper is easier than it sounds.

To call C functions from Python wrapper, you need to import ctypes foreign function library in Python code.

(You can read more about this library on Python official document.)

Load .so file that we have created in the previous step by creating an instance of CDLL. Just call to its constructor function CDLL(). It returns object variable (says libCalc).

Now, with this object variable, you can call and pass input parameters to C functions just like calling normal Python class functions.

Here is simple code…

from ctypes import *
libCalc = CDLL("./libcalci.so")
 
#call C function to check connection
libCalc.connect() 
 
#calling randNum() C function
#it returns random number
varRand = libCalc.randNum()
print "Random Number:", varRand, type(varRand)
 
#calling addNum() C function
#it returns addition of two numbers
varAdd = libCalc.addNum(20,30)
print "Addition : ", varAdd

Output:
Connected to C extension...
Random Number: 27 <type 'int'>
Addition: 50

In the program, we used function type() to identify return data type of the C function’s variable.

This is all about creating C library and calling C functions with Python. If you have any question or doubt, write in a comment. I do reply all comments.

Some points to Acknowledge:

We are using ctype native Python module to load shared library.
The ctype Python module is available from 2.5 Python version. So, just ensure you have the latest version installed on your system
All these commands and programs in this tutorial are run on Ubuntu Linux system. And it will work for all other systems as well.
Before learning Python, I learned C programming. Whenever I require, many times I reuse existing C programs (those are written earlier on my system) in Python. It saves my lots of time. Even, it is the useful approach of writing your own C library and executing complex logic faster in C functions.

Hope you enjoy this tutorial.

If you want to be the expert Python programmer, you can follow my complete Python tutorial for FREE.
