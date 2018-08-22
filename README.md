# NIPS-Paper-Clustering-2017
I web scraped all of the accepted papers from the N.I.P.S  2017 conference and clustered them by topic. The basic approach was to use NLP to parse the abstracts, use td-idf to determine what topics the papers were on, calculate cosine similarity, and cluster using the k-means algorithm.
Based on Brandon Rose's document clustering tutorial http://brandonrose.org/clustering
