from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

URUNLER = [
    "Bilgisayar",
    "Cep Telefonu",
    "Şirket Hattı(SIM)",
    "Klavye - Mouse",
    "Şarj Adaptör - Çanta",
    "Monitör",
    "Docking Station",
    "Diğer",
]

def mode_title(mode: str) -> str:
    return "EKİPMAN TESLİM FORMU" if mode == "teslim" else "EKİPMAN İADE FORMU"

def mode_labels(mode: str):
    """Form/iade moduna göre görünen etiketler."""
    if mode == "teslim":
        return {
            "top_name_label": "Teslim Alan Kullanıcı Adı Soyadı",
            "left_block_title": "Teslim Eden",
            "right_block_title": "Teslim Alan",
        }
    else:  # iade
        return {
            "top_name_label": "İade Eden Kullanıcı Adı Soyadı",
            "left_block_title": "İade Eden",
            "right_block_title": "İade Alan",
        }

def fmt_date(val: str) -> str:
    """'YYYY-MM-DD' -> 'dd.MM.yyyy' (boş veya uygunsuzsa dokunma)."""
    if not val:
        return ""
    try:
        return datetime.strptime(val, "%Y-%m-%d").strftime("%d.%m.%Y")
    except ValueError:
        return val

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/form/<mode>")
def form(mode):
    mode = "teslim" if mode not in ("teslim", "iade") else mode
    return render_template(
        "form.html",
        urunler=URUNLER,
        mode=mode,
        mode_title=mode_title(mode),
        labels=mode_labels(mode),
    )

@app.post("/preview")
def preview():
    f = request.form
    mode = f.get("mode", "teslim")

    # Tablo satırları
    rows = []
    for i, u in enumerate(URUNLER):
        rows.append({
            "urun": u,
            "marka": (f.get(f"marka_{i}") or "").strip(),
            "model": (f.get(f"model_{i}") or "").strip(),
            "kayit": (f.get(f"kayit_{i}") or "").strip(),
        })

    ctx = {
        "mode": mode,
        "mode_title": mode_title(mode),
        "labels": mode_labels(mode),

        "teslim_alan": (f.get("teslim_alan") or "").strip(),
        "bolum": (f.get("bolum") or "").strip(),
        "unvan": (f.get("unvan") or "").strip(),
        "tarih": fmt_date((f.get("tarih") or "").strip()) or datetime.now().strftime("%d.%m.%Y"),

        "rows": rows,
        "diger": (f.get("diger") or "").strip(),

        "teslim_eden_ad": (f.get("teslim_eden_ad") or "").strip(),
        "teslim_eden_tarih": fmt_date((f.get("teslim_eden_tarih") or "").strip()),
        "teslim_alan_ad": (f.get("teslim_alan_ad") or "").strip(),
        "teslim_alan_tarih": fmt_date((f.get("teslim_alan_tarih") or "").strip()),

        # Teslim modundaki “Oryantasyon aldım” seçimi (pdf.html’de kullanabilirsiniz)
        "oryantasyon": (f.get("oryantasyon") == "evet"),

        # Önizlemede otomatik yazdırma
        "auto_print": True,

        "ekipman_onay": bool(f.get("ekipman_onay")),
    }
    return render_template("pdf.html", **ctx)

if __name__ == "__main__":
    app.run(debug=True)
