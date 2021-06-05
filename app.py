from flask import Flask, render_template, request,redirect
from instamojo_wrapper import Instamojo

API_KEY = "test_8cd4e7c4c8d9da05a118b5e5904"

AUTH_TOKEN = "test_cbbdd7934f2238be7b6d6d7115b"

api = Instamojo(api_key=API_KEY,auth_token=AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
   return render_template('products.html')
@app.route('/payment')
def home1():
   return render_template('index.html')

@app.route('/success')
def success():
    val=request.args.get("payment_id")
    return render_template('success.html',val=val)

@app.route('/pay',methods=['POST','GET'])
def pay():
    if request.method == 'POST':
        name = request.form.get('name')
        purpose = request.form.get('purpose')
        email = request.form.get('email')
        amount = request.form.get('amount')
        phone=request.form.get('number')
        print(name,purpose,email,str(amount),str(phone))
        
        response = api.payment_request_create(
        amount=amount,
        purpose=purpose,
        buyer_name=name,
        send_email=True,
        email=email,
        phone=phone,
        send_sms=True,
        redirect_url="https://sample-payment-gateway-flask.herokuapp.com/success"
        )
        
        return redirect(response['payment_request']['longurl'])
    
    else:
        
        return render_template("index.html")

    
if __name__ == '__main__':
   app.run(debug=True)
