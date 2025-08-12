---
solution: Journey Optimizer
product: Journey Optimizer
title: Event configuration
description: Event configuration
redpen-status: CREATED_||_2025-08-11_21-10-50
---
# Event configuration{#section-overview}

Event configuration in Adobe Journey Optimizer is all about setting up the triggers that launch your personalized customer journeys. Whether you’re reacting to individual user actions (unitary events) or broadcasting updates to broader audiences (business events), these configurations turn data into actionable moments. You’ll explore how different event types—like profile-specific triggers, audience-based events, and Adobe Analytics integrations—fit into the larger journey framework. With topics ranging from data schemas and payload definitions to API-based real-time streaming, this section equips you to build journeys that are dynamic, precise, and impactful.

## Event Configuration

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 20px;">
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-book -->
                <path d="M128,0C75,0,32,43,32,96L32,416c0,53,43,96,96,96l288,0,32,0c17.7,0,32 -14.3 32 -32s-14.3 -32 -32 -32l0 -64c17.7,0,32 -14.3 32 -32l0 -320c0 -17.7 -14.3 -32 -32 -32L416,0,128,0zm0,384l256,0,0,64L128,448c-17.7 0 -32 -14.3 -32 -32s14.3 -32 32 -32zm32 -240c0 -8.8 7.2 -16 16 -16l192,0c8.8,0,16,7.2,16,16s-7.2 16 -16 16l-192 0c-8.8 0 -16 -7.2 -16 -16zm16,48l192,0c8.8,0,16,7.2,16,16s-7.2 16 -16 16l-192 0c-8.8 0 -16 -7.2 -16 -16s7.2 -16 16 -16z"/>
            </svg>
            Work with Journey Events
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn about journey events, their types, lifecycle, and configuration to trigger personalized journeys effectively.</p>
        <a href="../using/event/about-events.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn more</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-circle-play -->
                <path d="M0,256a256,256,0,1,1,512,0A256,256,0,1,1,0,256zM188.3,147.1c-7.6 4.2 -12.3 12.3 -12.3 20.9l0,176c0,8.7,4.7,16.7,12.3,20.9s16.8,4.1,24.3 -.5l144 -88c7.1 -4.4 11.5 -12.1 11.5 -20.5s-4.4 -16.1 -11.5 -20.5l-144 -88c-7.4 -4.5 -16.7 -4.7 -24.3 -.5z"/>
            </svg>
            Configure a Unitary Event
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Follow a step-by-step guide to configure unitary events, including defining payloads and identity types.</p>
        <a href="../using/event/about-creating.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Get started</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            ExperienceEvent Schemas
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Understand schema requirements and configurations for event ingestion and advanced functionalities.</p>
        <a href="../using/event/experience-event-schema.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Read the guidelines</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-chart-line -->
                <path d="M64,64c0 -17.7 -14.3 -32 -32 -32S0,46.3,0,64L0,400c0,44.2,35.8,80,80,80l400,0c17.7,0,32 -14.3 32 -32s-14.3 -32 -32 -32L80,416c-8.8 0 -16 -7.2 -16 -16L64,64zm406.6,86.6c12.5 -12.5 12.5 -32.8 0 -45.3s-32.8 -12.5 -45.3 0L320,210.7l-57.4 -57.4c-12.5 -12.5 -32.8 -12.5 -45.3 0l-112 112c-12.5 12.5 -12.5 32.8,0,45.3s32.8,12.5,45.3,0L240,221.3l57.4,57.4c12.5,12.5,32.8,12.5,45.3,0l128 -128z"/>
            </svg>
            Adobe Analytics Integration
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn how to integrate Adobe Analytics data to automate journeys and create personalized experiences.</p>
        <a href="../using/event/about-analytics.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">View tutorial</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-list-check -->
                <path d="M152.1,38.2c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,113C-2.3 103.6 -2.3 88.4,7,79s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zm0,160c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,273c-9.4 -9.4 -9.4 -24.6 0 -33.9s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zM224,96c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zm0,160c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zM160,416c0 -17.7 14.3 -32 32 -32l288,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-288 0c-17.7 0 -32 -14.3 -32 -32zM48,368a48,48,0,1,1,0,96,48,48,0,1,1,0 -96z"/>
            </svg>
            Configure a Business Event
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Step-by-step instructions for configuring business events, including schema definition and payload setup.</p>
        <a href="../using/event/about-creating-business.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Start configuring</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-gear -->
                <path d="M495.9,166.6c3.2,8.7,0.5,18.4 -6.4 24.6l-43.3 39.4c1.1,8.3,1.7,16.8,1.7,25.4s-.6 17.1 -1.7 25.4l43.3,39.4c6.9,6.2,9.6,15.9,6.4,24.6c-4.4 11.9 -9.7 23.3 -15.8 34.3l-4.7 8.1c-6.6 11 -14 21.4 -22.1 31.2c-5.9 7.2 -15.7 9.6 -24.5 6.8l-55.7 -17.7c-13.4 10.3 -28.2 18.9 -44 25.4l-12.5 57.1c-2 9.1 -9 16.3 -18.2 17.8c-13.8 2.3 -28 3.5 -42.5 3.5s-28.7 -1.2 -42.5 -3.5c-9.2 -1.5 -16.2 -8.7 -18.2 -17.8l-12.5 -57.1c-15.8 -6.5 -30.6 -15.1 -44 -25.4L83.1,425.9c-8.8 2.8 -18.6 0.3 -24.5 -6.8c-8.1 -9.8 -15.5 -20.2 -22.1 -31.2l-4.7 -8.1c-6.1 -11 -11.4 -22.4 -15.8 -34.3c-3.2 -8.7 -.5 -18.4 6.4 -24.6l43.3 -39.4C64.6,273.1,64,264.6,64,256s0.6 -17.1 1.7 -25.4L22.4,191.2c-6.9 -6.2 -9.6 -15.9 -6.4 -24.6c4.4 -11.9 9.7 -23.3 15.8 -34.3l4.7 -8.1c6.6 -11 14 -21.4 22.1 -31.2c5.9 -7.2 15.7 -9.6 24.5 -6.8l55.7,17.7c13.4 -10.3 28.2 -18.9 44 -25.4l12.5 -57.1c2 -9.1 9 -16.3 18.2 -17.8C227.3,1.2,241.5,0,256,0s28.7,1.2,42.5,3.5c9.2,1.5,16.2,8.7,18.2,17.8l12.5,57.1c15.8,6.5,30.6,15.1,44,25.4l55.7 -17.7c8.8 -2.8 18.6 -.3 24.5,6.8c8.1,9.8,15.5,20.2,22.1,31.2l4.7,8.1c6.1,11,11.4,22.4,15.8,34.3zM256,336a80,80,0,1,0,0 -160 80,80,0,1,0,0,160z"/>
            </svg>
            Send Events Using Streaming APIs
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Explore additional steps to send events using Streaming Ingestion APIs, including payload preparation and API calls.</p>
        <a href="../using/event/additional-steps-to-send-events-to-journey.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Follow the guide</a>
    </div>
</div>