# Steganaliz Teknikleri

## LSB (Least Significant Bit Insertion) Algoritması
Bu algoritmada mesajın, ses veya görüntü dosyasının en düşük anlamlı bitleri ile değiştirilerek dosyada minimum bozulma ile saklanması amaçlanmaktadır.

Örnekte 160 karakterlik bir mesaj wav formatındaki dosya içeriğine önce gizlenmiş, sonrasında gizlenen mesajın görüntülenmesi sağlanmıştır. Mesajin gizlenmesi sırasında dosyasın boyutunda herhangi bir değişiklik gözlemlenmemiştir. Çünkü mesajın gizlenmesi sırasında dosyaya yeni veriler eklenmemiş varsayılan veriler üzerinde değişiklik gerçekleştirilmiştir.

## JPEG Algoritması (DCT)
LSB yöntemi ses gibi ham veri içeren dosyalarda (.wav) doğrudan bit düzeyinde çalışırken, JPEG gibi sıkıştırılmış görsellerde bu mümkün değildir. Bunun yerine DCT algoritması kullanılır. JPEG sıkıştırmasında görüntü, 8x8 bloklara bölünür, her blok DCT dönüşümüne tabi tutulur. DCT katsayılarının en düşük etkili olanları değiştirilerek mesaj gizlenir. Bu yöntem kullanılarak elde edilen yeni görüntünün boyutunda küçülme gözlemlenmiştir.

## BPCS (Bit Plane Complexity Segmentation) Algoritması
Bu yöntem, özellikle yüksek karmaşıklığa sahip bölgeleri hedef alarak verilerin gizlenmesini sağlar. BPCS algoritması, medya dosyasındaki her bir bit düzeyindeki karmaşıklığı analiz eder ve bu bitleri mesaj bitleri ile değiştirerek mesajın gizlenmesini sağlar. 
 
Örnekte 160 karakterlik bir mesaj wav formatındaki dosya içeriğine önce gizlenmiş, sonrasında gizlenen mesajın görüntülenmesi sağlanmıştır. Mesajin gizlenmesi sırasında dosyasın boyutunda herhangi bir değişiklik gözlemlenmemiştir.

## Maskeleme Ve Filtreleme Yöntemleri
Maskeleme ve filtreleme, insan duyularının (özellikle görme ve işitme) algılayamadığı sınırları kullanarak veri gizleme işlemidir. Veriler, hedef medya dosyasının algılanamaz özellikleri içine gömülür ve veri gizleme işlemi gerçekleştirilir. 

Ses dosyalarında; yüksek frekanslı, gürültülü bölgelere veri gizlenirken video dosyalarında sahne geçişinin olduğu hareketli bölgelere veri gizlenmektedir. Görüntü dosyalarında ise renk geçişi bölgeleri verileri gizlemek için kullanılmaktadır.

Örnekte bu yöntem kullanılarak bir wav dosyasına 160 karakterlik bir veri gizleme işlemi gerçekleştirilmiştir. Bu işlem sonucunda dosya boyutunda herhangi bir değişiklik gözlemlenmemiştir. 

# Sezgisel Steganaliz Yöntemleri
Sezgisel Steganaliz Yöntemleri, steganografiyle gizlenmiş bilgileri tespit etmek için kullanılan, sezgiye dayanan analiz yöntemleridir. Bu yöntemler, matematiksel modellerden çok, belirli ipuçlarına, anomalilere ya da örüntülere dayalı çıkarımlar yapar.

