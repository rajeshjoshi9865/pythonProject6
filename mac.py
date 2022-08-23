from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route('/')
def home():
   return 'WELCOME TO KL UNIVERSITY'
@app.route('/cse')
def cseDept():
   return 'Dept of CSE '
@app.route('/ai')
def aiDept():
   return 'Dept of AI '
@app.route('/ds')
def dsDept():
   return 'Dept of Data Science '
@app.route('/csit')
def csit():
   return 'Dept of csit'
@app.route('/dept/<name>')
def dept(name):
   if name == 'cse':
      return redirect(url_for('cseDept'))
   elif name == 'ai':
      return redirect(url_for('aiDept'))
   elif name== 'csit':
      return redirector(url_for('csitDept'))
   else:
      return redirect(url_for('dsDept'))
if __name__ == "__main__":
   app.run(debug = True)