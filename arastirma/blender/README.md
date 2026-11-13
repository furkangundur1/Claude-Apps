# Blender'ın iç yapısı: ölçümler

Blender 4.0.2 (Ubuntu paketi) kuruldu ve kendi Python arayüzü üzerinden ölçüldü. Ölçüm betiği: [`olc.py`](olc.py)

```bash
blender -b --factory-startup --python olc.py
```

## Bulgular

- **Varsayılan sahne:** Cube, Light, Camera.
  - Küp: konum (0, 0, 0), ölçek 1, 8 köşe, 12 kenar, 6 yüz, 2×2×2 m.
  - Işık: nokta ışık, 1000 W, konum (4.0762, 1.0055, 5.9039), dönüş (37.26°, 3.16°, 106.94°).
  - Kamera: konum (7.3589, -6.9258, 4.9583), dönüş (63.56°, 0°, 46.69°), 50 mm lens.
- **Nesne ile şekil verisi ayrı:** Nesne konum, dönüş ve ölçeği tutar; şekli "mesh" verisi tutar. Bir mesh birden çok nesne tarafından paylaşılabilir (bağlı kopya, Alt+D).
- **Eksenler ve birim:** Yukarı Z ekseni, birim metre.
- **Hazır şekiller:** 11 (circle, cone, cube, cylinder, grid, ico_sphere, monkey, plane, torus, uv_sphere ve gizmo'lu küp).
- **İşlemler:** Program içinde 213 `OBJECT_OT_*` nesne işlemi tanımlı.
- **Dosya biçimi:** .blend dosyaları `BLENDER-v400` imzasıyla başlar. Biçim kendi kendini tarif eder: içindeki SDNA bloğu bütün veri yapılarını listeler.
- **Bağımlılıklar:** Ana dosya 79 MB; 340 kütüphaneye bağlı (Python 3.12, OpenGL, OpenEXR, OpenColorIO, OpenVDB, Embree, TBB, FFmpeg vb.).

## Bu bulgularla yapılanlar

- `uygulamalar/mini-3d-atolye`: aynı veri modeliyle (nesne + paylaşılabilir mesh, Z yukarı, G/R/S kısayolları) sıfırdan yazılmış prototip.

## Neden Blender'ın kendisi tarayıcıya eklenemez

- Boyut: milyonlarca satır C/C++ ve 79 MB'lık ana dosya. Yapıt sayfa sınırı 16 MB.
- Resmi bir tarayıcı sürümü yok.
- GPL lisansı: kodu kullanılırsa uygulamanın tamamı GPL olmak zorunda.
