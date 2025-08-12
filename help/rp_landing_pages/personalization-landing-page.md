---
solution: Journey Optimizer
product: Journey Optimizer
title: Personalization
description: Personalization
redpen-status: CREATED_||_2025-08-12_00-36-08
---
# Personalization{#section-overview}

Personalization in Adobe Journey Optimizer empowers you to craft tailored, impactful customer experiences by dynamically customizing content based on individual profiles, behaviors, and contextual data. Whether you’re creating personalized emails, notifications, or offers, the tools and techniques provided make it easy to connect the right message to the right person at the right time. Learn how the Personalization Editor, Handlebars syntax, and Adobe Experience Platform data work together to bring your ideas to life, explore reusable content blocks with expression fragments, and dive into advanced helper functions to unlock deeper possibilities. Each topic builds your skills step-by-step, ensuring you’re ready to design personalized journeys with confidence.

## Personalization Features and Guides

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 20px;">
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-circle-play -->
                <path d="M0,256a256,256,0,1,1,512,0A256,256,0,1,1,0,256zM188.3,147.1c-7.6 4.2 -12.3 12.3 -12.3 20.9l0,176c0,8.7,4.7,16.7,12.3,20.9s16.8,4.1,24.3 -.5l144 -88c7.1 -4.4 11.5 -12.1 11.5 -20.5s-4.4 -16.1 -11.5 -20.5l-144 -88c-7.4 -4.5 -16.7 -4.7 -24.3 -.5z"/>
            </svg>
            Get Started with Personalization
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn the basics of personalization in Adobe Journey Optimizer, including the personalization editor, data sources, and interactive experimentation tools.</p>
        <a href="../using/personalization/personalize.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Start learning personalization</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-list-check -->
                <path d="M152.1,38.2c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,113C-2.3 103.6 -2.3 88.4,7,79s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zm0,160c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,273c-9.4 -9.4 -9.4 -24.6 0 -33.9s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zM224,96c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zm0,160c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zM160,416c0 -17.7 14.3 -32 32 -32l288,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-288 0c-17.7 0 -32 -14.3 -32 -32zM48,368a48,48,0,1,1,0,96,48,48,0,1,1,0 -96z"/>
            </svg>
            Add and Validate Personalization
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Master the personalization editor to create customized content for emails, push notifications, URLs, and offers, with validation mechanisms for accuracy.</p>
        <a href="../using/personalization/personalization-build-expressions.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn to add personalization</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            Understanding Personalization Syntax
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Dive into the rules and examples of Handlebars-based personalization syntax to create dynamic and customized content.</p>
        <a href="../using/personalization/personalization-syntax.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Understand personalization syntax</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-puzzle-piece -->
                <path d="M192,104.8c0 -9.2 -5.8 -17.3 -13.2 -22.8C167.2,73.3,160,61.3,160,48c0 -26.5 28.7 -48 64 -48s64,21.5,64,48c0,13.3 -7.2 25.3 -18.8 34c-7.4 5.5 -13.2 13.6 -13.2 22.8c0,12.8,10.4,23.2,23.2,23.2l56.8,0c26.5,0,48,21.5,48,48l0,56.8c0,12.8,10.4,23.2,23.2,23.2c9.2,0,17.3 -5.8 22.8 -13.2c8.7 -11.6 20.7 -18.8 34 -18.8c26.5,0,48,28.7,48,64s-21.5 64 -48 64c-13.3 0 -25.3 -7.2 -34 -18.8c-5.5 -7.4 -13.6 -13.2 -22.8 -13.2c-12.8 0 -23.2 10.4 -23.2 23.2L384,464c0,26.5 -21.5 48 -48 48l-56.8 0c-12.8 0 -23.2 -10.4 -23.2 -23.2c0 -9.2 5.8 -17.3 13.2 -22.8c11.6 -8.7 18.8 -20.7 18.8 -34c0 -26.5 -28.7 -48 -64 -48s-64 21.5 -64 48c0,13.3,7.2,25.3,18.8,34c7.4,5.5,13.2,13.6,13.2,22.8c0,12.8 -10.4 23.2 -23.2 23.2L48,512c-26.5 0 -48 -21.5 -48 -48L0,343.2C0,330.4,10.4,320,23.2,320c9.2,0,17.3,5.8,22.8,13.2C54.7,344.8,66.7,352,80,352c26.5,0,48 -28.7 48 -64s-21.5 -64 -48 -64c-13.3 0 -25.3 7.2 -34 18.8C40.5,250.2,32.4,256,23.2,256C10.4,256,0,245.6,0,232.8L0,176c0 -26.5 21.5 -48 48 -48l120.8,0c12.8,0,23.2 -10.4 23.2 -23.2z"/>
            </svg>
            Reuse Expression Fragments
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Leverage reusable expression fragments for efficient and consistent personalization across campaigns and journeys.</p>
        <a href="../using/personalization/use-expression-fragments.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore expression fragments</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-database -->
                <path d="M480,80l0,48c0,44.2 -100.3 80 -224 80S32,172.2,32,128L32,80C32,35.8,132.3,0,256,0S480,35.8,480,80zM425.2,214.7c20.8 -7.4 39.9 -16.9 54.8 -28.6L480,288c0,44.2 -100.3 80 -224 80S32,332.2,32,288L32,186.1c14.9,11.8,34,21.2,54.8,28.6C131.7,230.7,191.5,240,256,240s124.3 -9.3 169.2 -25.3zM32,346.1c14.9,11.8,34,21.2,54.8,28.6C131.7,390.7,191.5,400,256,400s124.3 -9.3 169.2 -25.3c20.8 -7.4 39.9 -16.9 54.8 -28.6l0,85.9c0,44.2 -100.3 80 -224 80S32,476.2,32,432l0 -85.9z"/>
            </svg>
            Use Adobe Experience Platform Data for Personalization (Beta)
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn to use AEP datasets with the 'datasetLookup' helper function to personalize content dynamically.</p>
        <a href="../using/personalization/aep-data-perso.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Use AEP data for personalization</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-screwdriver-wrench -->
                <path d="M78.6,5C69.1 -2.4 55.6 -1.5 47,7L7,47c-8.5 8.5 -9.4 22 -2.1 31.6l80,104c4.5,5.9,11.6,9.4,19,9.4l54.1,0,109,109c-14.7 29 -10 65.4,14.3,89.6l112,112c12.5,12.5,32.8,12.5,45.3,0l64 -64c12.5 -12.5 12.5 -32.8 0 -45.3l-112 -112c-24.2 -24.2 -60.6 -29 -89.6 -14.3l-109 -109 0 -54.1c0 -7.5 -3.5 -14.5 -9.4 -19L78.6,5zM19.9,396.1C7.2,408.8,0,426.1,0,444.1C0,481.6,30.4,512,67.9,512c18,0,35.3 -7.2 48 -19.9L233.7,374.3c-7.8 -20.9 -9 -43.6 -3.6 -65.1l-61.7 -61.7L19.9,396.1zM512,144c0 -10.5 -1.1 -20.7 -3.2 -30.5c-2.4 -11.2 -16.1 -14.1 -24.2 -6l-63.9 63.9c-3 3 -7.1 4.7 -11.3 4.7L352,176c-8.8 0 -16 -7.2 -16 -16l0 -57.4c0 -4.2 1.7 -8.3 4.7 -11.3l63.9 -63.9c8.1 -8.1 5.2 -21.8 -6 -24.2C388.7,1.1,378.5,0,368,0C288.5,0,224,64.5,224,144l0,0.8,85.3,85.3c36 -9.1 75.8,0.5,104,28.7L429,274.5c49 -23 83 -72.8 83 -130.5zM56,432a24,24,0,1,1,48,0,24,24,0,1,1 -48 0z"/>
            </svg>
            Helper Functions Reference Guide
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">A comprehensive guide to personalization helper functions, including aggregation, arithmetic, and string operations.</p>
        <a href="functions-landing-page.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore helper functions</a>
    </div>
</div>

## Additional Resources

- **[Personalization Use Cases](personalization-use-cases-landing-page.md)** - Discover practical examples of personalization techniques, such as order status updates and cart abandonment emails.
