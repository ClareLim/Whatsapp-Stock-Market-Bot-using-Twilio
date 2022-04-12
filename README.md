A simple conversational whatsapp chatbot for stock market that allows you to get current stock prices in seconds! This mobile app is suppose to help the end-user get stock prices on the go.

How to get things up and running:
1. Ensure you have the right components pre-installed such as Flask, Twilio Python SDK and Ngrok
2. Ensure you start ngrok by running the following command: "ngrok http 4999"
3. Ensure you load the credentials into your environment again such as: "export TWILIO_ACCOUNT=xxxx" and "export TWILIO_TOKEN=xxxxx". Please obtain this from your Console in your Twilio sandbox environment. Also, load the market stack credentials. Do note to create an account first. Follow this format - "export MARKETSTACK_KEY=xxx". Insert your API Access Key in xxx that can be found in your marketstack dashboard.
4. Run "flask run -p 4999"
5. Connect your Twilio Sandbox for Whatsapp for you to test and prototype messaging via Whatsapp using the Twilio API. You can connect your whatsapp number by sending join <sandbox name>. Information for this can be found in your Twilio Console. Scroll down the left panel > Develop > Messaging > Settings > WhatsApp sandbox settings
6. Under your terminal for ngrok, you should see two lines under "Forwarding", copy the URL which should look something like this: "https://ad32-119-74-120-142.ngrok.io" and include this at the end: "/webhook"
7. According to the instructions in the Salesforce console, you should see something like this: "Ask them to send a WhatsApp message to +1 415 523 8886 with code join outside-tax." Follow that line of instructions as outlined in the Twilio Account page. 
8. At this point, you should receive an automated message that should look like: "You are all set! The sandbox can now send/receive messages from whatsapp:+14155238886. Reply stop to leave the sandbox any time."

User Guide:
When you type "welcome", you should see "Please type hi to get started".

When you type "hi", you should see "Hello, welcome to the stock market bot! Type sym:<stock_symbol> to know the price of the stock."

Afterwards, you can type the stock of choice in and choice of market. For example, "sym:CRM". If the symbol includes the market, please include it. For e.g. sym:IBM.XLON

For more information, please review: https://marketstack.com/search


