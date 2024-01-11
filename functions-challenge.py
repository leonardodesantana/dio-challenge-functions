ranks = {
    'Ferro': {'Rank': 'Ferro', 'Min Wins': 0, 'Max Wins': 10},
    'Bronze':{'Rank': 'Bronze', 'Min Wins': 11, 'Max Wins': 20},
    'Prata':{'Rank': 'Prata', 'Min Wins': 21, 'Max Wins': 50},
    'Ouro':{'Rank': 'Ouro', 'Min Wins': 51, 'Max Wins': 80},
    'Diamante':{'Rank': 'Diamante', 'Min Wins': 81, 'Max Wins': 90},
    'Lendário':{'Rank': 'Lendário', 'Min Wins':91, 'Max Wins':100},
    'Imortal': {'Rank': 'Imortal', 'Min Wins': 101, 'Max Wins': float('inf')}
}
def playerRank(wins, losses):
    for elo in ranks.values():
        if wins >= elo['Min Wins'] and wins <= elo['Max Wins']:
            return elo['Rank']
    return "Player sem rank."

def playerWL(wins, losses):
    rankedWL = wins - losses
    return rankedWL

wins = 11
losses = 43

rankedWL = playerWL(wins,losses)
elo = playerRank(wins,losses)

print("O Herói tem saldo de " + str(rankedWL) + " e está no nível de " + elo + ".")