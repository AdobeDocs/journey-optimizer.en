---
solution: Journey Optimizer
product: Journey Optimizer
title: Journey Optimizer datasets
description: Journey Optimizer datasets
redpen-status: CREATED_||_2025-08-11_21-06-02
---
# Journey Optimizer datasets{#section-overview}

Adobe Journey Optimizer datasets are the backbone of how you manage and utilize data to create meaningful customer experiences. They help you store, organize, and analyze data, whether it's tracking user interactions, managing profiles, or exporting insights for further analysis. This section walks you through accessing and previewing datasets, creating new ones, ensuring compliance with data governance policies, and even exporting data to cloud storage. You'll also explore practical SQL query examples for analyzing various types of events. Each topic is designed to empower you to leverage datasets effectively, whether you're building journeys or diving into advanced reporting.

## Journey Optimizer Datasets

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 20px;">
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-circle-play -->
                <path d="M0,256a256,256,0,1,1,512,0A256,256,0,1,1,0,256zM188.3,147.1c-7.6 4.2 -12.3 12.3 -12.3 20.9l0,176c0,8.7,4.7,16.7,12.3,20.9s16.8,4.1,24.3 -.5l144 -88c7.1 -4.4 11.5 -12.1 11.5 -20.5s-4.4 -16.1 -11.5 -20.5l-144 -88c-7.4 -4.5 -16.7 -4.7 -24.3 -.5z"/>
            </svg>
            Using and Managing Datasets in Adobe Journey Optimizer
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn how to access, create, manage, and govern datasets in Adobe Journey Optimizer, ensuring compliance and effective data utilization.</p>
        <a href="../using/data/get-started-datasets.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Get started with datasets</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-shield-halved -->
                <path d="M256,0c4.6,0,9.2,1,13.4,2.9L457.7,82.8c22,9.3,38.4,31,38.3,57.2c-.5 99.2 -41.3 280.7 -213.6 363.2c-16.7 8 -36.1 8 -52.8 0C57.3,420.7,16.5,239.2,16,140c-.1 -26.2 16.3 -47.9 38.3 -57.2L242.7,2.9C246.8,1,251.4,0,256,0zm0,66.8l0,378.1C394,378,431.1,230.1,432,141.4L256,66.8s0,0,0,0z"/>
            </svg>
            Datasets Time-to-live (TTL) Guardrails
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Understand TTL guardrails applied to system-generated datasets, their durations, and impacted functionality.</p>
        <a href="../using/data/datasets-ttl.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore TTL guardrails</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-list-check -->
                <path d="M152.1,38.2c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,113C-2.3 103.6 -2.3 88.4,7,79s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zm0,160c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,273c-9.4 -9.4 -9.4 -24.6 0 -33.9s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zM224,96c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zm0,160c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zM160,416c0 -17.7 14.3 -32 32 -32l288,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-288 0c-17.7 0 -32 -14.3 -32 -32zM48,368a48,48,0,1,1,0,96,48,48,0,1,1,0 -96z"/>
            </svg>
            Export Adobe Journey Optimizer Datasets
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn how to export datasets to cloud storage destinations for reporting, analysis, and archival purposes.</p>
        <a href="../using/data/export-datasets.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Export datasets</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            Adobe Journey Optimizer: Dataset Query Examples
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Access practical SQL query examples to analyze and manage data across Journey Optimizer datasets for various use cases.</p>
        <a href="../using/data/datasets-query-examples.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore query examples</a>
    </div>
</div>