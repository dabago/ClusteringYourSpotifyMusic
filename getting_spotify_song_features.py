#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 01:19:06 2019

@author: yotroz
"""

#%%

#spotify url: https://developer.spotify.com/console/get-several-tracks/?ids=3n3Ppam7vgaVa1iaRUc9Lp,3twNvmDtFQtAd5gMKedhLD

import requests
import json
import pandas as pd


#INSERT PATH WHERE YOU WANT TO SAVE CSV FILE HERE    
path = '/Users/yotroz/Ironhackers Dropbox/Octavio Ramirez/Work/MDBI_IE/Term_2/AI_ML_STATISTICAL_LEARNING_PREDICTION/spotify-project'

#INSERT YOUR NAME HERE
name = 'crazy-test'

#INSERT TOKEN HERE
token_key = 'BQBMBBE6bL9yIdhCrlp3fLlYpwmklxTZVXBcDmDeJAOqcoDneHv3JWT7x0O-pczS-upeGkFiwR3XWRF9BAVmDcloWOGyjX5ALXRYTwoEAjv1Ld1ThYJ6JYwmE7WZNG5xwshN7ciL3cKqpbkH6ZI1GwFbsEu0D8aAlf4'

token = 'Bearer ' + token_key

headers = {
    'Authorization': token,
}


response = requests.get('https://api.spotify.com/v1/me/tracks?offset=0&limit=50', headers=headers)

data = response.json()
print(data)
data = data['items']
ids =[]
song_names = []
artist = []
for song in data:
    ids.append(song['track']['id'])
    song_names.append(song['track']['name'])
    artist.append(song['track']['artists'][0]['name'])
    
    
print(ids)
#%%


songs_features = []

for song in ids:

    response = requests.get('https://api.spotify.com/v1/audio-features/{}'.format(song), headers=headers)
    data = response.json()
    songs_features.append(data)




#%%

features_list = []
i = 0 
for features in songs_features:
        features_list.append([features['energy'], features['liveness'],
                              features['tempo'], features['speechiness'],
                              features['acousticness'], features['instrumentalness'],
                              features['time_signature'], features['danceability'],
                              features['key'], features['duration_ms'],
                              features['loudness'], features['valence'],
                              features['mode'], features['type'],
                              features['uri'], song_names[i], artist[i]])
        i = i + 1

df = pd.DataFrame(features_list, columns=['energy', 'liveness',
                                              'tempo', 'speechiness',
                                              'acousticness', 'instrumentalness',
                                              'time_signature', 'danceability',
                                              'key', 'duration_ms', 'loudness',
                                              'valence', 'mode', 'type', 'uri', 'song_names', 'artist'])
    
#df.to_csv('/Users/yotroz/Ironhackers Dropbox/Octavio Ramirez/Work/MDBI_IE/Term_2/AI_ML_STATISTICAL_LEARNING_PREDICTION/spotify-project/octavios_songs.csv')
df.to_csv('{}/{}-songs.csv'.format(path, name), index=False)   
        


#%%
#DROP OTHER VARIABLES, ONLY FIVE REMAIN'
df_depured = df.drop(['energy', 'tempo', 'time_signature', 'key', 'duration_ms', 'loudness', 'valence', 'type', 'mode', 'song_names', 'artist'], axis=1)
df_depured.to_csv('{}/{}-songs-clean.csv'.format(path, name), index=False)   




#%%


