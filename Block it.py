import time
from datetime import datetime as dt
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["https://www.youtube.com/", "youtube.com", "www.youtube.com"]
#hosts_temp = "hosts"



while True:
    time_start = dt(dt.now().year, dt.now().month, dt.now().day, 7)
    time_end = dt(dt.now().year, dt.now().month, dt.now().day, 15)

    if dt.now() > time_start and dt.now() < time_end:
        print("Working hours....")

        with open(hosts_path, "r+") as myfile:
            content = myfile.read()

            for website in website_list:
                if website in content:
                    pass
                else:
                    myfile.write(redirect+" "+website+"\n")

    else:
        print("fun hours....")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0) # To get the pointer back on top

            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() # deletes everything below that line


    time.sleep(5) #so the program doesn't have to keep checking every millisecond

#To access using cmd:
#Run cmd as admin
#cd C:\users\malhaar\desktop\websiteblocker
#python "Block it.py"
