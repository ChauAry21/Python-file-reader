choose = input("do you want to create and write a file(cw) or search an existing file for a word (s) \n")

if choose == "cw":
    fileName = input("enter file name: \n")
    finalName = fileName + ".txt"

    file = open(finalName, "a+")

    file.write(input("write your file!!  \n"))
    file.close()
elif choose == "s":
    fileName = input("enter file name: \n")
    finalName = fileName + ".txt"

    file = open(finalName, "r+")

    print("reading " + finalName)
    print(file.read())

    rewrite = input("would you like to rewrite file? (y/n) \n")

    if rewrite == "y":
        cont = input("continue where you left off or start new? (c/r)\n")
        if cont == "c":
            file = open(finalName, "a+")
            file.write(file.read() + input("continue writing! \n"))
            file.close()
            file = open(finalName, "r+")
            print("your new file reads...")
            print(file.read())
            quit()
        elif cont == "r":
            file = open(finalName, "a+")
            file.write(input("restart your file! \n"))
            file.close()
            file = open(finalName, "r+")
            print("your new file reads...")
            print(file.read())
            quit()
        else:
            print("shutting down")
            quit()

    else:
        print("shutting down")
        quit()

else:
    print("unrecognised input")
    quit()