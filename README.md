# DigiProv — Dashboard EDA Literasi Digital Provinsi

Dashboard statis 38 provinsi (`index.html`, `app.js`, `data.js`) dengan login demo `admin` / `bps2024`.

## Menjalankan

```bash
python3 -m http.server 8001
```

Buka http://127.0.0.1:8001/.

## Sumber data (3 tipe)

| Tipe | Sumber | Indikator | Field |
| --- | --- | --- | --- |
| API (JSON) | WebAPI BPS var 656, tahun 124 (2024) | Akses internet penduduk 5+ | `pi_u`, `pi_r`, `pi_t` |
| Excel (XLSX) | BPS, 2024 | Rumah tangga memiliki/menguasai komputer | `kom_u`, `kom_r`, `kom_t` |
| CSV | BPS, 2024 | Akses internet rumah tangga, kepemilikan ponsel, keterampilan TIK 15–59 | `rt_*`, `hp_*`, `tik` |

Respons API disimpan sebagai cache di `data_sumber/bps_api_var656_2024.json` agar build tidak membutuhkan jaringan. API key tidak disimpan di repositori.

## Regenerasi `data.js`

```bash
BPS_API_KEY=<key> python3 scripts/fetch_api.py   # opsional, memperbarui cache API
python3 scripts/prep_data.py                     # menulis data.js
```

`scripts/prep_data.py` menggabungkan ketiga tipe sumber berdasarkan nama provinsi.
