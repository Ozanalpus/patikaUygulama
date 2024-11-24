points = ((3,4),(6,8),(9,12))
distances = []
distancevalue = 0
mindistance = float('inf')

def euclideanDistance():
    global mindistance
    for oklid in points:
        distancevalue = ((oklid[0] * oklid[0]) + (oklid[1] * oklid[1])) ** 0.5
        distances.append(distancevalue)
    for dist in distances:
        if dist < mindistance:
            mindistance = dist

euclideanDistance()

print("En düşük değer: " + str(mindistance))
