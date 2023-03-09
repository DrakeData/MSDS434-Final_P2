# MSDS 434 Final (Part II)
This repository contains code used for MSDS 434 Analytics Application Development Final Project (Part II). The final project consists of building a cloud-native analytics application that is hosted on the Google Cloud Platform (GCP).

## Table of Contents
COMING SOON

## Introduction
As an avid user of Spotify (averaging about 80,000 listening minutes per year), I am always impressed by their large variety of music and their recommendation algorithm to create a perfect customized playlist just for me. With Spotify providing access to over 100 million tracks, I wanted to dig deeper to figure out what makes a track popular and how they end up in my playlists. To do this, I will be taking a deeper look in Spotify’s track data and will build a machine learning model to see if I can predict if a track will be a bop or a flop based off of its audio features.

<img src="images/parks_and_rec_banger.gif" width="800" height="300" />

## About the Data
The Spotify track data set for this project was pulled [from Kaggle](https://www.kaggle.com/datasets/lehaknarnauli/spotify-datasets?select=tracks.csv) and it had over 580,000 unique tracks and their audio features.

### Audio Features
Details are from [Spotify's API Dcoumentation](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-several-audio-features)

| Name             | Data Type     | Definition    |
| ---------------- | ------------- | ------------- |
| id               | string        | The Spotify ID for the track|
| name             | string        | Track name|
| popularity       | int           | The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist's popularity is calculated from the popularity of all the artist's tracks|
| duration_ms      | int           |The duration of the track in milliseconds|
| explicit         | boolean       | Whether or not the track has explicit lyrics ( true = yes it does; false = no it does not OR unknown)|
| id_artists       | string        | The Spotify ID for the artist|
| release_date     | string        | The date the track was first released|
| danceability     | float         | Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable|
| energy           | float         | Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy|
| key              | int           | The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1|
| loudness         | float         | The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db|
| speechiness      | float         | Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks|
| acousticness     | float         | A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic|
| instrumentalness | float         | Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0|
| liveness         | float         | Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live|
| valence          | float         | A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry)|
| tempo            | float         | The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration|
| time_signature   | int           | An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4"|

## Requirements
- Access to [Google Cloud Platform (GCP)](https://cloud.google.com/)
- If using Python to download the Kaggle data set, a [Kaggle API Key](https://www.kaggle.com/docs/api) is needed.
    - Make sure to save the API key in 'C:\Users\USER_NAME\.kaggle' directory.

## Architecture

## Project Details

## Project Limitations

## Future Enhancements

## Repository Info
Created by: [Nicholas Drake](https://github.com/DrakeData)

Created Date: 03/06/2023
