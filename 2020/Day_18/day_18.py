with open("input") as f:
    math_problems = f.read().splitlines()


print(math_problems)


def summarising(problems):

    solutions = []

    for problem in problems:

        values = []

        print(problem)

        if "(" in problem:
            open_par = [i for i, val in enumerate(problem) if val == "("]
            close_par = [i for i, val in enumerate(problem) if val == ")"]

            par_part = problem[min(open_par):max(close_par) + 1]



            print(par_part)
            #klammern, rest = problem.split()



summarising(math_problems)

