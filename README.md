# What’s in a Hollywood Wall Street movie?
The inspiration for this project started with a blog post from Nick Maggiulli, who is a famous personal finance blogger, titled [The 13 Best Wall Street Movies](/https://ofdollarsanddata.com/wall-street-movies) Nick suggests 13 Wall Street movies which he believes are a must watch for everyone interested in finance.  

I'm partially interested in finance and very interested in data science, so I thought of analyzing the 13 movies to see if I could discover some insights. Let me also confess that one of my dreams is to write a movie. I'd love for the movie to be about data science, but I don't think many people would be interested in that. However, many people love finance movies, so owing to my love for numbers, it's highly likely that the movie I dream to write will be about finance.  

This brings me to the main question of my project: What’s in a Hollywood Wall Street movie? My plan of attack was to do a data analysis investigation of the 13 movies Nick listed in his blog.  

## Building the dataset
I wrote a Python script to scrape the data from the blog post using Requests and BeautifulSoup libraries. The data was then converted into a dataframe with Pandas library.  

Not all movies had scripts freely available online. So I downloaded subtitles for each movie `.srt` files and wrote a Python script that converted them to `.txt` files. This allowed me to perform some text analysis on them.  

Finally, I added the rating and duration of each movie that I got from IMDb. I now had full data set with 13 rows and 6 columns.  

## Cleaning the dataset
Converting the data from `.srt` file to `.txt` made the text data messier. That’s because `.srt` files have timestamps, line breaks, color schemes, and on and on. All this had to be cleaned up to effectively perform some text analysis.  

To speed up this text-cleaning task, I turned to regular expressions. This was a challenging task, but there's an upside: going through this process enhanced my knowledge of regular expressions.  

## Exploratory Data Analysis (EDA)
Now that the data set was clean, I proceeded to perform some analysis. Firstly, I wanted to see how each movie in the data set was rated on IMDb. I created a horizontal back graph to visualize this. Two movies in __The Wolf of Wall Street__ and __Inside Job__ had a rating of 8.2 which was the highest rating. The movie __Equity__ had the lowest rating of 5.6.  

I also plotted a cumulative histogram which showed that most of the movies had a rating of 7.0 or higher. So broadly speaking, Wall Street movies tend to do well.  

Another plot I created was a histogram showing their distribution of duration. It turns out that most Wall Street movies are between 100 and 130 minutes long. One movie in the dataset was an outlier. It was more than 170 minutes long.  

I also wanted to see the golden decade for Wall Street movies. So, I grouped them by decade and created a bar graph. The 2010s were the best decade for Wall Street movies.  

Lastly, I wanted to see if there was a relationship between the rating of the movie and its duration. Unsurprisingly, there is no relationship between how long a movie is and how it is rated.  

All the visualizations in my exploratory data analysis were created using Matplotlib. I used PayPal and Futura fonts.

## Topic modeling
Knowing that a Wall Street movie is about finance doesn't quite get into the inside of the movie. To discover the topics contained in each movie, I turned to NLTK and Gensim libraries. NLTK helped to tokenize the text, while Gensim helped to extract the topics.  

When I used the two libraries on the text I got the usual suspect topics like money, stocks, market, etc. However, what caught my attention were the two words that kept showing up in almost all the movies: fuck and shit. Having these two topics appear in three movies would have been a coincidence, but more than five? That calls for an investigation!  

This led me to the profanity plot. I expanded my dataset by creating two new columns *f_word* and *s_word*, which contained a count of how many times the words ‘shit’ and ‘fuck’ appeared in the script of each movie. Needless to say, the results were astounding.  

Since there were huge variations in the counts, for example, the __Trading Places__ had 11 f-words while __Boiler Room__ had 106, I normalized the data to make it easier to plot. Therefore, the lowest value was 0 and the highest was 1.  

## Sentiment analysis
To discover the sentiment of the movies, I used the library TextBlob. This scored the text on a scale of 0 to 1. With the neutral point at 0.5, values below indicated negative sentiment and values above indicated positive sentiment. Likewise, the text was measured for subjectivity where 0.5 was the neutral point, and values below represented fact while values above represented opinion.  

On the whole, Wall Street movies are very negative. Also, they score slightly above the neutral point for subjectivity, making them opinion-based.
