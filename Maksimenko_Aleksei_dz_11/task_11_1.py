class Date:

    def __init__(self, day_month_year):

        self.day_month_year = day_month_year
        data = self.set_name(day_month_year)
        self.date_validation(data)

    @classmethod
    def set_name(cls, day_month_year):
        b = day_month_year.split('-')
        try:
            date_edit = [int(b[i]) for i in range(len(b))]
            print(type(date_edit))
            print(date_edit)
            return date_edit
        except ValueError:
            print('only numbers')
            exit()

    @staticmethod
    def date_validation(data):
        print(type(data))
        print(data)
        if 0 <= data[0] > 31:
            print('wrong index for day')
            exit()
        elif 0 <= data[1] > 12:
            print('wrong index for month')
            exit()
        print(f'day: {data[0]}, month: {data[1]}, year: {data[2]}')


a = Date('10-12-2021')
