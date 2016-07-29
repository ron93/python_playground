
import json

user_input = raw_input("give me a number")
data= open("MOCK_DATA.json","r")

def check():
    if isinstance(int(user_input), int):
        with data as info:
            temp = json.load(info)
        for i in temp:
            if i.get("id") == int(user_input):
                print i.get("first_name") + "\n" + i.get("last_name")+ "\n" + i.get("email") + "\n" + i.get("gender")
    else:
        print "incorrect input"
check()

m_count = 0
f_count = 0
