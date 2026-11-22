"""
Add the website address (as a clickable link) to the CV PDF's contact lines.

    python tools/add_website_to_cv.py <input.pdf> <output.pdf> <website> <Carlito-Regular.ttf>

Page 1: appended to the white contact line in the navy header.
Page 2: added to the grey right-aligned header line.
The original PDF is never modified. Needs: pip install pymupdf (not required by the website itself).
"""

import sys

import pymupdf

src, dst, site, font_path = sys.argv[1:5]
url = site if site.startswith("http") else f"https://{site}"
label = site.removeprefix("https://").removeprefix("http://").rstrip("/")

font = pymupdf.Font(fontfile=font_path)
doc = pymupdf.open(src)


def find_span(page, needle):
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                if needle in span["text"]:
                    return span
    raise SystemExit(f"Could not find {needle!r} on page {page.number + 1}")


def rgb(color_int):
    return tuple(((color_int >> s) & 255) / 255 for s in (16, 8, 0))


# ---- Page 1: "Sandton ... | +27 ... | email"  ->  append "   |   website"
p1 = doc[0]
span = find_span(p1, "rlmolefe1999@gmail.com")
size, color = span["size"], rgb(span["color"])
x0, baseline = span["bbox"][2], span["origin"][1]
sep = "   |   "
tw = pymupdf.TextWriter(p1.rect)
tw.append((x0, baseline), sep + label, font=font, fontsize=size)
tw.write_text(p1, color=color)
sep_w = font.text_length(sep, fontsize=size)
link_w = font.text_length(label, fontsize=size)
p1.insert_link({"kind": pymupdf.LINK_URI, "uri": url,
                "from": pymupdf.Rect(x0 + sep_w, span["bbox"][1], x0 + sep_w + link_w, span["bbox"][3])})
page1_right = x0 + sep_w + link_w

# ---- Page 2: right-aligned "email  |  phone"  ->  "website  |  email  |  phone"
p2 = doc[1]
span = find_span(p2, "rlmolefe1999@gmail.com")
size, color = span["size"], rgb(span["color"])
right, baseline = span["bbox"][2], span["origin"][1]
new_text = f"{label}  |  {span['text']}"
new_w = font.text_length(new_text, fontsize=size)
# cover the old line with the white page background, then write the new one
p2.draw_rect(pymupdf.Rect(span["bbox"][0] - 1, span["bbox"][1] - 0.5, right + 1, span["bbox"][3] + 0.5),
             color=None, fill=(1, 1, 1))
tw = pymupdf.TextWriter(p2.rect)
tw.append((right - new_w, baseline), new_text, font=font, fontsize=size)
tw.write_text(p2, color=color)
p2.insert_link({"kind": pymupdf.LINK_URI, "uri": url,
                "from": pymupdf.Rect(right - new_w, span["bbox"][1],
                                     right - new_w + font.text_length(label, fontsize=size), span["bbox"][3])})

doc.set_metadata({"title": "Reorapetse Molefe - Curriculum Vitae", "author": "Reorapetse Molefe"})
doc.save(dst, garbage=3, deflate=True)
print(f"Saved {dst}  (page 1 line now ends at x={page1_right:.1f}pt; page width {p1.rect.width:.1f}pt)")
