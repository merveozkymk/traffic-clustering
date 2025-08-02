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

## Veri Seti

Projedeki trafik yoğunluğu verisi, T.C. Çevre, Şehircilik ve İklim Değişikliği Bakanlığı'nın sağladığı **resmi açık veri** platformundan alınmıştır.

🔗 [2025 Trafik Yoğunluğu Veri Seti](https://ulasav.csb.gov.tr/dataset/34-hourly-traffic-density-data-set/resource/70ecde5b-95ff-4168-b650-d726923408e8)

Veriyi indirip `traffic_density_202501.csv` olarak kaydederek `main.py` ile aynı klasöre koymanız yeterlidir.

## Çalıştırmak İçin

```bash
pip install -r requirements.txt
python main.py
```
Çalıştırma sonrası `trafik_kumeleme_haritasi.html` dosyası oluşur. Bu dosya tarayıcıda açılarak kümelerin harita üzerindeki dağılımı incelenebilir.

