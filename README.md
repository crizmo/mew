# Mew Interpreter Project

This project is a simple stack-based interpreter written in Python. It interprets a custom bytecode language with a variety of opcodes. 
The source code files are written in `.mew` extension.

## Project Structure

The project consists of the following files:

- `main.py`: The main driver of the program. It reads the `.mew` files, parses the opcodes and operands, and passes them to the interpreter for execution.
- `modules/interpreter.py`: Contains the Interpreter class which executes the opcodes.
- `modules/stack.py`: Contains the Stack class which is used by the interpreter to store values.
- `modules/opcodes.py`: Defines the opcodes that the interpreter can execute.

## Features

The interpreter supports a variety of opcodes, including `PUSH`, `PRINT`, `SHOW`, and `JUMP.EQ.0`. For a full list of supported opcodes, refer to the `opcodes.py` file.

## Usage

To use the interpreter, you need to provide it with a program written in the custom bytecode language. The program should be a list of opcodes and operands in a `.mew` file. Run the `main.py` file with the `.mew` file as an argument.

## Requirements

- Python 3.x

## Installation

No installation is necessary. Just clone the repository and run `main.py` with Python.

## Contributing

Contributions are welcome. Please submit a pull request or create an issue to discuss the changes you want to make.