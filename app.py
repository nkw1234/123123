from flask import Flask
app=Flask(__name__)

@app.route('/')
def hi():
    return 'i'

app.run(debug=True)
