import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import folium
import seaborn as sns

# verinin yüklenmesi
df = pd.read_csv("traffic_density_202501.csv")

# zaman bilgisi çıkarımı
df["DATE_TIME"] = pd.to_datetime(df["DATE_TIME"])
df["HOUR"] = df["DATE_TIME"].dt.hour
df["DAY_OF_WEEK"] = df["DATE_TIME"].dt.dayofweek
df["WEEKEND"] = df["DAY_OF_WEEK"].apply(lambda x: 1 if x >= 5 else 0)

# gerekli sütunların seçilmesi
features = df[[
    "LATITUDE", "LONGITUDE", "AVERAGE_SPEED", "MINIMUM_SPEED", 
    "MAXIMUM_SPEED", "NUMBER_OF_VEHICLES", "HOUR", "DAY_OF_WEEK", "WEEKEND"
]].dropna()

# özellikleri normalize etme
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# elbow yöntemi
sse = []
for k in range(2, 10):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    sse.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(2, 10), sse, marker='o')
plt.title("Elbow Yöntemi ile Küme Sayısı Belirleme")
plt.xlabel("Küme Sayısı (k)")
plt.ylabel("SSE (Hata)")
plt.grid(True)
plt.show()

# k-means kümeleme
kmeans = KMeans(n_clusters=4, random_state=42, n_init='auto') 
kmeans.fit(scaled_features)
df["CLUSTER"] = kmeans.labels_

# PCA ile Görselleştirme
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_features)
df['pca1'] = pca_result[:, 0]
df['pca2'] = pca_result[:, 1]

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='pca1', y='pca2', hue='CLUSTER', palette='Set1')
plt.title("PCA ile Küme Görselleştirme")
plt.xlabel("Bileşen 1")
plt.ylabel("Bileşen 2")
plt.grid(True)
plt.show()

# folium harita gösterimi
df_sampled = df.sample(n=150000, random_state=42) 
m = folium.Map(location=[41.01, 29.1], zoom_start=10) 
colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred'] 

for _, row in df_sampled.iterrows():
    folium.CircleMarker( 
        location=[row["LATITUDE"], row["LONGITUDE"]], 
        radius=3, 
        color=colors[row["CLUSTER"] % len(colors)], 
        fill=True, 
        fill_opacity=0.6 
    ).add_to(m) 

m.save("trafik_kumeleme_haritasi.html") 
