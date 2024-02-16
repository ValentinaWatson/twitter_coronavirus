# Coronavirus twitter analysis

In this project, I scanned all geotagged tweets sent in 2020 to monitor for the spread of the coronavirus on social media.

To do this, I imported from the Twitter dataset all of the tweets sent in 2020 allocated to a folder labeled the respective day that the message was tweeted. I then underwent a MapReduce procedure in order to analyze these tweets. After unzipping all of the tweets, I created a database that communicated how many tweets were sent by what country per day and then again with what language the tweets were sent in. So each folder had a dictionary that linked the country/language to the number of tweets that fell into that category. I then performed a reduction step that combined all the files per day into one file that counted how many tweets containing the hashtag coronavirus were sent in each country/language during the whole year. I then visualized these results using a horizontal bar graph that communicated how many tweets were sent by the top 10 most popular countries and languages. The country and language graphs are below in respective order:

<img src="coronavirus_fig-country_code.png" width="100%">
<img src="coronavirus_fig-country_code.png" width="100%">


This process was then repeated for #코로나바이러스 which is Korean. Again, the country and language graphs are below in respective order:

<img src="코로나바이러스_fig-country_code.png" width=100% />
<img src="코로나바이러스_fig-lang.png" width=100% />

Finally, I performed a final reduction and visualization step that graphed the changes in the frequency of different hashtags throughout the year. The results are below:

<img src=hashtags_over_time.png width=100% />
