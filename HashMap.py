# Adapted from concepts introduced in C950, Webinar 1 (W-1_ChainingHashTable_zyBooks_Key-Value.py)

class HashMap:
    # Initializes a list to serve as the internal storage of the hash map.
    # Big O Time Complexity: O(n) The constructor iterates over the range of the capacity to append an empty list
    # to the hashMap for each slot, directly proportional to the capacity value.
    # Big O Space Complexity: O(n) The initial size of the hashMap list is directly proportional to the capacity,
    # with each slot initialized as an empty list.
    def __init__(self, capacity=10):
        self.hashMap = []
        for i in range(capacity):  # Populates the hashMap with empty lists for chaining.
            self.hashMap.append([])

    # Inserts a new package record or updates an existing one based on the package ID.
    # Big O Time Complexity: O(n) in the worst case, where n is the number of records in a single chain.
    # This occurs when multiple package IDs hash to the same index, requiring iteration through the chain.
    # Big O Space Complexity: O(1) for inserting or updating a record, as the space required does not
    # scale with the number of records (excluding the internal list growth).
    def add(self, packageid, details):
        # Calculate the index for the packageID
        index = hash(packageid) % len(self.hashMap)
        chain = self.hashMap[index]

        # Check if packageID already exists and update details
        for record in chain:
            if record[0] == packageid:
                record[1] = details  # Update details if found.
                return True

        # If packageID is new, append its details to the chain
        chain.append([packageid, details])
        return True

    # Get the delivery details for a given packageID
    # Big O Time Complexity: O(n), due to potentially iterating through all records in a chain.
    # Big O Space Complexity: O(1), as retrieving a record does not require additional space.
    def get(self, packageid):
        index = hash(packageid) % len(self.hashMap)
        chain = self.hashMap[index]

        # Search for packageID in the chain
        for record in chain:
            if record[0] == packageid:
                return record[1]  # Return details if found.
        return None  # Return None if packageID not found

    # Removes a package record identified by the package ID
    # Big O Time Complexity: O(n), as it may need to iterate through the chain to find the package ID.
    # Big O Space Complexity: O(1), since deletion does not scale with the number of records.
    def delete(self, packageid):
        index = hash(packageid) % len(self.hashMap)
        chain = self.hashMap[index]

        # Iterate through the chain to find and remove the record.
        for record in chain:
            if record[0] == packageid:
                chain.remove([record[0], record[1]])
