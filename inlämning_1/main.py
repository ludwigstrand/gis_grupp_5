from flask import Flask, render_template, jsonify 
from sklearn.cluster import KMeans
import pandas as pd

app = Flask(__name__)

@app.route('/cluster')
def cluster():

    data = pd.read_csv('static/school_locations.csv')
    
    X = data[['xcoord', 'ycoord']].values 
    k = 5
    kmeans = KMeans(n_clusters=k, init = 'k-means++', random_state = 42, n_init = 10).fit(X)
    data['cluster'] = kmeans.labels_  

    response_data = {
        'clusters': data.to_dict(orient='records'),
        'centroids': kmeans.cluster_centers_.tolist()
    }
    return jsonify(response_data)

@app.route("/")
def home():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)
