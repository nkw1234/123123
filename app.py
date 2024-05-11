from flask import Flask')

@app.route(/)
def hi():
    return ('i')

app.run(debug=True)
