

annual_interest_rates = 4.2/100
deposit_time_month = 24
monthly_deposit_money = 4000


class AmountOfTime(object):
    time_type_multiple = {'year': 12 * 30 * 24 * 60, 'month': 30 * 24 * 60, 'day': 24 * 60, 'hour': 60, 'second': 1}

    def __init__(self, amount, time_type):
        self.type = time_type
        self.amount = amount
        self.value = self.time_type_multiple.get(time_type) * amount

    def get_time(self, time_type):
        return self.value/self.time_type_multiple.get(time_type)


def get_each_month_interest(interest_rates, time, money):
    interest_list = []
    interest_rates = interest_rates/12
    for i in range(int(time.get_time('month'))):
        interest_list.append(interest_rates * money * (i + 1))
    return interest_list


def get_interest(interest_rates, time, money):
    return sum(get_each_month_interest(interest_rates, time, money))


def get_principal_and_interest(interest_rates, time, money):
    principal = time.get_time('month') * money
    return get_interest(interest_rates, time, money) + principal


if __name__ == '__main__':
    # 不考虑复利的情况
    moneys = get_interest(annual_interest_rates, AmountOfTime(360, 'month'), monthly_deposit_money)
    print(moneys)
    print(360 * 4000)
    # 考虑复利的情况
    # todo

