from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    number = request.form.get('number')
    postfix = infixToPostfix('(3+45)*2 /(1 - 5)')
    print(postfix)
    print(calculatePostfix(postfix))
    
    return render_template('index.html', number=number)

def calculatePostfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.append(float(token))
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