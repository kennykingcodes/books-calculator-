# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 20:40:15 2021

@author: user
"""


while True:
    # welcome message
    print("Welcome")
    print("how long would it take you to finsih x amount of books in your life time")


    # User Inputs 
    b = (float(input("Number of books you plan to read per year: ")))
    n = (float(input("Number of number of books you want to read in your lifetime: ")))
    m = float(1) #year

    # Formula
    a = (float((m * (n)) / b))

    # Solution
    print("ANSWER : It would take you " + str(a) + "years to finish "  + str(n) + " number of books")
    print("Thank you")
    
    
        # check if user wants another calculation
        # break the while loop if answer is no
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break 
    
    




