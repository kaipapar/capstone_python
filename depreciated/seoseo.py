import csv
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import TfidfVectorizer


# Read keywords from input file
def read_keywords(file_path):
    keywords = []
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            i=0
            while i < len(row) and row[i] != '':
                keywords.append(row[i])
                i+=1

    return keywords


# Write clustered keywords to output file
def write_clusters_to_csv(file_path, clusters, keywords):
    with open(file_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Keyword", "Cluster"])
        for keyword, cluster in zip(keywords, clusters):
            writer.writerow([keyword, cluster])


# Calculate text similarity using TF-IDF
def text_similarity(keywords):
    vectorizer = TfidfVectorizer()
    keyword_matrix = vectorizer.fit_transform(keywords)
    return keyword_matrix


# Perform clustering
def cluster_keywords(similarity_matrix, num_clusters):
    clustering = AgglomerativeClustering(n_clusters=num_clusters)
    clusters = clustering.fit_predict(similarity_matrix.toarray())
    return clusters


# Main function
def main():
    input_file = "output.csv"
    output_file = "seoseo.csv"
    num_clusters = 15


    keywords = read_keywords(input_file)
    similarity_matrix = text_similarity(keywords)
    clusters = cluster_keywords(similarity_matrix, num_clusters)
    write_clusters_to_csv(output_file, clusters, keywords)


if __name__ == "__main__":
    main()