from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Assuming 'keywords' is a list of strings where each string contains keywords separated by spaces
#keywords = ['case management', 'document management', 'dev ops', 'software']
keywords = ['Mumbai', 'Delhi', 'London', 'Munich', 'Haryana']

# Vectorize the keywords
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(keywords)

# Apply K-means clustering
num_clusters = 3  # Adjust based on your data
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

# Assign clusters to keywords
clusters = kmeans.labels_

# Print the results
for keyword, cluster in zip(keywords, clusters):
    print(f"Keyword: {keyword}, Cluster: {cluster}")
