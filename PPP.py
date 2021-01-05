import openpyxl
import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()  # for plot styling
import numpy as np
import scipy
jobs = []
loans = []
count = 0
flag = 0
with open('/Users/kevinmetro/Documents/lol/ppp_loans_state_NJ.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        flag = 1
        
        
        if row['jobs_reported'] == "" or row['jobs_reported'] == 0:
            flag = 0
        if flag == 1:
            jobs.append(float(row['jobs_reported'])) 
            loans.append(float(row['loan_amount']))

import seaborn as sns
d = {'Number_of_Employees': jobs, 'Loan_Amount': loans}
sns.boxplot('Number_of_Employees','Loan_Amount',data=d)


#df1.plot('Number_of_Employees',kind='bar', figsize=(12,8))
print 'Average Jobs ' + str(sum(jobs) / len(jobs))
print 'Average Loan Amount ' + str(sum(loans) / len(loans))
loans.sort()
jobs.sort()
print 'Median Loans ' + str(loans[len(loans)/2])
print 'Median Jobs ' + str(jobs[len(jobs)/2])

f = plt.figure(figsize=(12, 8))
plt.matshow(df.corr(), fignum=f.number)
plt.xticks(range(df.shape[1]), df.columns, fontsize=14, rotation=45)
plt.yticks(range(df.shape[1]), df.columns, fontsize=14)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=16);
#bracket1 = []
#bracket2 = []
#bracket3 = []
#bracket4 = []
#bracket5 = []
#for x in loans:
#    
#    j = loans.index(x)
#    if jobs[j] <=50:
#        bracket1.append(x)
#    elif jobs[j] <=100:
#        bracket2.append(x)
#    elif jobs[j] <=150:
#        bracket3.append(x)
#    elif jobs[j] <=200:
#        bracket4.append(x)
#    else:
#        bracket5.append(x)
#data = {'<=50':sum(bracket1), '<=100':sum(bracket2), '<=150':sum(bracket3),  
#        '<=200':sum(bracket4), '>200':sum(bracket5)} 
#employees = list(data.keys()) 
#values = list(data.values()) 
#   
#fig = plt.figure(figsize = (10, 5)) 
#  
## creating the bar plot 
#plt.bar(employees, values, color ='yellow',  
#        width = 0.4) 
#  
#plt.xlabel("No. Employees in Company") 
#plt.ylabel("Total Loan Amount Given") 
#plt.title("Employees vs Loan Total Given") 
#plt.show() 
