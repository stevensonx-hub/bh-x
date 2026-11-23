import questionary

def boot():
    choice = questionary.select("Select Boot Option",
    choices=[
        "Fresh Boot(Erase all previous content)",
        "Continue with previous content",

    ],
    ).ask()

    if choice == "Fresh Boot(Erase all previous content)":
        print("Are you super ultra helicopter sure???? Cause you aint getting that stuff back")