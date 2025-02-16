#currency converter API #
This flask app allows the user to covert USD to other given currencies
#installation steps #
Clone this repository 
#features #
Takes in the amount of USD and the desired currency to convert to and out puts the converted amount.
#requirements#
Python 3.x
#API endpoint#
@app.route('/convert', methods=['POST'])
@app.route('/currencies', methods=['GET'])

#Example request & response

Posting data on the client side (curl)
Results to this.

$ curl -X POST http://127.0.0.1:5000/convert -H "Content-Type: application/json" -d '{"amount": 100, "currency": "UGX"}'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    67  100    33  100    34  12186  12555 --:--:-- --:--:-- --:--:-- 33500{
  "converted_amount": 360000
}
