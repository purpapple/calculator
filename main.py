from flask import Flask, render_template
import os

print("Welcome to Max's Calculator!")
opts = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Division"]
print("\n".join(opts))

opt = input("Enter the number of the operation you want to use: ")

if opt in ["1", "2", "3", "4"]:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if opt == "1":
        print(f"Result: {num1 + num2}")
    elif opt == "2":
        print(f"Result: {num1 - num2}")
    elif opt == "3":
        print(f"Result: {num1 * num2}")
    elif opt == "4":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")

elif opt == "DINO!":
    print("Launching web app in Replit webview...")

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    app.run(host="0.0.0.0", port=8080, debug=False)

elif opt == "MONKEY!":
    print("Launching...")

    monk = Flask(__name__, template_folder='MGG2')

    @monk.route('/')
    def index():
        return render_template('index.html')

    monk.run(host="0.0.0.0", port=8080, debug=False)

elif opt == "SUBSURF!":
    print("Launching...")
    sub = Flask(__name__, template_folder='SUBSURF')
    @sub.route('/')
    def index():
        return render_template('index.html')

    sub.run(host="0.0.0.0", port=8080, debug=False)
    
elif opt == "quit":
    print("ok")

elif opt == "GOOGLE!":
    print("Launching...")
    google = Flask(__name__, template_folder='GOOGLE')
    @google.route('/')
    def index():
        return render_template('index.html')
    
    google.run(host='0.0.0.0', port=8000, debug=False)

elif opt == "EVILMONKEY!":
    print("Launching...")
    evilmonk = Flask(__name__, template_folder='EVILMONKEY')
    @evilmonk.route('/')
    def index():
        return render_template('index.html')
    
    evilmonk.run(host='0.0.0.0', port=8000, debug=False)

elif opt == "VEX6":
    print("Launching...")
    vex6 = Flask(__name__, template_folder='VEX6')
    @vex6.route('/')
    def index():
        return render_template('index.html')
    
    vex6.run(host="0.0.0.0", port=8000, debug=False)

elif opt == "POKI!":
    print("Launching...")
    poki = Flask(__name__, template_folder='POKI')
    @poki.route('/')
    def index():
        return render_template('index.html')
    
    poki.run(host="0.0.0.0", port=8000, debug=False)