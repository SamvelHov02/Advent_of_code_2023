from sys import stdin

def main():
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14
    
    total_ids = 0
    game_count = 0
    total_sum = 0
    
    while True:
        game = stdin.readline()
        game_count = game_count + 1
        if game != "":
            game_format = change_input_format(game)
            games = count_max_in_game(game_format)
            valid = True 
            for color in games.keys():
                if color == 'red' and games[color] > red_cubes: 
                    valid = False
                    break
                elif color == 'blue' and games[color] > blue_cubes:
                    valid = False
                    break
                elif color == 'green' and games[color] > green_cubes:
                    valid = False
                    break
                
            if valid:
                total_ids = total_ids + 1     
                total_sum = total_sum + game_count
        else: break
        
    print(total_sum)
        

def change_input_format(game):
    first_index = game.find(':')
    new_game = game[first_index + 1:]
    new_game = new_game.strip()
    return new_game.split(';')
    

def count_max_in_game(game):
    colors = {'red': 0, 'green': 0, 'blue':0}
    
    # ['3 blue, 2 red']
    for sub in game:
        new_sub = sub.split(',')
        amount = 0
        # ['3 blue', '2 red']
        for color in new_sub:
            color = color.strip()
            color_str = ''
            amount = ""
            for character in color:
                if character.isnumeric():
                    amount  = amount + character
                elif character not in ['\n, ' ', \t']:
                    color_str = color_str + character
            
            amount = int(amount)
            color_str = color_str.strip()
            
            for key in colors.keys():
                if key == color_str and colors[key] < amount: 
                    colors[key] = amount
                    break
    
    return colors
        
    
if __name__ == '__main__':
    main()