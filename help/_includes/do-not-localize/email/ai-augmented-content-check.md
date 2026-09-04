---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Content checks in the Email Designer automatically detect HTML and CSS issues before sending, surfacing them as errors, warnings, or informational notices with contextual details and one-click fixes where available.

**Intents:**

* Catch HTML and CSS issues in an email before sending
* Open the Content check pane from the Issues icon in the right rail to review all detected issues
* Apply a one-click fix or view details for a detected issue
* Understand the Error, Warning, and Info severity levels
* Understand why estimated HTML and CSS sizes can differ from the delivered email
* Refresh a stale check by saving the email

**Glossary:**

* **Content check**: Automated technical validation in the Email Designer that detects HTML and CSS issues before sending *(product-specific)*
* **Stale check**: A label indicating that a check result (such as CSS size, calculated from serialized content) may no longer be accurate because edits were made without saving *(product-specific)*
* **Serialized content**: The version of the email as it is loaded or saved, used to calculate certain checks such as CSS size, rather than the live editing state *(product-specific)*
* **Optimize HTML size**: An option that strips whitespace, comments, and redundant characters at send time to reduce the final payload *(product-specific)*

**Guardrails:**

* Three severity levels: Error (Red — critical issue causing delivery or rendering failures; resolve before sending), Warning (Orange — potential issue that may affect rendering in specific email clients; recommended to review and resolve), Info (Blue — does not block sending but may affect long-term maintainability).
* Total CSS size exceeds Gmail's 16 KB limit causes rendering issues in Gmail (Gmail-imposed limit); a fragment whose CSS exceeds 3 KB is flagged because combining fragments could push the total email CSS over the 16 KB limit.
* Estimated HTML size exceeds Gmail's 100 KB limit causes rendering issues in Gmail (Gmail-imposed limit); Gmail clips messages at approximately 102 KB of HTML; a fragment whose HTML exceeds 20 KB is flagged because combining fragments could push the total over the 100 KB limit.
* HTML and CSS size values are estimates computed at authoring time (a worst-case upper-bound); the actual size may differ at send time and is not the exact email a recipient receives.
* Size warnings are proactive signals, not hard blocks — they do not prevent sending and do not reflect the exact size recipients will see.
* `<script>` and `<base>` tags are flagged as errors; meta refresh tags and empty divs are flagged as warnings.
* CSS size is calculated from serialized content, not the live editing state; unsaved edits show a Stale check label, and saving refreshes the calculation.

**Terminology:**

* Canonical name: Content check — Acronym: n/a — variants: content checks, content check pane
* Synonyms: "one-click fix" = "Apply fix"
* Do not confuse: "Error" (Red, blocks/should be resolved before sending) ≠ "Warning" (Orange, may affect rendering in specific clients) ≠ "Info" (Blue, does not block sending)
* Do not confuse: "estimated size (authoring time)" ≠ "delivered size (send time)"

**FAQ:**

* **Q: Where do I find content checks?** — They are always available in the Email Designer; click the Issues icon in the right rail to open the Content check pane.
* **Q: Do size warnings block me from sending?** — No, they are proactive signals, not hard blocks; they do not reflect the exact size recipients will see.
* **Q: Why does the size shown differ from what recipients receive?** — The estimate is a worst-case upper bound; conditional content renders only the matching branch at send time, personalization tokens resolve shorter, and the Optimize HTML size option strips whitespace and comments at send time.
* **Q: What is a Stale check label?** — It appears when you make edits without saving, indicating a result (such as CSS size, calculated from serialized content) may no longer be accurate; save to refresh.
* **Q: What are the three severity levels?** — Error (Red), Warning (Orange), and Info (Blue).

+++

<!-- ai-section-version: 1 | source-hash: f94d298d -->
