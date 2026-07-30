---
solution: Journey Optimizer
product: journey optimizer
title: Journey Optimizer feature availability
description: A single, consolidated reference to find which Adobe Journey Optimizer features are available, their lifecycle status (General Availability, Limited Availability, or Beta), which base offer they apply to, and when they shipped — without cross-referencing release notes.
feature: Get Started
topic: Content Management
role: Admin, User
level: Beginner, Intermediate
keywords: journey optimizer, feature availability, what's available, GA, limited availability, beta, lifecycle, release date, entitlement, base offer, campaigns, journeys
hide: true
---

# Journey Optimizer feature availability {#ajo-features-availability}

>[!BEGINSHADEBOX]

**On this page:** Find out which [!DNL Adobe Journey Optimizer] features are available, what lifecycle stage each is in (General Availability, Limited Availability, or Beta), which base offer they apply to, and when they shipped — so you can answer *"can I use this?"* without digging through release notes.

>[!ENDSHADEBOX]

This page consolidates feature availability across [!DNL Adobe Journey Optimizer] so you can confirm what you can use during pre-implementation scoping. Features are grouped by capability area. Within each area, every feature lists its current lifecycle status, the base offer it applies to, the date it became available, and any notes about configuration or regional restrictions.

Rows marked **Core capability** in the *Available since* column are long-standing, foundational features that have been generally available since before 2026. Dated rows reflect changes shipped in 2026.

>[!IMPORTANT]
>
>**Why can't I see a feature in my environment?** Features in **Limited Availability** or **Beta** are not visible to everyone — they roll out to a restricted set of organizations first. If a capability you read about doesn't appear in your environment, check its status below: if it's **LA** or **Beta**, contact your Adobe representative to request access. A feature being listed here does not mean it is enabled in your environment.

>[!NOTE]
>
>**Availability vs. entitlement.** This page tracks *feature lifecycle and availability* (whether a capability has shipped and at what maturity). Whether a feature is *included in your license* depends on your base offer and add-ons — see [Packages and capabilities](ajo-packages.md).

## What the lifecycle statuses mean {#status-definitions}

| Status | What it means |
|--------|--------------|
| **GA** — General Availability | Released to all environments. Available to any organization whose license includes the capability. |
| **LA** — Limited Availability | Released to a restricted set of organizations. **Contact your Adobe representative** to request access. |
| **Beta** | Early-access release for evaluation. May change before General Availability. May require opting in. |

## How "Applies to" maps to base offers {#applies-to}

The **Applies to** column refers to the three [!DNL Adobe Journey Optimizer] base offers:

- **Journey Optimizer – Campaigns** — batch, audience-based orchestration
- **Journey Optimizer – Journeys** — real-time, event-driven orchestration
- **Journey Optimizer – Campaigns & Journeys** — both

Channel, content, and platform features marked **All base offers** are available regardless of base offer, but most still require the relevant channel or advanced-capability add-on. See [Packages and capabilities](ajo-packages.md) for entitlement details.

## Features by capability area {#features-by-area}

>[!BEGINTABS]

>[!TAB Channels]

| Feature | Status | Applies to | Available since | Notes |
|---------|--------|-----------|-----------------|-------|
| New Mobile Message channel (SMS, MMS, RCS) | GA | All base offers | May 20, 2026 | Unifies SMS/MMS/RCS; native RCS authoring (images, carousels) |
| Deep links in the Email Designer | GA | All base offers | May 12, 2026 | Requires mobile app configuration |
| Optimize email for AI inboxes | GA | All base offers | April 17, 2026 | Apple Intelligence, Gmail Gemini |
| Sender parameters in email header | GA | All base offers | April 2026 | "Sender on behalf of From" / "via" |
| CC field in email channel settings | GA | All base offers | April 2026 | Supports personalization |
| Inbox | GA | All base offers | April 7, 2026 | — |
| Web push notifications channel | GA | All base offers | February 13, 2026 | Previously Beta |
| Live Activity for iOS | GA | All base offers | March 3, 2026 | Lock Screen / Dynamic Island; previously Beta |
| Direct mail channel in journeys | GA | Journeys; Campaigns & Journeys | January 29, 2026 | Previously LA |
| Direct mail channel in orchestrated campaigns | GA | Campaigns; Campaigns & Journeys | January 28, 2026 | — |
| LINE channel | GA | All base offers | 2025 | — |
| WhatsApp button support and tracking | GA | All base offers | May 2026 | Quick reply, CTA URL/phone |
| Email | GA | All base offers | Core capability | Requires Outbound Delivery add-on |
| Push notifications | GA | All base offers | Core capability | Requires Outbound Delivery or Mobile add-on |
| SMS / MMS | GA | All base offers | Core capability | Based on your licensed configuration |
| Direct mail | GA | All base offers | Core capability | Requires Outbound Delivery add-on |
| In-app messaging | GA | All base offers | Core capability | Requires Mobile add-on |
| Content cards | GA | All base offers | Core capability | Requires Mobile add-on |
| Web channel | GA | All base offers | Core capability | Requires Web add-on |
| Code-based experiences | GA | All base offers | Core capability | Requires Mobile or Web add-on |
| Landing pages | GA | All base offers | Core capability | — |
| WhatsApp | GA | All base offers | Core capability | Requires WhatsApp add-on; based on licensed configuration |

