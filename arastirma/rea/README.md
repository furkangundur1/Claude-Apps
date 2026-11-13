# REA: tersine mühendislik aracı

REA, yazılımların içini incelemek için kullanılan, komut satırından ve MCP üzerinden yapay zekâ ajanlarına bağlanan bir araç. Kaynak: `furkangundur1/rea` (morluto/rea'nın fork'u).

## Kurulum (Linux / bulut ortamı)

```bash
git clone https://github.com/furkangundur1/rea && cd rea
export PATH="/opt/node24/bin:$PATH"   # depo Node 24.22.1'e sabitli (.nvmrc)
npm ci
npm run build:cached
npm link                              # "rea" komutu her yerden çalışır
rea --version                         # 6.9.0
```

## Bulgular

- Ghidra, IDA, Hopper ya da Kuna olmadan çalışan komutlar sınırlı: `audit-release-exposure` gibi dosyayı tanıyan komutlar çalışıyor.
- Derin analiz (`analyze`, `decompile`) için bir motor gerekiyor. En kolayı Ghidra 12.1 veya üstü: Java 21 ve `GHIDRA_INSTALL_DIR` ortam değişkeni.
- `inspect-binary-layout` için pwntools içeren bir Python gerekiyor (`REA_PWNTOOLS_PYTHON`).
- Web siteleri için `analyze-web-bundle` var. Uzaktan hata ayıklama modunda açılmış bir Chrome'a bağlanıp sayfanın yüklediği scriptleri inceliyor. Sunucuda çalışan kısımları göremez.

## İlk ders: Kasa Laboratuvarı

`uygulamalar/kasa-laboratuvari` sayfası, küçük bir C programının şifresini makine kodundan bulma adımlarını gösteriyor:

1. `strings` ile gömülü yazılar → `kirmizi-elma-42`
2. `nm` ile fonksiyon adları → `sifre_kontrol`
3. `objdump` ile makine kodu → `strcmp` ile sabit yazıyla karşılaştırma

Programın makine kodundan geri çevrilmiş hali [`kasa.c`](kasa.c) dosyasında.
