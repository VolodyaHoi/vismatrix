# Visual Matrix
# Author: VolodyaHoi
# Version: 0.4
# Check README.md !

from multipledispatch import dispatch

class VisualMatrix():

    table = [] 
    length = []
    current_length = -1
    current_max = -1
    no_header = True
    matrix = []

    @staticmethod
    def addHeader(header):
        if VisualMatrix.no_header != False:
            VisualMatrix.table.insert(0, header)
            VisualMatrix.no_header = False
        

    @staticmethod
    def addRow(row):
        VisualMatrix.table.append(row)

    @dispatch(list, list)
    def setMatrix(user_matrix, header):
        
        if VisualMatrix.no_header == True:
            for i in range(0, len(user_matrix)):
                VisualMatrix.matrix.append(user_matrix[i])
            VisualMatrix.matrix.insert(0, header)
            VisualMatrix.table = VisualMatrix.matrix
            VisualMatrix.no_header = False
    
    @dispatch(list)
    def setMatrix(user_matrix):
        VisualMatrix.table = user_matrix

    @staticmethod
    def clear():
        VisualMatrix.table = [] 
        VisualMatrix.length = []
        VisualMatrix.current_length = -1
        VisualMatrix.current_max = -1
        VisualMatrix.no_header = True
        VisualMatrix.matrix = []

    @staticmethod
    def myMatrix():
        try:
            for i in range(0, len(VisualMatrix.table)):
                for j in range(0, len(VisualMatrix.table[0])):
                    if len(VisualMatrix.table[i][j]) > VisualMatrix.current_length:
                        VisualMatrix.current_length = len(VisualMatrix.table[i][j])
                VisualMatrix.length.append(VisualMatrix.current_length)
                VisualMatrix.current_length = -1

            
            for i in range(0, len(VisualMatrix.length)):
                if VisualMatrix.current_max < VisualMatrix.length[i]:
                    VisualMatrix.current_max = VisualMatrix.length[i]

            if VisualMatrix.current_max % 2 != 0:
                VisualMatrix.current_max = VisualMatrix.current_max + 1

            if VisualMatrix.no_header == False:

                for i in range(0, len(VisualMatrix.table[0])):    
                    print("+-" + "-" * VisualMatrix.current_max + "-", end="")
                    
                print("+")

            for i in range(0, len(VisualMatrix.table)):
                if VisualMatrix.no_header == True:
                    for j in range(0, len(VisualMatrix.table[0])):

                        if j == 0:
                            print("+-" + "-" * VisualMatrix.current_max + "-+", end="")
                        else:
                            print("-" + "-" * VisualMatrix.current_max + "-+", end="")
                        

                    print("")

                for j in range(0, len(VisualMatrix.table[0])):
                    if j == 0:
                        if VisualMatrix.current_max != len(VisualMatrix.table[i][j]):
                            if len(VisualMatrix.table[i][j]) % 2 == 0:
                                difChar = int((VisualMatrix.current_max - len(VisualMatrix.table[i][j])) / 2)
                                print("| " + " " * difChar + VisualMatrix.table[i][j] + " " * difChar + " |", end="")
                            else:
                                difChar = int((VisualMatrix.current_max - len(VisualMatrix.table[i][j])) / 2)
                                print("| " + " " + " " * difChar + VisualMatrix.table[i][j]  + " " * difChar + " |", end="")
                        else: 
                            if len(VisualMatrix.table[i][j]) % 2 == 0:
                                print("| " + VisualMatrix.table[i][j] + " |", end="")
                            else:
                                print("|  " + VisualMatrix.table[i][j] + " |", end="")
                    else:
                        if VisualMatrix.current_max != len(VisualMatrix.table[i][j]):
                            if len(VisualMatrix.table[i][j]) % 2 == 0:
                                difChar = int((VisualMatrix.current_max - len(VisualMatrix.table[i][j])) / 2)
                                print(" " + " " * difChar + VisualMatrix.table[i][j] + " " * difChar + " |", end="")
                            else:
                                difChar = int((VisualMatrix.current_max - len(VisualMatrix.table[i][j])) / 2)
                                print(" " + " " + " " * difChar + VisualMatrix.table[i][j]  + " " * difChar + " |", end="")
                        else: 
                            if len(VisualMatrix.table[i][j]) % 2 == 0:
                                print(" " + VisualMatrix.table[i][j] + " |", end="")
                            else:
                                print("  " + VisualMatrix.table[i][j] + " |", end="")
            
                print("")
                if VisualMatrix.no_header == False:
                    if i == 0:
                        for i in range(0, len(VisualMatrix.table[0])):    
                            print("+-" + "-" * VisualMatrix.current_max + "-", end="")
                        
                        print("+")

            for i in range(0, len(VisualMatrix.table[0])):    
                print("+-" + "-" * VisualMatrix.current_max + "-", end="")
                
            print("+")
            VisualMatrix.clear()
        except:            
            print("Module [Visual Matrix] send error! Check your code on errors.")
