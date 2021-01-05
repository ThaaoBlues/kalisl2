import sys,ctypes,os,subprocess,pyautogui,pyfiglet
from time import  sleep


#pip install opencv-python ctypes pyautogui pyfiglet

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def pinfo(text):
    print("[+] "+text.lower()[0].upper()+text.lower()[1:])

#make sure you are in the right directory
os.chdir(os.path.abspath(__file__).replace(os.path.basename(__file__),""))


if is_admin():
    print(pyfiglet.figlet_format("KALISL2"))
    pinfo(f"opening kali ms-store page...")
    subprocess.run(["start","ms-windows-store:"],shell=True)
    sleep(5)
    c = pyautogui.locateCenterOnScreen("search_bar.png",confidence=0.8)
    pyautogui.click(c[0],c[1])
    sleep(1)
    pyautogui.write("Kali Linux")
    sleep(1)
    pyautogui.press('enter')
    sleep(2)
    c = pyautogui.locateCenterOnScreen("kali_part.png",confidence=0.8)
    pyautogui.click(c[0],c[1])
    sleep(10)
    #main()
    pass
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)




def run_bash_cmd(cmd):
    subprocess.run(["bash","-c","\"",cmd,"\""],shell=True)


def main():
    sUsername = input("Please type a username to log in your future wsl machine :\n-->")
    sPassword = input("Please type a password to log in your future wsl machine :\n-->")

    if not os.path.isfile("bool"):
        #enabling necessary windows features
        pinfo("enabling necessary windows features")
        lFeatures = ["Microsoft-Windows-Subsystem-Linux","VirtualMachinePlatform"]
        for ft in lFeatures:
            subprocess.run(["DISM","/online","/enable-feature",f"/featurename:{ft}","/all","/norestart"],shell=True)

        

        pinfo("preparing your computer to restart")
        #placing files in startup folder
        open(f"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\bool","w")
        subprocess.run(["copy","quick_wsl2_setup.exe",f"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{os.path.basename(__file__)}"],shell=True)
        
        pinfo("restarting your computer and re-runing this script to get to the next step.\n don't worry this will be automatic.")
        sleep(10)
        subprocess.run(["shutdown","/r"],shell=True)

    else:

        #once the features are enabled
        #removing files from startup folder
        pinfo("removing files from startup folder")

        subprocess.run(["remove",f"\"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\bool\""])
        subprocess.run(["remove",f"\"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{os.path.basename(__file__)}\""])
        
        #enabling wsl2
        pinfo("enabling wsl2")

        subprocess.run(["wsl","--set-default-version","2"],shell=True)

        #downloading system (for french store)
        
        pinfo(f"opening kali ms-store page...")
        subprocess.run(["start","ms-windows-store:"],shell=True)
        sleep(5)
        c = pyautogui.locateCenterOnScreen("search_bar.png",confidence=0.8)
        pyautogui.click(c[0],c[1])
        sleep(1)
        pyautogui.write("Kali Linux")
        sleep(1)
        pyautogui.press('enter')
        sleep(2)
        c = pyautogui.locateCenterOnScreen("kali_part.png",confidence=0.8)
        pyautogui.click(c[0],c[1])
        sleep(10)


        c = pyautogui.locateCenterOnScreen("downland_button.png",confidence=0.8)
        pyautogui.click(c[0],c[1])
        while pyautogui.locateOnScreen("lauch_button.png",confidence=0.8) == None:
            sleep(10)
        c = pyautogui.locateCenterOnScreen("launch_button.png",confidence=0.8)
        pyautogui.click(c[0],c[1])


        sleep(30)
        #set up account
        pyautogui.write(sUsername)
        sleep(1)
        pyautogui.press('enter')
        sleep(1)
        pyautogui.write(sPassword)
        sleep(1)
        pyautogui.press('enter')
        sleep(1)
        pyautogui.write(sPassword)
        sleep(1)
        pyautogui.press('enter')
        sleep(1)
        #update repo
        pyautogui.write("sudo apt update & sudo apt dist-upgrade")
        sleep(1)
        pyautogui.write(sPassword)
        pyautogui.press('enter')

        if "kali" in os.listdir():
            pyautogui.write("sudo apt install kali-win-kex dbus-x11")
            pyautogui.press("enter")
            pinfo("Your WSL2 environnement is not set up ! just type bash to enter kali shell and kex in the shell to enter kali GUI")

            



