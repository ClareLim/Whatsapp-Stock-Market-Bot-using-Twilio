from flask import Flask
from flask import request
from twilio.rest import Client
from marketstack import get_stock_price
import os
# initialise flask application
app = Flask(__name__)

# we need account ID and token in order to initialise client
ACCOUNT_ID = os.environ.get('TWILIO_ACCOUNT')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
client = Client(ACCOUNT_ID, TWILIO_TOKEN)
TWILIO_NUMBER='whatsapp:+14155238886'

# write a function to send msg:
def send_msg(msg, recipient): 
    # print("sendmsg1")
    # print("TWILIO_NUMBER", TWILIO_NUMBER)
    # print("body", msg)
    # print("to", recipient)
    # print("ACCOUNT_ID", ACCOUNT_ID)
    # print("TWILIO_TOKEN", TWILIO_TOKEN)
    message = client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient
    )
    print(message)


# write a function to process msg:
def process_msg(msg): 
    response = ""
    if msg == "hi":
        response = "Hello, welcome to the stock market bot!"
        response += "Type sym:<stock_symbol>:<exchange_symbol> to know the price of the stock in selected market. E.g. sym:CRM:XNYS"
    elif 'sym:' in msg:
        data = msg.split(":")
        stock_symbol = data[1]
        stock_price = get_stock_price(stock_symbol)

        symbol =str(stock_price['symbol'])
        exchange = str(stock_price['exchange'])
        adj_high = str(stock_price['adj_high']) 
        adj_low = str(stock_price['adj_low'])
        adj_close = str(stock_price['adj_close'])
        dividend = str(stock_price['dividend']) 
        date = str(stock_price['date'])

        print(stock_price)

        # last_price = stock_price['last_price']
        # last_price_str = str(last_price)
        response = "The stock price of " + symbol + " at this exchange: " + exchange + " with the adjusted high of: " + adj_high + " with the adjusted low of: " + adj_low + " with the adjusted close of: " + adj_close + " with the dividend of: " + dividend + " as of time-stamp: " + date

        print(response)

    else:
        response = "Please type hi to get started."
    return response

# then we can start setting up routes

# this is the default route, that function will return a simple JSON object
# defining path for that route, and the corresponding handler
# @app.route("/")
# def hello():
#     return{
#         "Result": "You successfully created the first route!"
#     }

@app.route("/webhook", methods=["POST"])
def webhook():
    f = request.form
    msg = f['Body']
    sender = f['From']
    response = process_msg(msg)
    print(response)
    print(sender)
    send_msg(response, sender)
    #importing python debugger and adding it in
    # import pdb
    # pdb.set_trace()
    return "OK", 200

	# DONE - 0. Get Account ID and Token from Twilio and set in env
	# DONE - 1. Import client From Twilio
	# DONE - 2. Initialise client
	# DONE - 3. Write a function to process message
	# 4. Write a function to send message
	# 5. Generate a response
	# 6. Check response in whatsapp
