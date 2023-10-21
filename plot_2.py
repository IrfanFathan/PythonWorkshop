import numpy as np
import matplotlib.pyplot as plt
data ={'C':220,'C++':105,'java':3000,'python':2005} 
courses=list(data.keys())
values=list(data.values())
fig=plt.figure(figsize=(0,6))
plt.bar(courses,values,color='gray',width=0.4)
plt.xlabel("Courses offered")
plt.ylabel("No.of students enrolled  ")
plt.title("Students enrolled in different courses")
plt.show()      