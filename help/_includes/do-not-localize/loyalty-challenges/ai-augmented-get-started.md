---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces Loyalty Challenges, a gamified loyalty program capability in Adobe Journey Optimizer, and explains the three phases of setup, authoring/launch, and measurement, along with prerequisites and where to find detailed documentation.

**Intents:**

* Understand what Loyalty Challenges are and the business outcomes they enable.
* Distinguish the four challenge types: Standard, Streak, Sequential, and Bring your own data.
* Understand the three broad phases of using Loyalty Challenges: setup, execution, and measurement, and which roles typically perform each.
* Identify the prerequisites needed before creating a challenge, including permissions, program configuration, and target audience.
* Locate developer resources (REST APIs) for managing challenges and profile participation programmatically.

**Glossary:**

* **Loyalty Challenges**: A capability for creating engaging, gamified loyalty programs that reward customers for specific actions such as purchases, reviews, social media engagement, and referrals *(product-specific)*
* **Standard challenge**: A challenge type where customers complete any specified number of tasks in any order *(product-specific)*
* **Streak challenge**: A challenge type where customers complete the same task multiple times consecutively *(product-specific)*
* **Sequential challenge**: A challenge type where customers complete tasks in a defined order *(product-specific)*
* **Bring your own data challenge**: A challenge type (restricted availability) where the challenge framework of tasks and rewards is assembled from a Loyalty Challenges data integration; Settings, Content, and Messaging are configured the same way as for other challenge types *(product-specific)*
* **Loyalty Challenge Management**: A tool within Coworker skills for loyalty that lets you create and manage loyalty challenges using natural language prompts *(product-specific)*
* **Loyalty configurations**: The menu where administrators configure reward providers, event mappings, product inventory, exclusions, and global settings *(product-specific)*

**Guardrails:**

* Bring your own data challenges have restricted availability.

**Prerequisites and permissions:**

* You must be assigned to a Loyalty role to use Loyalty Challenges.
* Default roles are available for administrators, practitioners, and analysts in the Prod sandbox.
* For non-Prod sandboxes, your administrator must create a custom role with the required Loyalty permissions.
* Administrators configure reward providers, event mappings, product inventory, exclusions, and global settings in the Loyalty configurations menu; marketers who only create challenges do not need access to this menu.
* The target audience that defines which customers are eligible to participate must exist in Adobe Experience Platform before creating a challenge.

**Terminology:**

* Canonical name: Loyalty Challenges

**FAQ:**

* **Q: What challenge types are available?** — Standard, Streak, Sequential, and Bring your own data (restricted availability).
* **Q: What are the three phases of using Loyalty Challenges?** — Set up your program (admin), author and launch challenges (practitioner), and monitor performance (practitioner/analyst).
* **Q: What permissions do I need to use Loyalty Challenges?** — You must be assigned to a Loyalty role; default roles exist for administrators, practitioners, and analysts in the Prod sandbox, and a custom role is required in non-Prod sandboxes.
* **Q: Who needs access to the Loyalty configurations menu?** — Administrators who configure reward providers, event mappings, product inventory, exclusions, and global settings; marketers who only create challenges do not need access.
* **Q: Can I create challenges without an existing target audience?** — No, the target audience must exist in Adobe Experience Platform before creating your challenge.
* **Q: Can I manage loyalty challenges with natural language prompts?** — Yes, using Loyalty Challenge Management in Coworker skills for loyalty.

**Related pages:**

* To configure reward providers, event mappings, product inventory, and exclusions: Learn how to configure loyalty challenges (loyalty-challenges/loyalty-admin.md)
* To build and configure your first loyalty challenge: Learn how to create challenges (loyalty-challenges/create-challenges.md)
* To track program KPIs, challenge results, and task-level metrics: Explore Loyalty performance (loyalty-challenges/loyalty-performance.md)
* To configure Loyalty Challenges permissions: Learn how to configure Loyalty Challenges permissions (loyalty-challenges/loyalty-permissions.md)
* To confirm a target audience exists before creating a challenge: Learn how to work with audiences (audience/about-audiences.md)
* To create and manage loyalty challenges with natural language prompts: Coworker skills for loyalty (loyalty-challenges/loyalty-coworker-skills.md)
* To see Loyalty Challenges in action: interactive demo (loyalty-challenges/loyalty-challenges-demo.md)

**Personas:**

* **marketer:** Can create challenges by selecting a type: Standard, Streak, Sequential, or Bring your own data. Can configure settings such as audience, schedule, and rules, then define tasks and rewards, and publish the challenge to generate the auto-built journey. The page states that Bring your own data challenges have restricted availability. Where: "How it works".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Select a challenge type: Standard, Streak, Sequential, or Bring your own data.
* **Success check:** The challenge is live after you publish it and generate the auto-built journey.
* **Previous:** Confirm you have the required Loyalty role permissions: Loyalty Challenges permissions (loyalty-challenges/loyalty-permissions.md); Ensure the target audience exists in Adobe Experience Platform: About Adobe Experience Platform audiences (audience/about-audiences.md)
* **Next:** Build and configure your first loyalty challenge: Create loyalty challenges (loyalty-challenges/create-challenges.md); Track program KPIs, challenge results, and task-level metrics: Explore loyalty performance (loyalty-challenges/loyalty-performance.md)

+++

<!-- ai-section-version: 1 | source-hash: 373ca453 -->
