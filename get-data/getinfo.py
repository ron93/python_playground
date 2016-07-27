data = raw_input("Enter your id" "\n")
file = open("MOCK_DATA.json" + "r+")
if data in file.readline():