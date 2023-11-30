import urllib.request, urllib.parse, urllib.error
import random
requestssent = 0

scamurl = input("Enter URL to website that is scamming, replace the email with ||EMAIL||\n> ")
#scamurl = "https://www.rewardsgiant-au.com/svcg.aspx?SvcTP=3&apikey=6C0E62C4-FB5C-42A5-9D3B-10457F314A81&pID=31&params=email="

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
