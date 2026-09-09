# Smart Online Service — website

Complete source folder: HTML, CSS, JavaScript, images and assets. No build step,
no framework, no server code. Upload the folder as-is to any static host.

---

## 1. Editing prices and content — one file only

Everything you are likely to change lives in **`js/config.js`**.

| What you want to change | Where in `js/config.js` |
|---|---|
| WhatsApp number, email, Instagram | `whatsapp`, `email`, `instagram` at the top |
| Service names, prices, features | the `services: [...]` list |
| LinkedIn / Naukri dedicated sections | `linkedinSection`, `naukriSection` |
| Homepage reviews carousel | `landingReviews: [...]` |
| Scrolling text strips | `highlights`, `reviews` |
| Coming Soon cards | `comingSoon: [...]` |
| Welcome popup wording | `launchOffer` |
| Founder name, title, LinkedIn & website | `founder` |
| The two WhatsApp channels | `communities` |
| Facebook / LinkedIn / YouTube / X links | the socials block at the top |
| Hero stat numbers | `stats: [...]` |
| Template library listing | `sampleTemplates: [...]` |

Rules: keep the `"` quotes around text, keep the `,` at the end of each line,
save the file, then hard-refresh the browser (**Ctrl + F5**).

`original` is the struck-through price. The **% OFF** pill is calculated
automatically from `original` vs `price` — you never set the percentage by hand.

---

## 2. Current pricing (as per the requirements document)

| Service | Price | Note |
|---|---|---|
| Existing Resume Modify | ₹299 | per page |
| **ATS Resume Rewrite** | **₹349** | per page · 50% off ₹699 · main service |
| Indeed Optimization | ₹299 | profile |
| Resume + LinkedIn | ₹799 | combo |
| Resume + Naukri | ₹799 | combo |
| LinkedIn Optimization | ₹499 | also has its own section on the services page |
| Naukri Optimization | ₹499 | also has its own section on the services page |
| **Complete Career Boost** | **₹1,299** | flagship — resume + LinkedIn + Naukri + Indeed + cover letter |
| Build from Scratch | ₹3,999 | homepage card + `build.html` |

Removed as requested:

- The **ATS Resume Report (₹19)** and **5 ATS Resume Templates (₹49)** cards.
- The **free ATS score checker** in all its forms — the tool page, the results
  page, the hero score gauge, the nav link, the sample score report, and every
  FAQ / terms passage that described a scoring tool.
- The founder **photo**, and the years-of-experience line on the reviews page.
- The **sample billing / invoice** showcase (buttons, lightboxes and images).
- The previous owner's **Google Analytics** and **Microsoft Clarity** tracking.

---

## 3. Pages

`index.html` (home) · `services.html` · `samples.html` (66 templates) ·
`testimonials.html` (reviews) · `community.html` · `support.html` ·
`FAQ.html` · `services-faq.html` · `connect.html` · `build.html` ·
`naukri-linkedin.html` · `gifts.html` · `hr-gift.html` · `tools.html` ·
`social.html` · `certifications.html` · `certify.html` · `certificate.html` ·
`thank-you.html` · `privacy.html` · `terms.html`

---

## 4. Contact details currently wired in

- **WhatsApp (all "Get this" buttons):** `wa.me/917355670856` — a number link is
  required so the pre-written message works.
- **WhatsApp channels (two):**
  - *Proof & Reviews* — `whatsapp.com/channel/0029VbDAjrNJ93wN4u0akZ38`
  - *Job Updates* — `whatsapp.com/channel/0029Vb8SrbLIN9iqOMzW9X3r`

  Both appear on the community page; the Job Updates channel is the default
  used by the "Notify me" links on the Coming Soon cards.
- **Facebook:** facebook.com/share/1G6S2cyYMj/
- **Phone:** +91 73556 70856
- **Email + grievance email:** 10xdropgrow@gmail.com
- **Instagram:** instagram.com/smartonlineservice.in

YouTube, LinkedIn and X are left blank in the config — add a URL and the icon
appears automatically; leave it `""` and it stays hidden. The free-gift and
certificate unlock steps ask for an **Instagram follow only**.

**Founder links.** `founder.linkedin` and `founder.website` are empty, so both
buttons currently render as muted "· soon" chips rather than broken links. Paste
the URLs into `js/config.js` and they turn into real buttons automatically.

---

## 5. Templates & watermarks

Every preview in `assets/samples/` carries **one** clean diagonal watermark
across the middle plus a small branded footer strip.

The homepage hero deliberately shows **un-watermarked** shots — those live in
`assets/hero/` and are separate copies, so the samples page stays protected
while the hero still looks clean.

Clean originals are kept in `assets/samples/_original/`. To re-watermark after
changing the wording, edit `TEXT` / `FOOTER` at the top of
`tools-watermark-templates.py` and run:

```bash
python tools-watermark-templates.py
```

It always rebuilds from `_original/`, so the watermark never doubles up.

**Do not upload `assets/samples/_original/` to your live site** (~31 MB) —
delete it from the copy you publish.

To add a template: drop the image in `assets/samples/`, run the script, then add
a line to `sampleTemplates` in `js/config.js`.

---

## 6. Before you go live

1. **Domain.** Replace `smartonlineservice.in` with your real domain in
   `sitemap.xml`, `robots.txt`, and the `<link rel="canonical">` /
   `og:url` / `og:image` tags at the top of each page. `domain` in
   `js/config.js` should match.
2. **Delete `assets/samples/_original/`** from the uploaded copy.
3. **Delete `Website_Smartonlineservice.pdf`** from the uploaded copy.
4. **Analytics.** The previous site's Google Analytics and Microsoft Clarity
   tags have been removed. Paste your own tag into each page's `<head>` if you
   want tracking.
5. **Google reviews.** `googleReviewUrl` in the config is empty. Add your Google
   Business Profile review link so the "Rate us on Google" buttons work.
6. **HR contacts gift.** `hrContactsUrl` currently points at WhatsApp. Replace it
   with your own "anyone with the link" Google Sheet URL.

---

## 7. Placeholder content to replace with your own

These are working placeholders, not real client data. Swap them as soon as you
have your own:

- **Reviews** — `landingReviews` in `js/config.js` (homepage carousel) and the
  nine cards in `testimonials.html`. All names are generic; no third-party names
  or LinkedIn profiles are used anywhere.
- **Hero stats** — `stats` in the config.
- **Welcome popup** — the company-logo marquee is currently framed as
  *"Written for hiring at"*, i.e. the companies the resumes are formatted for.
  Only change it to a placement claim once you actually have those placements.
- **Community member count** — currently shows "Free to join" rather than a
  number. Add your real figure when you have it.

---

## 8. Testing locally

Open a terminal in this folder and run:

```bash
python -m http.server 5178
```

Then open <http://localhost:5178> in a browser. A plain local server is needed
because the pages load `js/config.js` — opening `index.html` by double-clicking
works in most browsers but a server matches production exactly.
