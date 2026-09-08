---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the different ways a live journey can end — including the global 91-day timeout, manual closure to new entrances, and emergency stop — along with their effects on in-progress profiles.

**Intents:**

* Close a live journey to new entrances while allowing current profiles to complete it
* Stop a journey immediately to halt all in-progress profiles
* Understand the difference between Closed, Stopped, and Finished journey statuses
* Determine when a journey is considered "finished" based on its type and configuration
* Delete a journey once it has reached the Finished status

**Glossary:**

* **End tag**: An auto-generated, non-removable node displayed at the end of each journey path during authoring; its label can be changed *(product-specific)*
* **Close to new entrances**: A manual action that prevents new profiles from entering a journey while allowing existing profiles to complete their path *(product-specific)*
* **Global journey timeout**: The 91-day maximum duration after which a journey automatically switches to Finished status and all profile data is removed *(product-specific)*
* **Stopped status**: A journey state in which all in-progress profiles are immediately halted; used only for emergencies *(product-specific)*

**Guardrails:**

* Closed and Stopped journeys cannot be restarted or deleted; only a new version or duplicate can be created.
* Only journeys in Finished status can be deleted.
* Stopping a journey requires the Manage journeys permission; journeys with inline campaigns or messaging nodes also require Campaigns > Publish Campaigns permission.
* After the 91-day global timeout, all profile journey data is removed and remaining profiles are automatically exited.
* A non-recurring Read Audience journey without long-running Wait, Reaction, or event-triggered nodes automatically transitions to Stopped approximately 96 hours (~4 days) after its scheduled run. The journey remains in Live status during this buffer. Waves-based journeys, and journeys that use Send-Time Optimization, are excluded from this auto-stop and remain subject to the 91-day global timeout unless manually closed or stopped.

**Terminology:**

* Canonical name: Close to new entrances — Acronym: n/a — variants: close journey, manually close
* Synonyms: "Stopped" journey ≠ "Closed" journey — stopped halts all profiles immediately; closed only blocks new entrances
* Do not confuse: "End tag" ≠ "End activity" — the End tag is auto-generated and cannot be removed; the End activity is a placeable canvas node

**FAQ:**

* **Q: What is the difference between closing and stopping a journey?** — Closing blocks new entrances but lets existing profiles finish; stopping immediately halts all profiles in their tracks.
* **Q: Why does a non-recurring journey remain in Live status for several days after its run?** — This is expected. AJO applies a safety buffer of ~96 hours (~4 days): 24 hours to allow in-flight sends to complete, plus 72 hours for Quiet Hours deferrals. The journey transitions to Stopped shortly after the buffer elapses.
* **Q: Do waves-based journeys auto-stop after ~96 hours?** — No. Waves-based journeys, and journeys that use Send-Time Optimization, are excluded from this automatic stop so they can stay active across all scheduled waves. They follow the standard 91-day journey timeout unless closed or stopped manually.
* **Q: When does a Read audience journey reach Finished status?** — For a non-recurring Read Audience journey: it auto-stops to Stopped approximately 96 hours (~4 days) after its scheduled run (safety buffer: 24h idle window + 72h Quiet Hours allowance). The journey remains in Live status during this buffer. If Wait, Reaction, or event nodes keep profiles active, the standard 91-day global timeout applies instead. Finished is reached when a Closed journey hits the 91-day global timeout, or per recurring-journey rules in the finished-definition table.
* **Q: Can I delete a Closed journey?** — No, only Finished journeys can be deleted.
* **Q: What happens to profiles still in a journey when the 91-day timeout hits?** — They are automatically exited from the journey at that point.
* **Q: Do I need special permissions to stop a journey?** — Yes, the Manage journeys permission is required, plus Campaigns > Publish Campaigns if the journey contains inline campaigns or messaging nodes.

+++
