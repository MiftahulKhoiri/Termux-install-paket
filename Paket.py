import os

def menu():

    print(""" 


                            ....
                           W$$$$$u
    {beruang beruang}       $$$$F**+      .oW$$$eu
                           ..ueeeWeeo    $$$$$$$$$
                       .eW$$$$$$$$$$$$b- $$$$$$$$$W
           ,,,,,,,uee$$$$$$$$$$$$$$$$$$ H$$$$$$$$$~
        :eoC$$$$$$$$$$$C""?$$$$$$$$$$$$ T$$$$$$$$"
         $$$*$$$$$$$$$$$$$e "$$$$$$$$$$$i$$$$$$F"
         ?f"!?$$$$$$$$$$$$$$ud$$$$$$$$$$$$$$$*Co
         $   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 !!!!m.*eeeW$$$$$$$$$$$f?$$$$$$$$$$$$$$$$$$$$$$$$U
 !!!!!! !$$$$$$$$$$$$$$  T$$$$$$$$$$$$$$$$$$$$$$$$
  *!!*.o$$$$$$$$$$$$$$$e,d$$$$$$$$$$$$$$$$$$$$$$$$:
 "eee$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$C
b ?$$$$$$$$$$$$$$**$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$!
Tb "$$$$$$$$$$$$$$*uL"$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
 $$o."?$$$$$$$$F" u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  $$$$en ```    .e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
   $$$B*  =*"?.e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F
    $$$W"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
     "$$$o#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
     ?$$$W$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" 

[01-05-2024]═════════[bagus choiri]═════════[V.1.0]$

==============================================
00. paket termux yang mau di install
-------------------------------------------
1.  Install Nmap 
2.  Install Hydra
3.  Install SQLMap
4.  Install Metasploit
5.  Install Ngrok
6.  Install Kali Nethunter
7.  Install angryFuzzer
8.  Install Red_Hawk
9.  Install Weeman
10. Install IPGeoLocation
11. Install Cupp
12. Install Instagram Bruteforcer (instahack)
13. Install Twitter Bruteforcer   (TwitterSniper)
14. Install Ubuntu
15. Install Fedora
16. Install viSQL
17. Install Hash-Buster
18. Install D-TECT
19. Install routersploit
------------------------------------------
99. keluar
==============================================
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "00":
        print("================================")
        print("pilih paket mana yang mau kamu install: nmap, hydra, sqlmap, metasploit, ngrok, angryFuzzer, red_hawk, weeman, IPGeoLocation, cupp, instahack, TwitterSniper, Hash-Buster, D-TECT, routersploit and viSQL?.")
        print("----------------")
        hm = input("[?] Continue? (Y/N): ").upper()
        print("================================")
        if hm == "Y":
            print("========================================================")
            print("[+] Wait a moment")
            print("This will take...")
            print("========================================================")
            os.system("apt update")
            os.system("apt install -y git")
            os.system("apt install -y python")
            os.system("apt install -y python2")
            os.system("apt install -y wget")
            os.sysetm("apt install -y nmap")
            os.system("apt install -y hydra ")
            os.system("apt update -y")
            os.system("apt install -y git")
            os.system("apt install python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("apt install wget")
            os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
            os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
            os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
            os.system("cd /data/data/com.termux/files/home && bundle install")
            os.system("cd /data/data/com.termux/files/home")
            os.system("apt update -y")
            os.system("apt install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("apt update -y")
            os.system("apt install -y git")
            os.system("apt install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
            os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
            os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home && pip2 install requests")
            os.system("cd /data/data/com.termux/files/home")
            os.system("apt update -y")
            os.system("apt install -y git")
            os.system("apt install -y php")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
            os.system("cd /data/data/com.termux/files/home")
            os.system("apt update -y")
            os.system("apt install -y python2")
            os.system("apt install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
            os.system("cd /data/data/com.termux/files/home && cd weeman")
            os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
            os.system("cd /data/data/com.termux/files/home")
            os.system("apt update -y")
            os.system("apt install -y git")
            os.system("apt install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
            os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
            os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home")
            os.system("apt update -y")
            os.system("apt install -y git")
            os.system("apt install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
            os.system("apt update -y")
            os.system("apt install -y git")
            os.system("apt install -y python")
            os.system("apt install -y nano")
            os.system("apt install requests")
            os.system("pip install beautifulsoup4")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
            os.system("apt update -y")
            os.system("apt install -y git")
            os.system("apt install -y python")
            os.system("apt install mechanicalsoup")
            os.system("apt install -y nano")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
            os.system("apt update -y")
            os.system("apt install -y git")
            os.system("apt install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
            os.system("apt update -y")
            os.system("apt install -y git")
            os.system("apt install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
            os.system("apt update -y")
            os.system("apt install -y git")
            os.system("apt install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
            os.system("apt update -y")
            os.system("apt install -y git")
            os.system("apt install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            os.system("clear")
            print("========================================")
            print("[+] selamat install selesai             :)")
            print("[+] selamat menggunakan                     <3")
            print("========================================")
        else:
            rmenu = input("[?] kembali ke menu? (Y/N): ").upper()
            if rmenu == "Y":
                menu()
            else:
                break
    if what == "1":
        os.system("cd /data/data/com.termux/files/home")
        os.system("apt update -y")
        os.system("apt install -y nmap")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] nmap sukses di install :)")
        print("[+] Type 'nmap' untuk mulai.")
        print("====================================")
        rmenu = input("[?] Back to menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("apt update -y")
        os.system("apt install -y hydra")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] hydra berhasil di install:)")
        print("[+] Type 'hydra' untuk memulai .")
        print("====================================")
        rmenu = input("[?] kembali ke menu ? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "3":
        os.system("cd /data/data/com.termux/files/home")
        os.system("apt update -y")
        os.system("apt install -y git")
        os.system("apt install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SQLMap selesai di install :)")
        print("[+] pergi ke sqlmap folder dan ketik 'python2 sqlmap.py' untuk memulai .")
        print("====================================")
        rmenu = input("[?] kembali ke menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "4":
        os.system("apt install -y wget")
        os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home && bundle install")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Metasploit sukses dibinstall :)")
        print("[+] Type 'msfconsole' to start.")
        print("====================================")
        rmenu = input("[?] kembali ke menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "5":
        os.system("apt update -y")
        os.system("apt install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] ngrok sukses di install :)")
        print("[+] pergi ke folder ngrok dan ketik'./ngrok http 80' to start.")
        print("====================================")
        rmenu = input("[?] kembali ke menu ? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "6":
        os.system("apt update -y")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
        os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] kali Nethunter sukses di install :)")
        print("[+] pergi ke folder Nethunter-In-Termux dan ketik './kalinethunter' untuk mulai.")
        print("====================================")
        rmenu = input("[?] Back to menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "7":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
        os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
        os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home && pip2 install requests")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] angryFuzzer installed successfully :)")
        print("[+] Go to angryFuzzer folder and type 'python2 angryFuzzer.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "8":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y php")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] RED_HAWK installed successfully :)")
        print("[+] Go to RED_HAWK folder and type 'php rhawk.php' to start.")
        print("====================================")
        rmenu = input("[?] Back to menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "9":
        os.system("pkg update -y")
        os.system("pkg install -y python2")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
        os.system("cd /data/data/com.termux/files/home && cd weeman")
        os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] weeman installed successfully :)")
        print("[+] Go to weeman folder and type 'python2 weeman.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "10":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
        os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
        os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] IPGeoLocation installed successfully :)")
        print("[+] Go to IPGeoLocation folder and type 'python ipgeolocation.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "11":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
        print("====================================")
        print("[+] Cupp installed successfully :)")
        print("[+] Go to cupp folder and type 'python cupp3.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "12":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y nano")
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
        print("====================================")
        print("[+] Instahack installed successfully :)")
        print("[+] Go to instahack folder and type 'python hackinsta.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "13":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pip install mechanicalsoup")
        os.system("pkg install -y nano")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
        print("====================================")
        print("[+] TwitterSniper installed successfully :)")
        print("[+] Go to TwitterSniper folder and type 'python TwitterSniper.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "14":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
        os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
        print("====================================")
        print("[+] Ubuntu installed successfully :)")
        print("[+] Go to termux-ubuntu folder and type './start.sh' to start.")
        print("====================================")
        rmenu = input("[?] Back to menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "15":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y wget")
        os.system("apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
        print("====================================")
        print("[+] Fedora installed successfully :)")
        print("[+] Type 'sh termux-fedora.sh f26_arm64' or 'sh termux-fedora.sh f26_arm' to start.")
        print("====================================")
        rmenu = input("[?] Back to menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "16":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
        print("====================================")
        print("[+] viSQL installed successfully :)")
        print("[+] Go to viSQL folder and type 'python2 viSQL.py --help' to start.")
        print("====================================")
        rmenu = input("[?] Back to menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "17":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
        print("====================================")
        print("[+] Hash-Buster installed successfully :)")
        print("[+] Go to Hash-Buster folder and type 'python2 hash.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "18":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
        print("====================================")
        print("[+] Hash-Buster installed successfully :)")
        print("[+] Go to Hash-Buster folder and type 'python2 hash.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "19":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
        os.system("cd /data/data/com.termux/files/home && cd routersploit")
        os.system("pip2 install -r requirements.txt")
        os.system("pip2 install -r requirements-dev.txt")
        os.system("pip2 install -r requests")
        print("====================================")
        print("[+] routersploit installed successfully :)")
        print("[+] Go to routersploit folder and type 'python2 rsf.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to menu? (Y/N): ").upper()
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "99":
        print("Bye.")
        break
