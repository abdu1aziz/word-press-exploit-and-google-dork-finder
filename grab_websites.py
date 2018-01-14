#!/bin/bash/python27
# Author: Abdul Aziz
"""
Description:
            This python script contains materials that can be potentially damaging or dangerous.
            If you do not fully understand something on this python script, then GO OUT OF HERE!
            Refer to the laws in your province/country before accessing, using,or in any other
            way utilizing these materials.These materials are for educational and research purposes
            only.Do not attempt to violate the law with anything contained here. If this is your intention,
            then LEAVE NOW! Neither administration of this server, the authors of this material, or anyone
            else affiliated in any way, is going to accept responsibility for your actions. Neither the
            author; Abdul Aziz is responsible for any damage caused using this script.

            ************************************************************************************************
            ***** All the information provided on this python script are for educational purposes only.*****
            *****    The python script is no way responsible for any misuse of the information.        *****
            ************************************************************************************************
"""
from google import search
import urllib2, os, requests


vuln_urls = 'tmp/vuln_sites.txt'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


welcome_banner = """\
%s*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
|%s   %sWELCOME TO ABDUL'S DORK FINDER%s       %s|
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
|%s         %sENTER YOUR GOOGLE DORK%s         %s|
|                   OR                   |
|%s  %sPRESS ENTER TO DISPLAY DEFAULT MENU  %s %s|
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-%s

""" % (bcolors.WARNING, bcolors.ENDC, bcolors.OKGREEN, bcolors.ENDC, bcolors.WARNING, bcolors.ENDC, bcolors.OKGREEN, bcolors.ENDC, bcolors.WARNING, bcolors.ENDC, bcolors.OKGREEN, bcolors.ENDC, bcolors.WARNING, bcolors.ENDC)


default_menu_banner = """\
%s*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
|  %sWORD PRESS PLUGLIN EXPLOIT MENU -- FILE UPLOAD%s  %s|
|                                                  |
%s|      PRESS 1 for WOOCOMMERCE PLUGIN EXPLOIT      |
|      PRESS 2 for DREAM WORK GALLERT EXPLOIT      |
|      PRESS 3 for UNIQUE PLUGIN FILE UPLOAD       |
|      PRESS 4 for FORMCRAFT PLUGIN EXPLOIT        |
|      PRESS 5 for CAT PRO PLUGIN EXPLOIT          |%s
%s*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-%s

""" %(bcolors.WARNING, bcolors.OKGREEN, bcolors.ENDC, bcolors.WARNING, bcolors.FAIL, bcolors.ENDC, bcolors.WARNING, bcolors.ENDC)
def decisionMaking():
    print ("\n" * 50)
    global dork_type
    print welcome_banner
    dork_type = raw_input("%s%s>> " % (bcolors.BOLD, bcolors.OKBLUE))
    if dork_type == '':
        print default_menu_banner
        choice = raw_input("%s%s>> " % (bcolors.BOLD, bcolors.OKBLUE))
        if choice == '1':
            dork_type = "inurl:/wp-content/plugins/woocommerce-product-options/includes/image-upload.php"
            dorkFinder()

        elif choice == '2':
            dork_type = "inurl:/wp-content/plugins/wp-dreamworkgallery/"
            dorkFinder()

        elif choice == '3':
            choice = "inurl:/wp-content/uploads/unique/1_uploadfolder/big/"
            dorkFinder()

        elif choice == '4':
            dork_type = "inurl:/wp-content/plugins/formcraft/file-upload/server/php/upload.php"
            dorkFinder()

        elif choice == '5':
            dork_type = "inurl:/wp-content/uploads/catpro/1_uploadfolder/big/"
            dorkFinder()
            pass
        else:
            decisionMaking()

    else:
        pass
        dorkFinder()


def dorkFinder():
    try:
        num = 0
        for url in search(dork_type, tld='com', lang='en', num=10, start=0, stop=50):
            num = num + 1
            create_file = open(vuln_urls, 'a+')
            create_file.write(url + '\n')
            print("[" + str(num) + "] -- " + url)
            create_file.close()
        print("%s[+] Success: RESULTS STORED IN vuln_urls.%s" % (bcolors.OKGREEN, bcolors.ENDC))
    except urllib2.HTTPError as httperr:
        file_error = open('error_caught.html', 'w')
        error_information = httperr.read()  # You can even read this error object just like a normal response file
        file_error.write(error_information)
        file_error.close()
        print(httperr.headers)  # Dump the headers to see if there's more information
        print('    --------------------------------------------\n\
        [-] Error Opening in Google Chrome.\n\
        --------------------------------------------\n\
        Google does try to prevent "unexpected"\n\
        queries from going through. In the normal br\n\
        -owser UI it would serve a captcha. It will\n\
        take into account the traffic pattern (too \n\
        rapid searches with "smart" queries, IP block\n\
        known to be used by spammers) and the behavior\n\
        of the client.\n\
        --------------------------------------------')
        os.system('google-chrome file:////home/py_lover/Desktop/proj_upload_bruteforce/error_caught.html')

def formatting_():
    line_num = 0
    rec_file = open(vuln_urls, 'r')
    for lines in rec_file:
        line_num = line_num + 1
    line_num = str(line_num)
    print("%s%s[+] TOTAL NUMBER OF VULNERABLE SITES: %s.%s" % (bcolors.BOLD, bcolors.FAIL, line_num, bcolors.ENDC))

def reading_data():
    vuln_sites_list = []
    rec_file = open(vuln_urls, 'r')
    lines_in_file = rec_file.readlines()
    for num_of_lines in lines_in_file:
        data = vuln_sites_list.append(num_of_lines[:-1])
    #print vuln_sites_list
    for sites in vuln_sites_list:
        make_req = requests.get(sites)

        if make_req.status_code == 200:
            print('%s[+] SITE VULNERABLE -->%s %s.' %(bcolors.OKGREEN, bcolors.ENDC, sites))

        elif make_req.status_code == 403:
            print("%s[+] SITE VULNERABLE%s %sBut Session Cookies Needed to Access Site.%s\n%s[^^^^^] SITE VULNERABLE%s --> %s." %(bcolors.OKGREEN, bcolors.ENDC, bcolors.WARNING, bcolors.ENDC, bcolors.OKGREEN, bcolors.ENDC, sites))

        elif make_req.status_code == 447:
            print("%s[-] SITE NOT VULNERABLE%s %sdue to Custom hot-fix by Web Developer Applied.%s\n%s[^^^^^] Error Code: %s %s --> %s" %(bcolors.FAIL, bcolors.ENDC, bcolors.WARNING, bcolors.ENDC, bcolors.FAIL, make_req.status_code, bcolors.ENDC, sites))

        else:
            print('%s[-] ERROR CODE: %s %s %sSITE NOT Vulnerable --> %s. %s' %(bcolors.FAIL, make_req.status_code, bcolors.ENDC, bcolors.WARNING, sites, bcolors.ENDC))

error_exception = """\
%s
\t*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
\t|   EXITTING DUE TO USER's COMMAND    |
\t|                                     |
\t|        CTRL+C DETECTED!             |
\t|                                     |
\t*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
%s
""" % (bcolors.FAIL, bcolors.ENDC)
try:
    decisionMaking()
    reading_data()
    formatting_()
except KeyboardInterrupt:
    print("\n"*12 + error_exception + "\n"*14)




#.....
