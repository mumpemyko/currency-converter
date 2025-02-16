from flask import Flask,jsonify,request

app = Flask(__name__)

#create a list of rates
rates = {"EUR":0.85, "UGX":3600, "KES":109.5}

#create a route 
@app.route('/convert' , methods=['POST'])

#create a function that converts from usd to other rates

def currency_converter():
    try:
        
        data = request.get_json()
        amount = data.get("amount")
        currency = data.get("currency")
        
        
        # Validate amount type
        if not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({"error": "Amount must be a positive number"}), 400
        
        #verify currency
        if currency not in rates:
            return jsonify({"error":"Currency not supported"}), 400
        
        converted = amount * rates[currency]
        
        
        return jsonify({"converted_amount": converted   })
    except Exception as err:
         return jsonify({"error": f"Server error: {str(err)}"}), 500
    
#Create and endpoint for reading the avaible currrencies

@app.route('/currencies', methods=['GET'])
def get_currencies():
        return jsonify (list (rates.keys()))
    
if __name__ == "__main__":
   app.run(debug=True)