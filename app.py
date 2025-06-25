from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def form():
    if request.method == "POST":
        try:
            maths = float(request.form.get('maths', 0))
            physics = float(request.form.get('physics', 0))
            chemistry = float(request.form.get('chemistry', 0))

            average_marks = (maths + physics + chemistry) / 3

            if average_marks >= 40:
                result = "Pass"
            else:
                result = "Fail"

            return render_template('form.html', score=average_marks, result=result)

        except ValueError:
            return render_template('form.html', error="Please enter valid numbers.")
    
    return render_template('form.html')

@app.route('/api', methods=["POST"])
def api():
    if request.is_json:
        data = request.get_json()
        a = float(data.get('a', 0))
        b = float(data.get('b', 0))
        return {"result": a + b}
    return {"error": "Invalid JSON"}, 400

#if __name__ == "__main__":
    #app.run(debug=True)
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # default to 5000 locally
    app.run(host="0.0.0.0", port=port)

