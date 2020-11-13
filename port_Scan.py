import socket
import re
import json
import requests 
import os
import subprocess

def scanner(IPs=[]):
        #Scans from a list of IP and ports if it finds an open port it
        #sends the port to servic_version to get version of the running service
        
        IPs = ["10.0.0.127"]
        ports = [1,20,21,22,23,80,443]
        t = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        for ip in IPs: 
              for p in ports:
                result = t.connect_ex((ip,p)) 
                if result == 0:
                        service = socket.getservbyport(p, 'tcp')
                        print(service)
                        print(str(ip) + ':' + str(service) + " Is open on TCP port " + str(p))
                        service_version(ip,p,service)
                        if p in ports:
                                pass
                                cve_api(service)
                elif result == 1: 
                        print(ip + " Is closed on TCP port " + p)


def service_version(ip,port,service):
        #grabs version of service running on a port using subprocess and netcat
        #command (does not work on windows)

        command = ["nc" , str(ip) ,str(port)]
        out = subprocess.Popen(command,
                               stdout = subprocess.PIPE,
                               stderr = subprocess.STDOUT)
        stdout,stdrr = out.communicate()
        version = stdout.split()[1]+ "/" + stdout.split()[2]
        version = version.strip("()")
        return cve_api(service + version) 


def cve_api(service_name):
        #takes service name and returns the cve from the api json file
        #='vsFTPd/1.1.1'
        #should return CVE-2008-2375 for the assignment
        url = 'https://cve.circl.lu/api/search/' + service_name
        response = requests.get(url)
        
        cve_id = json.loads(response.text)
        print(cve_id['results'][1]['id'])


scanner()
