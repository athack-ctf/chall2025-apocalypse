from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('page1')  # Form page where the user submits data

@app.route('/page1')
def page1():
    response = make_response(render_template('page1.html'))
    response.set_cookie('is_human', expires=0)
    response.set_cookie('is_chocolatechip', expires=0)
    response.set_cookie('love_cookie_so_much', expires=0)
    response.set_cookie('is_smart', expires=0)
    return response
    #return render_template('page1.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve the form data for each digit
    code = request.form.get('token')
   

 
    if code == '1081': 
      return render_template('flag.html', code=code)  # Send the code to the result page
    else:
      return render_template('emp.html', message='Incorrect Passcode, try again!' )
    
@app.route('/page2')
def cookie():
    if request.cookies.get('is_human') == 'true':
       return redirect('/human')
    

    
    response = make_response(render_template('page2.html'))
    response.set_cookie('is_human', 'false')
    response.set_cookie('is_chocolatechip', 'false')
    response.set_cookie('love_cookie_so_much', 'https://youtu.be/CgYSRaiGDnI?si=5UkC_Sg7A0k3tgn1')
    response.set_cookie('is_smart', '1')
    return response


@app.route('/human')
def ishuman():
     return render_template('human.html')


@app.route('/human_submit', methods=['POST'])
def human():

    if request.form.get('password')== 'APOCALYPSE2040':
        return render_template('files.html')

    else:
        return render_template('human.html', message='Wrong Password, try again!')

@app.route('/emp')
def emp():
    return render_template('emp.html')
@app.route('/emergencyfood')
def emergencyfood():
    return render_template('emergencyfood.html')

@app.route('/firstaid')
def firstaid():
    return render_template('firstaid.html')

if __name__ == '__main__':
    app.run(debug=True)
