import pandas as pd


def calculate_distance_matrix(df)->pd.DataFrame():

    lst = list(df['id_start'].drop_duplicates().values)
    lst.append(1001472)

    new_df = pd.DataFrame(index = lst,columns=lst)


    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if lst[i] == lst[j] :
                new_df.loc[lst[i],lst[j]] = 0
            else :
                ind = df[df['id_end'] == lst[j]].index[0]
                indi = df[df["id_start"] == lst[i]].index[0]
                dist = sum(df.iloc[indi:ind+1]["distance"])
                new_df.loc[lst[i],lst[j]] = dist



    for i in range(0,42):
        for j in range(0,42):
            if i == j or j> i:
                pass
            else:
                new_df.iloc[i,j] = new_df.iloc[j,i]
    return new_df




def unroll_distance_matrix(df)->pd.DataFrame():

    id_start = []
    id_end = []
    distance = []
    cols = list(df.columns)
    for i in range(len(cols)):
        for j in range (i+1 , len(cols)):
            id_start.append(cols[i])
            id_end.append(cols[j])
            distance.append(new_df.loc[cols[i],cols[j]])
    dic = {'id_start':id_start,'id_end':id_end,"distance":distance}
    df = pd.DataFrame(dic)
    return df


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():

    m = df[df["id_start"] == reference_id]['distance'].values.mean()
    low = m-(m *0.10)
    high = m+(m *0.10)
    lst = list(df[(df['distance'] >= low ) & (df['distance']<=high)]['id_start'].drop_duplicates().sort_values().values)
    return lst
   

def calculate_toll_rate(df)->pd.DataFrame():
    df['moto'] = 0.8 *df['distance']
    df['car'] = 1.2 *df['distance']
    df['rv'] = 1.5 *df['distance']
    df['bus'] = 2.2 *df['distance']
    df['truck'] = 3.6 *df['distance']
    return df

def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here

    return df

df = pd.read_csv("E:\MapUp-DA-Assessment-2024\datasets\dataset-2.csv")
new_df = calculate_distance_matrix(df)
new_df=unroll_distance_matrix(new_df)
lst = find_ids_within_ten_percentage_threshold(new_df,1001400)
new_df = calculate_toll_rate(new_df)
print(lst)