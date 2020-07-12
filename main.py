import solver
import boards


def main():
    print("\n###############")
    print("#SUDOKU-SOLVER#")
    print("###############")
    print("by Nico Peitz")

    print("\nBitte suche dir Eins von Fünf vorgefertigten Sudokus aus...")
    print("Tipp: Du kannst die Sudokus im Code verändern.")

    for i in range(len(boards.boards)):
        print("")
        print(str(i + 1) + ". Board")
        solver.printBoard(boards.boards[i])
        print("")

    numInput = input(
        "Bitte schreibe eine Zahl von 1-" + str(len(boards.boards)) + " in die Commandozeile und drücke ENTER: ")

    try:
        if int(numInput) > len(boards.boards) or int(numInput) < 1:
            print("Error: Input needs to be in the range of 1-" + str(len(boards.boards)) + "!")
            return reStart()
    except:
        print("Error: Input needs to be an Int!")
        return reStart()

    board = boards.boards[int(numInput) - 1]

    print("\nDu hast dich für das " + numInput + ". Board entschieden.")
    solver.printBoard(board)

    print("\nIch werde versuchen es zu lösen...")
    solver.solve(board)

    print("\nUnd hier ist mein Ergebnis.")
    solver.printBoard(board)

    return reStart()


def reStart():
    userInput = input("\nMöchtest du den Sudoku-Solver Neustarten? [y|n]: ")
    if userInput.lower() == "y":
        main()


main()
