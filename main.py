from Parser import Parser


def read_from_file():
    with open('formulas.txt', 'r') as f:
        formulas = f.read().splitlines()
    return formulas


def test_mode():
    global parser
    count = 0
    formulas = read_from_file()
    for i in formulas:
        print('-' * 20)
        print('y - Yes | n - No')
        print(f'Is the formula: {i} ?')
        answer = input()
        formula = parser.parse_formula(i)
        if (answer == 'y' and formula) or (answer == 'n' and not formula):
            print('Correctly')
            count += 1
        else:
            print('Wrong')
    else:
        print('-' * 20)
        print(f'Your result {count}/{len(formulas)}')
        print('-' * 20)


def check_mode():
    global parser
    formula = input('Enter the formula to check: ')
    print(formula)
    answer = parser.parse_formula(formula.rstrip())
    if answer:
        print('The entered formula is correct')
    else:
        print('The entered formula is NOT correct')


parser = Parser()

if __name__ == '__main__':
    while True:
        print('Select mode\n1 - test mode\n2 - check mode\n0 - exit ')
        choice = input()
        match choice:
            case '1':
                test_mode()
            case '2':
                check_mode()
                print('-'*20)
            case '0':
                break
            case _:
                print('Input Error')
