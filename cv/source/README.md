# PDF CV source

`../Siarhei_Vei_CV.pdf` is built from these files with ReportLab:

- `content.py` — all the text: summary, skills, certificates, work experience, personal projects, contacts. Edit this file.
- `build.py` — layout: header with the photo, grey bands, section titles, label/value tables, page footer.
- `photo.jpg` — the round photo in the header.

## Build

```bash
pip install reportlab
cd cv/source
python build.py photo.jpg ../Siarhei_Vei_CV.pdf
```

Fonts: Liberation Sans and DejaVu Sans on Linux (`/usr/share/fonts/truetype/...`); on Windows the script falls back to Arial (same metrics as Liberation Sans, so the pages break the same way) and Segoe UI Symbol for the `○` bullets.

The PDF is the same in `sergevei.github.io` and `cosmic-portfolio`: rebuild it in one repository and copy `Siarhei_Vei_CV.pdf` and `cv/source/` to the other. Keep `README.md` of `sergevei.github.io` in step with `content.py` — it is the text version of the same CV.
