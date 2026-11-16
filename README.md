# 1 TUNE and 6 CONTINENTS — static site

A static redesign of <https://1tune6continents.org/> built on [Pico CSS v2](https://picocss.com).

## Pages

- `index.html` — home
- `current-project.html` — the ΑΕΩΝ Tango project, musicians, creative team, film placeholder
- `music-institutions.html` — invitation for schools and conservatoires
- `contact.html` — contact details and a form that opens a pre-filled email

## Editing

Shared header and footer live in `_parts/head.html` and `_parts/foot.html`; each page body is `_parts/<page>.body.html`.
After editing anything in `_parts/`, rebuild the pages:

```sh
python3 build.py
```

Theme tokens (colours, fonts, spacing) are at the top of `css/site.css`. `css/pico.min.css` is vendored Pico 2.1.1.

## Preview

```sh
python3 -m http.server 8000
```

Then open <http://localhost:8000/>.

## Notes

- Fonts (Fraunces, Instrument Sans) load from Google Fonts and fall back to system serif/sans when offline.
- The contact form has no backend. Submitting opens the visitor's email client with the message pre-filled.
- `img/globe-instruments.jpg` is the image used on the original site; it carries a stock-photo watermark and should be replaced with a licensed version before publishing.
