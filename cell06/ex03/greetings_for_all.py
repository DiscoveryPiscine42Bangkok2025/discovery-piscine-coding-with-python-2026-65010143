def greetings(x= ""):
    try:
        x = float(x)
        print("Error! It was not a name.")
    except:
        if x =="":
            x = "noble stranger."
        print("Hello,",x)

greetings('Alexandra')
greetings("Wil")
greetings()
greetings(42)
