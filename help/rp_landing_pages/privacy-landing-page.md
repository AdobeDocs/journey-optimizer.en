---
solution: Journey Optimizer
product: Journey Optimizer
title: Privacy
description: Privacy
redpen-status: CREATED_||_2025-08-11_21-20-29
---

# Privacy{#section-overview}

Adobe Journey Optimizer’s Privacy tools empower you to manage sensitive customer data responsibly and comply with regulations like GDPR. Whether you need to handle access or deletion requests, track user actions, enforce consent preferences, or protect data through governance policies, these features work together to simplify data management while ensuring compliance and security. You’ll learn how to process privacy requests, audit user actions, manage consent, apply governance rules, and leverage advanced security options like Customer Managed Keys. These tools are designed to build trust, safeguard information, and seamlessly integrate privacy into your workflows.

## Privacy Features in Adobe Journey Optimizer

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 20px;">
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-book -->
                <path d="M128,0C75,0,32,43,32,96L32,416c0,53,43,96,96,96l288,0,32,0c17.7,0,32 -14.3 32 -32s-14.3 -32 -32 -32l0 -64c17.7,0,32 -14.3 32 -32l0 -320c0 -17.7 -14.3 -32 -32 -32L416,0,128,0zm0,384l256,0,0,64L128,448c-17.7 0 -32 -14.3 -32 -32s14.3 -32 32 -32zm32 -240c0 -8.8 7.2 -16 16 -16l192,0c8.8,0,16,7.2,16,16s-7.2 16 -16 16l-192 0c-8.8 0 -16 -7.2 -16 -16zm16,48l192,0c8.8,0,16,7.2,16,16s-7.2 16 -16 16l-192 0c-8.8 0 -16 -7.2 -16 -16s7.2 -16 16 -16z"/>
            </svg>
            Privacy Management Overview
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn how to manage privacy in Adobe Journey Optimizer and Adobe Experience Platform, including data requests, audit logs, consent, and governance policies.</p>
        <a href="../using/privacy/get-started-privacy.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Get started with privacy management</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-circle-play -->
                <path d="M0,256a256,256,0,1,1,512,0A256,256,0,1,1,0,256zM188.3,147.1c-7.6 4.2 -12.3 12.3 -12.3 20.9l0,176c0,8.7,4.7,16.7,12.3,20.9s16.8,4.1,24.3 -.5l144 -88c7.1 -4.4 11.5 -12.1 11.5 -20.5s-4.4 -16.1 -11.5 -20.5l-144 -88c-7.4 -4.5 -16.7 -4.7 -24.3 -.5z"/>
            </svg>
            Managing Privacy Requests
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Follow step-by-step instructions to create and handle privacy requests, ensuring GDPR compliance using the Privacy Service UI and API.</p>
        <a href="../using/privacy/requests.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn to manage privacy requests</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-list-check -->
                <path d="M152.1,38.2c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,113C-2.3 103.6 -2.3 88.4,7,79s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zm0,160c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,273c-9.4 -9.4 -9.4 -24.6 0 -33.9s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zM224,96c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zm0,160c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zM160,416c0 -17.7 14.3 -32 32 -32l288,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-288 0c-17.7 0 -32 -14.3 -32 -32zM48,368a48,48,0,1,1,0,96,48,48,0,1,1,0 -96z"/>
            </svg>
            Audit Logs for User Actions
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Track and monitor actions performed on Adobe Journey Optimizer resources using audit logs for compliance and troubleshooting.</p>
        <a href="../using/privacy/audit-logs.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore audit logs</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-screwdriver-wrench -->
                <path d="M78.6,5C69.1 -2.4 55.6 -1.5 47,7L7,47c-8.5 8.5 -9.4 22 -2.1 31.6l80,104c4.5,5.9,11.6,9.4,19,9.4l54.1,0,109,109c-14.7 29 -10 65.4,14.3,89.6l112,112c12.5,12.5,32.8,12.5,45.3,0l64 -64c12.5 -12.5 12.5 -32.8 0 -45.3l-112 -112c-24.2 -24.2 -60.6 -29 -89.6 -14.3l-109 -109 0 -54.1c0 -7.5 -3.5 -14.5 -9.4 -19L78.6,5zM19.9,396.1C7.2,408.8,0,426.1,0,444.1C0,481.6,30.4,512,67.9,512c18,0,35.3 -7.2 48 -19.9L233.7,374.3c-7.8 -20.9 -9 -43.6 -3.6 -65.1l-61.7 -61.7L19.9,396.1zM512,144c0 -10.5 -1.1 -20.7 -3.2 -30.5c-2.4 -11.2 -16.1 -14.1 -24.2 -6l-63.9 63.9c-3 3 -7.1 4.7 -11.3 4.7L352,176c-8.8 0 -16 -7.2 -16 -16l0 -57.4c0 -4.2 1.7 -8.3 4.7 -11.3l63.9 -63.9c8.1 -8.1 5.2 -21.8 -6 -24.2C388.7,1.1,378.5,0,368,0C288.5,0,224,64.5,224,144l0,0.8,85.3,85.3c36 -9.1 75.8,0.5,104,28.7L429,274.5c49 -23 83 -72.8 83 -130.5zM56,432a24,24,0,1,1,48,0,24,24,0,1,1 -48 0z"/>
            </svg>
            Performing Data Lifecycle Operations
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Discover how to manage data lifecycle tasks like updating and deleting records while maintaining data hygiene and adhering to organizational policies.</p>
        <a href="../using/privacy/data-hygiene.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn about data lifecycle operations</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-bullseye -->
                <path d="M448,256A192,192,0,1,0,64,256a192,192,0,1,0,384,0zM0,256a256,256,0,1,1,512,0A256,256,0,1,1,0,256zm256,80a80,80,0,1,0,0 -160 80,80,0,1,0,0,160zm0 -224a144,144,0,1,1,0,288,144,144,0,1,1,0 -288zM224,256a32,32,0,1,1,64,0,32,32,0,1,1 -64 0z"/>
            </svg>
            Consent Management
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Manage recipient consent preferences and policies to comply with privacy regulations and improve user trust and experiences.</p>
        <a href="consent-landing-page.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Get started with consent management</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-shield-halved -->
                <path d="M256,0c4.6,0,9.2,1,13.4,2.9L457.7,82.8c22,9.3,38.4,31,38.3,57.2c-.5 99.2 -41.3 280.7 -213.6 363.2c-16.7 8 -36.1 8 -52.8 0C57.3,420.7,16.5,239.2,16,140c-.1 -26.2 16.3 -47.9 38.3 -57.2L242.7,2.9C246.8,1,251.4,0,256,0zm0,66.8l0,378.1C394,378,431.1,230.1,432,141.4L256,66.8s0,0,0,0z"/>
            </svg>
            Data Governance Policies
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn how to implement data governance policies using labels and marketing actions to ensure compliance and protect sensitive data.</p>
        <a href="../using/action/action-privacy.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Set up data governance</a>
    </div>
</div>

## Additional Resources

- **[Customer Managed Keys (CMK)](../using/privacy/cmk.md)** - Set up and manage customer encryption keys for securing data in Adobe Journey Optimizer, ensuring privacy and security compliance.
