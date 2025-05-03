# Steganaliz Teknikleri

## LSB (Least Significant Bit Insertion) Algoritması
Bu algoritmada mesajın, ses veya görüntü dosyasının en düşük anlamlı bitleri ile değiştirilerek dosyada minimum bozulma ile saklanması amaçlanmaktadır.

Örnekte 160 karakterlik bir mesaj wav formatındaki dosya içeriğine önce gizlenmiş, sonrasında gizlenen mesajın görüntülenmesi sağlanmıştır. Mesajin gizlenmesi sırasında dosyasın boyutunda herhangi bir değişiklik gözlemlenmemiştir. Çünkü mesajın gizlenmesi sırasın dosyaya yeni veriler eklenmemiş varsayılan veriler üzerinde değişiklikler gerçekleştirilmiştir.