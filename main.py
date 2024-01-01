#your code
def change(x):
    if x == None:
        return 0
    if '<=' in x:
        return int(x.replace('<=',''))
    elif '>=' in x: 
        return int(x.replace('>=',''))
    return int(x)

df_it[["c_from","c_to"]] = df_it.maintenance_cost.str.split('-',expand=True) 
df_it.c_from = df_it.c_from.apply(change)
df_it.c_to = df_it.c_to.apply(change)

df_it.iloc[0,[2,3]] = df_it.iloc[0,[3,2]]
df_it