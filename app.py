from flask import Flask, render_template

app = Flask(__name__)

jobs = [
  {
    'id': 1,
    'title': 'Frontend Developer',
    'Location': 'Banglore',
    'Salary': 'Rs 2,00,000'
  },
  {
    'id': 2,
    'title': 'Backend Developer',
    'Location': 'Pune',
    'Salary': 'Rs 1,50,000'
  },
  {
    'id': 3,
    'title': 'Software Engineer',
    'Location': 'Vancouver',
    'Salary': 'CAD 20,000'
  },
  {
    'id': 4,
    'title': 'HR',
    'Location': 'Kolkata',
    'Salary': ''
  }
  
]

@app.route("/")
def bsae():
  return render_template('base.html', 
                         job=jobs, 
                         company_name= 'dope')

if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)