import time, requests

def executeSomething():
    r = requests.get('http://162.243.167.109/checkStatus')
    time.sleep(3600)

while True:
    executeSomething()
