import os
import change

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\t-Växlare-\n")

    pris = input("\tMata in pris på varan i kr: ")
    inbet = input("\tInbetalt belopp i kr: ")

    exChangeNow(int(pris), int(inbet))

def exChangeNow(priset, inbetalningen):
    
    if (priset > inbetalningen):
        print("\tFattas pengar! ")

    else:
        change_back = change.get_exchange_dict(inbetalningen, priset)

        print("\n\t-------------------------------------------")
        print ("\tVäxel tillbaka: \n")
        print(f"\tAntal 500 lappar: {change_back[500]}")
        print(f"\tAntal 200 lappar: {change_back[200]}")
        print(f"\tAntal 100 lappar: {change_back[100]}")
        print(f"\tAntal 50 lappar: {change_back[50]}")
        print(f"\tAntal 20 lappar: {change_back[20]}")
        print(f"\tAntal 10 kronor: {change_back[10]}")
        print(f"\tAntal 5 kronor: {change_back[5]}")
        print(f"\tAntal 2 kronor: {change_back[2]}")
        print(f"\tAntal 1 kronor: {change_back[1]}")





main()