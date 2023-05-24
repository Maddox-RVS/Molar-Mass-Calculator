elements = {
    "H": 1.008,
    "Li": 6.941,
    "Be": 9.012,
    "Na": 22.99,
    "Mg": 24.31,
    "K": 39.10,
    "Ca": 40.08,
    "Rb": 85.47,
    "Sr": 87.62,
    "Cs": 132.91,
    "Ba": 137.33,
    "Fr": 223,
    "Ra": 226,
    "Sc": 44.96,
    "Ti": 47.87,
    "V": 50.94,
    "Cr": 52.00,
    "Mn": 54.94,
    "Fe": 55.85,
    "Co": 58.93,
    "Ni": 58.69,
    "Cu": 63.55,
    "Zn": 65.41,
    "Y": 88.91,
    "Zr": 91.22,
    "Nb": 92.91,
    "Mo": 95.94,
    "Tc": 98,
    "Ru": 101.07,
    "Rh": 102.91,
    "Pd": 106.42,
    "Ag": 107.87,
    "Cd": 112.41,
    "Lu": 174.97,
    "Hf": 178.49,
    "Ta": 180.95,
    "W": 183.84,
    "Re": 186.21,
    "Os": 190.23,
    "Ir": 192.22,
    "Pt": 195.08,
    "Au": 196.97,
    "Hg": 200.59,
    "Lr": 262,
    "Rf": 267,
    "Db": 268,
    "Sg": 271,
    "Bh": 267,
    "Hs": 269,
    "Mt": 276,
    "Ds": 281,
    "Rg": 280,
    "B": 10.82,
    "C": 12.01,
    "N": 14.01,
    "O": 16.00,
    "F": 19.00,
    "Ne": 20.18,
    "Al": 26.98,
    "Si": 28.09,
    "P": 30.97,
    "S": 32.07,
    "Cl": 35.45,
    "Ar": 39.95,
    "Ga": 69.72,
    "Ge": 72.64,
    "As": 74.92,
    "Se": 78.96,
    "Br": 79.90,
    "Kr": 83.80,
    "In": 114.82,
    "Sn": 118.71,
    "Sb": 121.76,
    "Te": 127.60,
    "I": 126.90,
    "Xe": 131.29,
    "Tl": 204.38,
    "Pb": 207.2,
    "Bi": 208.98,
    "Po": 209,
    "At": 210,
    "Rn": 222,
    "La": 138.91,
    "Ce": 140.12,
    "Pr": 140.91,
    "Nd": 144.24,
    "Pm": 145,
    "Sm": 150.36,
    "Eu": 151.96,
    "Gd": 157.25,
    "Tb": 158.93,
    "Dy": 162.50,
    "Ho": 164.93,
    "Er": 167.26,
    "Tm": 168.93,
    "Yb": 173.04,
    "Ac": 227,
    "Th": 232.04,
    "Pa": 231.04,
    "U": 238.03,
    "Np": 237,
    "Pu": 244,
    "Am": 243,
    "Cm": 247,
    "Bk": 247,
    "Cf": 251,
    "Es": 252,
    "Fm": 257,
    "Md": 258,
    "No": 259,
    "He": 4.003
}


def Contains(str, str_check):
    for i in range(0, len(str)):
        if (str[i] == str_check):
            return True
    return False


def List_Contains_Parenthesis(list, str):
    for i in range(0, len(list)):
        if (Contains(list[i], str)):
            return True
    return False


def List_Contains_Digit(list):
    for term in list:
        for i in range(0, len(term)):
            if (term[i].isdigit()):
                return True
    return False


def Multiply(multiplyer, terms):
    new_terms = []
    for i in range(0, int(multiplyer)):
        for term in terms:
            new_terms.append(term)
    return new_terms


def Has_Numbers(str):
    for i in range(0, len(str)):
        if (str[i].isdigit()):
            return True
    return False


def Split_Elements(str):
    terms = []
    term = ""
    number_of_caps = 0
    number_of_openening_parenthesis = 0
    number_of_closing_parenthesis = 0
    in_parenthesis = False

    temp = ""
    for i in range(0, len(str)):
        if (str[i].isdigit()):
            temp += str[i]
        else:
            terms.append(temp)
            str = str[len(temp):len(str)]
            break

    for i in range(0, len(str)):
        if (str[i] == "("):
            number_of_openening_parenthesis += 1
            if (number_of_openening_parenthesis == 1):
                if (i != 0):
                    terms.append(term)
                term = ""
                number_of_caps = 1
                in_parenthesis = True
        elif (str[i] == ")"):
            number_of_closing_parenthesis += 1
        if (in_parenthesis == False):
            if (str[i].isupper()):
                number_of_caps += 1
            if (number_of_caps == 2):
                terms.append(term)
                term = ""
                number_of_caps = 1
        if (number_of_openening_parenthesis == number_of_closing_parenthesis):
            in_parenthesis = False
        term += str[i]
    else:
        terms.append(term)
        term = ""
    return terms


def Split_Isolated_Term(str):
    beginning_multiplyer = ""
    term = ""
    ending_multiplyer = ""

    if (Has_Numbers(str)):
        for i in range(0, len(str)):
            if (str[i].isdigit()):
                beginning_multiplyer += str[i]
            else:
                str = str[len(beginning_multiplyer):len(str)]
                break

        for i in range(0, len(str)):
            if (str[i].isalpha()):
                term += str[i]
            else:
                str = str[len(term):len(str)]
                if (str.isdigit() == False):
                    str = "1"
                if (beginning_multiplyer == ""):
                    beginning_multiplyer = "1"
                break

        ending_multiplyer = str
        total_terms = int(beginning_multiplyer) * int(ending_multiplyer)
        temp = []

        for i in range(0, total_terms):
            temp.append(term)
    else:
        temp = []
        temp.append(str)

    return temp


def Split_Parenthesis_Term(str):
    multiplyer = ""
    temp = []
    for i in reversed(range(len(str))):
        if (str[i].isdigit()):
            multiplyer += str[i]
        else:
            if (multiplyer == ""):
                multiplyer = "1"
            str = str[1:i]
            break

    temp_terms = Split_Elements(str)
    new_terms = []
    for i in range(1, len(temp_terms)):
        new_terms.append(temp_terms[i])

    for i in range(0, int(multiplyer)):
        for term in new_terms:
            temp.append(term)
    return temp


def Simplify(formula, start, end):
    new_formula = []
    for i in range(start, end):
        if (Contains(formula[i], "(") == False):
            temp = Split_Isolated_Term(formula[i])
            for term in temp:
                new_formula.append(term)
        else:
            temp_par = Split_Parenthesis_Term(formula[i])
            for term in temp_par:
                new_formula.append(term)
    return new_formula


input_ = input("Enter a chemical formula: ")
formula = ""

for i in range(0, len(input_)):
    if (input_[i] != " "):
        formula += input_[i]

terms = Split_Elements(formula)
if (terms[0] == ""):
    terms[0] = "1"

new_formula = []

new_formula = Simplify(terms, 1, len(terms))

while (List_Contains_Parenthesis(new_formula, "(") or List_Contains_Digit(new_formula)):
    new_formula = Simplify(new_formula, 0, len(new_formula))

new_formula = Multiply(terms[0], new_formula)

molar_mass = 0

try:
    for term in new_formula:
        molar_mass += elements[term]
    print(molar_mass)
except:
    print("INVALID SYNTAX ERROR!")
