# -*- coding: utf8 -*-
import os, sys
import test_run, test_list, test_results, test_html

if sys.executable.find("exe") != -1:
    clearscreen = "cls"
    testpath = ".\\test_runs\\"
else:
    clearscreen = "clear"
    testpath = "./test_runs/"


# Main Menu
def menu():
    os.system(clearscreen)  # clear a screen
    print"""
    
    ********************************
        TEST MANAGEMENT SYSTEM
    ********************************
    1 - Start tests
    2 - List of test starts
    3 - Displaying test results
    4 - Save test report in HTML format
    5 - Help
    6 - End
    ********************************
    """
    choice = raw_input("Enter the option number and press [Enter]:  ")
    return choice


# Take the choice and launch module   -   The while loops to which the number is assigned
choice = ""
while choice != "6":
    choice = menu()
    if choice == "1":
        os.system(clearscreen)
        test_run.run_tests(testpath)
    elif choice == "2":
        os.system(clearscreen)
        test_list.list_tests()
    elif choice == "3":
        os.system(clearscreen)
        test_results.show_test_results(testpath)
    elif choice == "4":
        os.system(clearscreen)
        test_html.test_html_report(testpath)
    elif choice == "5":
        os.system(clearscreen)
        print"""
    ********************************
        TEST MANAGEMENT SYSTEM
    ********************************
   
    Welcome to the test management system.
    This program is used to run tests and display
    test results on the screen in HTML format.
        """
        raw_input("Press [Enter]:  ")
