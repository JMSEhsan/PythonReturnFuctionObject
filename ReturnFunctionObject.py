#Ref.: Bell, Ana, Get Programming Lean to Code with Python, Manning 2018
#returning a function object from another function

def grumpy():
    print("I am a grumpy cat: ")
    def no_n_times(n):
        print("No", n, "times...")
        def no_m_more_times(m):
            print("...and no", m, "more times")
            def no_k_less_times(k):
                print("...and no", k, "times less")
                for i in range(n+m-k):
                    print("no")  
            return no_k_less_times
        return no_m_more_times
    return no_n_times
grumpy()(8)(2)(3)



