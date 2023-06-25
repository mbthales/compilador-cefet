# Parsinho

## Content Table

- [Parsinho](#parsinho)
  - [Content Table](#content-table)
  - [About ](#about-)
  - [Getting Started ](#getting-started-)
    - [Installation ](#installation-)
    - [Running ](#running-)
    - [How it Works ](#how-it-works-)
    - [Examples ](#examples-)
  - [Build With ](#build-with-)
  - [Contributing ](#contributing-)

## About <a name="about"></a>

Parsinho is a programming language in portuguese focused for those who are starting in the programming world.

## Getting Started <a name="getting_started"></a>

### Installation <a name="installation"></a>

- You need to have Python >= 3.10.6 and pip >= 22.0.2 in your machine.
- Clone this repository.
- Run `pip3 install -r requirements.txt `

### Running <a name="running"></a>

- Run `python3 yacc.py`

### How it Works <a name="how-it-works"></a>

- You can create a variable with `var`. Ex:
  - `var test = "hello"`
- To create a string, use quotation marks and not apostrophes
- You have the option to use three functions:
  - mostrar: show on terminal
  - maiusculo: transform the string to uppercase
  - minusculo: transform the string to lowercase
- You have the option to use the `se` conditional. It works like the `if` statement.
- `inicio` and `fim` denote the beginning and end of the block scope.

### Examples <a name="examples"></a>

```
var test = "hello"
mostrar(minusculo(test))
```

```
se 20 < 10
   inicio
      var test = "hello"
      mostrar(minusculo(test))
   fim
```

```
var test = "HELLO"
var test_minusculo = minusculo(test)
mostrar(test_minusculo)

se 5 < 10
   inicio
      mostrar("hey")
   fim
```

## Build With <a name="build_with"></a>

- Python

## Contributing <a name="contributing"></a>

If you're interested in contributing, please follow these steps:

1. Fork this repository and clone it to your local machine.
2. Create a new branch for your contribution.
3. Make your desired changes and improvements.
4. Test your changes to ensure they work correctly.
5. Commit your changes with a descriptive message.
6. Push your changes to your forked repository.
7. Open a pull request in this repository to submit your changes.

Thank you for your contribution!
