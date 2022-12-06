#define the variables in the equation
R = 1 #rate of star formation
f_p = 0.5 #fraction of stars with planets
n_e = 1 #number of planets per star with planets
f_l = 0.01 #fraction of planets that can support life
f_i = 0.01 #fraction of planets with life that develop intelligence
f_c = 0.01 #fraction of intelligent life that can communicate
L = 10 #length of time civilizations are detectable

#calculate the number of detectable extraterrestrial civilizations
N = R * f_p * n_e * f_l * f_i * f_c * L

#print the result
print(N)

