import time
from datetime import datetime as dt

#This is using the host file included in the folder, not the actual host file in System32
hosts_path = "UdemyCourse\WebsiteBlocker\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","www.twitter.com","twitter.com"]

while True:

    #Checks if it is within working hours
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours.")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website+"\n")
    else:
        print("Personal time.")
    time.sleep(5)
