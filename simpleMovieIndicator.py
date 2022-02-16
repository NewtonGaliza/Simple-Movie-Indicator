import numpy as np

user_pref = np.array([5,1,3])

best_movie = np.array([5,5,5])
lowest_movie = np.array([1,1,1])

movie1 = np.array([4,5,1])
movie2 = np.array([5,1,5])


best_choice = np.dot(best_movie, best_movie)
print ('Best Choice:',best_choice)
bad_choice = np.dot(lowest_movie, lowest_movie)
print ('Bad Choice:', bad_choice)

indicator_movie1 = np.dot(user_pref, movie1)
print ('Indicator for movie1:', indicator_movie1)


indicator_movie2 = np.dot(user_pref, movie2)
print ('Indicator for movie2:', indicator_movie2)
