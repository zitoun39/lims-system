# هذا السكربت يُنشئ هيكل مشروع Flask LIMS داخل مجلد المشروع

import os

folders = [
    "templates",
    "static",
]

files = {
    "app.py": "# Main Flask app",
    "models.py": "# SQLAlchemy models for LIMS",
    "requirements.txt": "Flask\nFlask-SQLAlchemy\nFlask-Cors",
    "templates/base.html": "<!-- Base layout -->",
    "templates/dashboard.html": "<!-- Dashboard page -->",
    "templates/sample_form.html": "<!-- Sample form page -->",
    "static/styles.css": "/* CSS placeholder */",
}

# إنشاء المجلدات
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# إنشاء الملفات
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ تم إنشاء هيكل المشروع!")
