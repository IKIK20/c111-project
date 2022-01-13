import pandas as pd
import plotly.figure_factory as ff
import statistics as st
import plotly.graph_objects as go
import random


df= pd.read_csv("medium_data.csv")
data= df["reading_time"].tolist()

population_mean=st.mean(data)
std= st.stdev(data)  

def random_set_of_mean():
    data_set=[]
    for i in range(0,100):
        rand=random.randint(0,30)
        value=data[rand]
        data_set.append(value)
    mean=st.mean(data_set)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_means= random_set_of_mean()
    mean_list.append(set_of_means)

mean= st.mean(mean_list)
std= st.stdev(mean_list)

first_stdev_start, first_stdev_end = mean - std, mean + std
second_stdev_start, second_stdev_end = mean - (2*std), mean + (2*std)
third_stdev_start, third_stdev_end = mean - (3*std), mean + (3*std)


df1= pd.read_csv("medium_data.csv")
data1= df1["reading_time"].tolist()

mean1= st.mean(data1)
std1= st.stdev(data1)
print (mean1,std1)

fig= ff.create_distplot([data1],["scores1"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.04], mode= "lines", name= "mean"))
fig.add_trace(go.Scatter(x=[mean1,mean1], y=[0,0.04], mode= "lines", name= "mean of sample 1"))

fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end], y=[0,0.04], mode= "lines", name= "stdev 1 end"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end], y=[0,0.04], mode= "lines", name= "stdev 2 end"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end], y=[0,0.04], mode= "lines", name= "stdev 3 end"))

#fig.show()

zscore= (mean1-mean) / std
print(zscore)

