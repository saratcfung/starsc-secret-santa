# STARSC Secret Santa

Christmas gift exchange for Huen, Tiffany, Ashley, Ronnie, Sara and Gu.

The server creates one permanent random derangement on initialization, before anyone registers. Each person selects their name, creates a password (at least 12 characters), and reveals their already assigned recipient immediately. Repeat visits return the same result. No waiting for others, no self-picks, no duplicate recipients.

## Privacy

First registration is trust-based: claim only your own name. A password cannot be reset. After registration the recipient is encrypted with AES-256-GCM using a PBKDF2-derived password key; the plaintext assignment for that participant is removed. Passwords are not stored. Strong, unique passphrases are essential. Unclaimed assignments are stored server-side, so this does not prevent inspection by the hosting account owner. The website has no organiser results endpoint or screen. Hosting owners can also modify application code; this is not protection against a malicious host.

## Personal hosting only

Deploy `worker/index.js` as a Cloudflare Worker with a D1 database bound as `DB`. Apply `drizzle/0000_santa.sql` once. Use a personal account, never a Nex account. Visit `/api/status` to initialize the permanent draw before sharing the URL. This endpoint returns only registration flags, never recipients.

GitHub Pages alone cannot run this backend. No production database has been created yet.

Run `npm test` with Node 26 (built-in SQLite). Tests use an isolated in-memory database and do not generate or inspect production results.
