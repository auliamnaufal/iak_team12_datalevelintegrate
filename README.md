# Dashboard EDA Literasi Digital Provinsi (gaya CoinMarketCap)

Dashboard web statis (HTML + CSS + JavaScript murni, tanpa library dan tanpa build step).

## Struktur
- `index.html` : kerangka halaman (login + aplikasi)
- `style.css`  : tampilan (terang/gelap otomatis)
- `app.js`     : login, statistik, grafik SVG, korelasi, tabel, integrasi API BPS
- `data.js`    : data hasil integrasi 4 sumber (kunci: provinsi)
- `data_sumber/` : 4 file asli (2 xlsx, 2 csv)
- `scripts/prep_data.py` : membaca 4 file sumber dan menghasilkan ulang `data.js`

## Menjalankan
Buka `index.html` di browser, atau jalankan server lokal:

    python3 -m http.server 8000      # lalu buka http://localhost:8000

Login demo: `admin` / `bps2024`.

## Memperbarui data
    pip install openpyxl
    python3 scripts/prep_data.py

## Catatan
- Login hanya di sisi browser (password tertulis di `app.js`, fungsi `login()`). Cocok untuk demo, bukan pengamanan sungguhan. Untuk produksi gunakan backend.
- Panel API BPS: tombol "Ambil dari API" memanggil `webapi.bps.go.id`. Jika diblokir CORS oleh browser, buka URL API di tab baru, salin JSON, lalu tempel di panel dan klik "Gabungkan ke data". Jangan menaruh WebAPI KEY di dalam kode.
