import pandas as pd
arpy = pd.read_csv('arpy.csv')
arpy.head()
def player_stats(age):

    arpy[arpy['age']==age]['overall_rating_change%'].hist(density = True,bins=100)
    arpy[arpy['age']==age].overall_rating_yearly.hist(density = True)

    print(arpy[arpy['age'] == age].sort_values('overall_rating_yearly', ascending = False).player_name.head(10))
    return arpy[arpy['age']==age].describe()[['overall_rating_change%','overall_rating_yearly']]
player_stats(20)
