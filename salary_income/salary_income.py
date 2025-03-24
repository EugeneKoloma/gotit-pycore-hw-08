import re
from decimal import Decimal
from typing import Callable, Iterator

digits_pattern = r"\d+\.\d{2}"

def generator_numbers(txt: str):
    parsed_txt = re.findall(digits_pattern, txt)
    for number in parsed_txt:
        yield Decimal(number).quantize(Decimal('0.01'))

def sum_profit(txt: str, gen_numbers: Callable[[str], Iterator[Decimal]]) -> Decimal:
    return sum(gen_numbers(txt), Decimal('0.00'))

if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)

    assert total_income == Decimal('1351.46')