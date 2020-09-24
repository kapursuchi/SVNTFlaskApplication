# Name: Suchi Kapur
# SVNT Interview
# Date: September 24, 2020
# Interview Date: September 25, 2020


# Importing flask to create flask app & sympy for isprime() function
from flask import *
from sympy import *

# Setting up flask app
app = Flask(__name__)

# Defining root page. This page uses the index.html file, which lists the purpose of this flask app
# and instructions for usage. The index.html file is located under the /templates directory
@app.route("/")
def root():
    return render_template('index.html')

# First requirement: This function displays the range from 1 to the specified number.
# The return value renders the list.html template which uses the numlist to display the range
@app.route("/<int:number>", methods=['GET', 'POST'])
def display_int(number):
    title = "Displaying Numbers Between 1 and " + str(number)
    numlist = []
    for i in range(1, number + 1):
        numlist.append(i)
    return render_template('list.html', len=len(numlist), numlist=numlist, title=title)

# Second requirement: This function displays odd numbers from 1 to the specified number.
# The return value renders the list.html template which uses the numlist to display the range
@app.route("/<int:number>/odd", methods=['GET', 'POST'])
def display_odd(number):
    title = "Displaying Odd Numbers Between 1 and " + str(number)
    numlist = []
    for i in range(1, number + 1):
        if i % 2 != 0:
            numlist.append(i)
    return render_template('list.html', len=len(numlist), numlist=numlist, title=title)

# Third requirement: This function displays odd numbers from 1 to the specified number.
# The return value renders the list.html template which uses the numlist to display the range
@app.route("/<int:number>/even", methods=['GET', 'POST'])
def display_even(number):
    title = "Displaying Even Numbers Between 1 and " + str(number)
    numlist = []
    for i in range(1, number + 1):
        if i % 2 == 0:
            numlist.append(i)
    return render_template('list.html', len=len(numlist), numlist=numlist, title=title)

# Fourth requirement: This function displays prime numbers from 1 to the specified number.
# The return value renders the list.html template which uses the numlist to display the range
# This function uses the sympy function isprime() to check whether or not the number is prime.
@app.route("/<int:number>/prime", methods=['GET', 'POST'])
def display_prime(number):
    title = "Displaying Prime Numbers Between 1 and " + str(number)
    numlist = []
    for i in range(1, number + 1):
        if isprime(i):
            numlist.append(i)
    return render_template('list.html', len=len(numlist), numlist=numlist, title=title)


# Run the flask app!
if __name__ == "__main__":
    app.run()
