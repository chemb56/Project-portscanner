#!/usr/bin/python

#import nmap module
import nmap
#variable called scanner

scanner = nmap.PortScanner()
#prompt a welcome banner to the user
print("Welcome,this is a simple nmap automation tool")

# A divider
print("<--------------------------------------------")
#Prompt the user to enter an ip address
ip_addr = input("Please enter the Ip address you want to scan:")
#Display what the user entered
print("The ip address you entered is:",ip_addr)
#sanitize the input
type(ip_addr)
#A variable to ask the user to select the type of nmap scan they want
resp = input("""\n Please enter the type of scan
                1)SYN ACK SCAN
                2)UDP SCAN
                3)COMPREHENSIVE SCAN\n""")
#Confirm the user's selection
print("You've selected:",resp)
#conditional statements to run the scan according to the option selected
#1.TCP SCAN
if resp=='1':
    print("Nmap version:",scanner.nmap_version())
    #scanning
    scanner.scan(ip_addr,'1-1024','-v -sS')
    #Display scan information
    print(scanner.scaninfo())
    #Display if ip address is active
    print("ip status:",scanner[ip_addr].state())
    #Display conection type
    print(scanner[ip-addr].all_protocols())
    #Display open ports
    print("open ports:", scanner[ip_addr] ['tcp'].keys())
#2.UDP SCAN
elif resp=='2':
        print("Nmap version:", scanner.nmap_version())
        #scanning
        scanner.scan(ip_addr, '1-1024', '-v -sV')
        #Display scan info
        print(scanner.scaninfo())
        #Display if ip address is active
        print("ip status:", scanner[ip_addr].state())
        #Display connection type
        print(scanner[ip_addr].all_protocols)
        #Display open ports
        print("open ports:", scanner[ip_addr]['udp'].keys())
#3.COMPREHENSIVE SCAN
elif resp=='3':
    print("Nmap version:", scanner.nmap_version())
                    #scanning
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
                    #Display scan info
    print(scanner.scaninfo())
                    #Display if ip address is active
    print("ip status:", scanner[ip_addr].state())
                    #Display connection type
    print(scanner[ip_addr].all_protocols)
                    #Display open ports
    print("open ports:", scanner[ip_addr]['tcp'].keys())
#4.INVALID OPTIONS
elif resp>='4':
    print("Please enter a valid option")
