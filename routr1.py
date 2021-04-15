import urllib.request
hostnames=input("enter the url:")
def connect(host=hostnames):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
# test
if connect():
    print("connected")
else:
    print("no internet!")

