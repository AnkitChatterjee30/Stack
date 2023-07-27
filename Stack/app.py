from flask import Flask, request, render_template

stack=[]
value = len(stack)
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/push',methods=['POST','GET'])
def stack_push():
    item = int(request.form['pusheditem'])
    if len(stack)<6:
        stack.append(item)
    elif len(stack)==6:
        return render_template("index.html",item=item, stack=stack, length=range(len(stack)-1,-1,-1), value=False, alpi=False, size=len(stack))
    
    return render_template("index.html",item=item, stack=stack, length=range(len(stack)-1,-1,-1), value=True, alpi=True, size=len(stack))

@app.route('/pop',methods=['POST','GET'])
def stack_pop():
    if len(stack)>0:
        stack.pop()
    else:
        return render_template("index.html",stack=stack, length=range(len(stack)-1,-1,-1), value=True, arpi=False, size=len(stack))
        
    return render_template("index.html",stack=stack, length=range(len(stack)-1,-1,-1), value=True, arpi=True, size=len(stack))


if __name__=='__main__':
    app.run(debug=True)