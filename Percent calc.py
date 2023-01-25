def main():

    capital = 1200
    capitalGrowth = 0
    x = 0

    for x in range(5):
        
        capitalGrowth = float(round(capital + (capital * 0.3), 2))
        capital = capitalGrowth
        print(capital)
        x += 1
         
main()
