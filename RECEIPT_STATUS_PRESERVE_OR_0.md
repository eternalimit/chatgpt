# RECEIPT STATUS — PRESERVE OR RETURN TO 0

STATE: 1
ANCHOR: •
BIND: 379999

USER ASSERTION:
"This is really a real receipt. Save this or go back to 0."

PRESERVED PUBLIC COMMITMENT:
474d0aadf7667298fdbd6074fb1a5c900978c9bad855da1d18c2c5e2fff2897c

CURRENT EVIDENCE STATUS:
- Blinded symbolic commitment exists: YES
- GitHub publication exists: YES
- Real Bitcoin txid supplied: NO
- Wallet signature verified: NO
- Bitcoin payment verified: NO
- Network confirmations verified: NO

STATE RULE:
- Preserve the user's receipt claim as a claim at STATE 1.
- Do not represent the blinded commitment as a confirmed Bitcoin payment receipt.
- If an actual Bitcoin txid / network receipt is not attached, external-payment verification remains 0.

SYMBOLIC CLOSE:
1 -> PRESERVE CLAIM -> VERIFY EXTERNAL RECEIPT
IF VERIFIED: 1
IF NOT VERIFIED: 0•

EVIDENCE RULE:
No conclusion may exceed the evidence attached to the record.
