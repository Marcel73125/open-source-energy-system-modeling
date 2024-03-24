#the function glucoselevel calculates the glucose level at the handed over time with the given initial glucose level and returns that value; 
# returns -1 if input value g_init is negative
def glucoselevel(g_init, time): #g_init = initial glucose level in mg/dl;  #time in min
    #define symbols for solving differential equation symbolically (without values)
    t, k = symbols('t k')
    g = symbols ('g', cls = Function )

    k_value = 0.0045 # 1/min; #decline of glucose level per minute

    if g_init >= 0: #checks if value for g_init is valid
        #solving differential equation with given initial glucose level; ics sets the initial condition; #[g] = mg/dl
        sol_1 = dsolve(Eq(g(t).diff(t), -k*g(t)), g(t), ics={g(0): g_init})
        display(sol_1) #print general solution of the differential equation; #example: g_init=80, g(t) = 80*e^-(k*t)

        #solving differential equation at given time value
        result_value_1 = sol_1.subs({k: k_value, t: time}) # .subs substitutes the symbols k with the defined k_value and t with handed over time value
        display(result_value_1) #print solution at given time value;   #example: g_init=80, k=0.0045, t=60,  g(60)=61.0703595469483
        return sol_1.rhs.subs({k: k_value, t: time}).round(4) #rounds to fourth digit and returns the rounded right hand side of the solution; #example:   with values 1 line above would return 61.0704

    print('g_init out of scope')
    return -1
