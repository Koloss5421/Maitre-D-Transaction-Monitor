import socket, sys, os, datetime, time
import thread

host = '192.168.100.114'
port = 5555
working_dir = 'F:/POSData/'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print('[*] Attempting to Bind: ' + host + ":" + str(port))
    s.bind((host, port))
except socket.error as e:
    print(str(e))

print('[*] Listening...')
s.listen(5)


def threaded_client(conn, addr):
    while True:
        data = conn.recv(1048)
        if not data:
            break

        ts = time.time()
        current_dir = working_dir + str(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')) + "/"
        if not os.path.isdir(current_dir):
            os.mkdir(current_dir)
        if addr == '192.168.100.101':
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file = open(current_dir + 'pos1.log', "a")
            if '--Begin--' in data:
                file.write(str(st) + "\t\t #############################################\n")
            data.replace('--End--', '')
            data.replace('--Begin--`', '')
            data.replace('showtext,01,', '')
            file.write(data + "\n")
        if addr == '192.168.100.102':
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file = open(current_dir + 'pos2.log', "a")
            if '--Begin--' in data:
                file.write(str(st) + "\t\t #############################################\n")
            data.replace('--End--', '')
            data.replace('--Begin--`', '')
            data.replace('showtext,01,', '')
            file.write(data + "\n")
        if addr == '192.168.100.103':
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file = open(current_dir + 'pos3.log', "a")
            if '--Begin--' in data:
                file.write(str(st) + "\t\t #############################################\n")
            data.replace('--End--', '')
            data.replace('--Begin--`', '')
            data.replace('showtext,01,', '')
            file.write(data + "\n")
        if addr == '192.168.100.104':
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file = open(current_dir + 'pos4.log', "a")
            if '--Begin--' in data:
                file.write(str(st) + "\t\t #############################################\n")
            data.replace('--End--', '')
            data.replace('--Begin--`', '')
            data.replace('showtext,01,', '')
            file.write(data + "\n")

        if addr == '192.168.100.105':
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file = open(current_dir + 'pos5.log', "a")
            if '--Begin--' in data:
                file.write(str(st) + "\t\t #############################################\n")
            data.replace('--End--', '')
            data.replace('--Begin--`', '')
            data.replace('showtext,01,', '')
            file.write(data + "\n")
        if addr == '192.168.100.106':
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file = open(current_dir + 'pos6.log', "a")
            if '--Begin--' in data:
                file.write(str(st) + "\t\t #############################################\n")
            data.replace('--End--', '')
            data.replace('--Begin--`', '')
            data.replace('showtext,01,', '')
            file.write(data + "\n")
        if addr == '192.168.100.107':
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file = open(current_dir + 'pos7.log', "a")
            if '--Begin--' in data:
                file.write(str(st) + "\t\t #############################################\n")
            data.replace('--End--', '')
            data.replace('--Begin--`', '')
            data.replace('showtext,01,', '')
            file.write(data + "\n")
        if addr == '192.168.100.108':
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file = open(current_dir + 'pos8.log', "a")
            if '--Begin--' in data:
                file.write(str(st) + "\t\t #############################################\n")
            data.replace('--End--', '')
            data.replace('--Begin--`', '')
            data.replace('showtext,01,', '')
            file.write(data + "\n")
        if addr == '192.168.100.109':
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file = open(current_dir + 'pos9.log', "a")
            if '--Begin--' in data:
                file.write(str(st) + "\t\t #############################################\n")
            data.replace('--End--', '')
            data.replace('--Begin--`', '')
            data.replace('showtext,01,', '')
            file.write(data + "\n")
        if addr == '192.168.100.110':
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file = open(current_dir + 'pos10.log', "a")
            if '--Begin--' in data:
                file.write(str(st) + "\t\t #############################################\n")
            data.replace('--End--', '')
            data.replace('--Begin--`', '')
            data.replace('showtext,01,', '')
            file.write(data + "\n")
        if addr == '192.168.100.111':
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file = open(current_dir + 'pos11.log', "a")
            if '--Begin--' in data:
                file.write(str(st) + "\t\t #############################################\n")
            data.replace('--End--', '')
            data.replace('--Begin--`', '')
            data.replace('showtext,01,', '')
            file.write(data + "\n")
        if addr == '192.168.100.112':
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file = open(current_dir + 'pos12.log', "a")
            if '--Begin--' in data:
                file.write(str(st) + "\t\t #############################################\n")
            data.replace('--End--', '')
            data.replace('--Begin--`', '')
            data.replace('showtext,01,', '')
            file.write(data + "\n")
        if addr == '192.168.100.113':
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            file = open(current_dir + 'pos13.log', "a")
            if '--Begin--' in data:
                file.write(str(st) + "\t\t #############################################\n")
            data.replace('--End--', '')
            data.replace('--Begin--`', '')
            data.replace('showtext,01,', '')
            file.write(data + "\n")

        print(data)
    conn.close()


while True:
    conn, addr = s.accept()
    print('[+] Connected to: ' + addr[0] + ":" + str(addr[1]))

    thread.start_new_thread(threaded_client, (conn, addr[0]))
