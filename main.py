import csv
import pandas as pd

# File CSV tunggal
FILE_PATH = './question_list.csv'
df = pd.read_csv(FILE_PATH, quoting=csv.QUOTE_NONE, encoding='utf-8', on_bad_lines='skip')

# Kata kunci per label
keywords = {
    "Problem": [
        "mati", "gangguan", "lambat", "jaringan", "los merah", "putus",
        "teknisi", "kunjungan", "jadwal teknisi"
    ],
    "Information": [
        "relokasi", "pindah rumah", "pindahin", "alamat baru",
        "daftar", "berlangganan", "pasang baru", "registrasi",
        "bayar", "pembayaran", "transfer",
        "upgrade", "ganti paket", "paket baru",
        "modem", "router", "lampu merah",
        "akun", "login", "password", "user", "id pelanggan",
        "promo", "diskon", "penawaran",
        "mybiznet", "aplikasi"
    ],
    "Request": [
        "tagihan", "invoice", "biaya"
    ],
    "Unknown": []  # fallback jika tidak ditemukan
}

def auto_label(text):
    text_lower = str(text).lower()
    for label, keys in keywords.items():
        for keyword in keys:
            if keyword in text_lower:
                return label
    return "lainnya"

# Proses file tunggal
df = pd.read_csv(FILE_PATH)

if 'pertanyaan' in df.columns:
    df['label'] = df['pertanyaan'].apply(auto_label)
    df.to_csv("labeled_question_list.csv", index=False)
    print("[✓] Labeling selesai: labeled_question_list.csv")
else:
    print("[!] Kolom 'pertanyaan' tidak ditemukan dalam file.")
