---
solution: Journey Optimizer
product: Journey Optimizer
title: Email deliverability
description: Email deliverability
redpen-status: CREATED_||_2025-08-11_20-34-41
---

# Email deliverability{#section-overview}

Email deliverability is all about ensuring your emails reach your audience’s inbox rather than getting lost in spam folders or blocked entirely—a critical factor for successful campaigns. In Adobe Journey Optimizer, you’ll learn how to improve deliverability by managing suppression lists to exclude problematic addresses, adapting email content to avoid spam filters, and building a strong sender reputation through practices like IP warmup. You’ll also explore advanced tools like DMARC authentication and SMTP relay for added security and compliance. Each topic connects to practical strategies that empower you to safeguard your email performance while enhancing trust with recipients.

## Email Deliverability Resources

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 20px;">
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-book -->
                <path d="M128,0C75,0,32,43,32,96L32,416c0,53,43,96,96,96l288,0,32,0c17.7,0,32 -14.3 32 -32s-14.3 -32 -32 -32l0 -64c17.7,0,32 -14.3 32 -32l0 -320c0 -17.7 -14.3 -32 -32 -32L416,0,128,0zm0,384l256,0,0,64L128,448c-17.7 0 -32 -14.3 -32 -32s14.3 -32 32 -32zm32 -240c0 -8.8 7.2 -16 16 -16l192,0c8.8,0,16,7.2,16,16s-7.2 16 -16 16l-192 0c-8.8 0 -16 -7.2 -16 -16zm16,48l192,0c8.8,0,16,7.2,16,16s-7.2 16 -16 16l-192 0c-8.8 0 -16 -7.2 -16 -16s7.2 -16 16 -16z"/>
            </svg>
            Introduction to Email Deliverability
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn the concepts, best practices, and tools for optimizing email deliverability in Adobe Journey Optimizer.</p>
        <a href="../using/reports/deliverability.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Get started with deliverability</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-list-check -->
                <path d="M152.1,38.2c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,113C-2.3 103.6 -2.3 88.4,7,79s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zm0,160c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,273c-9.4 -9.4 -9.4 -24.6 0 -33.9s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zM224,96c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zm0,160c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zM160,416c0 -17.7 14.3 -32 32 -32l288,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-288 0c-17.7 0 -32 -14.3 -32 -32zM48,368a48,48,0,1,1,0,96,48,48,0,1,1,0 -96z"/>
            </svg>
            Understanding Suppression Lists
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Discover how suppression lists protect sender reputation and improve email deliverability by managing problematic addresses.</p>
        <a href="../using/reports/suppression-list.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Understand the suppression list</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-shield-halved -->
                <path d="M256,0c4.6,0,9.2,1,13.4,2.9L457.7,82.8c22,9.3,38.4,31,38.3,57.2c-.5 99.2 -41.3 280.7 -213.6 363.2c-16.7 8 -36.1 8 -52.8 0C57.3,420.7,16.5,239.2,16,140c-.1 -26.2 16.3 -47.9 38.3 -57.2L242.7,2.9C246.8,1,251.4,0,256,0zm0,66.8l0,378.1C394,378,431.1,230.1,432,141.4L256,66.8s0,0,0,0z"/>
            </svg>
            Comply with New DMARC Requirements
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Ensure compliance with Google's and Yahoo's DMARC mandates to maintain email deliverability and sender reputation.</p>
        <a href="../using/configuration/dmarc-record-update.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn about DMARC requirements</a>
    </div>
</div>