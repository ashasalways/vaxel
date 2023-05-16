def exChange(belopp, sedel):
    return int(belopp) // sedel

def get_exchange_dict(inbetalning, priset):
    antal_mynt = 0
    pengar_tillbaka = 0

    sedlar_mynt_dictionary = {500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}

    #500-----------------------------------------
    pengar_tillbaka = inbetalning - priset
    antal_mynt = exChange(pengar_tillbaka, 500)
    pengar_tillbaka = pengar_tillbaka % 500
    sedlar_mynt_dictionary[500]

    #200-----------------------------------------
    antal_mynt = exChange(pengar_tillbaka, 200)
    pengar_tillbaka = pengar_tillbaka % 200
    sedlar_mynt_dictionary[200] = antal_mynt

    #100-----------------------------------------
    antal_mynt = exChange(pengar_tillbaka, 100)
    pengar_tillbaka = pengar_tillbaka % 100
    sedlar_mynt_dictionary[100] = antal_mynt

    #50------------------------------------------
    antal_mynt = exChange(pengar_tillbaka, 50)
    pengar_tillbaka = pengar_tillbaka % 50
    sedlar_mynt_dictionary[50] = antal_mynt

    #20------------------------------------------
    antal_mynt = exChange(pengar_tillbaka, 20)
    pengar_tillbaka = pengar_tillbaka % 20
    sedlar_mynt_dictionary[20] = antal_mynt

    #10------------------------------------------
    antal_mynt = exChange(pengar_tillbaka, 10)
    pengar_tillbaka = pengar_tillbaka % 10
    sedlar_mynt_dictionary[10] = antal_mynt

    #5-------------------------------------------
    antal_mynt = exChange(pengar_tillbaka, 5)
    pengar_tillbaka = pengar_tillbaka % 5
    sedlar_mynt_dictionary[5] = antal_mynt

    #2-------------------------------------------
    antal_mynt = exChange(pengar_tillbaka, 2)
    pengar_tillbaka = pengar_tillbaka % 2
    sedlar_mynt_dictionary[2] = antal_mynt

    #1-------------------------------------------
    antal_mynt = exChange(pengar_tillbaka, 1)
    pengar_tillbaka = pengar_tillbaka % 1
    sedlar_mynt_dictionary[1] = antal_mynt

    #print (f"500: {antal_mynt}")
    return sedlar_mynt_dictionary