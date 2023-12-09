with open("input") as f:
    
    sum_problem_1 = 0
    sum_problem_2 = 0
    
    for line in f:

        game_number, games = line.strip().split(":")
        individual_games = games.replace(";", ",").split(",")
        new_dict = {'red' : 0, 'green' : 0, 'blue' : 0}
        flag = True
        
        for game in individual_games:
            
            number, type = game.strip().split(" ")
            
            if int(number) > 12 and type == "red" or int(number) > 13 and type == "green" or int(number) > 14 and type == "blue":
                flag = False
                #to optimize the code, we can break the loop here, but for problem 2 we need to check all the games
            
            if new_dict[type] < int(number):
                new_dict[type] = int(number)
    
        if flag:
            sum_problem_1 += int(game_number.split(" ")[1])

        sum_problem_2 += new_dict['red'] * new_dict['green'] * new_dict['blue']
            
    print("What is the sum of the IDs of those games? ~ Answer:", sum_problem_1)
    print("What is the sum of the power of these sets? ~ Answer:", sum_problem_2)
                

