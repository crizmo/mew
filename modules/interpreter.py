from modules.opcodes import Opcodes
from modules.stack import Stack


def interpret(program: list, label_tracker: dict) -> None:
    pc = 0
    stack = Stack(256)

    while pc < len(program):
        opcode = program[pc]
        pc += 1

        # print(f"Executing opcode: {opcode}")

        if opcode == Opcodes.HALT:
            break

        if opcode == Opcodes.PUSH:
            number = program[pc]
            pc += 1
            stack.push(number)
        elif opcode == Opcodes.POP:
            stack.pop()
        elif opcode == Opcodes.ADD:
            a = stack.pop()
            b = stack.pop()
            stack.push(a + b)
        elif opcode == Opcodes.SUB:
            a = stack.pop()
            b = stack.pop()
            stack.push(b - a)
        elif opcode == Opcodes.PRINT:
            string_literal = program[pc]
            pc += 1
            print(string_literal)
        elif opcode == Opcodes.SHOW:
            if not stack.is_empty():
                value = stack.top()  # Peek the top value without removing it from the stack
                print("hi", value)
            else:
                print("Stack is empty")
        elif opcode == Opcodes.READ:
            number = int(input())
            stack.push(number)
        elif opcode == Opcodes.JUMP_EQ_0:
            number = stack.top()
            if number == 0:
                pc = label_tracker[program[pc]]
            else:
                pc += 1
        elif opcode == Opcodes.JUMP_GT_0:
            number = stack.top()
            if number > 0:
                pc = label_tracker[program[pc]]
            else:
                pc += 1
        else:
            print("Unexpected opcode received")
            exit(1)

        # print(f"Stack: {stack.buf}")
