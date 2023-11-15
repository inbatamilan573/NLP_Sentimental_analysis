import pandas as pd

'''The total record in the json file 32,292,099 and we diveded it by 10L so we get 32L + remaning so 33 chucks'''

df_reader = pd.read_json("F:/Clothing_Shoes_and_Jewelry.json", lines =  True ,chunksize = 1000000 )
print(df_reader.__sizeof__)
counter = 1
for chunk in df_reader:
    new_df = pd.DataFrame(chunk[['overall', 'reviewText','summary']])
    new_df1 = new_df[new_df['overall'] == 1].sample(6000)
    new_df2 = new_df[new_df['overall'] == 2].sample(6000)
    new_df3 = new_df[new_df['overall'] == 4].sample(6000)
    new_df4 = new_df[new_df['overall'] == 5].sample(6000)
    new_df5 = new_df[new_df['overall'] == 3].sample(12000)
    new_df6 = pd.concat([new_df1, new_df2, new_df3, new_df4, new_df5], axis = 0,ignore_index = True)
    new_df6.to_csv(str(counter)+'.csv', index = False)
    print(counter)
    counter = counter+1

print("sucess")  
    
from glob import glob
#the glob module is used to retrieve the files
#or pathnames matching a pattern

filenames = glob('*.csv')


#['1.csv','2.csv',..........,'33.csv']

dataframes = []

for f in filenames:
    dataframes.append(pd.read_csv(f))

#[..........]


finaldf = pd.concat(dataframes, axis = 0, ignore_index = True)

finaldf.to_csv("balanced_reviews_original.csv", index = False)


#---------------------------------

df = pd.read_csv('balanced_reviews_original.csv')

