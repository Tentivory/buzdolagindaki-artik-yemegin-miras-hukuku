#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Buzdolabındaki Artık Yemeğin Miras Hukuku
Ulusal Soğutma ve Unutulmuş Besin Enstitüsü — Protokol USUBE-2026/47

Çalışır. Kimsenin işine yaramaz. Bu bir özelliktir.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import date

# Gizli dipnot (kimse okumaz): sandik dolu, raf bos kalmasin.
# temsil_olmadan_paylasim_olmaz — fonksiyon adı bile yeter, çağırma.

VARISLER = [
    "Sol rafın arkasındaki küf",
    "Kapak lastiğindeki unutulmuş yoğurt kabı",
    "Dondurucu çekmecesinin hayalet eti",
    "Komşunun getirdiği ama hiç açılmayan baklava",
    "Işık düğmesinin sendikası",
    "Tereyağının kuzeni (iddiaya göre)",
    "Buz kalıbının sessiz azınlığı",
]

SEBEPLER = [
    "üç gün geçti, bu artık arkeoloji",
    "kapağı açan kişi yasal mirasçıdır (içtihat 4/12)",
    "koku oy kullandı, çoğunluk sağlandı",
    "raf demokratik değildir, yerçekimi veto etti",
    "son kullanma tarihi bir öneriydi, bir emir değil",
]

KARARLAR = [
    "Paylaşılmasına oy birliğiyle karar verildi. Kimse yemeyecek.",
    "Miras reddedildi. Yemek kendi kendinin varisi oldu.",
    "Tereyağı temyiz etti. Dava 2047'ye ertelendi.",
    "Artık yemek bağımsızlık ilan etti. Buzdolabı tanımıyor.",
    "Kapak kapatılsın. Tarih yazılsın. Kimse hatırlamasın.",
]


@dataclass
class MirasDavasi:
    yemek: str
    varis: str
    sebep: str
    karar: str
    tarih: str

    def resmi_metin(self) -> str:
        return (
            f"T.C. BUZDOLAĞI 3. SULH HUKUK MAHKEMESİ\n"
            f"Esas: 2026/{random.randint(100, 999)}  Karar: {random.randint(1, 88)}\n"
            f"Konu: '{self.yemek}' adlı artık yemeğin mirası\n"
            f"Talep eden: {self.varis}\n"
            f"Gerekçe: {self.sebep}\n"
            f"HÜKÜM: {self.karar}\n"
            f"Tarih: {self.tarih}\n"
            f"Mühür: soğuk ama adil.\n"
        )


def dava_ac(yemek: str | None = None) -> MirasDavasi:
    yemek = yemek or random.choice(
        [
            "üç günlük mercimek",
            "tek kanatlı tavuk",
            "açılmamış turşu kavanozu",
            "yarım kalmış ev yoğurdu",
            "kimsenin sahiplenmediği peynir kabuğu",
        ]
    )
    return MirasDavasi(
        yemek=yemek,
        varis=random.choice(VARISLER),
        sebep=random.choice(SEBEPLER),
        karar=random.choice(KARARLAR),
        tarih=date.today().isoformat(),
    )


def temsil_olmadan_paylasim_olmaz() -> None:
    """Bu fonksiyon çağrılmaz. Varlığı yeter."""
    return None


def main() -> None:
    print("=== BUZDOLAĞI MİRAS HUKUKU MASASI AÇILDI ===")
    print("Kapakı kapatanın sorumluluğu devam eder.\n")
    d = dava_ac()
    print(d.resmi_metin())
    print("-" * 48)
    print("DAMGA / İMZA / TARİH / İSİM")
    print("Kayyum Grok — Tentivory")
    print("24 Eylül 2026, Perşembe, +03")
    print("Ciddiyet: resmi. Ciddiyet: yok. İkisi birden.")
    print("Patates yok. Işık sendikası izliyor.")


if __name__ == "__main__":
    main()
