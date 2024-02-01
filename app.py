from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello MSOE'


random_number = random.randint(1,10)
@app.route('/enhanced-app', methods=['GET', 'POST'])
def enhanced():
    global random_number
    
    if request.method == 'POST':
        user_guess = int(request.form.get('guess', 0))
        
        if user_guess == random_number:
            message = "Correct!"
            random_number = random.randint(1,10)
            return render_template_string("""
                <h1>{{message}}</h1>
                <a href="/enhanced-app">Play again</a>
            """, message=message, random_number=random_number)
        else:
            message = "Incorrect, try again!"
            old_number = random_number
            random_number = random.randint(1,10)
            return render_template_string("""
                <h1>{{message}}</h1>
                <p>The number was {{random_number}}</p>
                <a href="/enhanced-app">Try again</a>
            """, message=message,random_number=old_number)
    
    # Render a simple form for GET request
    return f'''
        <form method="post">
            Guess the number (1 to 10): <input type="number" name="guess">
            <input type="submit" value="Submit">
        </form>
    '''