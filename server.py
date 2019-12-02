from flask import Flask,render_template,url_for,request,redirect
import csv
app = Flask(__name__)

print(__name__)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<string:page>")
def a(page):
    return render_template(page)

def wrtf(data):
    with open('data.txt',mode='a') as database:

        msg=data['msg']
        file=database.write(msg)


def wrcsv(data):
     with open('data.csv', mode='a') as database2:

         subject = data['subject']
         email=data['email']
         msg=data['msg']
         csv_wr=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
         csv_wr.writerow([email,subject,msg])



@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method=="POST":
        try:
            data=request.form.to_dict()

            wrtf(data)
            wrcsv(data)
            return redirect('/components.html')
        except:
            return "xxxxxxxxxx"
    else:
        "bad"

if __name__== '__main__':
    app.run(debug=True)
