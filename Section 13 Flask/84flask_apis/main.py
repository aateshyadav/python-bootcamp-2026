from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def json():
    marks={
    "harry":56,
    "rohan":67,
    "aakash":78,
    "shubham":100,
    "reena":67
    }
    values=[1, marks, 67]
    return jsonify(marks)

app.run(debug=True)