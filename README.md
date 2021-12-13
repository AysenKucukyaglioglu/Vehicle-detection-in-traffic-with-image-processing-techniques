# Vehicle detection in traffic with image processing techniques

**Görüntü İşleme ve OpenCV ile Trafikte Araç Algılama**

Bu çalışma görüntü işleme teknikleri kullanılarak Python ve OpenCV Kütüphanesi ile geliştirilmiştir. Projedeki amaç görüntüdeki araçların algılanması ve işaretlenmesi işlemidir. Bunun için girdi olarak mobese görüntüleri kullanılmıştır. Görüntü alınır ve işlemlerden geçirilir, görüntüdeki araçlar algılanır. 
Temel görüntü işleme metotlarının da kullanıldığı bu çalışmada video görüntüsü ‘cv2.VideoCapture()’ fonksiyonu ile çağrılarak başlanmıştır. Sonrasında arka plan çıkarma işlemi yapılmıştır. Bu işlem openCV kolaylığı ile yapılmıştır. Videodan yakalanan resim Şekil 1 de gösterilmiştir.
 
![şekil 1](https://github.com/AysenKucukyaglioglu/Vehicle-detection-in-traffic-with-image-processing-techniques/blob/main/videodan%20yakalnm%C4%B1%C5%9F%20resim.png)


Video görüntüsü alındıktan sonra arka plan çıkarma işlemi uygulanmıştır. Arka plan çıkarma işlemi görüntü işleme uygulamalarında sıklıkla kullanılan bir yöntemdir. Sabit bir zemin üzerindeki hareketli nesneleri yakalamak ve takip etmek için kullanılır. Bu işleyişteki mantık sabit arka planı referans alarak üzerindeki değişiklikleri yakalamaktır. Algoritma sabit kalan kısmı yani arka planı tespit eder ve üzerindeki değişiklikleri tespit ederek hareketleri yakalayabilir. Hareketli nesne tespiti için diğer yöntemlere göre daha hızlıdır çünkü baktığı tek şey sabit arka planı yakalamak ve diğer her şeyi bu referansa göre değerlendirmektir. Bu işlem createBackgroundSubtractorMOG2() fonksiyonu yardımıyla yapılmıştır. Arka planı çıkarılmış resim Şekil 2 de gösterilmiştir.
 
![şekil 2](https://github.com/AysenKucukyaglioglu/Vehicle-detection-in-traffic-with-image-processing-techniques/blob/main/arka%20plan%C4%B1%20%C3%A7%C4%B1kar%C4%B1lm%C4%B1%C5%9F%20resim.png)


Bu işlemlerin ardından siyah beyazlaşmış resim üzerinden cv2.findContours() fonksiyonu ile konturlar bulunmuştur. Konturlar, aynı renk veya yoğunluğa sahip olan tüm kesintisiz noktaları (sınır boyunca) birleştiren bir eğri olarak basitçe açıklanabilir. Konturlar, şekil analizi, nesne algılama ve tanıma için yararlı bir araçtır.
Dış hatlardaki algılanan araçlar için dikdörtgenler çizilmiştir. Bu işlem boundingRect() ve rectangle() methodları ile yapılmıştır.
Dikdörtgen işlemi Şekil 3 te gösterilmiştir.

 
![şekil 3](https://github.com/AysenKucukyaglioglu/Vehicle-detection-in-traffic-with-image-processing-techniques/blob/main/i%C5%9Faretlenmi%C5%9F%20resim.png)



**Sonuçlar ve Tartışma**
Görüntü işleme tekniklerinden yararlanarak otoyol trafiğinde akan araçların ilk olarak tanımlanması, daha sonra tanımlanan araçların sayılması ve şerit yoğunluklarının belirlenmesi iki farklı yöntem kullanılarak gerçekleştirilmiştir. Moment alan metodu ve çizgi metodunda sırası ile %92.5 ve %96.3 oranlarında başarı elde edilerek kullanılabilirlikleri ispatlanmıştır. Bu yöntemler kullanılarak geliştirilen uygulamaların yaygınlaşması ile karayolu düzenlemelerinde kullanılabilecek trafik verilerine kolaylıkla erişim imkânı sağlanacaktır. Aynı zamanda trafik yoğunluğunun belirlenmesinde ve sinyalizasyon çalışmalarında kullanılarak trafik problemlerinin çözümünde yardımcı olacağı düşünülmektedir. Araçların tespit edilmesi ve sayılmasının yanı sıra araçların sınıflandırılması da gerçekleştirilebilir. Böylece karayollarında belirlenen bölgelerin veya şeritlerin araç türlerine göre kullanım oranları tespit edilebilecektir.

Görüntü işleme teknikleri ve OpenCV kullanılarak geliştirilen bu uygulama ile otoyol trafiğinde akan araçların tanımlanması ve algılanması, trafik yoğunluğunun belirlenmesi gerçekleştirilmiştir. Kullanılan bu yöntemler geliştirilen trafik bazlı uygulamaların yaygınlaşması, karayolları düzenlemelerinde kullanılabilmek için uygulanabilir bir yöntem olmuştur. Bu uygulamanın trafik verilerine kolaylık sağlaması amaçlanmıştır. Aynı zamanda trafik yoğunluğunun belirlenmesinde ve sinyalizasyon çalışmalarında kullanılarak trafik problemlerinin çözümünde yardımcı olacağı düşünülmektedir. Araçların tespit edilmesi yanı sıra araçların sınıflandırılması da gerçekleştirilebilir. Böylece karayollarında belirlenen bölgelerin veya şeritlerin araç türlerine göre kullanım oranları tespit edilebilecektir.
