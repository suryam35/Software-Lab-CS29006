# In this python file, only the definitions for the magic functions and the basic operations
# for the question segments are provided. There may be the need to add new functions or overload 
# existing ones as per the question requirements.

class Vector:
        
    def __init__(self, *args): 

        # if arg is an int(dimension)
        if isinstance(args[0], int): 
            self._coords = [0]*args[0]
        else:
            self._coords = args[0]
        return

    def __len__(self):
        # return the dimension of the vector
        return len(self._coords)

    def __getitem__(self, j):
        # return the jth coordinate of the vector
        return self._coords[j]

    def __setitem__(self, j, val):
        # set the jth coordinate of vector to val
        self._coords[j] = val
        return

    def __add__(self, other):
        # u + v
        coordinates = []
        for i in range(len(self)):
            coordinates.append(self._coords[i] + other._coords[i])
        return Vector(coordinates)
            
    def __eq__(self, other):
        # return True if vector has same coordinates as other
        if self._coords == other._coords:
            return True
        else:
            return False
    
    def __ne__(self, other):
        # return True if vector differs from other
        if self._coords != other._coords:
            return True
        else:
            return False
    
    def __str__(self):
        # return the string representation of a vector within <>
        representation = "<"
        for coordinate in self._coords:
            representation = representation + str(coordinate) + "," 
        representation = representation[0:-1]
        representation = representation + ">"
        return representation

    def __sub__(self, other):
        # Soln for Qs. 2
        coordinates = []
        for i in range(len(self)):
            coordinates.append(self._coords[i] - other._coords[i])
        return Vector(coordinates)
    
    def __neg__(self):
        # Soln for Qs. 3
        coordinates = []
        for i in range(len(self)):
            coordinates.append(-self._coords[i])
        return Vector(coordinates)
    
    def __rmul__(self, value):
        return (self * value) 
    
    def __mul__(self, other):
        # Soln for Qs. 4, 5 and 6
        if isinstance(other,int):
            coordinates = [x*other for x in self._coords]
            return Vector(coordinates)
        else:
            dot_product = 0
            for i in range(len(self)):
                dot_product = dot_product + self._coords[i]*other._coords[i]
        return dot_product
    
def main():
    # v1 = Vector([3,6,7,4,5])
    # v2 = Vector (7)
    # v3 = Vector([1,2,3,4,5])
    # v4 = Vector([0,0,0,0,0])
    # print(v1)
    # print(v2)
    # print(v3)
    # print(len(v1))
    # print(v2 != v4)
    # print(v1 + v3)
    # print(v1 - v3)
    # print(-v3)
    # print(v3*3)
    # print(3*v3)
    # print(v1*v3)
    # print(v1[0])
    # v1[0] = 10
    # print(v1[0])
    v1 = Vector(5)
    # v2 = Vector (5)
    v2 = Vector([1,2,3,4,5])
    #print (v1)
    #print (v2)
    for i in range(5):
        v1[i] = 5
    #     v2[i] = i
    
    # v2=[5,8,1,6,2]
    print(v1)
    print(v2)

    print(v1*3)
    print(3*v2)
    print(v1*v2)
        # print (v1-v2)
        # print (v2-v1)

    # Add suitable print statements to display the results
    # of the different question segments
    return


if __name__ == '__main__':
    main()