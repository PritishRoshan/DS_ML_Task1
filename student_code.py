import pandas as pd
import matplotlib.pyplot as plt
#function to replace all 'yes' with 1 and 'no' with 0
def replace_yes(cell):
    if cell=="yes":
        return 1
    return 0
#conversion of 'yes' to 1 and 'no' to 0
df = pd.read_csv('/home/pritish/DS_ML_Task1/student-math.csv', converters = {
    'schoolsup':replace_yes,
    'famsup': replace_yes,
    'paid':replace_yes,
    'activities':replace_yes,
    'nursery':replace_yes,
    'higher':replace_yes,
    'internet':replace_yes,
    'romantic':replace_yes,
})
#for mean of marks in columns G1, G2 and G3
col = df.loc[: , "G1":"G3"]
df['final_grade'] = col.mean(axis=1)
#Remove all the three columns G1, G2 and G3
df = df.drop(['G1','G2','G3'], axis=1)
#save the new dataframe in a new csv file
df.to_csv('/home/pritish/DS_ML_Task1/new_final_grade.csv')
#plotting scatter plot between studytime and final_grade
plt.subplot(1,2,1)
plt.title('Scatter plot \n studytime vs. final_grade')
colors = [1.0,2.0,3.0,4.0]
plt.scatter(df.studytime, df.final_grade, c=df.studytime)
plt.xlabel('studytime--->')
plt.ylabel('final_grade--->')
#Boxplot of studytime and final_grade
plt.subplot(1,2,2)
plt.title('Box_Plot')
box_plot = df.boxplot(column=['final_grade', 'studytime'])
plt.show()
