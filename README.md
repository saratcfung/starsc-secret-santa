# STARSC Secret Santa

A one-off, static Christmas gift exchange hosted on personal GitHub Pages.

Each emailed invitation carries a random 256-bit decryption key in its URL fragment. The fragment is not sent to GitHub's web server. `draw.json` contains only encrypted assignments and opaque IDs. The browser unlocks one assignment and reveals it after a gift animation. No passwords, database, analytics, or third-party scripts.

Anyone who has a private invitation link can see that result. The organiser can access locally saved links or sent emails. This is not protection from an organiser with access to those links. Do not forward invitations.

## Permanent draw

`scripts/prepare-invitations.mjs` generates all six assignments once and refuses to overwrite an existing draw or invitation file. Never delete `draw.json` to reroll. Private invitations are in ignored `.private/invitations.json`; back this file up securely. It must never be committed or published. No email addresses or invitation keys belong in public files.

## Hosting

Publish the `main` branch root with GitHub Pages. No Cloudflare or Nex resources are required. On GitHub Free, this requires a public repository. A private repository needs an eligible paid GitHub plan.

## Validation

Run `npm test`. Tests check the real encrypted draw without printing results and verify wrong keys cannot unlock it.

## Invitation email

`email-template.html` is the public, reusable illustrated email template. It contains no addresses or private links. `python3 scripts/prepare-email.py` renders Sara's HTML and multipart `.eml` into the ignored `.private/` directory. It does not send mail. The artwork is hosted on the same GitHub Pages site; the button and text still work when an email client blocks images.

The original group photograph is not included in this repository. The published illustration is an anime adaptation made with permission for this personal exchange.
