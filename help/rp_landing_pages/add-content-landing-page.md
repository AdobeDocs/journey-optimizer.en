---
solution: Journey Optimizer
product: Journey Optimizer
title: Design your content
description: Design your content
redpen-status: CREATED_||_2025-08-11_20-32-28
---
# Design your content{#section-overview}

Designing your content in Adobe Journey Optimizer is all about creating personalized, impactful email experiences that connect with your audience. Whether you're adding dynamic layouts, reusable visual fragments, or customized links, each tool works together to give you full control over your email design. You’ll also discover how to integrate metadata for accessibility, personalize offers for greater relevance, and even apply advanced styles using custom CSS. With step-by-step guidance, these features empower you to build emails that are not only visually stunning but also tailored to your goals and your audience’s needs.

## Design Your Content

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 20px;">
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-puzzle-piece -->
                <path d="M192,104.8c0 -9.2 -5.8 -17.3 -13.2 -22.8C167.2,73.3,160,61.3,160,48c0 -26.5 28.7 -48 64 -48s64,21.5,64,48c0,13.3 -7.2 25.3 -18.8 34c-7.4 5.5 -13.2 13.6 -13.2 22.8c0,12.8,10.4,23.2,23.2,23.2l56.8,0c26.5,0,48,21.5,48,48l0,56.8c0,12.8,10.4,23.2,23.2,23.2c9.2,0,17.3 -5.8 22.8 -13.2c8.7 -11.6 20.7 -18.8 34 -18.8c26.5,0,48,28.7,48,64s-21.5 64 -48 64c-13.3 0 -25.3 -7.2 -34 -18.8c-5.5 -7.4 -13.6 -13.2 -22.8 -13.2c-12.8 0 -23.2 10.4 -23.2 23.2L384,464c0,26.5 -21.5 48 -48 48l-56.8 0c-12.8 0 -23.2 -10.4 -23.2 -23.2c0 -9.2 5.8 -17.3 13.2 -22.8c11.6 -8.7 18.8 -20.7 18.8 -34c0 -26.5 -28.7 -48 -64 -48s-64 21.5 -64 48c0,13.3,7.2,25.3,18.8,34c7.4,5.5,13.2,13.6,13.2,22.8c0,12.8 -10.4 23.2 -23.2 23.2L48,512c-26.5 0 -48 -21.5 -48 -48L0,343.2C0,330.4,10.4,320,23.2,320c9.2,0,17.3,5.8,22.8,13.2C54.7,344.8,66.7,352,80,352c26.5,0,48 -28.7 48 -64s-21.5 -64 -48 -64c-13.3 0 -25.3 7.2 -34 18.8C40.5,250.2,32.4,256,23.2,256C10.4,256,0,245.6,0,232.8L0,176c0 -26.5 21.5 -48 48 -48l120.8,0c12.8,0,23.2 -10.4 23.2 -23.2z"/>
            </svg>
            Use Content Components
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn how to add and customize components like text, buttons, images, and more to create dynamic email layouts.</p>
        <a href="../using/email/content-components.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Start using content components</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-layer-group -->
                <path d="M0,64C0,28.7,28.7,0,64,0L224,0l0,128c0,17.7,14.3,32,32,32l128,0,0,144 -208 0c-35.3 0 -64 28.7 -64 64l0,144 -48 0c-35.3 0 -64 -28.7 -64 -64L0,64zm384,64l-128 0L256,0,384,128zM200,352l16,0c22.1,0,40,17.9,40,40l0,8c0,8.8 -7.2 16 -16 16s-16 -7.2 -16 -16l0 -8c0 -4.4 -3.6 -8 -8 -8l-16 0c-4.4 0 -8 3.6 -8 8l0,80c0,4.4,3.6,8,8,8l16,0c4.4,0,8 -3.6 8 -8l0 -8c0 -8.8 7.2 -16 16 -16s16,7.2,16,16l0,8c0,22.1 -17.9 40 -40 40l-16 0c-22.1 0 -40 -17.9 -40 -40l0 -80c0 -22.1 17.9 -40 40 -40zm133.1,0l34.9,0c8.8,0,16,7.2,16,16s-7.2 16 -16 16l-34.9 0c-7.2 0 -13.1 5.9 -13.1 13.1c0,5.2,3,9.9,7.8,12l37.4,16.6c16.3,7.2,26.8,23.4,26.8,41.2c0,24.9 -20.2 45.1 -45.1 45.1L304,512c-8.8 0 -16 -7.2 -16 -16s7.2 -16 16 -16l42.9,0c7.2,0,13.1 -5.9 13.1 -13.1c0 -5.2 -3 -9.9 -7.8 -12l-37.4 -16.6c-16.3 -7.2 -26.8 -23.4 -26.8 -41.2c0 -24.9 20.2 -45.1 45.1 -45.1zm98.9,0c8.8,0,16,7.2,16,16l0,31.6c0,23,5.5,45.6,16,66c10.5 -20.3 16 -42.9 16 -66l0 -31.6c0 -8.8 7.2 -16 16 -16s16,7.2,16,16l0,31.6c0,34.7 -10.3 68.7 -29.6 97.6l-5.1 7.7c-3 4.5 -8 7.1 -13.3 7.1s-10.3 -2.7 -13.3 -7.1l-5.1 -7.7c-19.3 -28.9 -29.6 -62.9 -29.6 -97.6l0 -31.6c0 -8.8 7.2 -16 16 -16z"/>
            </svg>
            Leverage Visual Fragments
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Discover how to create reusable fragments to streamline your email design and improve content consistency.</p>
        <a href="../using/email/use-visual-fragments.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn about visual fragments</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-chart-line -->
                <path d="M64,64c0 -17.7 -14.3 -32 -32 -32S0,46.3,0,64L0,400c0,44.2,35.8,80,80,80l400,0c17.7,0,32 -14.3 32 -32s-14.3 -32 -32 -32L80,416c-8.8 0 -16 -7.2 -16 -16L64,64zm406.6,86.6c12.5 -12.5 12.5 -32.8 0 -45.3s-32.8 -12.5 -45.3 0L320,210.7l-57.4 -57.4c-12.5 -12.5 -32.8 -12.5 -45.3 0l-112 112c-12.5 12.5 -12.5 32.8,0,45.3s32.8,12.5,45.3,0L240,221.3l57.4,57.4c12.5,12.5,32.8,12.5,45.3,0l128 -128z"/>
            </svg>
            Add Links & Track Messages
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Enable tracking, insert links, and manage link appearances to optimize your email campaigns.</p>
        <a href="../using/email/message-tracking.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore tracking and links</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-bullseye -->
                <path d="M448,256A192,192,0,1,0,64,256a192,192,0,1,0,384,0zM0,256a256,256,0,1,1,512,0A256,256,0,1,1,0,256zm256,80a80,80,0,1,0,0 -160 80,80,0,1,0,0,160zm0 -224a144,144,0,1,1,0,288,144,144,0,1,1,0 -288zM224,256a32,32,0,1,1,64,0,32,32,0,1,1 -64 0z"/>
            </svg>
            Insert Personalized Offers
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Use decision management to dynamically display personalized offers tailored to your audience.</p>
        <a href="../using/email/add-offers-email.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Add personalized offers</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-file-alt -->
                <path d="M0,64C0,28.7,28.7,0,64,0L224,0l0,128c0,17.7,14.3,32,32,32l128,0,0,144 -208 0c-35.3 0 -64 28.7 -64 64l0,144 -48 0c-35.3 0 -64 -28.7 -64 -64L0,64zm384,64l-128 0L256,0,384,128zM200,352l16,0c22.1,0,40,17.9,40,40l0,8c0,8.8 -7.2 16 -16 16s-16 -7.2 -16 -16l0 -8c0 -4.4 -3.6 -8 -8 -8l-16 0c-4.4 0 -8 3.6 -8 8l0,80c0,4.4,3.6,8,8,8l16,0c4.4,0,8 -3.6 8 -8l0 -8c0 -8.8 7.2 -16 16 -16s16,7.2,16,16l0,8c0,22.1 -17.9 40 -40 40l-16 0c-22.1 0 -40 -17.9 -40 -40l0 -80c0 -22.1 17.9 -40 40 -40zm133.1,0l34.9,0c8.8,0,16,7.2,16,16s-7.2 16 -16 16l-34.9 0c-7.2 0 -13.1 5.9 -13.1 13.1c0,5.2,3,9.9,7.8,12l37.4,16.6c16.3,7.2,26.8,23.4,26.8,41.2c0,24.9 -20.2 45.1 -45.1 45.1L304,512c-8.8 0 -16 -7.2 -16 -16s7.2 -16 16 -16l42.9,0c7.2,0,13.1 -5.9 13.1 -13.1c0 -5.2 -3 -9.9 -7.8 -12l-37.4 -16.6c-16.3 -7.2 -26.8 -23.4 -26.8 -41.2c0 -24.9 20.2 -45.1 45.1 -45.1zm98.9,0c8.8,0,16,7.2,16,16l0,31.6c0,23,5.5,45.6,16,66c10.5 -20.3 16 -42.9 16 -66l0 -31.6c0 -8.8 7.2 -16 16 -16s16,7.2,16,16l0,31.6c0,34.7 -10.3 68.7 -29.6 97.6l-5.1 7.7c-3 4.5 -8 7.1 -13.3 7.1s-10.3 -2.7 -13.3 -7.1l-5.1 -7.7c-19.3 -28.9 -29.6 -62.9 -29.6 -97.6l0 -31.6c0 -8.8 7.2 -16 16 -16z"/>
            </svg>
            Generate Text Version
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Create and customize the plain text version of your email for recipients who cannot view HTML content.</p>
        <a href="../using/email/text-version-email.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Create a text version</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-gear -->
                <path d="M495.9,166.6c3.2,8.7,0.5,18.4 -6.4 24.6l-43.3 39.4c1.1,8.3,1.7,16.8,1.7,25.4s-.6 17.1 -1.7 25.4l43.3,39.4c6.9,6.2,9.6,15.9,6.4,24.6c-4.4 11.9 -9.7 23.3 -15.8 34.3l-4.7 8.1c-6.6 11 -14 21.4 -22.1 31.2c-5.9 7.2 -15.7 9.6 -24.5 6.8l-55.7 -17.7c-13.4 10.3 -28.2 18.9 -44 25.4l-12.5 57.1c-2 9.1 -9 16.3 -18.2 17.8c-13.8 2.3 -28 3.5 -42.5 3.5s-28.7 -1.2 -42.5 -3.5c-9.2 -1.5 -16.2 -8.7 -18.2 -17.8l-12.5 -57.1c-15.8 -6.5 -30.6 -15.1 -44 -25.4L83.1,425.9c-8.8 2.8 -18.6 0.3 -24.5 -6.8c-8.1 -9.8 -15.5 -20.2 -22.1 -31.2l-4.7 -8.1c-6.1 -11 -11.4 -22.4 -15.8 -34.3c-3.2 -8.7 -.5 -18.4 6.4 -24.6l43.3 -39.4C64.6,273.1,64,264.6,64,256s0.6 -17.1 1.7 -25.4L22.4,191.2c-6.9 -6.2 -9.6 -15.9 -6.4 -24.6c4.4 -11.9 9.7 -23.3 15.8 -34.3l4.7 -8.1c6.6 -11 14 -21.4 22.1 -31.2c5.9 -7.2 15.7 -9.6 24.5 -6.8l55.7,17.7c13.4 -10.3 28.2 -18.9 44 -25.4l12.5 -57.1c2 -9.1 9 -16.3 18.2 -17.8C227.3,1.2,241.5,0,256,0s28.7,1.2,42.5,3.5c9.2,1.5,16.2,8.7,18.2,17.8l12.5,57.1c15.8,6.5,30.6,15.1,44,25.4l55.7 -17.7c8.8 -2.8 18.6 -.3 24.5,6.8c8.1,9.8,15.5,20.2,22.1,31.2l4.7,8.1c6.1,11,11.4,22.4,15.8,34.3zM256,336a80,80,0,1,0,0 -160 80,80,0,1,0,0,160z"/>
            </svg>
            Add Metadata
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Enhance email readability and accessibility by configuring metadata like preheaders and document language.</p>
        <a href="../using/email/email-metadata.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Configure email metadata</a>
    </div>
</div>

## Additional Resources

- **[Add Custom CSS](../using/email/custom-css.md)** - Gain advanced styling control by applying custom CSS to your email content.
