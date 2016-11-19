
#!/usr/bin/python
# Nick Sanzotta
# Description: Enumerates employee names from LinkedIn.com based off company search results.
# Version v 1.9222016
import os, sys, getopt, getpass, re, requests, time
from sys import argv
from bs4 import BeautifulSoup

timestr = time.strftime("%Y%m%d-%H%M")
curr_time = time.time()

class colors:
   white = "\033[1;37m"
   normal = "\033[0;00m"
   red = "\033[1;31m"
   blue = "\033[1;34m"
   green = "\033[1;32m"
   lightblue = "\033[0;34m"


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def connection(email, password, companyName, pageResults, timeout, result):
    # outputTitle = 'linkScrape-data/'+companyName+'_employee-title_'+timestr+'.txt'
    client = requests.Session()
    homepage = 'https://www.linkedin.com'
    login = 'https://www.linkedin.com/uas/login-submit'
    html = client.get(homepage).content
    soup = BeautifulSoup(html,'lxml')
    csrf = soup.find(id="loginCsrfParam-login")['value']
    login_information = {
        'session_key': email,
        'session_password': password,
        'loginCsrfParam': csrf,
        }
    client.post(login, data=login_information)
    companyInfo = ''


    r1=client.get('https://www.linkedin.com/vsearch/p?type=people&keywords='+companyName)
    for z in range(1, pageResults):
        time.sleep(timeout)
        r1=client.get('https://www.linkedin.com/vsearch/p?type=people&keywords='+companyName+'&page_num='+str(z))
        m1 = re.findall(r"formatted_name\"\:\"[\w]*.[\w][\W]*.[\w]*", r1.text)
        m2 = re.findall(r"fmt_heading\"\:\"[\w]*.[\w][\W]*.[\w]*", r1.text)
        for i, j in zip(m1,m2):
           x1 = i
           x2 = j
           employee = re.sub('formatted_name":"','', x1)
           title = re.sub('fmt_heading":"','', x2)
           
           x=employee.encode("utf-8")
           y=title.encode("utf-8")
           x = x.replace('(',' ').split()

           result.append(x)

    cls()


def mangleOne(first_name, last_name, companyName, formatValue, domain):
    newname=first_name + last_name
    newname = newname+"@"+domain

    return newname

def mangleTwo(first_name, last_name, companyName, formatValue, domain):
    newname = last_name + first_name
    newname = newname+"@"+domain
    return newname

def mangleThree(first_name, last_name, companyName, formatValue, domain):
    newname = first_name + "." + last_name
    newname = newname+"@"+domain
    return newname


def mangleFour(first_name, last_name, companyName, formatValue, domain):
    newname = last_name + "." + first_name
    newname = newname+"@"+domain
    return newname

def mangleFive(first_name, last_name, companyName, formatValue, domain):
    newname = first_name + "_" + last_name
    newname = newname+"@"+domain
    
    return newname

def mangleSix(first_name, last_name, companyName, formatValue, domain):
    newname = last_name + "_" + first_name
    newname = newname+"@"+domain
    
    return newname


def mangleSeven(first_name, last_name, companyName, formatValue, domain):
    newname = first_name[0] + last_name
    newname = newname+"@"+domain
    
    return newname

def mangleEight(first_name, last_name, companyName, formatValue, domain):
    newname = last_name[0] + first_name
    newname = newname+"@"+domain
    
    return newname

def mangleNine(first_name, last_name, companyName, formatValue, domain):
    newname = first_name + last_name[0]
    newname = newname+"@"+domain
    
    return newname


def mangleTen(first_name, last_name, companyName, formatValue, domain):
    newname = first_name[0] + "." + last_name
    newname = newname+"@"+domain
    
    return newname

def mangleEleven(first_name, last_name, companyName, formatValue, domain):
    newname = last_name[0] + "." + first_name
    newname = newname+"@"+domain
    
    return newname

def mangleTwelve(first_name, last_name, companyName, formatValue, domain):
    newname = last_name[0:3] + first_name[0:2]
    newname = newname+"@"+domain
    
    return newname


def mangleThirteen(first_name, last_name, companyName, formatValue, domain):
    newname = last_name[0:4] + first_name[0:3]
    newname = newname+"@"+domain
    
    return newname

def mangleAll(first_name, last_name, companyName, formatValue, domain):
    newname = list()

    newname.append(mangleOne(first_name, last_name, companyName, formatValue, domain))
    newname.append(mangleTwo(first_name, last_name, companyName, formatValue, domain))
    newname.append(mangleThree(first_name, last_name, companyName, formatValue, domain))
    newname.append(mangleFour(first_name, last_name, companyName, formatValue, domain))
    newname.append(mangleFive(first_name, last_name, companyName, formatValue, domain))
    newname.append(mangleSix(first_name, last_name, companyName, formatValue, domain))
    newname.append(mangleSeven(first_name, last_name, companyName, formatValue, domain))
    newname.append(mangleEight(first_name, last_name, companyName, formatValue, domain))
    newname.append(mangleNine(first_name, last_name, companyName, formatValue, domain))
    newname.append(mangleTen(first_name, last_name, companyName, formatValue, domain))
    newname.append(mangleEleven(first_name, last_name, companyName, formatValue, domain))
    newname.append(mangleTwelve(first_name, last_name, companyName, formatValue, domain))
    newname.append(mangleThirteen(first_name, last_name, companyName, formatValue, domain))
    return newname

