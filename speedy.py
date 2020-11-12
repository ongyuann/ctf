import socket
import codecs

def netcat(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    
    #welcome message
    data = s.recv(1024)
    print ("Received:",repr(data))
    
    #reply 'ok'
    content = 'ok'
    payload = str.encode(content)
    s.sendall(payload)
    
    #receive first question
    data = s.recv(1024)
    print ("Received:",repr(data))
    data = s.recv(1024)
    print ("Received:",repr(data))
    
    #reply first answer
    answer = answerer(data.decode('utf-8'))
    payload = str.encode(answer)
    s.sendall(payload)

    #receive second question
    data = s.recv(1024)
    print ("Received:",repr(data))
    data = s.recv(1024)
    print ("Received:",repr(data))

    #reply second question
    data = data.decode('utf-8')
    data = data.split(' ')
    data = data[4:]
    data = " ".join(str(x) for x in data)
    answer = answerer(data)
    payload = str.encode(answer)
    s.sendall(payload)

    #receive third question
    data = s.recv(1024)
    print ("Received:",repr(data))
    data = s.recv(1024)
    print ("Received:",repr(data))

    #reply third question
    data = data.decode('utf-8')
    data = data.split(' ')
    data = data[4:]
    data = " ".join(str(x) for x in data)
    answer = answerer(data)
    payload = str.encode(answer)
    s.sendall(payload)
    
    #receive flag
    data = s.recv(1024)
    print ("Received:",repr(data))
    data = s.recv(1024)
    print ("Received:",repr(data))

    #shut connection
    s.shutdown(socket.SHUT_WR)
    print ("Connection closed.")
    s.close()


def answerer(question):
    answer = ''
    question = question.replace(".","")
    question = question.replace("?","")
    question = question.replace("\n","")
    print ('[+] question:' + question)
    #analyze question
    if "Shifted by 13" in question:
        value = question.split(' ')[8]
        answer = codecs.encode(value,'rot_13')
    if "Can you add" in question:
        value1 = question.split(' ')[4]
        value2 = question.split(' ')[6]
        answer = int(value1) + int(value2)
        answer = str(answer)
    if "Multiply" in question:
        value1 = question.split(' ')[2]
        value2 = question.split(' ')[4]
        answer = int(value1) * int(value2)
        answer = str(answer)
    if "Biggest port number" in question:
        answer = '65535'
    if "DNS zone transfer" in question:
        answer = 'TCP'
    if "Divide" in question:
        value1 = question.split(' ')[2]
        value2 = question.split(' ')[4]
        answer = int(value1) / int(value2)
        answer = int(round(answer))
        answer = str(answer)
    if "Given" in question:
        value1 = question.split(' ')[2]
        value2 = question.split(' ')[4]
        answer = int(value1) - int(value2) + 2
        answer = str(answer)
    if "I am not sure" in question:
        answer = "teletype"
    if "Reverse" in question:
        value = question.split(' ')[3]
        answer = value[::-1]

    #output answer
    print ('[+] answer: ' + answer)
    return answer

cheat_sheet = {
        "Shifted by 13" : "rot13"
        }

netcat('18.234.76.35',22226)
