import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- Görüntüyü Yükle ---
# 'orijinal_goruntu.jpg' yerine kendi dosya yolunuzu yazın.
# cv2.IMREAD_GRAYSCALE ile görüntüyü doğrudan gri seviyeli olarak okuyoruz.
image_path = 'indir1.jpg' 
orijinal_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Görüntü yüklenemezse hata ver
if orijinal_img is None:
    print(f"Hata: Görüntü yüklenemedi. Dosya yolunu kontrol edin: {image_path}")
    # Programı sonlandır veya bir varsayılan görüntü oluştur
else:
    print("Orijinal görüntü başarıyla yüklendi.")

# --- Yardımcı Fonksiyonlar (Histogram ve Karşılaştırma için) ---

def plot_histogram(ax, img, title):
    """Verilen matplotlib eksenine görüntünün histogramını çizer."""
    ax.hist(img.ravel(), 256, [0, 256])
    ax.set_title(title)
    ax.set_xlim([0, 256])

def show_comparison(orig, processed, method_name):
    """Orijinal ve işlenmiş görüntüyü ve histogramlarını yan yana gösterir."""
    
    # 2x2 bir çizim alanı oluştur
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Orijinal Görüntü
    axes[0, 0].imshow(orig, cmap='gray')
    axes[0, 0].set_title('Orijinal Görüntü')
    axes[0, 0].axis('off')
    
    # Orijinal Histogram
    plot_histogram(axes[1, 0], orig, 'Orijinal Histogram')
    
    # İşlenmiş Görüntü
    axes[0, 1].imshow(processed, cmap='gray')
    axes[0, 1].set_title(f'{method_name} Sonucu')
    axes[0, 1].axis('off')
    
    # İşlenmiş Histogram
    plot_histogram(axes[1, 1], processed, f'{method_name} Histogramı')
    
    plt.tight_layout()
    plt.suptitle(f'Yöntem Karşılaştırması: {method_name}', fontsize=16, y=1.03)
    
    # Görseli kaydetmek için (Teslim Edilmesi Gerekenler 1)
    plt.savefig(f'sonuc_{method_name.lower().replace(" ", "_")}.png')
    plt.show()


# 1. Histogram Eşitleme
he_img = cv2.equalizeHist(orijinal_img)

# Sonuçları göster ve kaydet
show_comparison(orijinal_img, he_img, 'Histogram Eşitleme')


# 2. CLAHE
# Parametreler: clipLimit kontrastı sınırlar, tileGridSize ise görüntünün bölüneceği ızgara boyutudur.
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_img = clahe.apply(orijinal_img)

# Sonuçları göster ve kaydet
show_comparison(orijinal_img, clahe_img, 'CLAHE')


# 3. Histogram Germe (Normalization)
# cv2.NORM_MINMAX, piksel değerlerini 0-255 aralığına gerer.
stretched_img = cv2.normalize(orijinal_img, None, 0, 255, cv2.NORM_MINMAX)

# Sonuçları göster ve kaydet
show_comparison(orijinal_img, stretched_img, 'Histogram Germe')


# 4. Logaritmik Dönüşüm (DÜZELTİLMİŞ KOD)

# NumPy veri tipi taşması (overflow) ve log(0) hatasından kaçınmak için
# görüntüyü önce float tipine dönüştürmeliyiz.
img_float = np.float64(orijinal_img)

# c sabitini hesaplarken de float versiyonun max değerini kullanalım
c = 255 / np.log(1 + np.max(img_float))

# Log dönüşümünü ( s = c * log(1 + r) ) float dizi üzerinde uygula
log_img_float = c * (np.log(img_float + 1))

# İşlem bittikten sonra, sonucu tekrar 0-255 aralığındaki
# uint8 tipine güvenle dönüştürebiliriz.
log_img = np.array(log_img_float, dtype=np.uint8)

# Sonuçları göster ve kaydet
show_comparison(orijinal_img, log_img, 'Logaritmik Dönüşüm')


# 5. Gamma Dönüşümü
# Farklı gamma değerlerini deneyelim
gamma_values = [0.4, 1.0, 2.5]

for gamma in gamma_values:
    # Gamma düzeltmesi için bir 'lookup table' (arama tablosu) oluşturmak daha verimlidir.
    # Formül: s = 255 * (r / 255) ^ gamma
    lookUpTable = np.empty((1, 256), np.uint8)
    for i in range(256):
        lookUpTable[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    
    gamma_img = cv2.LUT(orijinal_img, lookUpTable)
    
    method_title = f'Gamma Dönüşümü (Gamma={gamma})'
    show_comparison(orijinal_img, gamma_img, method_title)

# Orijinal görüntüyü göster (başlangıç noktası)
# plt.figure(figsize=(6, 6))
# plt.imshow(orijinal_img, cmap='gray')
# plt.title('Orijinal Görüntü')
# plt.axis('off')
# plt.show()