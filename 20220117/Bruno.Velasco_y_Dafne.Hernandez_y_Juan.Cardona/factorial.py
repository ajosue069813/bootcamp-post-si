#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Factorial
"""
from operaciones import factorial

def main():
    """
    Los wafles son hotcakes musculosos
    """
    n = int(input("Ingrese un numero para factorial:\n "))
    res = factorial(n)
    print(f"El factorial del numero ingresado es: {factorial(n)}\n")



if __name__ == "__main__":
    main()
