---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to author deep links in email and SMS content, configure them in Journey Optimizer, and handle the tracked links in iOS and Android apps so recipients land on the right in-app screen.

**Intents:**

* Author a deep link in email (Email Designer or Personalization editor code) and in SMS (Url helper function)
* Complete the Journey Optimizer configuration for universal links (iOS) and app links (Android)
* Implement mobile app handling of tracked `mclick` links in iOS and Android
* Follow recommended practices and troubleshoot deep links that do not open the app or the expected screen
* Test deep links end-to-end by sending a proof and clicking on real devices

**Glossary:**

* **Deep link**: A link that takes recipients from an email or SMS message directly to a specific screen or content in a mobile app *(product-specific)*
* **Universal links (iOS) / App links (Android)**: HTTPS-based deep links the configuration on this page applies to *(product-specific)*
* **AASA / assetLinks.json**: The association files hosted on your delegated subdomain for iOS (AASA) and Android (assetLinks.json) *(product-specific)*
* **`/ee/v1/mclick/*`**: Tracked URLs that Adobe hosts and resolves for deep link clicks when link tracking is enabled *(product-specific)*

**Guardrails:**

* Deep links will not work unless you complete both the configuration and the mobile app implementation steps on this page.
* Deep linking is supported for both iOS and Android using tracked URLs (`/ee/v1/mclick/*`) for compatibility and click tracking.
* The configuration section applies when you use universal links (iOS) and app links (Android), which are HTTPS-based deep links.
* Tracked deep link clicks use URLs under `/ee/v1/mclick/*`, which Adobe hosts and resolves, and apply when link tracking is enabled for the message.
* For non-tracked links, the URL is not rewritten through Adobe systems; you must configure universal links or app links on your own domains and hosting.
* The app must perform a GET on the `mclick` URL and read the `Location` header, then route based on the final URL; do not simply open the `mclick` URL in a browser.
* Hosting the AASA (iOS) and assetLinks.json (Android) files requires contacting Adobe Customer Care with the delegated subdomain and app bundle ID; Android also requires the SHA-256 certificate fingerprint.

**Terminology:**

* Canonical name: Deep link — Acronym: n/a — variants: deeplink, Deeplink (Insert link option)
* Synonyms: "universal links" (iOS) and "app links" (Android) = the HTTPS-based deep link setup
* Do not confuse: "`/ee/v1/mclick/*`" (tracked deep link flow handled as an app deep link) ≠ "`/ee/v1/click/`" (opens in the device's default web browser, standard click tracking)
* Do not confuse: "tracked links" (rewritten through Adobe, use `mclick`) ≠ "non-tracked links" (not rewritten; configured on your own domains)

**FAQ:**

* **Q: What must be done before deep links work?** — Complete both the configuration steps in Journey Optimizer and the mobile app implementation steps for iOS and Android.
* **Q: How should the app handle the tracked link?** — Perform a GET on the `mclick` URL, read the `Location` header, and route based on the final URL; do not open the `mclick` URL directly in a browser.
* **Q: What happens if the app is not installed?** — If the same HTTPS URL can be served by your website, the link can open a web page as a fallback.
* **Q: Are UTM parameters available in the app?** — Yes; UTM parameters configured in Journey Optimizer are included in the final URL returned in the `Location` header.
* **Q: How do I test end-to-end?** — Send a proof (create a proof with a deep link) and click it on iOS and Android devices, for both installed and not-installed scenarios, validating on real devices.
* **Q: Should I use a custom URL scheme like `appname://path`?** — You can, but the recommended approach is a universal link or app link (`https://`) matching the HTTPS-based setup on this page.

+++

<!-- ai-section-version: 1 | source-hash: 826ad9b9 -->
