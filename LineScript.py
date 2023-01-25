def main():
    
    counter = 0
    line = 0    
    lineCheck = "I will not tell lies to my parents ever again."
    
    while counter != 100:

        print("------------------------------------------------")
        print("\"I will not tell lies to my parents ever again.\"")
        print("------------------------------------------------")

        line = input("Input Line: ")

        if line == lineCheck:

            counter += 1
            print(counter)

        else:

            print("retype the sentence")
        


main()
