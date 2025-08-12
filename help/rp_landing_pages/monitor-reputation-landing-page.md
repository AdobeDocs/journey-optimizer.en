---
solution: Journey Optimizer
product: Journey Optimizer
title: Monitor email addresses
description: Monitor email addresses
redpen-status: CREATED_||_2025-08-11_21-08-58
---

# Monitor email addresses{#section-overview}

Managing the health of your email campaigns starts with monitoring the email addresses you send to, ensuring your messages reach the right inboxes while protecting your sender reputation. In Adobe Journey Optimizer, you’ll learn how to use tools like suppression lists to block problematic addresses, retries to handle temporary issues, and allowed lists to control who receives your emails. Each topic builds on the last, showing you how to prevent delivery failures, manage exclusions, and maintain secure, efficient communication with your audience. Whether you’re troubleshooting bounces, refining settings, or securely testing campaigns, these features put you in control of your email deliverability strategy.

## Monitor Email Addresses

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 20px;">
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-list-check -->
                <path d="M152.1,38.2c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,113C-2.3 103.6 -2.3 88.4,7,79s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zm0,160c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,273c-9.4 -9.4 -9.4 -24.6 0 -33.9s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zM224,96c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zm0,160c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zM160,416c0 -17.7 14.3 -32 32 -32l288,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-288 0c-17.7 0 -32 -14.3 -32 -32zM48,368a48,48,0,1,1,0,96,48,48,0,1,1,0 -96z"/>
            </svg>
            Manage the Suppression List
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn how to control email deliverability by managing suppression lists, including adding, removing, and exporting addresses and domains.</p>
        <a href="../using/configuration/manage-suppression-list.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">View Suppression List Guide</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-gear -->
                <path d="M495.9,166.6c3.2,8.7,0.5,18.4 -6.4 24.6l-43.3 39.4c1.1,8.3,1.7,16.8,1.7,25.4s-.6 17.1 -1.7 25.4l43.3,39.4c6.9,6.2,9.6,15.9,6.4,24.6c-4.4 11.9 -9.7 23.3 -15.8 34.3l-4.7 8.1c-6.6 11 -14 21.4 -22.1 31.2c-5.9 7.2 -15.7 9.6 -24.5 6.8l-55.7 -17.7c-13.4 10.3 -28.2 18.9 -44 25.4l-12.5 57.1c-2 9.1 -9 16.3 -18.2 17.8c-13.8 2.3 -28 3.5 -42.5 3.5s-28.7 -1.2 -42.5 -3.5c-9.2 -1.5 -16.2 -8.7 -18.2 -17.8l-12.5 -57.1c-15.8 -6.5 -30.6 -15.1 -44 -25.4L83.1,425.9c-8.8 2.8 -18.6 0.3 -24.5 -6.8c-8.1 -9.8 -15.5 -20.2 -22.1 -31.2l-4.7 -8.1c-6.1 -11 -11.4 -22.4 -15.8 -34.3c-3.2 -8.7 -.5 -18.4 6.4 -24.6l43.3 -39.4C64.6,273.1,64,264.6,64,256s0.6 -17.1 1.7 -25.4L22.4,191.2c-6.9 -6.2 -9.6 -15.9 -6.4 -24.6c4.4 -11.9 9.7 -23.3 15.8 -34.3l4.7 -8.1c6.6 -11 14 -21.4 22.1 -31.2c5.9 -7.2 15.7 -9.6 24.5 -6.8l55.7,17.7c13.4 -10.3 28.2 -18.9 44 -25.4l12.5 -57.1c2 -9.1 9 -16.3 18.2 -17.8C227.3,1.2,241.5,0,256,0s28.7,1.2,42.5,3.5c9.2,1.5,16.2,8.7,18.2,17.8l12.5,57.1c15.8,6.5,30.6,15.1,44,25.4l55.7 -17.7c8.8 -2.8 18.6 -.3 24.5,6.8c8.1,9.8,15.5,20.2,22.1,31.2l4.7,8.1c6.1,11,11.4,22.4,15.8,34.3zM256,336a80,80,0,1,0,0 -160 80,80,0,1,0,0,160z"/>
            </svg>
            Managing Retries and Suppression Lists
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Understand and configure retry mechanisms for soft bounce errors to optimize email deliverability and suppression rules.</p>
        <a href="../using/configuration/retries.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn About Retries</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-shield-halved -->
                <path d="M256,0c4.6,0,9.2,1,13.4,2.9L457.7,82.8c22,9.3,38.4,31,38.3,57.2c-.5 99.2 -41.3 280.7 -213.6 363.2c-16.7 8 -36.1 8 -52.8 0C57.3,420.7,16.5,239.2,16,140c-.1 -26.2 16.3 -47.9 38.3 -57.2L242.7,2.9C246.8,1,251.4,0,256,0zm0,66.8l0,378.1C394,378,431.1,230.1,432,141.4L256,66.8s0,0,0,0z"/>
            </svg>
            Configuring the Allowed List
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Discover how to configure an allowed list to ensure secure and authorized email communications for testing and production.</p>
        <a href="../using/configuration/allow-list.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore Allowed List Configuration</a>
    </div>
</div>