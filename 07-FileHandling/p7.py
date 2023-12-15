def f(arr):
    import re
    statement=re.compile(r'^[a-z0-9_]{4,12}$')
    dobranazwa=[word for word in arr if statement.match(word)]
    sum=len(dobranazwa)
    print(sum)









f(["uek","water_7_x","anna.may","a_b_c_d_e_f"])