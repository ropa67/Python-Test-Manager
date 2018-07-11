# -*- coding: 852 -*-
import datetime, math


def test_firstname(fname):
    fname_input = raw_input("\tEnter your name: ")
    if fname_input == fname:
        return "SUCCESS"
    else:
        return "FAILUER - EXPECTED " + fname + " RECEIVED " + fname_input


def test_lastname(lname):

    lname_input = raw_input("\tEnter your surname: ")
    if lname_input == lname:
        return "SUCCESS"
    else:
        return "FAILUER - EXPECTED " + lname + " RECEIVED " + lname_input


def test_prime_number():
    try:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        num = raw_input("\tPrime Number Test - Enter the number from 1 to 99: ")
        number = int(num)
    except:
        print "\n\t Problem with a prime number. Enter correct number!\n"
        return test_prime_number()

    if number in primes:
        return "SUCCESS"
    else:
        return "FAILUER - " + str(number) + " is't the first number in the range from 1 to 99"


def run_tests(testpath):
    def testcount(test_results):
    # test results
        tests_passed = 0
        tests_failed = 0
        tests_error = 0
        for test_result in test_results:
            if test_result == "SUCCESS":
                tests_passed += 1
            elif test_result.startswith("FAILUER"):
                tests_failed += 1
            else:
                tests_error += 1
        results = [tests_passed, tests_failed, tests_error]
        return results

    # Run tests
    print """
    ********************************
             CALLING TESTS
    ********************************
    """
    result_firstname = test_firstname("Kamil")
    result_lastname = test_lastname("Ropski")
    result_prime_number = test_prime_number()
    total_results = [result_firstname, result_lastname, result_prime_number]
    results = testcount(total_results)

    # Output test results to screen
    print """
    ********************************
        RESULTS OF START  TEST
    ********************************
    Name Test - %s
    Surname Test - %s
    Prime Number Test - %s
    ********************************
    Number of tests completed successfully:  %s
    Number of failed tests:  %s
    Number of tests completed with an error:  %s
    """ % (result_firstname, result_lastname, result_prime_number, results[0], results[1], results[2])

    # data storage template XML
    test_output_xml = """<testresult>
    <testfirstname>%s</testfirstname>
    <testlastname>%s</testlastname>
    <testprimenumber>%s</testprimenumber>
    <testspassed>%i</testspassed>
    <testsfailed>%i</testsfailed>
    <testserror>%i</testserror>
    </testresult>""" % (result_firstname, result_lastname, result_prime_number, results[0], results[1], results[2])

    today = datetime.datetime.now().strftime("%m-%d-%Y")
    output_filename = testpath + today + ".xml"
    try:
        # open, save and close xml with a data.
        test_output = open(output_filename, "w")
        test_output.write(test_output_xml)
        test_output.close()
    except:
        print("Problem with a saveing to a file!")
    raw_input("Press [Enter]:  ")