>[!TAB Journeys]

| Feature | Status | Applies to | Available since | Notes |
|---------|--------|-----------|-----------------|-------|
| Journey Fragments | GA | Journeys; Campaigns & Journeys | June 9, 2026 | Reusable journey nodes; sandbox tooling support |
| Journey Simulation | GA | Journeys; Campaigns & Journeys | June 9, 2026 | Validate logic with simulated users |
| Journey path optimization – Targeting | GA | Journeys; Campaigns & Journeys | June 8, 2026 | Deterministic path targeting |
| Supplemental identifier support for external audiences | GA | Journeys; Campaigns & Journeys | June 11, 2026 | CSV and Federated Audience Composition |
| Journey path experimentation | GA | Journeys; Campaigns & Journeys | April 7, 2026 | A/B and multi-armed bandit; "Scale the winner" |
| Action activity in journeys | GA | Journeys; Campaigns & Journeys | February 20, 2026 | Replaces deprecated native channel activities |
| Content decision activity | GA | Journeys; Campaigns & Journeys | February 10, 2026 | Previously LA |
| Quiet hours (time-based exclusions) | GA | Journeys; Campaigns & Journeys | January 29, 2026 | Previously LA |
| Generate content for journey expressions | Beta | Journeys; Campaigns & Journeys | June 3, 2026 | Public Beta |
| Journey arbitration | LA | Journeys; Campaigns & Journeys | February 24, 2026 | Contact your Adobe representative |
| Journey arbitration – AI models | LA | Journeys; Campaigns & Journeys | April 2026 | Contact your Adobe representative |
| Dataset lookup support in journeys | LA | Journeys; Campaigns & Journeys | March 2026 | For customers entitled to dataset lookup |
| Wave sending of outbound messages (journeys) | LA | Journeys; Campaigns & Journeys | March 16, 2026 | GA in campaigns; LA in journeys |
| Automated (event-triggered) journeys | GA | Journeys; Campaigns & Journeys | Core capability | Real-time, 1:1 orchestration |
| Real-time event triggers | GA | Journeys; Campaigns & Journeys | Core capability | — |
| Read audience (audience-based) journeys | GA | Journeys; Campaigns & Journeys | Core capability | — |
| Journey reports | GA | Journeys; Campaigns & Journeys | Core capability | — |

>[!TAB Campaigns]

| Feature | Status | Applies to | Available since | Notes |
|---------|--------|-----------|-----------------|-------|
| Chained orchestrated campaigns | GA | Campaigns; Campaigns & Journeys | May 20, 2026 | Trigger a campaign from another campaign's End activity |
| Incremental query activity in orchestrated campaigns | GA | Campaigns; Campaigns & Journeys | April 30, 2026 | Targets only net-new eligible profiles/events |
| Copy orchestrated campaigns across sandboxes | GA | Campaigns; Campaigns & Journeys | April 2026 | Imported campaigns land in draft status |
| Test activity in orchestrated campaigns | GA | Campaigns; Campaigns & Journeys | March 2026 | — |
| Trigger orchestrated campaigns using a signal | GA | Campaigns; Campaigns & Journeys | March 2026 | Remains a batch campaign |
| Transactional category in orchestrated campaigns | GA | Campaigns; Campaigns & Journeys | March 2026 | Rolled out gradually by region |
| Wave sending of outbound messages (campaigns) | GA | Campaigns; Campaigns & Journeys | February 19, 2026 | LA in journeys |
| Batch campaigns | GA | Campaigns; Campaigns & Journeys | Core capability | Scheduled, audience-based sends |
| Orchestrated campaigns (multi-step workflows) | GA | Campaigns; Campaigns & Journeys | Core capability | email, SMS, push, direct mail only |
| Transactional messaging | GA | All base offers | Core capability | email, push, SMS; included with every base offer |

>[!TAB Content & AI]

