---
solution: Journey Optimizer
product: Journey Optimizer
title: Channel configuration
description: Channel configuration
redpen-status: CREATED_||_2025-08-11_21-10-00
---

# Channel configuration{#section-overview}

Channel configuration in Adobe Journey Optimizer empowers you to manage how messages are delivered across various channels—like email, SMS, push notifications, and web—ensuring tailored and effective communication. Whether you're setting up technical parameters, configuring subdomains, or optimizing email deliverability with IP warmup plans, each step is designed to enhance message performance and compliance. You'll also find tools to monitor email reputation, manage suppression lists, and even archive messages for auditing purposes. Dive deeper into the topics ahead to discover how these configurations work together, helping you create seamless, impactful customer experiences.

## Channel Configuration

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 20px;">
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-circle-play -->
                <path d="M0,256a256,256,0,1,1,512,0A256,256,0,1,1,0,256zM188.3,147.1c-7.6 4.2 -12.3 12.3 -12.3 20.9l0,176c0,8.7,4.7,16.7,12.3,20.9s16.8,4.1,24.3 -.5l144 -88c7.1 -4.4 11.5 -12.1 11.5 -20.5s-4.4 -16.1 -11.5 -20.5l-144 -88c-7.4 -4.5 -16.7 -4.7 -24.3 -.5z"/>
            </svg>
            Getting Started with Channel Configuration
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn the steps to configure channels in Adobe Journey Optimizer, including technical parameters and advanced settings for optimal performance.</p>
        <a href="../using/configuration/get-started-configuration.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Get started with channel configuration</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-list-check -->
                <path d="M152.1,38.2c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,113C-2.3 103.6 -2.3 88.4,7,79s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zm0,160c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,273c-9.4 -9.4 -9.4 -24.6 0 -33.9s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zM224,96c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zm0,160c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zM160,416c0 -17.7 14.3 -32 32 -32l288,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-288 0c-17.7 0 -32 -14.3 -32 -32zM48,368a48,48,0,1,1,0,96,48,48,0,1,1,0 -96z"/>
            </svg>
            Set Up and Manage Channel Configurations
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Follow a detailed guide to create, edit, deactivate, and monitor channel configurations, ensuring proper technical parameters and compliance.</p>
        <a href="../using/configuration/channel-surfaces.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn how to set up channel configurations</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-gear -->
                <path d="M495.9,166.6c3.2,8.7,0.5,18.4 -6.4 24.6l-43.3 39.4c1.1,8.3,1.7,16.8,1.7,25.4s-.6 17.1 -1.7 25.4l43.3,39.4c6.9,6.2,9.6,15.9,6.4,24.6c-4.4 11.9 -9.7 23.3 -15.8 34.3l-4.7 8.1c-6.6 11 -14 21.4 -22.1 31.2c-5.9 7.2 -15.7 9.6 -24.5 6.8l-55.7 -17.7c-13.4 10.3 -28.2 18.9 -44 25.4l-12.5 57.1c-2 9.1 -9 16.3 -18.2 17.8c-13.8 2.3 -28 3.5 -42.5 3.5s-28.7 -1.2 -42.5 -3.5c-9.2 -1.5 -16.2 -8.7 -18.2 -17.8l-12.5 -57.1c-15.8 -6.5 -30.6 -15.1 -44 -25.4L83.1,425.9c-8.8 2.8 -18.6 0.3 -24.5 -6.8c-8.1 -9.8 -15.5 -20.2 -22.1 -31.2l-4.7 -8.1c-6.1 -11 -11.4 -22.4 -15.8 -34.3c-3.2 -8.7 -.5 -18.4 6.4 -24.6l43.3 -39.4C64.6,273.1,64,264.6,64,256s0.6 -17.1 1.7 -25.4L22.4,191.2c-6.9 -6.2 -9.6 -15.9 -6.4 -24.6c4.4 -11.9 9.7 -23.3 15.8 -34.3l4.7 -8.1c6.6 -11 14 -21.4 22.1 -31.2c5.9 -7.2 15.7 -9.6 24.5 -6.8l55.7,17.7c13.4 -10.3 28.2 -18.9 44 -25.4l12.5 -57.1c2 -9.1 9 -16.3 18.2 -17.8C227.3,1.2,241.5,0,256,0s28.7,1.2,42.5,3.5c9.2,1.5,16.2,8.7,18.2,17.8l12.5,57.1c15.8,6.5,30.6,15.1,44,25.4l55.7 -17.7c8.8 -2.8 18.6 -.3 24.5,6.8c8.1,9.8,15.5,20.2,22.1,31.2l4.7,8.1c6.1,11,11.4,22.4,15.8,34.3zM256,336a80,80,0,1,0,0 -160 80,80,0,1,0,0,160z"/>
            </svg>
            Guided Channel Setup
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Configure mobile and web channels efficiently with step-by-step instructions and resources provided during the setup process.</p>
        <a href="guided-setup-landing-page.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore Guided Channel Setup</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-screwdriver-wrench -->
                <path d="M78.6,5C69.1 -2.4 55.6 -1.5 47,7L7,47c-8.5 8.5 -9.4 22 -2.1 31.6l80,104c4.5,5.9,11.6,9.4,19,9.4l54.1,0,109,109c-14.7 29 -10 65.4,14.3,89.6l112,112c12.5,12.5,32.8,12.5,45.3,0l64 -64c12.5 -12.5 12.5 -32.8 0 -45.3l-112 -112c-24.2 -24.2 -60.6 -29 -89.6 -14.3l-109 -109 0 -54.1c0 -7.5 -3.5 -14.5 -9.4 -19L78.6,5zM19.9,396.1C7.2,408.8,0,426.1,0,444.1C0,481.6,30.4,512,67.9,512c18,0,35.3 -7.2 48 -19.9L233.7,374.3c-7.8 -20.9 -9 -43.6 -3.6 -65.1l-61.7 -61.7L19.9,396.1zM512,144c0 -10.5 -1.1 -20.7 -3.2 -30.5c-2.4 -11.2 -16.1 -14.1 -24.2 -6l-63.9 63.9c-3 3 -7.1 4.7 -11.3 4.7L352,176c-8.8 0 -16 -7.2 -16 -16l0 -57.4c0 -4.2 1.7 -8.3 4.7 -11.3l63.9 -63.9c8.1 -8.1 5.2 -21.8 -6 -24.2C388.7,1.1,378.5,0,368,0C288.5,0,224,64.5,224,144l0,0.8,85.3,85.3c36 -9.1 75.8,0.5,104,28.7L429,274.5c49 -23 83 -72.8 83 -130.5zM56,432a24,24,0,1,1,48,0,24,24,0,1,1 -48 0z"/>
            </svg>
            Delegate and Manage Email Subdomains
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn to delegate and configure email subdomains to optimize deliverability and maintain domain reputation.</p>
        <a href="delegate-subdomains-landing-page.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Delegate email subdomains</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-chart-line -->
                <path d="M64,64c0 -17.7 -14.3 -32 -32 -32S0,46.3,0,64L0,400c0,44.2,35.8,80,80,80l400,0c17.7,0,32 -14.3 32 -32s-14.3 -32 -32 -32L80,416c-8.8 0 -16 -7.2 -16 -16L64,64zm406.6,86.6c12.5 -12.5 12.5 -32.8 0 -45.3s-32.8 -12.5 -45.3 0L320,210.7l-57.4 -57.4c-12.5 -12.5 -32.8 -12.5 -45.3 0l-112 112c-12.5 12.5 -12.5 32.8,0,45.3s32.8,12.5,45.3,0L240,221.3l57.4,57.4c12.5,12.5,32.8,12.5,45.3,0l128 -128z"/>
            </svg>
            Implement an IP Warmup Plan
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Create and execute IP warmup plans to establish sender reputation and enhance email deliverability.</p>
        <a href="implement-ip-warmup-plan-landing-page.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn about IP warmup plans</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-shield-halved -->
                <path d="M256,0c4.6,0,9.2,1,13.4,2.9L457.7,82.8c22,9.3,38.4,31,38.3,57.2c-.5 99.2 -41.3 280.7 -213.6 363.2c-16.7 8 -36.1 8 -52.8 0C57.3,420.7,16.5,239.2,16,140c-.1 -26.2 16.3 -47.9 38.3 -57.2L242.7,2.9C246.8,1,251.4,0,256,0zm0,66.8l0,378.1C394,378,431.1,230.1,432,141.4L256,66.8s0,0,0,0z"/>
            </svg>
            Monitor Email Deliverability and Reputation
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Manage suppression lists, allowed lists, and retry mechanisms to optimize email deliverability and reputation.</p>
        <a href="monitor-reputation-landing-page.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Monitor email addresses</a>
    </div>
</div>

## Additional Resources

- **[Using Seed Lists](../using/configuration/seed-lists.md)** - Learn how to create and manage seed lists to monitor email deliveries and ensure campaign assurance.
- **[Archiving Support for Compliance](../using/configuration/archiving-support.md)** - Configure archiving features like BCC emails and dataset management to ensure compliance with regulations like GDPR and HIPAA.
- **[Managing Execution Addresses](../using/configuration/primary-email-addresses.md)** - Configure and prioritize email or phone number fields for communication across journeys and campaigns.
