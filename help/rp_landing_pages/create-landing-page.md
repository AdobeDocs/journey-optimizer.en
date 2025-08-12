---
solution: Journey Optimizer
product: Journey Optimizer
title: Create audiences
description: Create audiences
redpen-status: CREATED_||_2025-08-11_20-45-40
---
# Create audiences{#section-overview}

Creating audiences in Adobe Journey Optimizer empowers you to define, manage, and refine the groups of people you want to target with personalized messaging and experiences. Whether you're segmenting based on profile attributes like preferences or tracking real-time events like purchases, this feature lets you build dynamic, data-driven audience definitions tailored to your goals. You'll explore different segmentation methods, from real-time updates to batch processing, and discover flexible evaluation options for keeping your campaigns precise and timely. Plus, you'll learn how to combine audiences, enrich data, and even import custom groups—giving you all the tools you need to connect with the right people, at the right time.

## Create Audiences

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 20px;">
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-list-check -->
                <path d="M152.1,38.2c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,113C-2.3 103.6 -2.3 88.4,7,79s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zm0,160c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,273c-9.4 -9.4 -9.4 -24.6 0 -33.9s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zM224,96c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zm0,160c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zM160,416c0 -17.7 14.3 -32 32 -32l288,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-288 0c-17.7 0 -32 -14.3 -32 -32zM48,368a48,48,0,1,1,0,96,48,48,0,1,1,0 -96z"/>
            </svg>
            Build Segment Definitions in Adobe Journey Optimizer
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn how to define audience segments, including step-by-step instructions for using attributes, events, and various evaluation methods.</p>
        <a href="../using/audience/creating-a-segment-definition.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn how to create segment definitions</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-puzzle-piece -->
                <path d="M192,104.8c0 -9.2 -5.8 -17.3 -13.2 -22.8C167.2,73.3,160,61.3,160,48c0 -26.5 28.7 -48 64 -48s64,21.5,64,48c0,13.3 -7.2 25.3 -18.8 34c-7.4 5.5 -13.2 13.6 -13.2 22.8c0,12.8,10.4,23.2,23.2,23.2l56.8,0c26.5,0,48,21.5,48,48l0,56.8c0,12.8,10.4,23.2,23.2,23.2c9.2,0,17.3 -5.8 22.8 -13.2c8.7 -11.6 20.7 -18.8 34 -18.8c26.5,0,48,28.7,48,64s-21.5 64 -48 64c-13.3 0 -25.3 -7.2 -34 -18.8c-5.5 -7.4 -13.6 -13.2 -22.8 -13.2c-12.8 0 -23.2 10.4 -23.2 23.2L384,464c0,26.5 -21.5 48 -48 48l-56.8 0c-12.8 0 -23.2 -10.4 -23.2 -23.2c0 -9.2 5.8 -17.3 13.2 -22.8c11.6 -8.7 18.8 -20.7 18.8 -34c0 -26.5 -28.7 -48 -64 -48s-64 21.5 -64 48c0,13.3,7.2,25.3,18.8,34c7.4,5.5,13.2,13.6,13.2,22.8c0,12.8 -10.4 23.2 -23.2 23.2L48,512c-26.5 0 -48 -21.5 -48 -48L0,343.2C0,330.4,10.4,320,23.2,320c9.2,0,17.3,5.8,22.8,13.2C54.7,344.8,66.7,352,80,352c26.5,0,48 -28.7 48 -64s-21.5 -64 -48 -64c-13.3 0 -25.3 7.2 -34 18.8C40.5,250.2,32.4,256,23.2,256C10.4,256,0,245.6,0,232.8L0,176c0 -26.5 21.5 -48 48 -48l120.8,0c12.8,0,23.2 -10.4 23.2 -23.2z"/>
            </svg>
            Get Started with Audience Composition
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Discover how to create workflows that combine, enrich, and manage existing audiences for personalized campaigns.</p>
        <a href="../using/audience/get-started-audience-orchestration.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore audience composition workflows</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-file-upload -->
                <path d="M0,64C0,28.7,28.7,0,64,0L224,0l0,128c0,17.7,14.3,32,32,32l128,0,0,144 -208 0c-35.3 0 -64 28.7 -64 64l0,144 -48 0c-35.3 0 -64 -28.7 -64 -64L0,64zm384,64l-128 0L256,0,384,128zM200,352l16,0c22.1,0,40,17.9,40,40l0,8c0,8.8 -7.2 16 -16 16s-16 -7.2 -16 -16l0 -8c0 -4.4 -3.6 -8 -8 -8l-16 0c-4.4 0 -8 3.6 -8 8l0,80c0,4.4,3.6,8,8,8l16,0c4.4,0,8 -3.6 8 -8l0 -8c0 -8.8 7.2 -16 16 -16s16,7.2,16,16l0,8c0,22.1 -17.9 40 -40 40l-16 0c-22.1 0 -40 -17.9 -40 -40l0 -80c0 -22.1 17.9 -40 40 -40zm133.1,0l34.9,0c8.8,0,16,7.2,16,16s-7.2 16 -16 16l-34.9 0c-7.2 0 -13.1 5.9 -13.1 13.1c0,5.2,3,9.9,7.8,12l37.4,16.6c16.3,7.2,26.8,23.4,26.8,41.2c0,24.9 -20.2 45.1 -45.1 45.1L304,512c-8.8 0 -16 -7.2 -16 -16s7.2 -16 16 -16l42.9,0c7.2,0,13.1 -5.9 13.1 -13.1c0 -5.2 -3 -9.9 -7.8 -12l-37.4 -16.6c-16.3 -7.2 -26.8 -23.4 -26.8 -41.2c0 -24.9 20.2 -45.1 45.1 -45.1zm98.9,0c8.8,0,16,7.2,16,16l0,31.6c0,23,5.5,45.6,16,66c10.5 -20.3 16 -42.9 16 -66l0 -31.6c0 -8.8 7.2 -16 16 -16s16,7.2,16,16l0,31.6c0,34.7 -10.3 68.7 -29.6 97.6l-5.1 7.7c-3 4.5 -8 7.1 -13.3 7.1s-10.3 -2.7 -13.3 -7.1l-5.1 -7.7c-19.3 -28.9 -29.6 -62.9 -29.6 -97.6l0 -31.6c0 -8.8 7.2 -16 16 -16z"/>
            </svg>
            How to Import Audiences Using Custom CSV Upload
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Find out how to import audiences through CSV files and map attributes to profiles for seamless integration.</p>
        <a href="../using/audience/custom-upload.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn about custom uploads</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-shield-halved -->
                <path d="M256,0c4.6,0,9.2,1,13.4,2.9L457.7,82.8c22,9.3,38.4,31,38.3,57.2c-.5 99.2 -41.3 280.7 -213.6 363.2c-16.7 8 -36.1 8 -52.8 0C57.3,420.7,16.5,239.2,16,140c-.1 -26.2 16.3 -47.9 38.3 -57.2L242.7,2.9C246.8,1,251.4,0,256,0zm0,66.8l0,378.1C394,378,431.1,230.1,432,141.4L256,66.8s0,0,0,0z"/>
            </svg>
            Federated Audience Composition
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn how to enhance audience segmentation by securely integrating data from trusted partners and data warehouses.</p>
        <a href="../using/audience/federated-audience-composition.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn about federated audience composition</a>
    </div>
</div>