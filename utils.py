from sympy import symbols, dsolve, Eq, plot, Function
from IPython.display import display

#define symbols for solving differential equation symbolically (without values)
t, k = symbols('t k')
g = symbols ('g', cls = Function )
k_value = 0.0045 # 1/min; #decline of glucose level per minute

#the function glucoselevel calculates the glucose level in mg/dl at the handed over time in minutes with the given initial glucose level 
# and returns that value; # returns -1 if input value g_init is negative
def glucoselevel(g_init, time): #g_init = initial glucose level in mg/dl;  #time in min
    if g_init >= 0: #checks if value for g_init is valid
        #solving differential equation with given initial glucose level; ics sets the initial condition; #[g] = mg/dl
        sol_1 = dsolve(Eq(g(t).diff(t), -k*g(t)), g(t), ics={g(0): g_init})
        display(sol_1) #print general solution of the differential equation; #example: g_init=80, g(t) = 80*e^-(k*t)

        #solving differential equation at given time value
        result_value_1 = sol_1.subs({k: k_value, t: time}) # .subs substitutes the symbols k with the defined k_value and t with handed over time value
        display(result_value_1) #print solution at given time value;   #example: g_init=80, k=0.0045, t=60,  g(60)=61.0703595469483
        return sol_1.rhs.subs({k: k_value, t: time}).round(4) #rounds to fourth digit and returns the rounded right hand side of the solution; #example:   with values 1 line above would return 61.0704
    return -1

#the function printglucoselevel calculates the glucose level in mg/dl at the handed over time in hours with a modeled threshold of 70mg/dl 
# at the given initial glucose level and plots it in the interval [0,time]
# returns 0 if inputs were valid; # returns -1 if either g_init or time_hours is negative
def printglucoselevel(g_init, time_hours):
    if g_init >= 0: #checks if value for g_init is valid
        #solving differential equation with given initial glucose level; (g(t)) - 70) models threshold at which level is dangerously low for humans;
        #ics sets the initial condition; #[g] = mg/dl
        sol_2 = dsolve(Eq(g(t).diff(t), -k*(g(t) - 70)), g(t), ics={g(0): g_init})
        display(sol_2) #print general solution of the differential equation; #example: g_init=80, g(t) = 70 + 10*e^-(k*t)

        if time_hours >= 0:
            #solving differential equation with modeled threshold at given time value
            result_value_2 = sol_2.subs({k: k_value, t: time_hours}) # .subs substitutes the symbols k with the defined k_value and t with handed over time value
            display(result_value_2) #print solution at given time value;   #example: g_init=80, k=0.0045, t=10,  g(10)=79.559974818331

            plot(sol_2.rhs.subs({k: k_value}), (t, 0, time_hours*60), xlabel='t in [min]', ylabel='Glucoselevel in [mg/dl]',axis_center=(0,70.5)) #plots glucose level in the interval [0,time]
            return 0
    return -1
