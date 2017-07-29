# Maitre'D Transaction Monitor
Monitors TCP Packets sent from Maitre'D Terminals and writes the data to a log file in a folder for each day and terminal

[-] == Removed

[*] == Changed

[+] == Added

# Version 1.4 Changelog:
  The goal of Version 1.4 of 'MTM' was to make it completely configurable. I wanted it be usable on any system configuration so I created
  two new config files. The terminals config, terminals.cfg, allows you to customize logfile names and IP address in which it should receive the data from. The Main
  configuration, 'maitredmon.cfg', allows you to configure the server's IP Address, Port, and the Log Save location. If either config does not exist or are configured 
  improperly the program will throw errors.
[-] Hardcoded configuration

[-] Hardcoded ip addresses

[-] Hardcoded log names

[+] Config for system variables(host IP, host port, and log directory)

[+] Error Messages for no config file

[+] Error Messages for improper config length (Not enough variables or too many, very general but more later)

[+] Config for terminals

[+] Error Messages for no terminal config

[+] Error Messages for no variables in terminal config (If the person doesn't configure terminals right, that's on them)


