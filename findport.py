import socket
import sys

host = sys.argv[1]
skeletonkey = sys.argv[2]
username = sys.argv[3]


def portfinder (host, skeletonkey, username):
    with open('portNums') as fp:
        for line in fp:
            port = int(line)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2.0)
            s.connect((host, port))
            try:
                s.send(skeletonkey)
                data = s.recv(1024)
                # print(data)
                s.send(username)
                passinfo = s.recv(1024)
                if "Password" in passinfo:
                    # print(passinfo)
                    # print(line)
                    return port
                s.close()
            except socket.timeout:
                continue


foundPort = portfinder(host, skeletonkey, username)
print(foundPort)
