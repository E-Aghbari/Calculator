from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        equation = request.form.get('equation')
        if equation: 
            postFix = infixToPostfix(equation)
            result = calculatePostfix(postFix)
            return str(result) 
        else:
            return "No equation provided", 400
    else:
        return render_template('index.html')  

def calculatePostfix(expression):
    if not expression:
        return None
    
    stack = []
    tokens = expression.split()
    for token in tokens:
        if token.isdigit() or '.' in token:
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

    result = stack.pop()
    if result.is_integer():
        return int(result)
    else:
        return result


def infixToPostfix(expression):
    if not expression:
        return None

    stack = []
    postfix = []
    current_number = ''
    precedence = {'^': 3, '/': 2, '*': 2, '+': 1, '-': 1}
    associativity = {'^': 'R', '/': 'L', '*': 'L', '+': 'L', '-': 'L'}

    for token in expression:
        if token.isdigit() or token == '.': 
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