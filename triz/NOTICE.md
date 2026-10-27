# Third-party notices

## Contradiction matrix data (`triz/scripts/matrix.json`)

The cell values of the classical Altshuller contradiction matrix were taken from
[pytriz](https://github.com/mmysior/pytriz) (`resources/matrix_values.csv`, version 0.4.0)
and converted to JSON. Three typos in the source were corrected:

| Cell (improving, worsening) | Source | Corrected |
|---|---|---|
| 1, 38 | `26, 35 18, 19` | 26, 35, 18, 19 |
| 8, 25 | `35, 16, 32 18` | 35, 16, 32, 18 |
| 19, 9 | `8, 35, 35` | 8, 35 |

Thirty-two cells, including the three above, were cross-checked against the matrix published
at [triz40.com](https://www.triz40.com/aff_Matrix.htm); all matched.

Parameter and principle names are the standard English names used in TRIZ literature.
All descriptions and examples in `triz/references/` were written for this project.

pytriz license:

```
MIT License

Copyright (c) 2026 Marek Piotr Mysior

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
