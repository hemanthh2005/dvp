import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd


data=pd.read_csv('dataset3.csv')



data_num=data.set_index('USN')

student1=data_num.loc['4MC24CS001']
student2=data_num.loc['4MC24CS002']

fig,axis=plt.subplots(1,2,figsize=(15,5))
fig.suptitle('Student Information',size=24,color='blue')

sb.barplot(ax=axis[0],x=student1.index,y=student1.values)
axis[0].set(xlabel='Courses',ylabel='Marks')
axis[0].set_title('4MC24CS001',size=16,color='red')

sb.lineplot(ax=axis[1],x=student2.index,y=student2.values,marker='D',markerfacecolor='blue',color='red',linestyle='--')

axis[1].set(xlabel='Courses',ylabel='Marks')
axis[1].set_title('4MC24CS002',size=14,color='red')

plt.show()

# import pandas as pd
# import seaborn as sb
# import matplotlib.pyplot as plt
#
# # Read the CSV file
# data = pd.read_csv('dataset3.csv')
#
# # Set 'USN' as the index
# data_num = data.set_index('USN')
#
# # Access student data by their USN
# student1 = data_num.loc['4MC24CS001']
# student2 = data_num.loc['4MC24CS002']
#
# # Create plots
# fig, axis = plt.subplots(1, 2, figsize=(15, 5))
# fig.suptitle('Student Information', size=24, color='blue')
#
# # Bar plot for student 1
# sb.barplot(ax=axis[0], x=student1.index, y=student1.values)
# axis[0].set(xlabel='Courses', ylabel='Marks')
# axis[0].set_title('4MC24CS001', size=16, color='red')
#
# # Line plot for student 2
# sb.lineplot(ax=axis[1], x=student2.index, y=student2.values, marker='D', markerfacecolor='blue', color='red', linestyle='--')
# axis[1].set(xlabel='Courses', ylabel='Marks')
# axis[1].set_title('4MC24CS002', size=14, color='red')
#
# # Show the plot
# plt.show()
