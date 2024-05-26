class Vacancy:
    def __init__(self, name, url, sal_from, sal_to, requirement):
        self.name = name
        self.url = url
        self.sal_from = sal_from if sal_from else 0
        self.sal_to = sal_to if sal_to else 0
        self.requirement = requirement

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.url}, {self.sal_from}, {self.sal_to}, {self.requirement})'

    def __str__(self):
        return f'{self.name}, {self.url}, {self.sal_from}, {self.sal_to}, {self.requirement}'

    def __lt__(self, other):
        """
        Метод определяет является ли зарплата указанная в self меньше, чем в other
        """
        if self.sal_from is None and other.sal_from is None:
            if self.sal_to is None and other.sal_to is not None:
                return True
            elif self.sal_to is not None and other.sal_to is None:
                return True
            elif None not in [self.sal_to, other.sal_to]:
                return self.sal_to < other.sal_to
            elif self.sal_to is None and other.sal_to is None:
                return False
        elif self.sal_from is None and other.sal_from is not None:
            return True
        elif self.sal_from is not None and other.sal_from is None:
            return False
        elif self.sal_from == other.sal_from:
            return self.sal_to < other.sal_to
        else:
            return self.sal_from < other.sal_from

    def __gt__(self, other):
        """
        Метод определяет является ли зарплата указанная в self больше, чем в other
        """
        if self.sal_from is None and other.sal_from is None:
            if self.sal_to is None and other.sal_to is not None:
                return False
            elif self.sal_to is not None and other.sal_to is None:
                return True
            elif None not in [self.sal_to, other.sal_to]:
                return self.sal_to > other.sal_to
            elif self.sal_to is None and other.sal_to is None:
                return False
        elif self.sal_from is None and other.sal_from is not None:
            return False
        elif self.sal_from is not None and other.sal_from is None:
            return True
        elif self.sal_from == other.sal_from:
            return self.sal_to > other.sal_to
        else:
            return self.sal_from > other.sal_from

    def __eq__(self, other):
        """
        Метод проверяет равенство зарплат двух экземпляров класса
        """
        return self.sal_from == other.sal_from and self.sal_to == other.sal_to
