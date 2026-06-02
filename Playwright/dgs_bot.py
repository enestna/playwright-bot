import os
import json
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

def dgs_akilli_veri_botu():
    klasor_adi = "DGS_Veri_Arsivi"
    if not os.path.exists(klasor_adi):
        os.makedirs(klasor_adi)

    with sync_playwright() as p:
        print("DGS Koçu: Akıllı Veri Motoru başlatılıyor...")
        
        try:
            
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            hedef_site = "https://www.unirehberi.com/dgs-matematik-konulari/"
            print(f"Hedef siteye bağlanılıyor: {hedef_site}")
            
            page.goto(hedef_site, wait_until="domcontentloaded", timeout=60000)
            print("Tablo analiz ediliyor...")
            
            page.wait_for_selector("table")
            satirlar = page.locator("table tr").all()
            
            baslik_hucreleri = satirlar[0].locator("td, th").all_inner_texts()
            tum_basliklar = [b.strip() for b in baslik_hucreleri]
            
            yil_indeksleri = []
            for indeks, baslik in enumerate(tum_basliklar):
                if baslik.isdigit() and len(baslik) == 4:
                    yil_indeksleri.append({"indeks": indeks, "yil": int(baslik)})
            
            yil_indeksleri.sort(key=lambda x: x["yil"], reverse=True)
            son_yillar = yil_indeksleri[:8]
            
            hedef_yillar_liste = [y['yil'] for y in son_yillar]
            print(f"Hedeflenen En Güncel Yıllar: {hedef_yillar_liste}")

            veri_seti = []
            print("Veriler yıllara göre eşleştirilip çekiliyor...")
            
            for satir in satirlar[1:]:
                hucreler = satir.locator("td, th").all_inner_texts()
                if len(hucreler) > 1:
                    konu = hucreler[0].strip()
                    satir_verisi = {"Konu": konu}
                    
                    for hedef in son_yillar:
                        sutun_indeksi = module_index = hedef["indeks"]
                        yil_adi = str(hedef["yil"])
                        
                        if sutun_indeksi < len(hucreler):
                            deger = hucreler[sutun_indeksi].strip()
                            satir_verisi[yil_adi] = deger if deger.isdigit() else "0"
                        else:
                            satir_verisi[yil_adi] = "0"
                            
                    veri_seti.append(satir_verisi)

            json_yolu = os.path.join(klasor_adi, "dgs_akilli_8_yillik_veri.json")
            with open(json_yolu, "w", encoding="utf-8") as f:
                json.dump(veri_seti, f, ensure_ascii=False, indent=4)
            
            print(f"İşlem tamam! En güncel yılların verisi '{json_yolu}' dosyasına kaydedildi.")

            tablo_elementi = page.locator("table").first
            foto_yolu = os.path.join(klasor_adi, "dogrulama_tablosu_akilli.png")
            tablo_elementi.screenshot(path=foto_yolu)
            
        except PlaywrightTimeoutError:
            print("Kritik Hata: Hedef siteye bağlanırken zaman aşımı oluştu.")
        except Exception as e:
            print(f"Sistem Hatası: Beklenmeyen bir durum oluştu -> {e}")
        finally:
            if 'browser' in locals():
                browser.close()
                print("Tarayıcı güvenli bir şekilde kapatıldı.")

if __name__ == "__main__":
    dgs_akilli_veri_botu()