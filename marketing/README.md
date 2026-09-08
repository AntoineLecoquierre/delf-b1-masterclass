# Marketing assets

Product images for the Payhip listings. Not used by the site — these are
uploaded to Payhip by hand.

| File | Size | Where it goes |
|---|---|---|
| `cheat-sheet-product.jpg` | 1600×900 | Cheat Sheet product page |
| `cheat-sheet-square.jpg` | 1200×1200 | Shop grid, which crops to a square |
| `plan-weekly-product.jpg` | 1600×900 | Weekly product page |
| `plan-weekly-square.jpg` | 1200×1200 | Weekly, shop grid |
| `plan-twice-weekly-product.jpg` | 1600×900 | Twice weekly product page |
| `plan-twice-weekly-square.jpg` | 1200×1200 | Twice weekly, shop grid |
| `plan-intensive-product.jpg` | 1600×900 | Intensive product page |
| `plan-intensive-square.jpg` | 1200×1200 | Intensive, shop grid |

## Regenerating

`src/` holds the HTML the images are rendered from, plus the Playwright
script that shoots them. Both pages expect `cheat-sheet-cover.jpg` (copied
from `images/`) and the brand fonts as `font1.ttf`–`font7.ttf` in the same
directory — Inter Bold/SemiBold/Medium/Regular, then Playfair Display Bold
Italic/Bold/ExtraBold, in that order. Fetch them from Google Fonts with a
plain curl, which returns full TTFs rather than subsets.

    node shot.js /abs/path/product.html out.png 1600 900
    node shot.js /abs/path/square.html  out.png 1200 1200

The three plan images come from `plan.py`, which writes six HTML files from
one template — the numbers, the copy and the filled dots are the only things
that differ, so the set stays consistent when a price or a session count
changes. Run it, shoot the files it wrote, then downsample as above.

    python3 plan.py

Fetch the fonts with a plain `curl` and no `-A` flag: sending a browser
user-agent gets you woff2 back, and the @font-face rules here want TTFs.

Shot at deviceScaleFactor 2, then downsampled to the sizes above — text
stays crisp that way.
