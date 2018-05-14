import os
import subprocess
import pyttsx3
import time
import getpass

# Function to speak stuff
def speak(var):
    engine = pyttsx3.init()
    engine.say(var)
    engine.runAndWait()


# Function to handle menu
def Menu():
    run = 1;
    while True:
        os.system("clear")
        os.system("tput setaf 2")
        print("\t\t\t\t\t-----------------------------------")
        os.system("tput setaf 1")
        print("\t\t\t\t\t\tWelcome to my menu")
        user = getpass.getuser()
        welcome = "Welcome" + user
        speak(welcome)
        os.system("tput setaf 2")
        print("\t\t\t\t\t-----------------------------------")
        print()
        print("\t\t\t\t\t    Press 1: Date\n\t\t\t\t\t    Press 2: Calendar\n\t\t\t\t\t    Press 3: Create  File\n\t\t\t\t\t    Press 4: Exit")
        print("\t\t\t\t\t-----------------------------------")
        speak("What can I do for you?")
        x = int(input("\t\t\t\t\t    Enter your choice : "))

        ### Date
        if x == 1:
            cmdout = subprocess.getstatusoutput("date")
            
            if cmdout[0] == 0:
                print("\t\t\t\t\t    {}".format(cmdout[1]))
                dt = subprocess.getstatusoutput("date +%d")
                mon = subprocess.getstatusoutput("date +%B")
                yr = subprocess.getstatusoutput("date +%Y")
                calout = dt[1] + " " + mon[1] + " " + yr[1]
                speak(calout)
            else:
                print("\t\t\t\t\t    Error!!")
                speak("Incorrect Input")
            time.sleep(1)
            
        ## Cal
        elif x == 2:
            cmdout = subprocess.getstatusoutput("cal")
            if cmdout[0] == 0:
                print("\t\t\t\t\t    {}".format(cmdout[1]))
                mon = subprocess.getstatusoutput("date +%B")
                yr = subprocess.getstatusoutput("date +%Y")
                calout = mon[1] + " " + yr[1]
                speak(calout)
            else:
                print("\t\t\t\t\t    Error!!")
                speak("Incorrect Input")
            time.sleep(1)
        
        ## Create FileName
        elif x == 3:
            speak("Enter Filename")
            file_name=input("\t\t\t\t\t    Enter Filename : ");
            cmdout=subprocess.getstatusoutput("touch {0}".format(file_name));
            if cmdout[0] == 0:
                speak("File created successfully")
            else:
                print("\t\t\t\t\t    Error!!")
                speak("Incorrect Input")
            time.sleep(1)
        
        ## Exit the menu
        elif x == 4:
            os.system("exit")
            speak("See you again, Goodbye")
            time.sleep(1)
            break
        
        run= run + 1;


# Driver 
def main():
    # To print username
    #print(getpass.getuser())
    Menu()
    os.system("clear")



#Run Driver
main()
