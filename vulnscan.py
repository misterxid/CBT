from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
        i = 0
        while i<=j:
                print " ",
                i+=1
def Search():
        f = open("cbt.txt","r");
        link = raw_input("Masukan website target: ")
        print "\n\nOUTPUT : \n"
        while True:
                sub_link = f.readline()
                if not sub_link:
                        break
                req_link = "http://"+link+"/"+sub_link
                req = Request(req_link)
                try:
                        response = urlopen(req)
                except HTTPError as e:
                        continue
                except URLError as e:
                        continue
                else:
                        print "FOUND! = ",req_link
def Desktop():
       Space(7);  print " CBT VULNERABILITY"
       Space(7);  print " MR_XID"
       Space(7);  print " JATIM BLACKHAT"
Desktop()
Search()