| Feature | Status | Applies to | Available since | Notes |
|---------|--------|-----------|-----------------|-------|
| Content Advisor Selector | GA | All base offers | May 19, 2026 | AI semantic search for assets and fragments |
| Integrations (third-party data sources) | GA | All base offers | May 4, 2026 | Previously Beta |
| Restrict inheritance breaking in fragments | GA | All base offers | May 21, 2026 | Lock fragments against local edits |
| Adobe Express integration | GA | All base offers | April 23, 2026 | Previously LA |
| Generate content for personalization expressions | GA | All base offers | April 13, 2026 | In personalization editor and Email Designer |
| Convert images to email content templates | GA | All base offers | March 31, 2026 | Previously LA |
| Landing page custom forms | GA | All base offers | March 26, 2026 | Previously LA (US and Australia) |
| Integration of custom Firefly and third-party image models | GA | All base offers | March 2, 2026 | Adobe, Partner (Gemini), and custom models |
| Advanced HTML editor for email templates | LA | All base offers | March 10, 2026 | Email content templates only; contact your representative |
| Email expert mode in email content | LA | All base offers | April 9, 2026 | Contact your Adobe representative |
| Email Designer themes | LA | All base offers | November 5, 2025 | Previously Beta; contact your representative |
| Email Designer (drag-and-drop) | GA | All base offers | Core capability | Visual and HTML authoring |
| Content fragments | GA | All base offers | Core capability | Reusable content blocks |
| Content templates | GA | All base offers | Core capability | — |
| Personalization editor | GA | All base offers | Core capability | Expression-based personalization |
| Generate Content | GA | All base offers | Core capability | Requires AI licensing terms |

>[!TAB Decisioning]

All Decisioning features require the **Decisioning** add-on. See [Packages and capabilities](ajo-packages.md).

| Feature | Status | Applies to | Available since | Notes |
|---------|--------|-----------|-----------------|-------|
| Decisioning support in Direct Mail channel | GA | All base offers | June 3, 2026 | Supports batch decisioning |
| Decisioning rules and ranking formula AI optimization | GA | All base offers | May 5, 2026 | AI-suggested simplifications |
| Decisioning support in email channel | GA | All base offers | April 6, 2026 | Mirror pages supported |
| AI model monitoring | GA | All base offers | March 9, 2026 | Personalized optimization models only |
| Decisioning support in SMS channel | GA | All base offers | February 2, 2026 | — |
| Decisioning support in Push channel | GA | All base offers | January 30, 2026 | — |
| Adobe Experience Manager content fragments in Decisioning | LA | All base offers | May 20, 2026 | Contact your Adobe representative |
| Offer decisioning (decision policies) | GA | All base offers | Core capability | Real-time best-offer selection |
| AI-powered ranking | GA | All base offers | Core capability | Machine-learning offer optimization |

>[!TAB AI agents]

| Feature | Status | Applies to | Available since | Notes |
|---------|--------|-----------|-----------------|-------|
| Journey Agent: create a journey | GA | Journeys; Campaigns & Journeys | January 12, 2026 | Natural-language journey creation |
| Journey Optimizer AI Agent integration via MCP | Beta | All base offers | April 2026 | Public Beta; Claude Web and Desktop |
| Journey Agent: channel content create | LA | All base offers | March 4, 2026 | Contact your Adobe representative |

>[!TAB Administration & data]

| Feature | Status | Applies to | Available since | Notes |
|---------|--------|-----------|-----------------|-------|
| Certificate-based custom authentication in custom actions | GA | All base offers | June 4, 2026 | For certificate-based identity (e.g., Microsoft Entra ID) |
| Customer alerts for campaign lifecycle events | GA | All base offers | June 1, 2026 | Subscribe at sandbox level |
| URL parameter encryption | GA | All base offers | June 1, 2026 | Previously LA; needs key registry permissions |
| Self-service migration tooling APIs | GA | All base offers | February 3, 2026 | — |
| Custom action monitoring | GA | All base offers | February 3, 2026 | Previously LA |
| Message export | GA | All base offers | January 28, 2026 | Available as an add-on |
| Action campaign retrieval API | GA | All base offers | November 24, 2025 | — |
| Migrate subdomains to custom delegation | LA | All base offers | February 19, 2026 | Contact your Adobe representative |
| Sandboxes | GA | All base offers | Core capability | Up to 5 sandboxes; additional available |
| Unified profiles and audiences | GA | All base offers | Core capability | Built on Adobe Experience Platform |
| Reporting and live reports | GA | All base offers | Core capability | — |
| Permissions and access control | GA | All base offers | Core capability | Role-based access |
| REST APIs | GA | All base offers | Core capability | API-first framework |

>[!ENDTABS]

>[!NOTE]
>
>This list is compiled from the [2026 release notes](../rn/release-notes-2026.md) and the [current release notes](../rn/release-notes.md) and reflects the latest known status of each feature. It is not exhaustive. For the full history and the newest additions, always check the [release notes](../rn/release-notes.md).

## Related resources {#related}

- **Understand what's in your package** — [Packages and capabilities](ajo-packages.md)
- **See everything that shipped** — [Release notes](../rn/release-notes.md) | [2026 release notes](../rn/release-notes-2026.md)
- **Get started** — [Get started with Journey Optimizer](get-started.md)
