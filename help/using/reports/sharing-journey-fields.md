---
solution: Journey Optimizer
product: journey optimizer
title: journey fields
description: journey fields
feature: Journeys, Reporting
topic: Content Management
role: Developer, Admin
level: Experienced
exl-id: 177b4a97-c757-40ca-a190-fbd88169e5e2
TQID: https://experienceleague.adobe.com/dpQ6PEm-afX4PZuWSPrpAWDH7yBhUKZHZRF134VehAg
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a9f73820-6899-47c2-a597-3fec28ab756a
    internal-label: Reporting
  - id: b49ca41f-eb7a-4f4b-abeb-a97c06fd0c04
    internal-label: Track and monitor
subfeature_v2:
  - id: d145add9-d5b9-481b-aa8a-e15e6bb7f813
    internal-label: Performance monitoring
  - id: a7289281-9ae4-47b1-b8cf-4028b98af776
    internal-label: Deliverability
  - id: b5afe8bf-bda6-41b5-ba06-922638872d63
    internal-label: Metrics catalog
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
---
# Journey fields {#sharing-journey-fields}

>[!BEGINSHADEBOX]

**On this page:** Reference the journey fields used in the journey schema to describe each journey in journey step event reporting, such as journey ID, version, name, and description.

>[!ENDSHADEBOX]

This field group is used in the **journey** schema (in relation with **journeyStepEvent**). It contains the fields listed below.


>[!NOTE]
>
>Learn more about journey properties attributes [in this section](../building-journeys/expression/journey-properties.md#journey-properties-fields).


## journeyID {#journeyid-field}

Id of the main journey.

Type: string

## journeyVersionID {#journeyversionid-field}

Id of the journey version. This id represents the identity of a journey.

Type: string

## name {#name-field}

Name of the journey.

Type: string

>[!NOTE]
>
>The journey name is used to link journey execution data with reporting datasets. If you rename a journey, ensure that the new name matches the name in your reporting dataset to maintain accurate reporting. A mismatch can cause reporting data to not appear as expected. Learn more about [troubleshooting missing reporting data](../building-journeys/report-journey.md#troubleshooting-missing-data).

## description {#description-field}

Description of the journey.

Type: string

## version {#version-field}

Version, represented as `major`.`minor`

Type: string
