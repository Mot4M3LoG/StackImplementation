def isempty(stack):
    if stack[0] is None:
        return True
    else:
        return False


def isfull(stack):
    if stack[19] is None:
        return False
    else:
        return True


def push(stack, x):
    global indexer
    if not isfull(stack):
        stack[indexer] = x
        indexer += 1
    else:
        print("stack is full.")


def pop(stack):
    global indexer
    if not isempty(stack):
        value = stack[indexer-1]
        stack[indexer-1] = None
        indexer -= 1
        return value
    else:
        print("stack is empty.")


def top(stack):
    global indexer
    if not isempty(stack):
        value = stack[indexer - 1]
        return value
    else:
        print("stack is empty.")
        return False


def converter(math_str, stack):
    global indexer
    output = ' '
    for char in math_str:
        if char in {' '}:
            if not output.endswith(' '):
                output = output + ' '
                continue

        elif char.isdigit() or char in {'.'}:
            output = output + str(char)

        elif char in {'+', '-', '/', '*', '('}:
            if char in {'('}:  # highest priority
                push(stack, char)
            elif char in {'+', '-'}:  # second priorities
                stack_top = top(stack)
                if stack_top in {'/', '*'} or isempty(stack):  # if lower
                    # priority in stack, push current to stack
                    push(stack, char)
                else:
                    while True:  # else, while the same priority,
                        # put into output, otherwise push into stack
                        stack_top = top(stack)
                        if stack_top in {'(', ')', '*', '/'} or isempty(stack):
                            push(stack, char)
                            break
                        else:
                            output = output + str(pop(stack))
            else:
                while True:
                    stack_top = top(stack)
                    if stack_top in {'(', ')'} or isempty(stack):
                        push(stack, char)
                        break
                    else:
                        output = output + str(pop(stack))

        elif char in {')'}:
            while True:
                if stack[indexer-1] == '(':
                    pop(stack)
                    break
                else:
                    holder = pop(stack)
                    output = output + str(holder) + ' '

    while not isempty(stack):
        if not output.endswith(' '):
            output = output + ' '
        holder = pop(stack)
        output = output + str(holder)
    print("the expression rewritten looks like " + str(output))
    return output


def calculator(output, stack):
    global indexer
    indexer = 0
    str_holder = ''
    for char in output:
        if char.isdigit() or char in {'.'}:
            str_holder = str_holder + str(char)
        elif char in {' '} and (str_holder != ''):
            push(stack, float(str_holder))
            str_holder = ''
        elif char in {'+'}:
            value_holder = 0
            value_holder = value_holder + float(pop(stack))
            value_holder = value_holder + float(pop(stack))
            push(stack, value_holder)
        elif char in {'-'}:
            value_holder = 0
            value_holder = value_holder - float(pop(stack))
            value_holder = value_holder + float(pop(stack))
            push(stack, value_holder)
        elif char in {'-'}:
            value_holder = 0
            value_holder = value_holder - float(pop(stack))
            value_holder = value_holder + float(pop(stack))
            push(stack, value_holder)
        elif char in {'*'}:
            value_holder = 0
            value_holder = value_holder + float(pop(stack))
            value_holder = value_holder * float(pop(stack))
            push(stack, value_holder)
        if char in {'/'}:
            value_holder2 = float(pop(stack))
            value_holder = (float(pop(stack))) / value_holder2
            push(stack, value_holder)
    print("the value of expression = " + str(pop(stack)))


Stack = [None] * 20
indexer = 0
maths = input("enter your math: ")
out = converter(maths, Stack)
calculator(out, Stack)
