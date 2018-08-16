import sys
import whois

def check_whois():
    for line in open(sys.argv[1], "r", encoding="utf8"):
        if line[0]== '#':
            pass
        else:
            try:
                w = whois.whois(line[:-1])
                print("""
                =============== Domain: {} ==============
                NameServer: {} \n 
                Name: {} \n
                Organization: {} \n
                Register Date: {} \n
                Expiration Date: {} \n
                =========================================""".format(line[:-1], w.name_servers, w.name, w.org , w.creation_date, w.expiration_date))
            except:
                print("WHOIS NOT FOUND: {}".format(line[:-1]))

check_whois()
