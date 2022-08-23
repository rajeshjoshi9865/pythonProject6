from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
 return 'Hello %s!' % name

if __name__ == '__main__':
 app.run()
@app.route('/emp/<int:emp1>')
def show__emp(emp1):
  return 'EMP ID Number %d' %emp1
if __name__ == '__main__':
 app.run()

