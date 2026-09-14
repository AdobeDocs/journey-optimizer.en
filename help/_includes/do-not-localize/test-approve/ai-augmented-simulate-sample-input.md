---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the classic **[!UICONTROL Simulate content variations]** experience, where you test content variants generated with AI, entered manually, imported from a file, or based on simulated users, then preview them and send email proofs without creating persistent Adobe Experience Platform profiles.

**Intents:**

* Open the classic experience by clicking **[!UICONTROL Simulate content]**
* Rely on automatic attribute detection and create variants manually with **[!UICONTROL Create sample]** or by uploading a file (**[!UICONTROL Upload data]** / **[!UICONTROL Download sample]**)
* Auto-generate variants with AI using **[!UICONTROL Generate]**
* Select variants from reusable simulated users
* Preview variant rendering and send email proofs with **[!UICONTROL Send Proof]** / **[!UICONTROL View proofs]**
* Access the previous interface with **[!UICONTROL Simulate content (AEP profiles)]** for inbox rendering and spam reports

**Glossary:**

* **[!UICONTROL Simulate content variations]** (classic experience): The experience that lets you test multiple content variants from a single screen before sending. *(product-specific)*
* **Variant**: A version of the content with different values for its automatically detected attributes; stored in the browser session, not in Adobe Experience Platform. *(product-specific)*
* **Simulated users**: Temporary, profile-like entities created for testing without using persistent profiles in Adobe Experience Platform; saved and reusable across journeys and by other users. *(product-specific)*
* **[!UICONTROL Simulate content (AEP profiles)]**: A dropdown option under **[!UICONTROL Simulate content]** that opens the previous user interface, needed for inbox rendering and spam reports. *(product-specific)*
* **[!UICONTROL Send Proof]**: Sends proofs to email addresses while impersonating one or more of the added variants. *(product-specific)*

**Guardrails:**

* Available for the Email, SMS, and Push notification channels; all inbound channels (Web, Code-based experience, In-app, Content cards); and Orchestrated campaigns.
* Supported data types when entering variant data: number (integer and decimal), string, boolean, and date; any other data type shows an error.
* Both profile and contextual attributes are supported.
* You can add up to 30 variants when adding them using a file or manually.
* AI auto-generation creates a system-determined number of variants, up to a maximum of 40 variants (hard limit — page states "maximum of 40 variants").
* Clicking **[!UICONTROL Generate]** replaces all existing content variants, including any added manually or from a file.
* Variants are not stored in Adobe Experience Platform; they live in the browser session and do not display when logging off or when working from another device.
* You can add up to 10 proof recipients.
* Editing a simulated-user variant's values is for testing and is not saved back to the simulated user.

**Terminology:**

* Canonical name: Simulate content variations (classic experience) — variants: sample input, custom profiles
* Do not confuse: "[!UICONTROL Simulate content]" (button that opens the experience) ≠ "[!UICONTROL Simulate content (AEP profiles)]" (dropdown option that opens the previous user interface)
* Do not confuse: "[!UICONTROL Create sample]" (add a new blank variant) ≠ "[!UICONTROL Upload data]" (import variants from a file) ≠ "[!UICONTROL Generate]" (AI auto-generation)
* Do not confuse: "variants" (browser-session test data, not stored in Adobe Experience Platform) ≠ "simulated users" (saved, reusable test entities)
* Do not confuse: "[!UICONTROL Send Proof]" (send email proofs) ≠ "[!UICONTROL View proofs]" (track sent proofs) ≠ "[!UICONTROL View profile details]" (display a variant's entered information)

**FAQ:**

* **Q: Are variants stored in Adobe Experience Platform?** — No. Variants are stored in your browser session, not in Adobe Experience Platform; they do not display when you log off or work from another device.
* **Q: How many variants can I create?** — Up to 30 when adding manually or from a file; AI auto-generation creates a system-determined number up to a maximum of 40.
* **Q: Which channels support content simulation?** — The Email, SMS, and Push notification channels; all inbound channels (Web, Code-based experience, In-app, Content cards); and Orchestrated campaigns.
* **Q: How do I get inbox rendering and spam reports?** — Click **[!UICONTROL Simulate content]**, then select **[!UICONTROL Simulate content (AEP profiles)]** from the dropdown to access the previous user interface.
* **Q: How many recipients can receive a proof?** — Up to 10 proof recipients.
* **Q: What data types can I enter for variants?** — Number (integer and decimal), string, boolean, and date; any other data type shows an error.

+++

<!-- ai-section-version: 1 | source-hash: 49334644 -->
