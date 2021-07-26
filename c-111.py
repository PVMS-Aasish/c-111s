import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df=pd.read_csv("studentMarks.csv")
math_data=df["Math_score"].tolist()

#fig=ff.create_distplot([math_data],["Math_score"],show_hist=False)
#fig.show()

math_mean=statistics.mean(math_data)
std_deviation=statistics.stdev(math_data)
print("math_mean:- "+str(math_mean))
print("math_stdev:- "+str(std_deviation))

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(math_data)-1)
        value=math_data[random_index]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean


mean_list=[]

for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation=statistics.stdev(mean_list)
mean=statistics.mean(mean_list)

first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)
print("std_1",first_std_deviation_start,first_std_deviation_end)
print("std_2",second_std_deviation_start,second_std_deviation_end)
print("std_3",third_std_deviation_start,third_std_deviation_end)

fig=ff.create_distplot([mean_list],["Math_score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))    
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="STD_DEV_1_START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="STD_DEV_1_END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="STD_DEV_2_START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="STD_DEV_2_END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode="lines",name="STD_DEV_3_START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="STD_DEV_3_END"))
fig.show()