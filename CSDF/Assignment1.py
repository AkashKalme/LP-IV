#                       Assignment No.: 1
# 1. Write a program for Tracking Emails and Investigating Email Crimes.
# i.e. Write a program to analyze e–mail header.

import re


def matchre(data, *args):
    for regstr in args:
        matchObj = re.search(regstr + '.*', data, re.M | re.I)
        if matchObj:
            print(matchObj.group(0).lstrip().rstrip())
        else:
            print("No ", regstr, "found")


filename = input("Enter the path for email header file:")
fo = open(filename, "r")
data = fo.read()
matchre(data, "MIME-version", "Date:", "Subject:",
        "Delivered-to:", "From:", "^to:")
fo.close()
