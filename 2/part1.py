max_score = {"red": 12, "green": 13, "blue": 14}

def game_possible(game_str: str) -> bool:
    score_strs = game_str.split(",")
    scores = {"red": 0, "green": 0, "blue": 0}
    for score_str in score_strs:
        [count_str, colour] = score_str.split()
        scores[colour] = int(count_str)
    for colour, score in scores.items():
        if score > max_score[colour]:
            return False
    return True

def main():
    with open("_input") as input:
        lines = input.readlines()
        total: int = 0
        for line in lines:
            [game_id_str, games_str] = line.split(":")
            
            game_id = int(game_id_str.split()[1])

            if all([game_possible(game_str) for game_str in games_str.split(";")]):
                total += game_id        
                
    print(total)

if __name__ == "__main__":
    main()