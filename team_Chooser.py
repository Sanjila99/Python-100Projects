from random import choice
 
def assign_teams(players,team_size):
    team1_name=input("Enter the name for Team1:")
    team2_name=input("Enter the name for Team2:")

    team1=[]
    team2=[]

    while len(players)>0:
        if len(players)<team_size:
            print("Error:Not enough players for the speocifed team size.")
            return [],[]
        playerA=choice(players)
        print(playerA)
        team1.append(playerA)
        players.remove(playerA)
        
    
        playerB=choice(players)
        print(playerB)
        team2.append(playerB)
        players.remove(playerB)
   
    return team1,team2,team1_name,team2_name

def main():
    players=[]
    while True:
        player=input("Enter player name (or type 'done' to finish):")
        if player.lower()=='done':
          break
        players.append(player)

    team_size = int(input("Enter the desired team size: "))

    team1, team2, team1_name, team2_name = assign_teams(players, team_size)

    print(f"{team1_name}: {team1}")
    print(f"{team2_name}: {team2}")

if __name__ == "__main__":
    main() 