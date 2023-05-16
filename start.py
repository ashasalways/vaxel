import os
import change

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\t-Växlare-\n")

    pris = input("\tMata in pris på varan i kr: ")
    inbet = input("\tInbetalt belopp i kr:")

    exChangeNow(int(pris), int(inbet))

def exChangeNow(priset, inbetalningen):
    
    if priset > inbetalningen():
        print("\tFattas pengar!")




main()