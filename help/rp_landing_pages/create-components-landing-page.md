---
solution: Journey Optimizer
product: Journey Optimizer
title: Create components
description: Create components
redpen-status: CREATED_||_2025-08-11_20-58-59
---
# Create components{#section-overview}

In Adobe Journey Optimizer, creating components like placements, decision rules, and collection qualifiers empowers you to personalize and streamline your marketing efforts. Placements help you ensure the right offers appear in the right spots, decision rules let you define which audiences see specific offers for targeted engagement, and collection qualifiers make organizing and finding offers a breeze. Together, these tools give you full control over how offers are delivered, managed, and tailored to your audience. Whether you're configuring settings, defining eligibility, or organizing your offer library, each topic builds on the other to help you achieve smarter decisioning with ease.

## Create Components

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 20px;">
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-list-check -->
                <path d="M152.1,38.2c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,113C-2.3 103.6 -2.3 88.4,7,79s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zm0,160c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,273c-9.4 -9.4 -9.4 -24.6 0 -33.9s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zM224,96c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zm0,160c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zM160,416c0 -17.7 14.3 -32 32 -32l288,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-288 0c-17.7 0 -32 -14.3 -32 -32zM48,368a48,48,0,1,1,0,96,48,48,0,1,1,0 -96z"/>
            </svg>
            Guide to Creating Placements for Offers
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn how to create and manage placements to ensure the right offer content appears in the right locations within Adobe Journey Optimizer.</p>
        <a href="../using/offers/offer-library/creating-placements.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn how to create placements</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-bullseye -->
                <path d="M448,256A192,192,0,1,0,64,256a192,192,0,1,0,384,0zM0,256a256,256,0,1,1,512,0A256,256,0,1,1,0,256zm256,80a80,80,0,1,0,0 -160 80,80,0,1,0,0,160zm0 -224a144,144,0,1,1,0,288,144,144,0,1,1,0 -288zM224,256a32,32,0,1,1,64,0,32,32,0,1,1 -64 0z"/>
            </svg>
            How to Create Decision Rules in Adobe Journey Optimizer
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Define decision rules to personalize offers by targeting specific audience segments using Adobe Experience Platform data.</p>
        <a href="../using/offers/offer-library/creating-decision-rules.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn how to create decision rules</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-tags -->
                <path d="M345,39.1L472.8,168.4c52.4,53,52.4,138.2,0,191.2L360.8,472.9c-9.3 9.4 -24.5 9.5 -33.9 0.2s-9.5 -24.5 -.2 -33.9L438.6,325.9c33.9 -34.3 33.9 -89.4 0 -123.7L310.9,72.9c-9.3 -9.4 -9.2 -24.6 0.2 -33.9s24.6 -9.2 33.9,0.2zM0,229.5L0,80C0,53.5,21.5,32,48,32l149.5,0c17,0,33.3,6.7,45.3,18.7l168,168c25,25,25,65.5,0,90.5L277.3,442.7c-25 25 -65.5 25 -90.5 0l-168 -168C6.7,262.7,0,246.5,0,229.5zM144,144a32,32,0,1,0 -64 0,32,32,0,1,0,64,0z"/>
            </svg>
            How to Create and Manage Collection Qualifiers in Adobe Journey Optimizer
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Organize and locate offers more effectively by creating and managing collection qualifiers, previously known as 'tags'.</p>
        <a href="../using/offers/offer-library/creating-tags.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn how to create and manage collection qualifiers</a>
    </div>
</div>