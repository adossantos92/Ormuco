class Version:
    def __init__(self, version_number):
        self.value = version_number

    def compare(self, version_to_compare):
        for value1, value2 in zip(self.value.split('.'), version_to_compare.value.split('.')):
            value1, value2 = self.format_numbers(value1, value2)
            if value1 > value2:
                return 1
            elif value1 < value2:
                return -1
        return 0

    def __eq__(self, other):
        return self.compare(other) == 0

    def __lt__(self, other):
        return self.compare(other) < 0

    def __le__(self, other):
        return self.compare(other) <= 0

    @staticmethod
    def format_numbers(n1, n2):
        if len(n1) > len(n2):
            n2 = n2.ljust(len(n1), '0')
        elif len(n2) > len(n1):
            n1 = n1.ljust(len(n2), '0')
        return int(n1), int(n2)
