---
solution: Journey Optimizer
product: journey optimizer
title: About Adobe Experience Platform audiences
description: Learn how to work with Adobe Experience Platform audiences
feature: Audiences, Profiles
topic: Content Management
role: User
level: Beginner
exl-id: 71c652ba-f38f-452c-9c1b-dcd728307baf
TQID: https://experienceleague.adobe.com/HkybhydJwQDHVEXCKM5o16ZNeiBk-n9mogm-2pwFKus
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: baecb07f-ce89-4ebb-9cd9-0f7c053f944f
    internal-label: Journey management
subfeature_v2:
  - id: f42b4d14-fe8a-428b-b62e-e7995eaab1b3
    internal-label: Audience Qualification events
  - id: b32bb433-f8c6-4931-8e52-e657230a3bf2
    internal-label: Audiences
  - id: e95b6013-acbe-46e9-a3b5-b80e14088d7d
    internal-label: Audience guardrails
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---
# Custom Upload {#custom-upload}

>[!BEGINSHADEBOX]

**On this page:** Learn how to import an audience from a CSV file using the Adobe Experience Platform Audience Portal and map its identity attribute to customer profiles.

>[!ENDSHADEBOX]

Adobe Experience Platform Audience Portal allows you to import an audience using a CSV file.

During the custom upload process, specify the CSV attribute to use as the identity and the profile identity it maps to. This establishes a link between the audience data and the profile. If the CSV file contains an identity value not found in the profile, a new profile is created with that identity value.

![](assets/import-audience.png)

Detailed information on how to import audiences is available in Adobe Experience Platform [Segmentation Service documentation](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-portal#import-audience){target="_blank"}.

>[!NOTE]
>
>For custom upload audiences (CSV upload) and other external audiences, **[!UICONTROL Incremental read]** is not functionally supported today. On each recurrence, the **entire audience** is retrieved, regardless of the Incremental read toggle setting.

Learn how to upload audiences in CSV format in video:

>[!VIDEO](https://video.tv.adobe.com/v/3421714?quality=12)
