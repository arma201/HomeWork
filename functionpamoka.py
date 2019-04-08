# import random
# from Controller import getScores
# from Controller import addScore
# from Controller import giveHint
from Controller import printHighscores
# from Controller import checkNumber
from Controller import playGame


# scores = getScores()

printHighscores()

nuo = int(input("Nuo kurio skaiciaus spesim? Kokia intervalo pradzia?"))
iki = int(input("Iki kurio skaiciaus spesim? Kokia intervalo pabaiga?"))

playGame(nuo=nuo, iki=iki)




# r - read
# w - write (perrasys tai, kas viduje yra)
# a - add write (dades iki to, kas viduje yra)





