import numpy as np

movie_names=np.array(["Movie1","Movie2","Movie3","Movie4","Movie5"])
watch_duration=np.array([120,90,150,75,180])

print("Total Duration: ",watch_duration.sum())
print("Average Watch Duration: ",watch_duration.mean())
print("Longest Movie: ",movie_names[watch_duration.argmax()])
print("Shortest Movie: ",movie_names[watch_duration.argmin()])

print()

watch_duration=watch_duration/60 

# for i in watch_duration:
#     if i>2:
#         print(i)

for i,j in enumerate(watch_duration): # i=>index,j=>değer
    print(f"{movie_names[i]},{j} hours")