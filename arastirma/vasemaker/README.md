# VaseMaker → Kemik Atölyesi

[VaseMaker](https://github.com/dcityorg/vasemaker), Gary Muhonen'in tarayıcıda çalışan parametrik vazo tasarımcısı. MIT lisanslı (lisans metni: [`VASEMAKER-LICENSE.txt`](VASEMAKER-LICENSE.txt)). Next.js, three.js ve React Three Fiber ile yazılmış, yaklaşık 43 bin satır.

## Taşınanlar (Kemik Atölyesi sürüm 20)

Kod, Kemik Atölyesi'nin kendi geometri çekirdeğine uyarlandı. VaseMaker'ın arayüzü kopyalanmadı.

1. **Kesit şekilleri** (`SECTION_SHAPES`, çekirdekte §3b): çokgen, gül, dişli, limaçon (kalp), Cassini (fıstık), damla, böbrek, yonca, sikloid (yıldız), süperformül, yumurta. Her şeklin en büyük yarıçapı 1'e ölçeklenir, böylece ağız ölçüleri (L, W) dış sınır olarak kalır. En dar yer, en geniş yerin %18'inin altına inmez; bu sınır cidarın kendi içine çakışmasını önler.
2. **Şekil geçişi:** taban kesiti (`sec_a`) ile ağız kesiti (`sec_b`) arasında yükseklik boyunca doğrusal geçiş.
3. **Bükme:** `twist` (derece) ve `twist_wave`. Formül VaseMaker'daki sineTwist ile aynı: açı = en büyük açı · sin(dalga · 90° · t).
4. **Dokular:** dalga sırtı, yuvarlak çubuk, kare oluk, sepet örgüsü, Voronoi hücre, taş dokusu (`vm-*` anahtarlı desenler).

## Doğrulama

- 11 şekil × (geçişsiz, geçişli, bükmeli, dalgalı bükmeli) = 48 kombinasyon: hepsi kapalı ağ, kopuk kenar yok.
- Yeni ayarlara dokunulmadığında eski modellerin köşe koordinatları bit bit aynı.
- Tarayıcıda gül kesiti, bükme, geçiş, Voronoi ve sepet örgüsü denendi; konsol hatası yok.

## Henüz taşınmayanlar

- MoldMaker: alçı döküm kalıbı parçaları (bölünmüş iki, üç parçalı; dökme ağzı)
- HandleMaker: kulp ve kulp kalıbı
- SprigMaker: SVG, görsel ya da yazıdan kabartma süs ve kalıbı
- Delikli (cutout) gövde, taban mührü, eğri tutamaçlı profil düzenleyici, Bezier ile ofset ve bükme eğrileri
