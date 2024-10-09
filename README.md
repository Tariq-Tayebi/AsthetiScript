# The AsthetiScript Programming Language

## What Is It
The AsthetiScript Programming Language is a compiled, programming language with syntax similar to Python and C/C++. Apart from containing many native features from many universal languages, AsthetiScript also combines its versatile, easy to understand syntax with attributes not in many programming languages. For example, AsthetiScript can make web applications accompanying or overtaking HTML and CSS, while performing advanced calculations with speed usually reserved for C and C++.

## Quick Facts
>Year Created: 2024

>Where was it created: Sydney, Australia

>Compiled or Interpreted: Compilied by an interpreter!

>Standard Library: asc>...

>File Extension: .asth

## Tutorial and Syntax

In AsthetiScript, a '>' symbol denotes parenthood and childhood, compared to a '.' in Python. AsthetiScript uses an '@' symbol to include libraries, including the standard library. At the start of every code, you must type ```@using std - asc```. 
### Text
AsthetiScript has very high text functionality. To do plain text, type ```asc>text>plain("Text")``` for plain text or ```asc>text("Text")``` for text with the same style. There are many ways to format in console.
For example:
```asc>text>orange("HI")```
```asc>text>underline("HI")```

You can also make a custom ASCII code:
```asc>text>customcode("HI", 40)```

The class text contains all text functionality.

### If statements
AsthetiScript has a simple if statement syntax, the should method:
```
should (1 > 0) $
 asc>text("HI")
```
A ```$``` is used to show an if statement, instead of a {} or : in other languages.

we don't use asc>... as it is not in the standard library, but a key functionality.

Else if statement:
```
elshould (condition) $
 excecute
```

We also have a conditional operator (sometimes called the ternary operator in other languages):
```
x = conditional(1 > 0, true="true", "false")
```
you can take out the true= and false=, it is optional if you can't remember the side which is true or false.

### Variables
There are ints, floats, doubles, strings, and arrays in AsthetiScript.

You do not need to declare variable types.

Int:
```
var = 0
```

String:
```
var = "Sring"
```

Floats and Doubles:
```
var = 1.0
```

Array:
```
var = asc>array(4)
```
This creates an array with a length of 4.
