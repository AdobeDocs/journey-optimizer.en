---
solution: Journey Optimizer
product: journey optimizer
title: Onboarding project guide | Adobe Journey Optimizer
description: Plan and manage an Adobe Journey Optimizer onboarding project across admin, data, developer, and marketer roles.
feature: Get Started
topic: Content Management
role: Admin
level: Intermediate
hide: true
keywords: journey optimizer, onboarding, onboarding project, rollout, implementation plan, admin, csm, implementation partner, phased checklist
---
# Onboarding project guide {#onboarding-hub}

>[!BEGINSHADEBOX]

**On this page:** Plan and coordinate a full Adobe Journey Optimizer rollout with a phased checklist that spans the administrator, data engineer, developer, and marketer roles.

>[!ENDSHADEBOX]

This page is for **system administrators and implementation partners** coordinating a full Journey Optimizer rollout. It provides a phased checklist covering all roles, with links to the detailed role-specific guides.

>[!NOTE]
>
>If you are an individual getting started with a specific role, go to [Get started with Journey Optimizer](../../rp_landing_pages/get-started-landing-page.md) instead.

## Phase 1 — Environment setup (Administrator) {#phase-1}

Complete these foundational tasks first so the other roles can begin their work:

* [ ] Provision sandboxes (dev, staging, production)
* [ ] Configure user roles and permissions in Adobe Admin Console
* [ ] Set up product profiles and object-level access control
* [ ] Delegate subdomains and configure IP pools
* [ ] Configure channel configurations (email, SMS, push, web, in-app, direct mail)
* [ ] Set up suppression lists and consent policies

➡️ See full details: [Get started for administrators](path/administrator.md)

## Phase 2 — Data foundation (Data Engineer) {#phase-2}

Build the data layer that powers profiles, audiences, and journey triggers:

* [ ] Define identity namespaces
* [ ] Create XDM schemas (profile, experience events, relational)
* [ ] Set up and enable datasets for Real-Time Customer Profile
* [ ] Configure data ingestion (batch and streaming)
* [ ] Create computed attributes
* [ ] Configure journey events and data sources

➡️ See full details: [Get started for data engineers](path/data-engineer.md)

## Phase 3 — Technical integrations (Developer) {#phase-3}

Connect your applications so journeys can run on real-time data:

* [ ] Integrate Mobile SDK (iOS/Android) with push setup
* [ ] Implement Web SDK for web experiences and web push
* [ ] Implement event sending from applications
* [ ] Build custom action endpoints for external system integrations
* [ ] Validate using Adobe Experience Platform Assurance

➡️ See full details: [Get started for developers](path/developer.md)

## Phase 4 — First experiences (Marketer) {#phase-4}

Put the foundation to work by launching your first journeys and campaigns:

* [ ] Build first audience (segment definition or CSV upload)
* [ ] Create a test journey with email action
* [ ] Set up content templates and fragments
* [ ] Publish and monitor a campaign
* [ ] Review live reports

➡️ See full details: [Get started for marketers](path/marketer.md)

## Onboarding checklist (printable) {#checklist}

| Phase | Owner | Status |
|-------|-------|--------|
| Environment setup | Administrator | |
| Data foundation | Data Engineer | |
| Technical integrations | Developer | |
| First experiences | Marketer | |

## Related resources {#related-resources}

* [Roles and responsibilities](quick-start.md) — How the four roles work together and the recommended implementation order.
* [Journey Optimizer tutorials](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/overview){target="_blank"} — Step-by-step videos and guided walkthroughs for every role.
* [Get started with data management](../data/gs-data.md) — How data is ingested, unified, and activated.
