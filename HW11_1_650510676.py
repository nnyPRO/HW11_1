#!/usr/bin/env python3
# เมษนี ลายเฮือง
# 650510676
# HW11_1
# 204203 Sec 002

# 0) ** Import pandas as pd.**
import pandas as pd
# 0) ** Read ./input.txt as a dataframe called sal.**
''' DO PART 0 FIRST '''
sal = pd.read_csv('input.txt')

# 1) ** then show the shape of the data frame


def q01():
    print("Q01")
    result = sal   # edit this

    print(result)   # Dont change this

# 2) ** Check the head of the DataFrame. **


def q02():
    print("Q02")
    result = sal.head()   # edit this

    print(result)   # Dont change this


# 3) ** Use the .info() method to find out how many entries there are.**


def q03():
    print("Q03")
    result = sal.info()   # edit this

    print(result)   # Dont change this

# 4) ** What is the average BasePay ?


def q04():
    print("Q04")
    result = sal['BasePay'].sum()/5   # edit this

    print(result)   # Dont change this


# 5) ** What is the highest amount of OvertimePay in the dataset ? **
def q05():
    print("Q05")
    result = sal['OvertimePay'].max()   # edit this

    print(result)   # Dont change this


# 6) ** What is the job title of JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **
def q06():
    print("Q06")
    result = None   # edit this

    print(result)   # Dont change this


# 7) ** How much does JOSEPH DRISCOLL make (including benefits)? **
def q07():
    print("Q07")
    result = None   # edit this

    print(result)   # Dont change this


# 8) ** What is the name of highest paid person (including benefits)?**
# ['EmployeeName'])
def q08():
    print("Q08")
    result = None   # edit this

    print(result)   # Dont change this


# 9) ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**
def q09():
    print("Q09")
    result = None   # edit this

    print(result)   # Dont change this


# 10) ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **
def q10():
    print("Q10")
    result = None   # edit this

    print(result)   # Dont change this


# 11) ** How many unique job titles are there? **
def q11():
    print("Q11")
    result = None   # edit this

    print(result)   # Dont change this


# 12) ** What are the top 5 most common jobs? **
def q12():
    print("Q12")
    result = None   # edit this

    print(result)   # Dont change this

# 13) ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **


def q13():
    print("Q13")
    result = None   # edit this

    print(result)   # Dont change this


# 14) ** How many people have the word Chief in their job title? (This is pretty tricky) **
def q14():
    print("Q14")

    result = None   # edit this

    print(result)   # Dont change this


# 15) ** Bonus: show correlation between length of the Job Title string and Salary? **
def q15():
    print("Q15")
    result = None   # edit this

    print(result)   # Dont change this


if __name__ == '__main__':
    q01()
    q02()
    q03()
    q04()
    # q05()
    # q06()
    # q07()
    # q08()
    # q09()
    # q10()
    # q11()
    # q12()
    # q13()
    # q14()
    # q15()
