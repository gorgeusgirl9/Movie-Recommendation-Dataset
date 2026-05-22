https://huggingface.co/spaces/gorgeus/Movie_Recommendation_Dataset
https://github.com/gorgeusgirl9/Movie-Recommendation-Dataset
https://www.kaggle.com/code/gorgeusgirl/movie-recommendation-dataset


# 🎬 Film Öneri Sistemi (Content-Based Recommendation)

## Proje Hakkında
Bu proje, kullanıcıların seçtiği filmlere dayanarak benzer özelliklere sahip (tür, anahtar kelimeler, özet) 5 adet film önerisinde bulunan interaktif bir **İçerik Tabanlı Öneri Sistemi** (Content-Based Recommender System) uygulamasıdır.

## Teknik Yaklaşım
Sistem, `scikit-learn` kütüphanesini kullanarak metinsel verileri vektörel uzaya taşır ve filmler arasındaki anlamsal benzerliği hesaplar:

- **Veri İşleme:** `pandas` kullanılarak ham veri seti temizlendi ve 'genres', 'overview' sütunları birleştirilerek özgün bir 'tags' özniteliği oluşturuldu.
- **Vektörleştirme:** `CountVectorizer` ile metinler sayısal vektörlere dönüştürüldü (5000 özellik ile sınırlandırıldı).
- **Benzerlik Analizi:** `Cosine Similarity` metriği kullanılarak tüm filmler arası açısal uzaklıklar hesaplandı.
- **Deployment:** Uygulama `Streamlit` ile interaktif bir dashboard arayüzüne dönüştürülerek canlıya alındı.

## Kurulum ve Çalıştırma
Projeyi kendi ortamınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:
