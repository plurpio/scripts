import urllib.request, urllib.parse, urllib.error
import random
requestssent = 0

scamurl = input("Enter URL to website that is scamming, replace the email with ||EMAIL||\n> ")

while True:
    email = str(random.randrange(1000000000))+"@gmail.com"
    scamurlreq = scamurl.replace("||EMAIL||", email)
    req = urllib.request.Request(
            scamurlreq, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                }
            )

    urllib.request.urlopen(req)
    requestssent = requestssent + 1
    print("\nRequests Sent:", requestssent, "\nEmail:", email)
