import socket
web = input ('𝙞𝙡𝙞𝙖𝙘𝙤𝙙𝙚_𝙙𝙚𝙫 >> Enter url site :')
ip = socket.gethostbyname(web)
print (ip)