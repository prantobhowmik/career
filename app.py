from flask import Flask, render_template, jsonify

app = Flask(__name__)



@app.route("/")
def base():
  return render_template('base.html',
                         pname='Pranto Bhowmik',
                         footer_name='All rights reserved \u00A9 Pranto Bhowmik 2023'
                         )
@app.route("/app/contact.html")
def contact():
  return render_template('contact.html',
                         pname='Pranto Bhowmik',
                         footer_name='All rights reserved \u00A9 Pranto Bhowmik 2023'
                         )
  
if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)