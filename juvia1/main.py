from flask import Flask
app = Flask(__name__)

from urllib2 import urlopen
from bs4 import BeautifulSoup
from twilio.rest import TwilioRestClient

account_sid = "" 
auth_token  = ""  

client = TwilioRestClient(account_sid, auth_token)

@app.route('/checkStatus')
def checkStatus():
	url = 'http://www.juviasplace.com/product-p/jmb001.htm'
	html = urlopen(url)
	soup = BeautifulSoup(html)
	answer = 'Stock Status:(Out of Stock)'

	stock = soup.find_all("div", {"itemprop":"offers"})
	content = ''.join(str(t) for t in stock)

	if answer in content:
		print "out of stock"
	else:
		message = client.messages.create(body="The Juvia's July Beauty Box is currently in stock. Get it now while it lasts.",
	    to="+1",    
	    from_="+1")

	return 'Nothing to see here.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

