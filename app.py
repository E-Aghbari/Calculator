from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    number = request.form.get('number')
    postfix = infixToPostfix('2 / 2')
    print(postfix)
    print(calculate(postfix))
    
    return render_template('index.html', number=number)

def calculate(expression):
    stack = []

    for token in expression:
        if '0' <= token <= '9':
            stack.append(token)
        else:
            if token == '+':
                stack.append(float(stack.pop(-2)) + float(stack.pop(-1)))
            elif token == '-':
                stack.append(float(stack.pop(-2)) - float(stack.pop(-1)))
            elif token == '*':
                stack.append(float(stack.pop(-2)) * float(stack.pop(-1)))
            elif token == '/':
                stack.append(float(stack.pop(-2)) / float(stack.pop(-1)))
            # elif token == '^':
            #     stack.append(int(stack.pop(-2)) / int(stack.pop(-1)))


    return stack[0]


def infixToPostfix(infixEx):
    stack = []
    postFix = []

    precedence = {'^': 3, '/': 2, '*': 2, '+': 1, '-': 1}

    for token in infixEx:
        if  '0' <= token <= '9':
            postFix.append(token)
        
        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                postFix.append(stack.pop())
            stack.pop()
        
        elif token == ' ':
            continue

        else:
            while (stack and stack[-1] != '(' and (precedence[token] < precedence[stack[-1]] or (precedence[token] == precedence[stack[-1]] and associativity(token) == 'L'))):
                postFix.append(stack.pop())
            stack.append(token)
    
    while stack:
        postFix.append(stack.pop())

    return (''.join(postFix))

def associativity(operator):
    if operator == '^':
        return 'R'
    return 'L'

if __name__ == '__main__':
    app.run(debug = True)