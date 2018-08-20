import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(server.system.listMethods())
print(server.system.methodHelp('phone'))
result = server.phone("Bert")  # Bert is evil! go back!  -->Hints from previous problem
print(result)  # 555-ITALY
