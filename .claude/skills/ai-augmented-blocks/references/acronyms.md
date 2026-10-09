# Approved acronyms

A block normally contains only what its own page body says (golden rule). Acronyms are the one
exception, because the Terminology section exists to help retrieval: people type "OLAC", "STO"
or "AEP" into the AI Assistant, not always the full name. An acronym may appear in a block's
Terminology line in either of two cases:

1. **It is used on the page body** (for example "Send-Time Optimization (STO)"), or
2. **It is on the approved list below**, with the expansion given here.

Anything else is removed by the verifier. Never invent an acronym or an expansion. If a block
has no acronym, **omit the line**; do not write `Acronym: n/a`.

Format in a block: `Canonical name: <full name> — Acronym: <ACR> — variants: ...`. Use the
expansion exactly as written below.

## Approved (spelled out in the docs)

| Acronym | Expansion | Confirmed in |
|---|---|---|
| AJO | Adobe Journey Optimizer | `content-card/content-card-configuration-sdk.md` |
| AEP | Adobe Experience Platform | `building-journeys/choose-validation-method.md` |
| CJA | Customer Journey Analytics | `building-journeys/journey-faq.md` |
| FAC | Federated Audience Composition | `building-journeys/journey-faq.md` |
| OLAC | Object level access control | `administration/object-based-access.md` |
| STO | Send-Time Optimization | `building-journeys/journey-faq.md` |
| TTL | Time-to-live | `audience/get-started-profiles.md` |
| XDM | Experience Data Model | `administration/attribute-based-access.md` |
| CTR | Clickthrough rate | `building-journeys/success-metrics.md` |
| CTOR | Clickthrough open rate | `building-journeys/success-metrics.md` |
| WCAG | Web Content Accessibility Guidelines | `email/accessible-content.md` |

## Needs the author's confirmation (not spelled out in the docs)

Do not use these in a block until a writer confirms the expansion and adds it to the table above.

| Acronym | Proposed expansion | What the docs show |
|---|---|---|
| ACS | Adobe Campaign Standard | Only in front-matter keywords (`using-adobe-campaign-standard.md`) |
| ACC | Adobe Campaign Classic (v7/v8) | Never spelled out; the pages say "Adobe Campaign v7/v8" |
| ABAC | Attribute-based access control | Only as "RBAC/ABAC" in `custom-channel/get-started-custom-channel.md` |

## Maintaining the list

Add an entry only when a page in `help/using/` spells the acronym out, or a writer confirms it.
Record the page, so the next reviewer can check it.
