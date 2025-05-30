# 🏷️ Auto Labeling untuk Pertanyaan Berdasarkan Kata Kunci

Skrip ini digunakan untuk melabeli data pertanyaan dalam file CSV (`question_list.csv`) secara otomatis berdasarkan kata kunci yang telah didefinisikan. Hasilnya disimpan dalam file `labeled_question_list.csv`.
format file header kolom nya harus (pertanyaan) dan result nya tiap pertanyaan akan terdapat sparator (,) dan lebel.
<br>example :
Harga STB berapa ya?”",Problem


---

## 📂 Struktur File
├── question_list.csv <br>
├── auto_labeling.py <br>
└── labeled_question_list.csv <br>


## 🧰 Requirements

Instalasi library yang dibutuhkan:

```bash
pip install -r requirements.txt
```

Jalankan program:

```bash
python main.py
```
