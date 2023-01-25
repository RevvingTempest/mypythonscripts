def main():

    myBudget = 2893.05
    endProgram = 1
    
    
    while endProgram != "q":              
        
        newBudgetQuestion = input("\nDo you have a new balance? ").lower()
        

        if newBudgetQuestion == "y":
            

            try:
                
                newBudget = False
                

                while (newBudget != float) or (newBudget != int) or (newBudget != "q"):
                    

                    try:

                        
                        if newBudget == "y":

                            break

                        else:                    

                            newBudget = float(input("\nEnter new balance: "))                       
                            break
                        

                    except ValueError:
                        

                        try:

                            while newBudget != "y":

                                newBudget = str(input("\nDo you want to cancel (press y or n)? ").lower())


                                if newBudget == "y":
                                    
                                    break

                                elif newBudget == "n":

                                    break

                                else:

                                    print("Enter a valid option.")


                        except ValueError:

                            continue


                if (newBudget != myBudget) and (newBudget != "q"):
                   
                   myBudget = float(newBudget)
                

            except ValueError:

                print("Enter a y or n.")
                continue
        
        
        print("\n=================================================================")
        
        currentSharePrice = float(input("\nWhat is the current share price? "))
        
        maxSharesCanBuy = '%.2f'%(myBudget / currentSharePrice)
        
        print("\n\nYou can buy \n\n" + str(">>>> " + maxSharesCanBuy + " <<<<")
              + "\n\nshares with your budget\n")

        endProgram = input("\nTo quit, press q, otherwise press any key to continue ").lower()

main()
