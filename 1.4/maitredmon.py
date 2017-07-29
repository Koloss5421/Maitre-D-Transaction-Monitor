# Created By: John "Koloss" Hardin
# Version 1.4

import socket, sys, os, datetime, time
import thread

config = {}
terminals = {}

def findConfig():  # Find the config file and fill in host, port and log directory
    configFile = "maitredmon.cfg"  # The hardcoded cfg file name.
    if os.path.isfile(configFile):  # Check if the config exists
        file = open(configFile, 'r')  # open the config as 'file'
        for line in file:  # iterate over each line in the file
            if '#' not in line: # check if the line is a comment
                global config  # pull in the config dictionary as global to edit
                a = line.strip('\n')  # remove the newline from the end as 'a'
                b = a.split('=')  # Split the 2 values from the stripped 'a' var
                if b[0] == 'port':  # if the current line is the port variable
                    config[b[0]] = int(b[1])  # Convert the variable value to an int
                else:
                    config[b[0]] = str(b[1])  # just to be sure, everything else needs to be a string
                if b[0] == 'logdir':  # check if the logdir folder exists
                    if not os.path.isdir(b[1]):
                        exit("[!] The log directory '" + b[1] + "' does NOT exist!\n"  
                             "[!] To Solve create directory '" + b[1] + "' or\n" # if the log does folder not exist Exit
                             "[!] change the logdir location in 'maitredmon.cfg'\n")
    else:  # if the config does not exist, Exit with error.
        exit("[!] Config file 'maitredmon.cfg' does NOT exist!\n"
             "[!] Please create one based off the github template.\n"
             "[*] https://github.com/Koloss5421/Maitre-D-Transaction-Monitor/templates")
    if not len(config) == 3:
        exit("[!] Config file does not contain all variables or has too many!\n"
             "[!] Please edit based off the github template.\n"
             "[*] https://github.com/Koloss5421/Maitre-D-Transaction-Monitor/templates")

def loadTerminals():
    terminalCfg = 'terminals.cfg'  # Hardcoded terminal config
    if os.path.isfile(terminalCfg):  # check if terminals config exists
        file = open(terminalCfg, 'r')  # open the config as file
        for line in file:  # iterate over each line in the config
            if '#' not in line:  # check if the line is a comment
                global terminals
                a = line.strip('\n')  # remove the newline from the end as 'a'
                b = a.split(',')  # split the key and variables at the ','
                terminals[b[0]] = b[1]  # use the terminal name as the key and the address as the value of that key
    else:
        exit("[!] The terminals config file '" + terminalCfg + "' does NOT exist!\n"
             "[!] Please create one based off the github template.\n"
             "[*] https://github.com/Koloss5421/Maitre-D-Transaction-Monitor/templates")
    if not len(terminals) > 0:
        exit("[!] There are NO terminals listed in terminal config!\n"
             "[!] Please edit based off the github template.\n"
             "[*] https://github.com/Koloss5421/Maitre-D-Transaction-Monitor/templates")

findConfig()
loadTerminals()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print('[*] Attempting to Bind: ' + config['host'] + ":" + str(config['port']))
    s.bind((config['host'], config['port']))
except socket.error as e:
    print(str(e))

print('[*] Listening...')
s.listen(5)


def threaded_client(conn, addr):
    while True:
        data = conn.recv(1048)
        if not data:  # if the is no data break the connection
            break

        ts = time.time()  # get current computer time
        # current_dir = The log directory from the cfg + the current year,month,day(Ex. 20170729|07/29/2017) as folder
        current_dir = config['logdir'] + str(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')) + "/"
        if not os.path.isdir(current_dir):  # if the current date folder does not exist
            os.mkdir(current_dir)  # create it

        for key, value in terminals.iteritems():  # iterate over the terminals array to find IP
            if addr == value:  # if an IP is found and it is the connection address, log it
                st = datetime.datetime.fromtimestamp(ts).strftime('[%Y-%m-%d %H:%M:%S]')  # create timestamp from ts
                file = open(current_dir + key + '.log', "a")  # logfile name = pos name from terminals config + .log
                a = data.replace('--End--', '')
                b = a.replace('--Begin--', '')
                c = b.replace('showtext,01,', '')
                if '--Begin--' in data:
                    file.write(str(st) + "\t##################################################\n")
                file.write(c + '\n')
                file.close()
        print(data)
    conn.close()


while True:
    conn, addr = s.accept()
    print('[+] Connected to: ' + addr[0] + ":" + str(addr[1]))

    thread.start_new_thread(threaded_client, (conn, addr[0]))
