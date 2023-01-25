import random

def main():

    for x in range(25):

        print("insert into invoice values (" + str(random.randint(1111111111, 9999999999)) + "," + str(random.randint(1111111111, 9999999999)) + \
              "," + str(round(random.uniform(500.00, 2000.00), 2))+ ",null,null);")

        x = x + 1

main()
