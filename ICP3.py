from collections import Counter

print("################################## Part - 1 #############################################")

class Employee:
    #Initializing the constructor
    emp_count = 0;
    emp_salaries = []
    def __init__(self,name, family, salary, department):
        self.emp_department_name = department
        self.emp_salary = salary
        self.emp_family = family
        Employee.emp_count +=1
        Employee.emp_salaries.append(salary)
        self.emp_name = name

    def get_salary(self):
        total_salaries=0;
        for s in Employee.emp_salaries:
            total_salaries = total_salaries + s
        return total_salaries/len(Employee.emp_salaries)

# Inheriting the Employee class to FullTimeEmployee Class

class FullTimeEmployee(Employee):
    def _init_(self, name, family, salary, department):
        Employee._init_(self, name, family, salary, department)

f1 = FullTimeEmployee("Pranu", "Mutha", 1200000, "CS")
f2 = FullTimeEmployee("Sirisha","Rella", 1200000, "CS")
f3 = FullTimeEmployee("Nikki","Pateel", 600000, "CS")
avg_salary = FullTimeEmployee.get_salary(Employee)
print("All the employees together has an average salary of",avg_salary)


print("################################## Part - 2 (Web Scraping) #############################################")
from bs4 import BeautifulSoup
import urllib.request
import requests

def web_scrap():
    html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")   #Passing url to get the content of html
    soup = BeautifulSoup(html.content, "html.parser")                        #Parsing through soup parser
    print("Title of the web page is ",soup.title.string)

#returning the results with href and printing out with it
    # for r in soup.find_all('a'):
    #     print(r.get('href'))
web_scrap()

print("################################## Part - 3 (Numpy) #############################################")
import numpy as np

# temp = np.random.random_integers(0,20,15)
# a = np.random.randint(0,20,15)
a = np.array([5, 4, 12, 12, 2, 0, 5, 4, 6, 1])
print(a)
co = Counter(a)

for k, v in co.items():
    if v == max(co.values()):
        print(k)

# integers = np.array([5, 4, 12, 12, 2, 0, 5, 4, 6, 1])
# print("Input Array",integers)
# x = []
# temp = np.bincount(integers)
# x = np.argmax(temp)
# print(temp)
# print(x)



# print(np.argmax(np.bincount(integers)))

#r = np.random.randint(20,size=15)

# print("The most frequently repeated integer is:",np.bincount(r).argmax())





