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
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
subfeature_v2:
  - id: fb9a80eb-bebc-492f-a0e9-584595621ebb
    internal-label: Publish
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
