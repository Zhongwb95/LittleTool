

class AmountOfTime(object):
    time_type_multiple = {'year': 12 * 30 * 24 * 60, 'month': 30 * 24 * 60, 'day': 24 * 60, 'hour': 60, 'second': 1}

    def __init__(self, amount, time_type):
        self.type = time_type
        self.amount = amount
        self.value = self.time_type_multiple.get(time_type) * amount

    def get_time(self, time_type):
        return self.value/self.time_type_multiple.get(time_type)


# 不考虑复利的情况
def get_each_month_interest(interest_rates, time, money):
    interest_list = []
    interest_rates = interest_rates/12
    for i in range(int(time.get_time('month'))):
        interest_list.append(interest_rates * money * (i + 1))
    return interest_list


def get_compound_interest(compound_interest_cycle, interest_list):
    interest = 0
    num = int(len(interest_list)/compound_interest_cycle) * compound_interest_cycle
    for i in range(num):
        interest += interest_list[i]
    return interest


# 考虑复利的情况
def get_each_month_interest_(interest_rates, time, money, cycle):
    interest_list = []
    interest_rates = interest_rates/12
    for i in range(int(time.get_time('month'))):
        interest = get_compound_interest(cycle, interest_list)
        interest_list.append(interest_rates * (money * (i + 1) + interest))
    return interest_list


def get_interest(interest_rates, time, money):
    return sum(get_each_month_interest(interest_rates, time, money))


def get_interest_(interest_rates, time, money, cycle):
    return sum(get_each_month_interest_(interest_rates, time, money, cycle))


def get_principal_and_interest(interest_rates, time, money):
    principal = time.get_time('month') * money
    return get_interest(interest_rates, time, money) + principal


def get_principal_and_interest_(interest_rates, time, money, cycle):
    principal = time.get_time('month') * money
    return get_interest_(interest_rates, time, money, cycle) + principal


if __name__ == '__main__':
    annual_interest_rates = 4.5 / 100
    month_ = 12
    cycles = 6
    monthly_deposit_money = 4100

    time_ = AmountOfTime(month_, 'month')

    # 不考虑复利的情况
    moneys = get_interest(annual_interest_rates, time_, monthly_deposit_money)
    print('收益 =', moneys)
    print('本利和 =', month_ * monthly_deposit_money + moneys)

    # 考虑复利的情况
    moneys = get_interest_(annual_interest_rates, time_, monthly_deposit_money, cycles)
    print('收益 =', moneys)
    print('本利和 =', month_ * monthly_deposit_money + moneys)

    # 哎！ 穷啊！
