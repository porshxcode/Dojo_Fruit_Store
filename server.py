from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    fname = request.form["first_name"]
    lname = request.form["last_name"]
    sid = request.form ["student_id"]
    apple = request.form["apple"]
    strawberry = request.form["strawberry"]
    raspberry = request.form["raspberry"]
    total = [int(apple)+int(strawberry)+int(raspberry)]
    print(request.form)
    print (f"Charging,{fname} {lname} for {total} fruits")
    return render_template("checkout.html", fname=fname,lname=lname, sid=sid, apple=int(apple),strawberry=int(strawberry),raspberry=int(raspberry))

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    