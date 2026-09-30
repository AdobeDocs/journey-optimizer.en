---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains best practices to reduce SMS costs in Journey Optimizer by keeping messages short, avoiding special characters and UCS-2 encoding, and checking character counts before sending.

**Intents:**

* Keep SMS messages short to be billed as a single SMS part
* Avoid special characters that increase message length in GSM encoding
* Prevent UCS-2 encoding that reduces the per-SMS character allowance
* Check the character count before sending using Simulate content
* Interpret the difference between Journey Optimizer reporting and provider reporting

**Glossary:**

* **GSM 7-bit encoding**: Encoding supported by most SMS providers where a single SMS can contain up to 160 characters *(product-specific)*
* **UCS-2 encoding**: Encoding applied by the provider when a message includes non-GSM characters; it supports only 70 characters per SMS *(product-specific)*
* **Concatenation**: The automatic splitting of a message that exceeds 160 characters into multiple SMS parts *(product-specific)*
* **Simulate content**: The feature whose simulation methods let you verify character counts before sending *(product-specific)*
* **x/1500 count**: The visual indicator of the technical payload limit, not the per-message limit *(product-specific)*
* **Journey Optimizer reporting**: Reporting that counts the full message as one send, regardless of SMS parts *(product-specific)*
* **Provider reporting**: Reporting that reflects the actual number of SMS message parts used for delivery *(product-specific)*

**Guardrails:**

* Journey Optimizer allows up to 1,500 characters in an SMS message body; a warning appears when you exceed this limit, and messages beyond this threshold trigger an error (hard limit — enforced with an error).
* SMS messages are typically billed by providers based on a 160-character limit per message; GSM 7-bit encoding allows up to 160 characters per single SMS, and messages exceeding this length are automatically split into multiple SMS parts.
* Concatenation part counts: less than 160 characters is 1 SMS part; 161-306 characters is 2 SMS parts; 307-459 characters is 3 SMS parts.
* Special characters such as `| ^ € { } [ ] ~ \` are counted as two characters in GSM encoding, so they reach the 160-character limit more quickly.
* Non-GSM characters cause UCS-2 encoding, which supports only 70 characters per SMS.
* The x/1500 count is the technical payload limit, not the per-message limit (for example, the 160-character GSM 7-bit limit), and it does not include characters from dynamic personalization or certain special characters.
* Adobe supports UTF-8 encoding in the editor, which differs from GSM 7-bit encoding.

**Terminology:**

* Canonical name: SMS cost optimization — Acronym: n/a — variants: SMS cost best practices
* Do not confuse: "Journey Optimizer reporting" (counts the full message as one send regardless of SMS parts) ≠ "Provider reporting" (reflects the actual number of SMS parts used for delivery)
* Do not confuse: "x/1500 count" (technical payload limit) ≠ "160-character limit" (GSM 7-bit per-message billing limit)
* Do not confuse: "GSM 7-bit encoding" (160 characters per SMS) ≠ "UCS-2 encoding" (70 characters per SMS) ≠ "UTF-8 encoding" (supported in the editor)

**FAQ:**

* **Q: What is the maximum SMS length in Journey Optimizer?** — Up to 1,500 characters in the SMS message body; a warning appears when you exceed this limit, and messages beyond this threshold trigger an error.
* **Q: Why is my single message billed as multiple SMS?** — GSM 7-bit encoding allows up to 160 characters per SMS part, so longer messages are automatically split (concatenation) into multiple parts, and a 1,600-character message could consume 10 SMS credits even though it appears as a single message.
* **Q: How do special characters affect message length?** — Characters such as `| ^ € { } [ ] ~ \` are counted as two characters in GSM encoding, so they reach the 160-character limit more quickly.
* **Q: What triggers UCS-2 encoding and why does it matter?** — Non-GSM characters such as Chinese or Arabic text, trademark symbols, or hard returns from rich-formatting tools trigger UCS-2 encoding, which supports only 70 characters per SMS and can increase billing.
* **Q: How can I check the character count before sending?** — Use plain-text applications or either simulation method in Simulate content; note that the displayed count does not include characters from dynamic personalization or certain special characters.
* **Q: Why do the Journey Optimizer and provider reports differ?** — Journey Optimizer reporting counts the full message as one send regardless of SMS parts, while provider reporting reflects the actual number of SMS parts used for delivery.

+++

<!-- ai-section-version: 1 | source-hash: 1aa8a940 -->
