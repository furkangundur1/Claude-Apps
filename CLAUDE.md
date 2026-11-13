# Yapay zekâ asistanları için çalışma notları

Bu depo kullanıcının bütün projelerinin merkezidir. Bir sohbette bu deponun yolu verildiyse önce `README.md` dosyasını oku; hangi uygulamanın nerede olduğu ve canlı adresleri orada.

## Kullanıcı hakkında

- Türkçe konuşur ve yazar. Bütün cevaplar, arayüz metinleri ve belgeler Türkçe olmalı.
- Çoğunlukla sesle ya da telefondan yazar; kelimeler bozuk gelebilir. Bağlamdan anlamaya çalış, emin değilsen kısa bir soru sor.
  - "tersine mühendislik", "rüya", "rea", "reha" genellikle **REA** aracını kasteder.
  - "kemik atölyesi" ana projeyi, Kemik Atölyesi uygulamasını kasteder.
- Arkeolog: kemik eserler ve seramik kaplar üzerine çalışır. Aynı zamanda müzisyendir ve Logic Pro kullanır.
- Hızlı ilerleyen prototipleri sever, ayrıntıyı sonra ister. Önce mantığı kısaca anlat, sonra işe başla.
- Yapılan her şeyin bu depoda kalıcı olarak saklanmasını ister.

## Uygulamalarla nasıl çalışılır

- Her uygulama tek dosyalık bir HTML sayfası: `uygulamalar/<ad>/index.html`.
- Canlı sürümler claude.ai yapıtı (artifact) olarak yayınlanır; adresler `README.md` tablosunda.
- Bir uygulamayı değiştirirken:
  1. Önce canlı yapıtı oku (başka bir sohbette değişmiş olabilir). Depodaki kopyadan farklıysa canlı olanı esas al ve depoyu güncelle.
  2. Değişikliği yap, tarayıcıda dene (Playwright), sonra **aynı adrese** yayınla. Adres değişmemeli.
  3. Değişen dosyayı bu depoya kaydet ve gönder (commit + push).
- Yayınlanmış sayfaları okurken servis, dosyanın başına kendi `<!doctype html>…<body>` satırını ve sonuna `</body></html>` ekleyebilir. Depoya kaydetmeden önce bu sarmalayıcıyı çıkar; depodaki dosya yayınlanan kaynaktır.
- Kemik Atölyesi'nin `foto/`, `kucuk/`, `levha/`, `modeller/` klasörleri sayfayla birlikte yayınlanan dosyalardır. Yalnızca `index.html` değiştiyse sadece onu yayınlamak yeterli; diğer dosyalar yapıtta kalır.

## Kemik Atölyesi'nin iç yapısı (kısa)

- Three.js 0.128 kullanır.
- Geometri çekirdeği `const C = (() => { ... })()` bloğundadır. Gövde `makeModel()` içindeki `outer(t, θ)` fonksiyonuyla tanımlanır: `t` yükseklik (0 taban, 1 ağız), `θ` açı.
- Arayüz parametreleri `DEFAULTS` nesnesinde tutulur, `kernelParams()` onları çekirdeğe çevirir.
- `.kfld` sınıflı alanlar `data-key` ile otomatik bağlanır. Yeni bir ayar eklemek için `DEFAULTS`, `kernelParams` ve HTML alanı yeterlidir.
- Yeni yüzey desenleri "Yeni kabartma desenleri" bölümündeki `NEW` / `INFO` listelerine eklenir.
- VaseMaker'dan gelen kod MIT lisanslıdır; lisans notu kodda durmalıdır (`arastirma/vasemaker`).

## Sınırlar

- Kapalı kaynak yazılımların (Logic Pro, Meshy vb.) kodu ya da tasarımı kopyalanmaz. Çalışma mantığından ilham alınıp kendi kodumuz yazılır.
- Açık kaynak kod kullanılırsa lisansı kontrol edilir: MIT serbesttir, ama kaynak gösterilir; GPL kod, bütün uygulamanın GPL olmasını gerektirir.
