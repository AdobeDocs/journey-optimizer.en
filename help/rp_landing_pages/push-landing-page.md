---
solution: Journey Optimizer
product: Journey Optimizer
title: Push notification channel
description: Push notification channel
redpen-status: CREATED_||_2025-08-11_20-37-12
---
# Push notification channel{#section-overview}

Push notifications in Adobe Journey Optimizer are a powerful way to engage your mobile app users by delivering timely, personalized messages directly to their devices—even when they’re not actively using your app. Whether you’re looking to re-engage dormant users, share updates, or drive specific actions, this channel lets you create impactful campaigns tailored to your audience. In this section, you’ll explore everything from setting up push notifications and designing compelling content to validating and sending your messages. Along the way, you’ll learn how to optimize for different platforms (iOS and Android), manage opt-ins, and leverage advanced features like silent notifications and rapid delivery modes for large-scale outreach. Let’s turn your app into a dynamic communication hub!

## Push Notification Channel

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 20px;">
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-book -->
                <path d="M128,0C75,0,32,43,32,96L32,416c0,53,43,96,96,96l288,0,32,0c17.7,0,32 -14.3 32 -32s-14.3 -32 -32 -32l0 -64c17.7,0,32 -14.3 32 -32l0 -320c0 -17.7 -14.3 -32 -32 -32L416,0,128,0zm0,384l256,0,0,64L128,448c-17.7 0 -32 -14.3 -32 -32s14.3 -32 32 -32zm32 -240c0 -8.8 7.2 -16 16 -16l192,0c8.8,0,16,7.2,16,16s-7.2 16 -16 16l-192 0c-8.8 0 -16 -7.2 -16 -16zm16,48l192,0c8.8,0,16,7.2,16,16s-7.2 16 -16 16l-192 0c-8.8 0 -16 -7.2 -16 -16s7.2 -16 16 -16z"/>
            </svg>
            Introduction to Push Notifications
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn the basics of push notifications, their purpose, prerequisites, and how they fit into Adobe Journey Optimizer workflows.</p>
        <a href="../using/push/get-started-push.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn more</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-circle-play -->
                <path d="M0,256a256,256,0,1,1,512,0A256,256,0,1,1,0,256zM188.3,147.1c-7.6 4.2 -12.3 12.3 -12.3 20.9l0,176c0,8.7,4.7,16.7,12.3,20.9s16.8,4.1,24.3 -.5l144 -88c7.1 -4.4 11.5 -12.1 11.5 -20.5s-4.4 -16.1 -11.5 -20.5l-144 -88c-7.4 -4.5 -16.7 -4.7 -24.3 -.5z"/>
            </svg>
            Create and Configure Push Notifications
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Step-by-step guide to creating and configuring push notifications, including Rapid delivery mode for urgent, large-scale campaigns.</p>
        <a href="../using/push/create-push.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Start creating</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-puzzle-piece -->
                <path d="M192,104.8c0 -9.2 -5.8 -17.3 -13.2 -22.8C167.2,73.3,160,61.3,160,48c0 -26.5 28.7 -48 64 -48s64,21.5,64,48c0,13.3 -7.2 25.3 -18.8 34c-7.4 5.5 -13.2 13.6 -13.2 22.8c0,12.8,10.4,23.2,23.2,23.2l56.8,0c26.5,0,48,21.5,48,48l0,56.8c0,12.8,10.4,23.2,23.2,23.2c9.2,0,17.3 -5.8 22.8 -13.2c8.7 -11.6 20.7 -18.8 34 -18.8c26.5,0,48,28.7,48,64s-21.5 64 -48 64c-13.3 0 -25.3 -7.2 -34 -18.8c-5.5 -7.4 -13.6 -13.2 -22.8 -13.2c-12.8 0 -23.2 10.4 -23.2 23.2L384,464c0,26.5 -21.5 48 -48 48l-56.8 0c-12.8 0 -23.2 -10.4 -23.2 -23.2c0 -9.2 5.8 -17.3 13.2 -22.8c11.6 -8.7 18.8 -20.7 18.8 -34c0 -26.5 -28.7 -48 -64 -48s-64 21.5 -64 48c0,13.3,7.2,25.3,18.8,34c7.4,5.5,13.2,13.6,13.2,22.8c0,12.8 -10.4 23.2 -23.2 23.2L48,512c-26.5 0 -48 -21.5 -48 -48L0,343.2C0,330.4,10.4,320,23.2,320c9.2,0,17.3,5.8,22.8,13.2C54.7,344.8,66.7,352,80,352c26.5,0,48 -28.7 48 -64s-21.5 -64 -48 -64c-13.3 0 -25.3 7.2 -34 18.8C40.5,250.2,32.4,256,23.2,256C10.4,256,0,245.6,0,232.8L0,176c0 -26.5 21.5 -48 48 -48l120.8,0c12.8,0,23.2 -10.4 23.2 -23.2z"/>
            </svg>
            Design Your Push Notification
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Discover how to design and personalize push notifications with media, buttons, silent notifications, custom data, and advanced options.</p>
        <a href="../using/push/design-push.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Design now</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-list-check -->
                <path d="M152.1,38.2c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,113C-2.3 103.6 -2.3 88.4,7,79s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zm0,160c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,273c-9.4 -9.4 -9.4 -24.6 0 -33.9s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zM224,96c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zm0,160c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zM160,416c0 -17.7 14.3 -32 32 -32l288,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-288 0c-17.7 0 -32 -14.3 -32 -32zM48,368a48,48,0,1,1,0,96,48,48,0,1,1,0 -96z"/>
            </svg>
            Preview, Validate, and Send Push Notifications
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn how to preview, validate, and send push notifications, ensuring successful delivery and error resolution.</p>
        <a href="../using/push/send-push.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Check and send</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-gear -->
                <path d="M495.9,166.6c3.2,8.7,0.5,18.4 -6.4 24.6l-43.3 39.4c1.1,8.3,1.7,16.8,1.7,25.4s-.6 17.1 -1.7 25.4l43.3,39.4c6.9,6.2,9.6,15.9,6.4,24.6c-4.4 11.9 -9.7 23.3 -15.8 34.3l-4.7 8.1c-6.6 11 -14 21.4 -22.1 31.2c-5.9 7.2 -15.7 9.6 -24.5 6.8l-55.7 -17.7c-13.4 10.3 -28.2 18.9 -44 25.4l-12.5 57.1c-2 9.1 -9 16.3 -18.2 17.8c-13.8 2.3 -28 3.5 -42.5 3.5s-28.7 -1.2 -42.5 -3.5c-9.2 -1.5 -16.2 -8.7 -18.2 -17.8l-12.5 -57.1c-15.8 -6.5 -30.6 -15.1 -44 -25.4L83.1,425.9c-8.8 2.8 -18.6 0.3 -24.5 -6.8c-8.1 -9.8 -15.5 -20.2 -22.1 -31.2l-4.7 -8.1c-6.1 -11 -11.4 -22.4 -15.8 -34.3c-3.2 -8.7 -.5 -18.4 6.4 -24.6l43.3 -39.4C64.6,273.1,64,264.6,64,256s0.6 -17.1 1.7 -25.4L22.4,191.2c-6.9 -6.2 -9.6 -15.9 -6.4 -24.6c4.4 -11.9 9.7 -23.3 15.8 -34.3l4.7 -8.1c6.6 -11 14 -21.4 22.1 -31.2c5.9 -7.2 15.7 -9.6 24.5 -6.8l55.7,17.7c13.4 -10.3 28.2 -18.9 44 -25.4l12.5 -57.1c2 -9.1 9 -16.3 18.2 -17.8C227.3,1.2,241.5,0,256,0s28.7,1.2,42.5,3.5c9.2,1.5,16.2,8.7,18.2,17.8l12.5,57.1c15.8,6.5,30.6,15.1,44,25.4l55.7 -17.7c8.8 -2.8 18.6 -.3 24.5,6.8c8.1,9.8,15.5,20.2,22.1,31.2l4.7,8.1c6.1,11,11.4,22.4,15.8,34.3zM256,336a80,80,0,1,0,0 -160 80,80,0,1,0,0,160z"/>
            </svg>
            Push Notification Configuration
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Detailed guidance on configuring push notifications, including data flow, technical setup, mobile onboarding, and testing procedures.</p>
        <a href="push-config-landing-page.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Configure now</a>
    </div>
</div>