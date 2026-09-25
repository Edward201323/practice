class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # stores key -> value, timetamp
        # we can have the timestamp as the index, but that array can get very long even if there is onyl one value 
        # best solution is to have a hashmap inside of a hashmap
        # when setting, search for key inside d, if it doesn't exist create a new dictionary
        # after that, insert (timestamp, value) into key's dictionary
        if key not in self.d:
            self.d[key] = {}
        
        self.d[key][timestamp] = value
        
         

    def get(self, key: str, timestamp: int) -> str:
        # search inside d for key, then inside d[key] for timestamp
        if key in self.d and timestamp in self.d[key]:
            return self.d[key][timestamp]
        if key in self.d:
            while timestamp > 0:
                timestamp -= 1
                if timestamp in self.d[key]:
                    return self.d[key][timestamp]

        return ""
