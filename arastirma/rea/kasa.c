/* Kasa Laboratuvarı: makine kodundan (objdump, x86-64) geri çevrilmiş kaynak.
   Değişken adları derlemede kaybolduğu için yeniden verildi; fonksiyon adları dosyada duruyordu.
   Derleme: gcc -O1 -o kasa kasa.c */
#include <stdio.h>
#include <string.h>

int sifre_kontrol(const char *girilen) {
    return strcmp(girilen, "kirmizi-elma-42") == 0;
}

int main(void) {
    char tampon[64];
    printf("Kasa sifresi: ");
    if (fgets(tampon, sizeof tampon, stdin) == NULL)
        return 1;
    tampon[strcspn(tampon, "\n")] = '\0';   /* Enter'ı sil */

    if (sifre_kontrol(tampon))
        puts("Kasa acildi!");
    else
        puts("Yanlis sifre.");
    return 0;
}
