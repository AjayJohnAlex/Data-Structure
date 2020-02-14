'''
Properties:
1.No duplicate value
2.Add, Get or Delete at BigO(1)
3.Its stored in key-value pairs
4.Can store any data type

Components:
1.Array => DS to store the data
2. Hash Function => Function to convert key into an array function.
3.Collision Handling => Multiple key-value pair in the same cell ; resolved by LikedList or use a list() to store each pair
'''


class Hashmap:

    def __init__(self):
        '''Creating a list with a definite size'''
        self.size = 6
        self.map = [None] * self.size

    def getHash(self, key):
        '''Getting the hash value for the data ; this here would give us the location in the list'''
        hash = 0
        for char in str(key):
            '''ord gets the numerical value of a single str'''
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        '''We fist get the location and
        1. If the list location is empty then simply add it
        2. Else if its not empty its checked if the key already exists and if its needs to be updated
        3. Else the new (key,value) is appended in the location
        '''
        key_hash = self.getHash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True

        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        ''' Getting the hash value from key and then searching the list with that value
        If the hash_value has data then it is checked if it matches with the key value ; it is checked for all key values
        Else if the hash_value doens't exist it throws a message '''
        key_hash = self.getHash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]

        else:
            return "Invalid Key"
        return True

    def delete(self, key):
        ''' Getting the hash value from key and then searching the list with that value
        If the hash_value has data then it is checks along the len of the data ; and searchs each data with the key and when the key is found; its removed from list.
        Else if the hash_value doens't exist it throws a message '''

        key_hash = self.getHash(key)

        if self.map[key_hash] is not None:
            for i in range(0, len(self.map[key_hash])):
                if self.map[key_hash][i][0] == key:
                    self.map[key_hash].pop(i)
                    return True
        else:
            return "Invalid Key"

    def printed(self):

        print("Your HashMap :  Phone Book \n")

        print(self.map, " Awesome \n")

        for item in self.map:
            if item is not None:
                print(str(item))


h = Hashmap()

h.add('Ajay', '987654321')
h.add('Vijay', '123456789')
h.add('Asha', '123456543')
h.add('Suja', '9573633829')
h.add('Alex', '846814645')
h.add('Anoop', '3814481968')
h.add('John', '3814481968')
h.add('Jibin', '5849861849')

h.printed()

h.delete('Vijay')

h.printed()
print("Anoop", h.get("Anoop"))
