#!/usr/bin/env python
# -*- coding: utf8 -*-

from xml.dom import minidom
import time

def show_test_results(testpath):
    
    print"""
    ********************************
         DISPLAY OF TEST RESULTS
    ********************************
    """
    prompt = """
    Enter the date of the test call
    in format 'Month-Day-Year' (American Format)'
    """
    test_date = raw_input (prompt)
    test_run_file = testpath + test_date + ".xml"
    
    # Get nodes from XML document
    try:
        test_run = minidom.parse(test_run_file)
    except:
        print "\n\tProblem with opening the test results file!\n"
        raw_input("Press [Enter]:  ")
        return
        
    test_result_node = test_run.childNodes[0]
    test_firstname_node = test_result_node.childNodes[1]
    test_lastname_node = test_result_node.childNodes[3]
    test_prime_node = test_result_node.childNodes[5]
    test_passed_node = test_result_node.childNodes[7]
    test_failed_node = test_result_node.childNodes[9]
    test_error_node = test_result_node.childNodes[11]
    
    # Get text from relevant nodes
    test_firstname_result = test_firstname_node.firstChild.data
    test_lastname_result = test_lastname_node.firstChild.data
    test_prime_result = test_prime_node.firstChild.data
    test_passed_result = test_passed_node.firstChild.data
    test_failed_result = test_failed_node.firstChild.data
    test_error_result = test_error_node.firstChild.data
    
    # Produce result to screen
    print """
    ********************************
       RESULTS OF TESTING %s
    ********************************
    Name Test - %s
    Surname Test - %s
    The first number test - %s
    ********************************
    Number of tests completed successfully:  %s
    Number of failed tests:  %s
    Number of tests completed with an error:  %s
    """ % (test_date, test_firstname_result, test_lastname_result,
           test_prime_result, test_passed_result, test_failed_result,
           test_error_result)

    raw_input("Press [Enter]:  ")
