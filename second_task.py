import re

def generator_numbers(text: str):
    try:
        
        pattern = r'(?<=\s)\d+\.\d{2}(?=\s)'
        match = re.findall(pattern, text)
        for i in match:
            yield float(i)
            
    except:
        return 0
    
def sum_profit(text, func):
    try:
        generator = func(text)
        general_salary = 0.00
        for i in generator:
            general_salary += i
        return general_salary
    except:
        return 0

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
    