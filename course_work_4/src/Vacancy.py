class Vacancy:
    def __init__(self, name, url, sal_from, sal_to, requirement):
        self.name = name
        self.url = url
        self.sal_from = sal_from
        self.sal_to = sal_to
        self.requirement = requirement

    def __str__(self):
        return f'{self.name}, {self.url}, {self.sal_from}, {self.sal_to}, {self.requirement}'
