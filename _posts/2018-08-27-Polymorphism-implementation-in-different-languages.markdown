---
layout: post
title:  "Polymorphism implementation in dfferent languages"
date:   2018-08-27 10:48:54 +0800
categories: daily-posts
---

In fact, only referring polymorphism can be ambiguous as there are some more specific concepts regarding very different polymorphism behaviours in programming languages. And in this article, I am going to only talk about how to implement polymorphism in behaviours level using these code(Some of the languages listed below is object-oriented languages and thus may have built-in design to achieve it).

See [wikipedia](https://en.wikipedia.org/wiki/Polymorphism_(computer_science)) for some more details, here I am going to write about ad hoc polymorphism and parametric polymorphism(if the language has).

## C
The key is functions pointers.
See [StackOverflow-how-can-i-simulate-oo-style-polymorphism-in-c](https://stackoverflow.com/questions/524033/how-can-i-simulate-oo-style-polymorphism-in-c) 

[The most upvoted answer](https://stackoverflow.com/a/524060/7122122), I think, is incorrect, as also talked by another user in the comments. I think it is about inheritence, not polymorphism...

[This answer](https://stackoverflow.com/a/524056/7122122) seems to be right. 

Seems to what I have read in  the book ``clean architecture``. 

C code example from the book: 

```C
struct FILE {
	void (*open)(char* name, int mode);
	void (*close)();
	int (*read)();
	void (*write)(char);
	void (*seek)(long index, int mode);
};
```

`The IO driver for the console will define those functions and load uop a FILE data structure with their addresses -- something like this:
`

```C
#include "file.h"

void open(char* name, int mode) {/*...*/}
void close() {/*...*/}
int read() {int c; /*...*/ return c;}
void write(char c) {/*...*/}
void seek(long index, int mode) {/*...*/}
struct FILE console = {open, close, read, write, seek};
```

```
Now if STDIN is defined as a FILE*, and if it points to the console data structure, then getchar() might be implemented this way:
```

```C
extern struct FILE* STDIN

int getchar() {
	return STDIN->read();
}
```

[And the third answer](https://stackoverflow.com/a/524076/7122122) shows a simple implementation of C++ polymorphism.

In fact, I think it varies a lot for different people and different persons to define the behaviours of elements of OOP, such as inheritence and polymorphism. It is only meaningful to talk OOP in the boundary of a specific laguage.

Also, Appendix B in this paper shows a sample implementation in GNU C of the object model described in this paper. This code, and that of the benchmarks discussed in the text, can be downloaded from [here](http://piumarta.com/software/id-objmodel)

The code is too long, not going to show it here... And various pointers are used...🙄

REF

http://www.vpri.org/pdf/tr2006003a_objmod.pdf

https://stackoverflow.com/questions/524033/how-can-i-simulate-oo-style-polymorphism-in-c

Clean code: Clean Architecture: A Craftsman's Guide to Software Structure and Design -- Robert C. Martin


## TypeScript
From a [blog](http://rachelappel.com/write-object-oriented-javascript-with-typescript) of a developer in typescript team

>TypeScript enables polymorphism via method overrides as you can see in the example below. The Withdraw and Deposit methods of the CheckingAccount and SavingsAccount classes derive from the parent BankAccount class. In the child classes, we can override these methods and add our own business logic customizations, such as waving a fee if the balance is more than a specified amount.

>```typescript
export module Bank
{
    export interface Fee { ChargeFee(amount: number); }
    export class BankAccount implements Fee {
        ChargeFee(amount: number) { }
    }
}
class SavingsAccount extends BankAccount
{
    ChargeFee(amount: number)
    {
        if (this.Balance > 1000) { amount = 0; }
        else { amount += 1.00; }        
        this.Balance =+ amount;
    }
```

>In this case, we overrided the ChargeFee that was originally part of the Fee interface. Polymorphism is an essential characteristic of OO programming, as code would be quite redundant without it.

REF

https://www.reddit.com/r/typescript/comments/3jn5w1/is_adhoc_polymorphism_supported_in_typescript/

http://rachelappel.com/write-object-oriented-javascript-with-typescript/

## Cpp

@TODO


### ad hoc polymorphism

### parametric polymorphism
parametric polymorphism is usually called templates in C++,

## Rust
@TODO

## Java

@TODO
## Csharp
From csharp doc, the article itself is more worth reading a lot than solely some explanation here, recommend reading the article.

>You can use polymorphism to solve this problem in two basic steps: 

>Create a class hierarchy in which each specific shape class derives from a common base class.

>Use a virtual method to invoke the appropriate method on any derived class through a single call to the base class method.

>First, create a base class called `Shape`, and derived classes such as `Rectangle`, `Circle`, and `Triangle`. Give the Shape class a virtual method called Draw, and override it in each derived class to draw the particular shape that the class represents. Create a List<Shape> object and add a Circle, Triangle and Rectangle to it. To update the drawing surface, use a foreach loop to iterate through the list and call the Draw method on each Shape object in the list. Even though each object in the list has a declared type of Shape, it is the run-time type (the overridden version of the method in each derived class) that will be invoked. 
```C#

Copy
using System;
using System.Collections.Generic;

public class Shape
{
    // A few example members
    public int X { get; private set; }
    public int Y { get; private set; }
    public int Height { get; set; }
    public int Width { get; set; }
   
    // Virtual method
    public virtual void Draw()
    {
        Console.WriteLine("Performing base class drawing tasks");
    }
}

class Circle : Shape
{
    public override void Draw()
    {
        // Code to draw a circle...
        Console.WriteLine("Drawing a circle");
        base.Draw();
    }
}
class Rectangle : Shape
{
    public override void Draw()
    {
        // Code to draw a rectangle...
        Console.WriteLine("Drawing a rectangle");
        base.Draw();
    }
}
class Triangle : Shape
{
    public override void Draw()
    {
        // Code to draw a triangle...
        Console.WriteLine("Drawing a triangle");
        base.Draw();
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Polymorphism at work #1: a Rectangle, Triangle and Circle
        // can all be used whereever a Shape is expected. No cast is
        // required because an implicit conversion exists from a derived 
        // class to its base class.
        var shapes = new List<Shape>
        {
            new Rectangle(),
            new Triangle(),
            new Circle()
        };

        // Polymorphism at work #2: the virtual method Draw is
        // invoked on each of the derived classes, not the base class.
        foreach (var shape in shapes)
        {
            shape.Draw();
        }

        // Keep the console open in debug mode.
        Console.WriteLine("Press any key to exit.");
        Console.ReadKey();
    }

}

/* Output:
    Drawing a rectangle
    Performing base class drawing tasks
    Drawing a triangle
    Performing base class drawing tasks
    Drawing a circle
    Performing base class drawing tasks
 */
```

REF

https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/polymorphism

## Python



## Haskell
@TODO

## Golang
Use interfaces, 

REF

https://en.wikipedia.org/wiki/Polymorphism_(computer_science)

https://stackoverflow.com/questions/34908695/polymorphism-in-golang


