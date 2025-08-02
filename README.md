# Trafik Yoğunluğu Kümeleme Projesi

Bu projede, İstanbul'daki trafik yoğunluğu verileri kullanılarak KMeans algoritması ile kümeleme yapılmıştır. Projede aşağıdaki adımlar uygulanmıştır:

- Zaman etkenli öznitelik çıkarımı (saat, hafta sonu vb.)
- Verilerin normalize edilmesi
- Elbow yöntemi ile optimum küme sayısının belirlenmesi
- KMeans ile kümeleme
- PCA ile boyut indirgeme ve görselleştirme
- Seaborn ve Matplotlib ile küme görselleştirme
- Folium ile harita üzerinde kümelerin gösterimi

## Kullanılan Kütüphaneler

- pandas
- matplotlib
- seaborn
- sklearn
- folium

## Çalıştırmak İçin

```bash
pip install -r requirements.txt
python main.py
```
Not: Çalıştırdıktan sonra trafik_kumeleme_haritasi.html dosyasını açarak kümeleme sonucunu harita üzerinde görebilirsiniz.

