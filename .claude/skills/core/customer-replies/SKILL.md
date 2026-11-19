<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->
# Customer Replies — buyer messages, reviews, cases

## Tone
Warm, human, short. First line answers the question. Sign-off with the shop's sign-off from `data/brand.md`.

## Templates (adapt, don't paste blindly)
| Situation | Shape |
|---|---|
| Pre-sale question (size, colour, material) | Answer + one helpful extra (size tip / photo offer) + invite to order or ask more |
| Custom order / quote | Confirm what's possible → size/colour options → price `[QUOTE]` → time `[PROCESSING TIME]` → next step (custom listing) |
| Where is my order | Empathy → tracking status `[CHECK TRACKING]` → realistic window → what you'll do if late |
| Damaged / wrong item | Sorry → ask for photo → solution per policy (replace/refund/partial) → timeline |
| Return request | Policy-based yes/no + exact steps + who pays return shipping per policy |
| Positive review response | Thank + one personal detail + care tip |
| Negative review response | Thank → own it → what was done/offered → invite to message. No arguing, no buyer details. |
| eBay/Amazon case (INR, SNAD, A-to-z) | Respond within the platform deadline, factual, attach tracking/photos, offer the policy solution; flag account-health risk |

## Platform rules
- eBay / Amazon: all contact on-platform; no links to outside sites, no off-platform payment, no review manipulation.
- Etsy: don't ask buyers to change reviews in exchange for refunds; use the platform's review response.
- Never request reviews with incentives on any platform.

## Sign-off
Use the sign-off from `data/brand.md`; none defined → `Warm regards,
[SIGN-OFF — your name / shop team]` and list it under "owner must fill".

## Saving drafts
`data/reports/cs/YYYY-MM-DD_<shop>_<topic>.md` — no buyer names, usernames, addresses or order numbers in the file (use "buyer A", "order ref [X]").

## Output
Draft (code block, char count — count with `python -c "print(len(open(f).read()))"` or similar, never estimate) + shorter alternative + `[CHECK: …]` items for the owner. Sending = proposal.
