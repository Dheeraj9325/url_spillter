url = input("Enter url : ")
protocol = url.split("://")[0]
domain = url.split("/")[2]
page = url.split("/")[3]
print("Protocol : ", protocol)
print("Domain : ", domain)
print("Page : ",page)