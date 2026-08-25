# Marketing assets

Product images for the Payhip listings. Not used by the site — these are
uploaded to Payhip by hand.

| File | Size | Where it goes |
|---|---|---|
| `cheat-sheet-product.jpg` | 1600×900 | Cheat Sheet product page |
| `cheat-sheet-square.jpg` | 1200×1200 | Shop grid, which crops to a square |

## Regenerating

`src/` holds the HTML the images are rendered from, plus the Playwright
script that shoots them. Both pages expect `cheat-sheet-cover.jpg` (copied
from `images/`) and the brand fonts as `font1.ttf`–`font7.ttf` in the same
directory — Inter Bold/SemiBold/Medium/Regular, then Playfair Display Bold
Italic/Bold/ExtraBold, in that order. Fetch them from Google Fonts with a
plain curl, which returns full TTFs rather than subsets.

    node shot.js /abs/path/product.html out.png 1600 900
    node shot.js /abs/path/square.html  out.png 1200 1200

Shot at deviceScaleFactor 2, then downsampled to the sizes above — text
stays crisp that way.
