import requests
import os

def dir_brute(url, wordlist): 
	#bruteforce url diretories and return '200' OK responses
	#Takes in base site (needs to end in / ) to search and wordlist to use 
	#returns a list of valid responses

        valid_dir = []

        words = open(wordlist, 'r')
        directories = words.read().splitlines()
        words.close()


        for i in directories: 
                r = requests.get(url + i, verify=False)
                #print("testing : " + url + i + "/flag.txt \n")
                if r.status_code == 200:
                        print("VALID 200 dir at : " + i)
                        valid_dir.append(url+ i)
                else:
                        pass

                        #print("failed dir at : " + i + " " + str(r.status_code))
        print(valid_dir)



        
dir_brute(input("Enter full web address to directory"),r'C:\Users\Zach\Desktop\finalLabScripts\directories.txt')
# result = CNS{0421008445828ceb46f496700a5fa65e}
# dir at /backup/
