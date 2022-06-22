# Project_Devrim

Araba yakıt ve elektrik tüketimi hesaplama programı.

## Bot Fuel Tr

Bot Script; Aytemiz Petrol sayfasına bağlanıp güncel akaryakıt fiyatlarını (benzin, mazot ve lpg) alıp daha sonra bunu veritabanına kaydediyor. Script her gün saat 8:45'te otomatik olarak çalışmakta ve güncellemiş olduğu veritabanını GitHub Proje sayfasına göndermektedir.

## Menü

### 11. Elektrikli araç şarj maliyeti hesapla

Elektrikli araçlar için depo dolum maliyeti, fabrika ve kullanıcı verisine göre menzil ve km başına kaç liralık elektrik harcadığı bilgisini veriyor.

### 12. Hibrit araç şarj/depo dolum maliyeti hesapla

Bu modül yapım aşamasında.

### 13. Benzinli/Dizel araç depo dolum maliyeti hesapla

Benzinli / Dizel araçlar için depo dolum maliyeti, fabrika verisine göre menzil ve km başına kaç liralık akaryakıt harcadığı bildisini veriyor.

### 21. Araç bilgisi göster

Bu modül yapım aşamasında.

### 22. Tüm araçların bilgisini göster

Veri tabanında olan tüm araçları listeleyebilirsiniz.

### 31. Güncel akaryakıt fiyatlarını göster

Bugün geçerli olan akaryakıt satış pompa satış fiyatlarıdır.

### 32. Geçmiş akaryakıt fiyatlarını göster

Geçmiş günlere ait akaryakıt fiyatlarıdır.

### 41. Güncel elektrik fiyatlarını göster

EPDK tarafından yayınlan tüm abone gruplarına ait güncel elektrik fiyatlarıdır. Fiyatlar baz fiyatlardır. Son tüketici için dağıtım ücretleri ve vergilerin hesaplanarak eklenmesi gerekiyor.

## car.db

Araba bilgilerinin bulunduğu veritabanıdır. Elektrikli, Hibrit ve İçten yanmalı araçlar için 3 farklı tablo bulunmaktadır.

## unitprices.db

Birim fiyatların olduğu veritabanı. Güncel ve geçmişe ait elektrik ve akayarkıt fiyatları bulunmaktadır.
