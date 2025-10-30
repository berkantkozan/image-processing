
````markdown
# Histogram Tabanlı Görüntü İyileştirme Uygulamaları

Bu proje, "Görüntü İşleme" dersi ödevi (ÖDEV-I) kapsamında geliştirilmiştir. Python, OpenCV ve Matplotlib kütüphanelerini kullanarak, bir gri seviyeli görüntü üzerinde 5 farklı histogram tabanlı iyileştirme tekniğini uygular ve sonuçları görsel olarak karşılaştırır.

## 🚀 Uygulanan Yöntemler

Bu betik, aşağıdaki 5 temel görüntü iyileştirme yöntemini uygular:

1.  **Histogram Eşitleme (Histogram Equalization):** Görüntünün genel kontrastını artırmak için klasik global histogram eşitleme.
2.  **Uyarlamalı Histogram Eşitleme (CLAHE):** Görüntüyü küçük bölgelere (tiles) ayırarak yerel kontrastı iyileştiren gelişmiş bir yöntem.
3.  **Histogram Germe (Histogram Stretching):** Piksel değer aralığını 0-255 arasına "gererek" düşük kontrastlı görüntüleri canlandıran bir normalizasyon tekniği.
4.  **Logaritmik Dönüşüm (Log Transformation):** `s = c * log(1 + r)` formülü ile özellikle karanlık bölgelerdeki detayları belirginleştirmek için kullanılır.
5.  **Gamma Dönüşümü (Power-Law Transformation):** `s = c * r^gamma` formülü ile görüntünün parlaklık dengesini esnek bir şekilde ayarlar. Betik, üç farklı `gamma` (gamma) değeri (0.4, 1.0, 2.5) ile test yapar.

## 🛠️ Gereksinimler

Betiği çalıştırmak için aşağıdaki Python kütüphanelerinin kurulu olması gerekmektedir:

* **OpenCV (cv2):** Görüntü işleme fonksiyonları için.
* **NumPy:** Veri dizileri ve matematiksel işlemler için.
* **Matplotlib:** Görüntüleri ve histogramları görselleştirmek için.

Bu kütüphaneleri `pip` kullanarak yükleyebilirsiniz:

```bash
pip install opencv-python-headless
pip install numpy
pip install matplotlib
````

## 🏃‍♀️ Nasıl Çalıştırılır?

1.  Betiği (örn. `odev.py` olarak) ve iyileştirmek istediğiniz görüntü dosyasını (örn. `indir1.jpg`) aynı dizine kaydedin.

2.  Betik içerisindeki `image_path` değişkenini kendi görüntü dosyanızın adıyla güncelleyin:

    ```python
    # 'indir1.jpg' yerine kendi dosya yolunuzu yazın.
    image_path = 'indir1.jpg' 
    orijinal_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    ```

3.  Terminal veya komut istemcisini açın ve betiğin bulunduğu dizine gidin.

4.  Aşağıdaki komutla betiği çalıştırın:

    ```bash
    python odev.py
    ```

## 📊 Çıktılar

Betiği çalıştırdığınızda, her yöntem için:

1.  **Ekranda Gösterim:** Orijinal görüntü, işlenmiş görüntü ve bu iki görüntünün histogramlarını içeren bir karşılaştırma grafiği (`matplotlib` penceresinde) açılır.
2.  **Dosya Kaydı:** Aynı karşılaştırma grafiği, `sonuc_histogram_eşitleme.png`, `sonuc_clahe.png`, `sonuc_gamma_dönüşümü_(gamma=0.4).png` vb. isimlerle `.png` formatında betiğin bulunduğu dizine otomatik olarak **kaydedilir**.

<!-- end list -->

```

---

Bu metni kopyalayıp, projenizin olduğu dizinde `README.md` adıyla yeni bir dosyaya yapıştırabilirsiniz.
```