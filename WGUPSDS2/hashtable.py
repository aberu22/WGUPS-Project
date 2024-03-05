class HashMap:
    def __init__(self, size=20):
        # Create a list of empty buckets with the specified initial capacity.
        #Adibi, Yasaman. Zybooks, learn.zybooks.com/zybook/WGUC950Template2023/chapter/6/section/1. Accessed 3 Mar. 2024. 
        self.size = size
        self.list = [[] for _ in range(size)]

    def insert(self, key, value):
        # Calculate index table where the key-value pair should be inserted.
        index = hash(key) % self.size
        Table_list = self.list[index]

        # Check if the key already exists in the table. if it does need to update value.
        for kv in Table_list:
            if kv[0] == key:
                kv[1] = value
                return True

        # If the key doesn't exist, append the key-value pair to the table .
        Table_list.append([key, value])
        return True

    def lookup(self, key):
        # Calculate the table  where the key should be located.
        index = hash(key) % self.size
        Table_list = self.list[index]

        # Check if the key exists in the table list.
        for kv in Table_list:
            if kv[0] == key:
                return True

        # If the key is not found, return False.
        return False

    def remove(self, key):
        # Calculate the table index where the key-value pair should be inserted.
        index = hash(key) % self.size
        Table_list = self.list[index]

        # Iterate over the key-value pairs in the bucket and delete the pair if the key matches.
        for i, kv in enumerate(Table_list):
            if kv[0] == key:
                del Table_list[i]
                return True  # Return True if removal is successful

        return False  # Return False if the key is not found

 
    
    def get(self, key):
        # Calculate the bucket where the key-value pair should be located.
        index = hash(key) % self.size
        Table_list = self.list[index]

        # Search the bucket for the specified key and return the corresponding value.
        for kv in Table_list:
            if kv[0] == key:
                return kv[1]

        # If the key is not found, return None.
        return None

    




