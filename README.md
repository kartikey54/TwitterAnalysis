# TwitterAnalysis

Work in progress

Using textblob for Natural language Processing, this script extracts sentiments from most recent 100 tweets about the topic.
It then generates a csv file titled *topic*.csv mentioning the number of positive tweets, number of negative tweets and then mentions the tweets under their respective sections.

Eg, A recent search about donald trump yields 4 positive and 37 negative tweets. :P 

Run script from command line as :-

*dir*/python twextract.py *topicName*

Eg. python twextract.py tesla 

This makes a tesla.csv

Default topic is set as 'India'.
