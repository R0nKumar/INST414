import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv('nba.csv')

players = ['James Harden', 'LeBron James', 'Kemba Walker']

attr = ['age', 'player_height','player_weight','pts', 'reb', 'ast']
stats = df[attr]

for player in players:
    # get index of targeet
    target = player
    target_indexes = df[df['player_name'] == target].index
    target_index = target_indexes[0]

    # get stats of target
    target_stats = stats.loc[target_index]

    # get stats for everyone who isn't the target
    for index in target_indexes:
        gen_stats = stats[stats.index != index]

    # reshape target stats
    target_stats = target_stats.values.reshape(1,-1)

    # perform cosine similarity using target stats
    stats['Cosine_Similarity'] = stats.apply(lambda row: cosine_similarity(row.values.reshape(1, -1), target_stats)[0, 0], axis=1)
    stats_sorted = stats.sort_values(by='Cosine_Similarity', ascending=False).head(11)

    # print results
    print(target, "'s similar players: ")
    for index in stats_sorted.index:
        name = df._get_value(index, 'player_name')
        print(name)
    print("   ")

