import json
import os
import urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, '..', 'data_sumber', 'bps_api_var656_2024.json')
URL = ('https://webapi.bps.go.id/v1/api/list/model/data/lang/ind/domain/0000/'
       'var/656/th/124/key/{key}')

key = os.environ.get('BPS_API_KEY')
if not key:
    raise SystemExit('Set BPS_API_KEY terlebih dahulu, contoh: BPS_API_KEY=... python3 scripts/fetch_api.py')

req = urllib.request.Request(URL.format(key=key), headers={
    'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'),
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://www.bps.go.id/',
})
with urllib.request.urlopen(req, timeout=60) as r:
    data = json.load(r)
if data.get('status') != 'OK':
    raise SystemExit('Respons API tidak OK: ' + str(data)[:200])
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print('Respons API disimpan:', OUT, '| provinsi:', len(data.get('vervar', [])))
