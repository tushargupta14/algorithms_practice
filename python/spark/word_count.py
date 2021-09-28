import pyspark
sc = pyspark.SparkContext()

# Top word counts
inputFile = "gs://*******/notebooks/jupyter/shakes.txt"
lines = sc.textFile(inputFile)
words = lines.flatMap(lambda line: line.split())
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda count1, count2: count1 + count2).sortBy(
    lambda x : x[1], ascending=False)
wordCounts.take(10)

# Top word counts after removing stop words
import nltk
nltk.download()
from nltk.corpus import stopwords
stops = set(stopwords.words('english'))
wordCounts = words.filter(lambda x: x.lower() not in stops).map(lambda x: (x,1)).reduceByKey(lambda a, b: a+b).sortBy(
    lambda x : -x[1])