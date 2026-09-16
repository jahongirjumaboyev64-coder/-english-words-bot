# English Words Bot

Bu repositoryda avval faqat `word_list.json` bor edi, shuning uchun bot kodi ko'rinmasdi va ishga tushmasdi. Hozir `bot.py` qo'shildi.

## Ishga tushirish

1. Python 3.10 yoki undan yangi versiyani o'rnating.
2. Kutubxonalarni o'rnating:

```bash
pip install -r requirements.txt
```

3. Telegram BotFather'dan olingan tokenni environment variable sifatida belgilang:

Linux/macOS:

```bash
export BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
python bot.py
```

Windows PowerShell:

```powershell
$env:BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
python bot.py
```

## Buyruqlar

- `/start` — botni boshlash
- `/random` — tasodifiy so'z va tarjima
- `/unit 1` — tanlangan unit so'zlari
- `/help` — yordam

Tokenni GitHub'ga yozmang. Agar token avval repositoryga yuborilgan bo'lsa, BotFather orqali uni yangilang.
