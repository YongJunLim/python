import collections
Player = collections.namedtuple('Player', 'score name')
numStudent = int(input("Enter number of students: "))
nameScore = {}

for i in range(1, numStudent+1):
        name = input("Enter student's name: ")
        score = int(input("Enter {0}'s score: ".format(name)))
        nameScore[name] = score

best = sorted([Player(v,k) for (k,v) in nameScore.items()], reverse=True)
print(nameScore)
player1 = best[0]
player2 = best[1]
print("{0}'s score: {1}".format(player1.name, player1.score))
print("{0}'s score: {1}".format(player2.name, player2.score))
