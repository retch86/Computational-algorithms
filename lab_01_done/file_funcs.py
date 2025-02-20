from Point_class import Point


def readTable(name):
    pointTable = []
    file = open(name)
    for line in file.readlines():
        row = list(map(float, line.split(" ")))
        pointTable.append(Point(row[0], row[1], row[2]))
    file.close()
    return pointTable

def printTable(pointTable):
    print("┌───────┬────────────┬────────────┬────────────┐")
    print("│ {:^5s} │ {:^10s} │ {:^10s} │ {:^10s} │".format("№", "X", "Y", "Y\'"))
    print("├───────┼────────────┼────────────┼────────────┤")
    for i in range(len(pointTable)):
        print("│ {:^5d} │ {:^10.3f} │ {:^10.3f} │ {:^10.3f} │".format(i,
                                                            pointTable[i].x,
                                                            pointTable[i].y,
                                                            pointTable[i].derivative))
    print("└───────┴────────────┴────────────┴────────────┘")