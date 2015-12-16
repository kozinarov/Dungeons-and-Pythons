class Dungeons:

    def __init__(self, filename):
        self._filename = filename
        self._list_of_lists = []

    def read_file(self):
        with open(self._filename, 'r') as data:
            self._list_of_lists = [list(line) for line in data]

    def print_map(self):
        s = ''
        d = self._list_of_lists
        for elem in d:
            s += ''.join(elem)
        return s

    def solve(self):
        
        for i in range(0, len(self._list_of_lists[0])):
            pass

