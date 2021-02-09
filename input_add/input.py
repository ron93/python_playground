user_name = raw_input("hi,what/'s your name" "\n")
file = open("data.txt", "r+")
if user_name not in file.readline():
    file.write(user_name +"\n")
    file.close()
    print "success " + user_name  + " entered"
else:
    print "ERROR " + user_name +" already in file"
    file.close()

