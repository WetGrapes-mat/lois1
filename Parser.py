#########################################################################################
# Лабораторная работа 1 по дисциплине ЛОИС
# Выполнена студентом группы 021702
# БГУИР Дюбайло М.А.
# Вариант 2 - Проверить, является ли строка формулой сокращенного языка логики высказываний
# 01.03.2023

class Parser:
    def parse_formula(self, str_formula):
        unary_formula = self.parse_unary_formula(str_formula)
        if unary_formula:
            return unary_formula
        atomic_formula = self.parse_atomic_formula(str_formula)
        if atomic_formula:
            return atomic_formula
        binary_formula = self.parse_binary_formula(str_formula)
        if binary_formula:
            return binary_formula
        logic_constant = self.parse_logic_constant(str_formula)
        if logic_constant:
            return logic_constant
        return None

    def parse_binary_formula(self, str_formula):
        if len(str_formula) > 4 and str_formula[0] == '(' and str_formula[-1] == ')':
            position = 2
            brackets = 0
            if str_formula[1] == '(':
                brackets += 1
            while position < len(str_formula) - 1 and brackets != 0:
                if str_formula[position] == '(':
                    brackets += 1
                elif str_formula[position] == ')':
                    brackets -= 1
                position += 1
            if brackets != 0:
                return None
            left = None
            right = None
            if position > len(str_formula) - 3:
                return None
            operation = str_formula[position:position + 2]
            if operation == '\\/' or operation == '/\\' or operation == '->':
                left = self.parse_formula(str_formula[1:position])
                right = self.parse_formula(str_formula[position + 2:-1])
            elif str_formula[position] == '~':
                left = self.parse_formula(str_formula[1:position])
                right = self.parse_formula(str_formula[position + 1:-1])
            if not right or not left:
                return None
            if str_formula[position] in ['~', '-', '\\', '/']:
                return str_formula
        return None

    def parse_atomic_formula(self, str_formula):
        if str_formula.isupper() and str_formula.isalpha():
            return str_formula[0]
        return None

    def parse_logic_constant(self, str_formula):
        if str_formula == '1' or str_formula == '0':
            return str_formula
        return None

    def parse_unary_formula(self, str_formula):
        if len(str_formula) > 3 and str_formula[0] == '(' and str_formula[1] == '!' and str_formula[-1] == ')':
            negative = self.parse_formula(str_formula[2:-1])
            if negative:
                return str_formula
        return None


if __name__ == '__main__':
    p = Parser()
    print(p.parse_formula(''))
