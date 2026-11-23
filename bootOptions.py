#boot return Contiue|Erase all|

import questionary


#make all files blank
def freshBoot():
    print("...Erasing all files...")

def signIn


#usr erase or go to sign in and sign up screen 
def boot():
    choice = questionary.select("Select Boot Option",
    choices=[
        "Continue with previous content",
        "Setup Sequence(*note this erases all content)",
        "Erase all (Erase all previous content and go to a setup screen)",
        

    ],
    ).ask()

    if choice == "Erase all (Erase all previous content and go to a setup screen)":
        sure = input("Are you super ultra helicopter sure???? Cause you aint getting that stuff back brotato(type 'yes i am super sure and a chicken' or 'no'): ")
        while sure != "yes i am super sure and a chicken":
            sure = input("Admit your a chicken, just do it: ")
            if sure == "no":
                return
        #call freshboot
        return "Erase all"
    elif choice == "Setup Sequence(*note this erases all content)":
        return "Setup"
    else:
        return "Continue"

        #move to sign in screen
