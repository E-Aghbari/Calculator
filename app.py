from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    equation = request.form.get('equation')
    postFix = infixToPostfix(equation)
    result = calculatePostfix(postFix)
    return render_template('index.html', result = result)

def calculatePostfix(expression):
    if not expression:
        return None
    
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)
            # elif token == '^':
            #     stack.append(int(stack.pop(-2)) / int(stack.pop(-1)))


    return stack.pop()


def infixToPostfix(expression):
    if not expression:
        return None

    stack = []
    postfix = []
    current_number = ''
    precedence = {'^': 3, '/': 2, '*': 2, '+': 1, '-': 1}
    associativity = {'^': 'R', '/': 'L', '*': 'L', '+': 'L', '-': 'L'}

    for token in expression:
        if token.isdigit(): 
            current_number += token
        elif token == ' ' and current_number: 
            postfix.append(current_number)
            current_number = ''
        elif token in precedence:
            if current_number:
                postfix.append(current_number)
                current_number = ''
            while (stack and stack[-1] != '(' and
                   (precedence[stack[-1]] > precedence[token] or
                    (precedence[stack[-1]] == precedence[token] and associativity[token] == 'L'))):
                postfix.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            if current_number:
                postfix.append(current_number)
                current_number = ''
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()

    if current_number:
        postfix.append(current_number)

    while stack:
        postfix.append(stack.pop())

    return ' '.join(postfix)

if __name__ == '__main__':
    app.run(debug = True)