def name(companyName, formatValue, domain, result):
    # filename = "linkScrape-data/"+companyName+"-"+"mangle-"+str(formatValue)+"_"+timestr+".txt"
    for i in range(len(result)):
        person = result[i]
        # print person
        first_name = person[0]
        last_name = person[1]
        person.append(mangleAll(first_name, last_name, companyName, formatValue, domain))
    return result


def write(companyName, formatValue, newname):
    filename = "linkScrape-data/"+companyName+"-"+"mangle-"+str(formatValue)+"_"+timestr+".txt"
    with open(filename, 'a') as f:
        f.write(newname+"\n")


def help():
  
    print " Usage: python linkScrape.py <OPTIONS> \n"
    print " Example: python linkScrape.py -e LinkedInUser@email.com -c google -m 99 -d google.com\n"
    # print " Example: python linkScrape.py -m 7 -i ~/Company/names.txt\n"
    # print " Raw output saved to: linkedIn/linkScrape-data/Company_time.txt "
    # print " Formatted output saved to: linkedIn/linkScrape-data/Company-mangle[x]_time.txt \n"
    print colors.lightblue + " Login options:\n" + colors.normal
    print "\t -e <email>\t\tYour LinkedIn.com Email Address. "
    print "\t -p <pass>\t\tYour LinkedIn.com Password. "
    print colors.lightblue + "\n Search options:\n" + colors.normal
    print "\t -c <company>\t\tCompany you want to enumerate.(Prepends to filename if used with -i) "
    print "\t -r <results>\t\tSearches x amount of LinkedIn.com pages (Default is 5)."
    print "\t -t <secs>\t\tSets timeout value. (Default is 5.)"
    print colors.lightblue + "\n Mangle options:\n" + colors.normal
    print """\t -m <mangle>\t\t
                                 1)FirstLast        ex:nicksanzotta
                                 2)LastFirst        ex:sanzottanick
                                 3)First.Last       ex:nick.sanzotta
                                 4)Last.First       ex:sanzotta.nick
                                 5)First_Last       ex:nick_sanzotta
                                 6)Last_First       ex:sanzotta_nick
                                 7)FLast            ex:nsanzotta
                                 8)LFirst           ex:snick
                                 9)FirstL           ex:nicks
                                10)F.Last           ex:n.sanzotta
                                11)L.Firstname      ex:s.nick
                                12)FirLa            ex:nicsa
                                13)Lastfir          ex:sanznic
                                99)All              Mangle all types
    """
    print "\t -d <domain>\t\tAppend @domain.com to enumerated user list."
    print "\t -i <input>\t\tUse local file instead of LinkedIn.com to perform name Mangle against."
    print colors.lightblue + "\n Misc:\n" + colors.normal
    print "\t -h <help>\t\tPrints this help menu."
    sys.exit(2)

def main(argv):
    # print(banner)
    email= ''
    password= ''
    companyName= ''
    formatValue = 99
    pageResults = 5
    timeout = 5
    domain = ''
    outputTitle = ''

    if not os.path.exists("linkScrape-data/"):
        os.mkdir("linkScrape-data/")


    try:
        opts, args = getopt.getopt(argv, 'e:c:r:t:o:m:d:i:h',['email=','company=','results=','timeout=','output=','mangle=','--domain=','--input=','help'])
        #GETOPT Menu:
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                help()
                sys.exit(2)
            elif opt in ('-e', '--email'):
                email = arg
                password = getpass.getpass(r'Enter password: ')
            elif opt in ('-c', '--company'):
                companyName = arg
                output = 'linkScrape-data/'+companyName+'_'+timestr+'.txt'
            elif opt in ('-r', '--results'):
                pageResults = int(arg)
                pageResults+=1
            elif opt in ('-t', '--timeout'):
                timeout = int(arg)
            elif opt in ('o','--output'):
                output = arg
            elif opt in ('-m', '--mangle'):
                formatValue = int(arg)
            elif opt in ('-d','--domain'):
                domain = arg
            elif opt in ('-i','--input'):
                inputfile = arg
                output = inputfile
                name(companyName, output, formatValue, domain)
                sys.exit(2)
            else:
                help()
                sys.exit(2)
        result = list()
        connection(email, password, companyName, pageResults, timeout, result)
        name(companyName, formatValue, domain, result)
        # print result
        print "\nCompleted in: %.1fs\n" % (time.time() - curr_time)
        return result
        

    except getopt.GetoptError:
        help()
        sys.exit(2)


if __name__ == "__main__":
    main(argv[1:])
