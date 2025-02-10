---
solution: Journey Optimizer
product: journey optimizer
title: About Adobe Experience Platform audiences
description: Learn how to work with Adobe Experience Platform audiences
feature: Audiences, Profiles
topic: Content Management
role: User
level: Beginner
---

# Custom Upload {#custom-upload}

Adobe Experience Platform Audience Portal allows you to import an audience using a CSV file.

During the custom upload process, specify the CSV attribute to use as the identity and the profile identity it maps to. This establishes a link between the audience data and the profile. If the CSV file contains an identity value not found in the profile, a new profile is created with that identity value.

>[!NOTE]
>
>For custom upload audiences, if "Incremental read" is enabled in a recurring journey, profiles are only retrieved on the first recurrence, as these audiences are fixed.

![](assets/import-audience.png)

Detailed information on how to import audiences is available in Adobe Experience Platform [Segmentation Service documentation](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-portal#import-audience){target="_blank"}.

Learn how to upload audiences in CSV format in video:

>[!VIDEO](https://video.tv.adobe.com/v/3421714?quality=12)
