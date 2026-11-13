# Atölye

Furkan Gündür'ün uygulamalarının, araştırma notlarının ve belgelerinin ana deposu. Bütün projeler burada toplanır. Yeni bir sohbette bu deponun yolunu vermek, o sohbetin her şeyi buradan okuyup devam edebilmesi için yeterlidir.

Yapay zekâ asistanları için çalışma kuralları [`CLAUDE.md`](CLAUDE.md) dosyasındadır.

## Uygulamalar

Her uygulama tek bir HTML sayfasıdır ve claude.ai'de "yapıt" (artifact) olarak yayınlanır. Depodaki dosya kaynaktır; yayınlanmış adres, kullandığın canlı sürümdür.

| Uygulama | Klasör | Canlı adres | Ne yapar |
|---|---|---|---|
| **Kemik Atölyesi** (ana proje) | [`uygulamalar/kemik-atolyesi`](uygulamalar/kemik-atolyesi) | https://claude.ai/artifact/JXHhcf8B6G6e5UssSe3ypK | Arkeolojik kemik eser ve kap stüdyosu: 3B form, desen, kulp, teknik çizim, rapor, proje galerisi. VaseMaker'dan kesit şekilleri, bükme ve 6 doku eklendi (sürüm 20). |
| **Ses Atölyesi** | [`uygulamalar/ses-atolyesi`](uygulamalar/ses-atolyesi) | https://claude.ai/artifact/Wt1Bp6avCUN8TnkDcLD3Zs | Tarayıcıda müzik stüdyosu (DAW): Logic Pro düzenine benzeyen arayüz, FL Studio tarzı adım sıralayıcı, piyano rulosu, mikser, akıllı kontroller, sentez sesler, klavyeden kayıt. |
| **ArkeoKap Stüdyo** | [`uygulamalar/arkeokap-studyo`](uygulamalar/arkeokap-studyo) | https://claude.ai/artifact/1BZDbxrU6TdtMX6uHWhipn | Arkeolojik seramik kap stüdyosu. Kemik Atölyesi bunun üzerine kuruldu. |
| **Çanak Çömlek Stüdyosu** | [`uygulamalar/canak-comlek-studyosu`](uygulamalar/canak-comlek-studyosu) | https://claude.ai/artifact/EuRrSzB7qkwcVug4QJedrf | İlk seramik kap modelleyici. ArkeoKap'ın atası. |
| **Kemik Eserler 3B** | [`uygulamalar/kemik-eserler-3b`](uygulamalar/kemik-eserler-3b) | https://claude.ai/artifact/Ggoc5eeGsTdrajxaK93bFs | Kemik eserlerin 3B modellerini gösteren sayfa. Modeller Kemik Atölyesi'ndekilerle aynı. |
| Kemik Atölyesi (eski sürüm) | [`uygulamalar/kemik-atolyesi-eski`](uygulamalar/kemik-atolyesi-eski) | https://claude.ai/artifact/5E4LnPPuHZrWxdsemF8n1y | Önceki ayrı Kemik Atölyesi. Görseller ana Kemik Atölyesi klasöründe. |
| Mini 3D Atölye | [`uygulamalar/mini-3d-atolye`](uygulamalar/mini-3d-atolye) | https://claude.ai/artifact/BzYHfw4R8x8fvXoKWTRmeL | Blender'ın veri modeli incelenerek sıfırdan yazılmış küçük 3B editör prototipi. |
| Kasa Laboratuvarı | [`uygulamalar/kasa-laboratuvari`](uygulamalar/kasa-laboratuvari) | https://claude.ai/artifact/5TosLXgnUZnUw8kJpCmEEd | İlk tersine mühendislik dersi: küçük bir programın şifresini makine kodundan bulma. |

### Kemik Atölyesi'nin verileri

`uygulamalar/kemik-atolyesi/` içinde sayfanın kullandığı dosyalar da var:

- `foto/`: eser fotoğrafları (AP06–AP09 envanter numaraları)
- `kucuk/`: küçük önizleme görselleri
- `levha/`: yayın levhaları
- `modeller/`: tamamlanmış 3B modeller (JSON)

Sayfa bu dosyaları göreli yolla (`foto/...`) okur, bu yüzden klasör yapısı bozulmamalıdır.

## Belgeler

Claude Docs'ta duran, birlikte düzenlenen belgeler. Adresleri ve özetleri [`belgeler/README.md`](belgeler/README.md) içinde.

## Araştırma

- [`arastirma/rea`](arastirma/rea): REA (tersine mühendislik aracı) kurulumu ve kullanımı.
- [`arastirma/blender`](arastirma/blender): Blender'ın iç yapısını ölçtüğümüz betik ve bulgular.
- [`arastirma/vasemaker`](arastirma/vasemaker): VaseMaker'dan Kemik Atölyesi'ne neyin, nasıl taşındığı ve lisansı.

## Yol haritası

- **Kemik Atölyesi:** VaseMaker'ın döküm kalıbı üreticisi, kabartma süs (sprig), delikli gövde, taban mührü; modifier yığını; heykel (sculpt) fırçaları.
- **Ses Atölyesi:** Ableton tarzı döngü ızgarası, WAV dışa aktarma, mikrofonla kayıt, örneklenmiş sesler, otomasyon.
- **Genel:** Blender .blend dosyası okuma.
