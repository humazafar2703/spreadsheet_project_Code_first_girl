import pandas as pd
import numpy as np
data = pd.read_csv('sales.csv')
print(data.head(12))

# the average monthly sales

monthly_sales = data['sales'].mean()
print('Average Monthly Sales: ${}'.format(monthly_sales))

# the average monthly expenditure

monthly_expenditure = data['expenditure'].mean()
print('Average Monthly Expenditure: ${}'.format(monthly_expenditure))

# sale statistical description

sale_description = data['sales'].describe()
print('Statistical Information about Sale:{}'.format(sale_description))


# expenditure statistical description

expenditure_description = data['expenditure'].describe()
print('Statistiical Information about Expenditure: {}'.format(expenditure_description))



# total sale for the year 2018

totalsale = data['sales'].sum()
print('Total sales: ${}'.format(totalsale))

# total expenditure for the year 2018

totalexpenditure = data['expenditure'].sum()
print('Total expenditures: ${}'.format(totalexpenditure))

#total annual net profit

netprofit = totalsale - totalexpenditure
print('Net Profit: ${}'.format(netprofit))

# monthly net profit
print(data.head())

monthlynetamountlist= data['sales'] - data['expenditure']
print('Net Amount: ${}'.format(monthlynetamountlist))


# adding column for monthly net profit (loss)
data['net profit or loss'] = monthlynetamountlist

print(data.head(12))

import matplotlib.pyplot as plt
month = range(1,13)
plt.bar(month,data['sales'])
plt.ylabel('Sales in$')
plt.xlabel('MONTH')
plt.show()

month = range(1,13)
plt.bar(month,data['net profit or loss'])
plt.ylabel('Net Profit (or Loss) in $')
plt.xlabel('MONTH')
plt.show()


# percentage change in sales

data['percentage change in sale'] =np.round(data['sales'].pct_change()* 100, 1)

print(data.head(13))

# best performing month
data_max = data.max(axis=0)
print ('Best Performance')
print(data_max)

#best performing month
max_index= data['net profit or loss'].idxmax()
print('Best Performing Month is: {} with the sale of ${} with the net profit of ${}'.format(data['month'][max_index] ,str(data['sales'][max_index]) ,str(data['net profit or loss'][max_index])))


#worst performing month
min_index= data['net profit or loss'].idxmin()
print('Worst Performing Month is: {} with the sale of ${} with the net loss of ${}'.format(data['month'][min_index] ,str(data['sales'][min_index]) ,str(data['net profit or loss'][min_index])))

