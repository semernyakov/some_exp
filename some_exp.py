# connect to the database
import sqlite3

# create empty list
list_of_rows = []

try:
    conn = sqlite3.connect('domains.db')
    print("Connected to database successfully")

    # select all the data from the table domains and print it
    cursor = conn.execute("SELECT * FROM domains")
    print("Printing all the data from the table domains:")

    # append all the rows to the list
    for row in cursor:
        list_of_rows.append(row)

    # print the list
    #print(list_of_rows)

except sqlite3.Error as e:
    print(e,  e.args, "Db connection error")
    raise Exception("Could not connect to database")

finally:
    # close the connection
    conn.close()
    print("Closed database successfully")

# extract the domain name from the list_of_rows list
list_of_domains = list(map(lambda x: x[1], list_of_rows))

# print the list of domains
# print("Printing the list of domains:")
# print(list_of_domains)


# function for creating reg expression for the different domain name
def reg_expression(domain):
    # extract subdomains from the domain if the domain level is more than 2
    if len(domain.split('.')) > 2:
        # split the domain name by '.'
        subdomains = domain.split('.')
        print(subdomains)
        # create reg expression for the different subdomains
        list_of_subdomains = []
        for i in range(len(subdomains) - 2):
            reg_expression = f"^{subdomains[i]}\.{subdomains[i+2]}\."
            # return reg_expression for the different subdomains
            print(reg_expression)

            list_of_subdomains.append(reg_expression)
            print(list_of_subdomains)
        # return reg_expression for the different subdomains
        print(reg_expression)
        return reg_expression

domain = 'beff5a50-11b0-4508-afac-ce0876334d1d.static.developer.xxx.com'

reg_expression(domain)

# ===================================================================================
# function for validate url
import re


def validate_url(url):
    regex = '^(https|http|ftp|ftps)\:\/\/[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(\/\S*)?$'
    if re.search(regex, url):
        return True
    else:
        return False

#


import re

dm = 'beff5a50-11b0-4508-afac-ce0876334d1d.static.developer.xxx.com'

# generate re function for dm string
def reg_expression(dm):
    n = dm.split('.')
    digit, alpha = set(), set()

    for i in n[0]:
        if i.isdigit():
            digit.add(i)
        if i.isalpha():
           alpha.add(i)

    # sort digit and alpha sets
    alpha, digit = sorted(alpha), sorted(digit)

    regex = f"[{alpha[0]}-{alpha[-1]}{digit[0]}{digit[-1]}-]"
    print(regex)

    if re.search(regex, n[0]):
        print('True')
        return True
    else:
        print('False')
        return False

    return regex

reg_expression(dm)

# ===================================================================================

if len(n) == 3:
    return True
else:
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
if re.search(regex, dm):
    return True
else:
    return False
