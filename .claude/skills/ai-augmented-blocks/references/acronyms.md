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

## Approved (spelled out in the docs, or confirmed by the author)

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
| ACS | Adobe Campaign Standard | confirmed by the author (2026-10-09) |
| ACC | Adobe Campaign Classic (v7/v8) | confirmed by the author (2026-10-09) |
| ABAC | Attribute-based access control | confirmed by the author (2026-10-09) |
| AT | Adobe Target | confirmed by the author (2026-10-11) |
| AEM | Adobe Experience Manager | confirmed by the author (2026-10-11) |

## Short names

These are not acronyms but are accepted short forms. A block may use them in Terminology
variants, with the full name as the canonical name.

| Short form | Full name | Confirmed in |
|---|---|---|
| Platform | Adobe Experience Platform (also AEP) | confirmed by the author (2026-10-11) |

## Terms and distinctions

Terms that AI tools tend to mix up. Use the definition and keep the two sides apart. Sources are
the AJO docs pages named in the last column.

| Term | Meaning | Source |
|---|---|---|
| Federated Audience Composition (FAC) | The capability available in Journey Optimizer that lets you query a data warehouse for data or profile attributes to compose and enrich audiences, leaving sensitive data in the warehouse. The author calls it the add-on / module; the published pages say "capability" (the add-on wording is only in an HTML comment on `orchestrated/orchestrated-campaigns-faq.md`), so blocks say "capability". | `audience/federated-audience-composition.md` |
| Federated audience | An audience created through Federated Audience Composition. It is the output you use in journeys and campaigns. Approved variant: "Federated Data Audience" (the author's name for it; the docs say "federated audience"). | `building-journeys/journey-faq.md`, `audience/target-audiences.md` |

**Do not confuse:** FAC (the capability, the tool) is not a federated audience (one audience it
produces). Do not use "FAC" to mean an audience, or "federated audience" to mean the capability.

## Needs the author's confirmation

None at the moment. When a block needs an acronym that is neither on the page body nor in the
table above, do not use it: report it under **Gaps found** and ask a writer to confirm the
expansion, then add it to the table.

## Maintaining the list

Add an entry only when a page in `help/using/` spells the acronym out, or a writer confirms it.
Record the page, so the next reviewer can check it.
