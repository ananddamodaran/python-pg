#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pgm no : 09
Created on Tue Jun 21 21:13:18 2022
Title: Print the digits of a two digit
        integer using input()
@author: anand.dev
"""

number = int(input('Enter two digit number: ?'))

ones = number % 10
tens = number // 10

print('Ones: ', ones, 'Tens: ', tens)
