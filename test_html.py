#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
from xml.dom import minidom

def test_html_report(testpath):
    print"""
    ********************************
        CREATING AN HTML REPORT
    ********************************
    """
    prompt = """
    Enter the date of the test call
    in format 'Month-Day-Year' (American Format)'
    """
    test_date = raw_input (prompt)

    test_run_file = testpath + test_date + ".xml"

    # Reading nodes from an XML file
    try:
        test_run = minidom.parse(test_run_file)
    except:
        print "\n\tError opening call results!\n"
        raw_input("Press [Enter]:  ")
        return
    test_result_node = test_run.childNodes[0]
    test_firstname_node = test_result_node.childNodes[1]
    test_lastname_node = test_result_node.childNodes[3]
    test_prime_node = test_result_node.childNodes[5]
    test_passed_node = test_result_node.childNodes[7]
    test_failed_node = test_result_node.childNodes[9]
    test_error_node = test_result_node.childNodes[11]
    
    # Read text from nodes
    test_firstname_result = test_firstname_node.firstChild.data
    test_lastname_result = test_lastname_node.firstChild.data
    test_prime_result = test_prime_node.firstChild.data
    test_passed_result = test_passed_node.firstChild.data
    test_failed_result = test_failed_node.firstChild.data
    test_error_result = test_error_node.firstChild.data
    
    # Save results to html
    html_output = u"""
    <HTML>
    <TITLE>Test Raports - %s</TITLE>
    <HR>
    <H1>RESULTS OF RECORDING TESTS %s</H1>
    <HR>
    <BODY>
    Name Test - %s<br>
    Surname Test - %s<br>
    Prime Number Test - %s<br>
    <HR>
    Number of tests completed successfully:  %s<br>
    Number of failed tests:  %s<br>
    Number of tests completed with an error:  %s<br>
    </BODY>
    </HTML>
    """ % (test_date, test_date, test_firstname_result, test_lastname_result, \
    test_prime_result, test_passed_result, test_failed_result, test_error_result)
    
    filename = os.path.join(os.curdir, 'test_report_html', test_date + ".html")
    output_file = open(filename, 'w')
    output_file.write(html_output.encode('utf8'))
    output_file.close()
    
    print "\n\t-- The HTML report generation has finished --"
    raw_input("\tPress [Enter]:  ")
    

    
