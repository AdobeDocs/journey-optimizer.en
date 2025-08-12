---
solution: Journey Optimizer
product: Journey Optimizer
title: Syntax
description: Syntax
redpen-status: CREATED_||_2025-08-11_20-10-54
---

# Syntax{#section-overview}

Dive into the powerful syntax capabilities of Adobe Journey Optimizer's Advanced Expression Editor, where you can craft precise, dynamic expressions to fine-tune your customer journeys. Whether you're organizing complex data with operators, querying collections, or applying conditional logic, the syntax tools give you the flexibility to adapt to real-world scenarios. Explore key topics like field references for accessing data, data types for ensuring accuracy, and journey properties for real-time customization. Each concept builds on the last, creating a cohesive toolkit for creating smarter, more effective journeys. Ready to unlock what’s possible? Let’s get started!

## Syntax: Build Expressions in Adobe Journey Optimizer

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 20px;">
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            Advanced Expression Editor Syntax
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn the detailed syntax rules for using the Advanced Expression Editor, including parentheses, case sensitivity, and returned expression types.</p>
        <a href="../using/building-journeys/expression/generalities.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore Advanced Syntax</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-list-check -->
                <path d="M152.1,38.2c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,113C-2.3 103.6 -2.3 88.4,7,79s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zm0,160c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,273c-9.4 -9.4 -9.4 -24.6 0 -33.9s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zM224,96c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zm0,160c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zM160,416c0 -17.7 14.3 -32 32 -32l288,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-288 0c-17.7 0 -32 -14.3 -32 -32zM48,368a48,48,0,1,1,0,96,48,48,0,1,1,0 -96z"/>
            </svg>
            Conditional Instruction (if, then, else)
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Master the usage of conditional instructions to create complex expressions and optimize workflows in your journeys.</p>
        <a href="../using/building-journeys/expression/conditional-instruction.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn Conditional Syntax</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-book -->
                <path d="M128,0C75,0,32,43,32,96L32,416c0,53,43,96,96,96l288,0,32,0c17.7,0,32 -14.3 32 -32s-14.3 -32 -32 -32l0 -64c17.7,0,32 -14.3 32 -32l0 -320c0 -17.7 -14.3 -32 -32 -32L416,0,128,0zm0,384l256,0,0,64L128,448c-17.7 0 -32 -14.3 -32 -32s14.3 -32 32 -32zm32 -240c0 -8.8 7.2 -16 16 -16l192,0c8.8,0,16,7.2,16,16s-7.2 16 -16 16l-192 0c-8.8 0 -16 -7.2 -16 -16zm16,48l192,0c8.8,0,16,7.2,16,16s-7.2 16 -16 16l-192 0c-8.8 0 -16 -7.2 -16 -16s7.2 -16 16 -16z"/>
            </svg>
            Understanding Data Types
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Get a comprehensive overview of data types used in expressions, including JSON formats, serialization, and examples.</p>
        <a href="../using/building-journeys/expression/data-types.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">View Data Types Reference</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            Using Field References
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Understand how to reference fields in expressions, including advanced use cases and default value handling.</p>
        <a href="../using/building-journeys/expression/field-references.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn Field Reference Syntax</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-gear -->
                <path d="M495.9,166.6c3.2,8.7,0.5,18.4 -6.4 24.6l-43.3 39.4c1.1,8.3,1.7,16.8,1.7,25.4s-.6 17.1 -1.7 25.4l43.3,39.4c6.9,6.2,9.6,15.9,6.4,24.6c-4.4 11.9 -9.7 23.3 -15.8 34.3l-4.7 8.1c-6.6 11 -14 21.4 -22.1 31.2c-5.9 7.2 -15.7 9.6 -24.5 6.8l-55.7 -17.7c-13.4 10.3 -28.2 18.9 -44 25.4l-12.5 57.1c-2 9.1 -9 16.3 -18.2 17.8c-13.8 2.3 -28 3.5 -42.5 3.5s-28.7 -1.2 -42.5 -3.5c-9.2 -1.5 -16.2 -8.7 -18.2 -17.8l-12.5 -57.1c-15.8 -6.5 -30.6 -15.1 -44 -25.4L83.1,425.9c-8.8 2.8 -18.6 0.3 -24.5 -6.8c-8.1 -9.8 -15.5 -20.2 -22.1 -31.2l-4.7 -8.1c-6.1 -11 -11.4 -22.4 -15.8 -34.3c-3.2 -8.7 -.5 -18.4 6.4 -24.6l43.3 -39.4C64.6,273.1,64,264.6,64,256s0.6 -17.1 1.7 -25.4L22.4,191.2c-6.9 -6.2 -9.6 -15.9 -6.4 -24.6c4.4 -11.9 9.7 -23.3 15.8 -34.3l4.7 -8.1c6.6 -11 14 -21.4 22.1 -31.2c5.9 -7.2 15.7 -9.6 24.5 -6.8l55.7,17.7c13.4 -10.3 28.2 -18.9 44 -25.4l12.5 -57.1c2 -9.1 9 -16.3 18.2 -17.8C227.3,1.2,241.5,0,256,0s28.7,1.2,42.5,3.5c9.2,1.5,16.2,8.7,18.2,17.8l12.5,57.1c15.8,6.5,30.6,15.1,44,25.4l55.7 -17.7c8.8 -2.8 18.6 -.3 24.5,6.8c8.1,9.8,15.5,20.2,22.1,31.2l4.7,8.1c6.1,11,11.4,22.4,15.8,34.3zM256,336a80,80,0,1,0,0 -160 80,80,0,1,0,0,160z"/>
            </svg>
            Collection Management Functions
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Explore functions like 'all', 'first', 'last', and 'at' to manipulate and query collections in your expressions.</p>
        <a href="../using/building-journeys/expression/collection-management-functions.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Discover Collection Functions</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-screwdriver-wrench -->
                <path d="M78.6,5C69.1 -2.4 55.6 -1.5 47,7L7,47c-8.5 8.5 -9.4 22 -2.1 31.6l80,104c4.5,5.9,11.6,9.4,19,9.4l54.1,0,109,109c-14.7 29 -10 65.4,14.3,89.6l112,112c12.5,12.5,32.8,12.5,45.3,0l64 -64c12.5 -12.5 12.5 -32.8 0 -45.3l-112 -112c-24.2 -24.2 -60.6 -29 -89.6 -14.3l-109 -109 0 -54.1c0 -7.5 -3.5 -14.5 -9.4 -19L78.6,5zM19.9,396.1C7.2,408.8,0,426.1,0,444.1C0,481.6,30.4,512,67.9,512c18,0,35.3 -7.2 48 -19.9L233.7,374.3c-7.8 -20.9 -9 -43.6 -3.6 -65.1l-61.7 -61.7L19.9,396.1zM512,144c0 -10.5 -1.1 -20.7 -3.2 -30.5c-2.4 -11.2 -16.1 -14.1 -24.2 -6l-63.9 63.9c-3 3 -7.1 4.7 -11.3 4.7L352,176c-8.8 0 -16 -7.2 -16 -16l0 -57.4c0 -4.2 1.7 -8.3 4.7 -11.3l63.9 -63.9c8.1 -8.1 5.2 -21.8 -6 -24.2C388.7,1.1,378.5,0,368,0C288.5,0,224,64.5,224,144l0,0.8,85.3,85.3c36 -9.1 75.8,0.5,104,28.7L429,274.5c49 -23 83 -72.8 83 -130.5zM56,432a24,24,0,1,1,48,0,24,24,0,1,1 -48 0z"/>
            </svg>
            Operators in Advanced Expressions
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Dive into the usage of operators such as logical, comparison, arithmetic, and string operations in expressions.</p>
        <a href="../using/building-journeys/expression/operators.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore Operators</a>
    </div>
</div>

## Additional Resources

- **[Journey Properties](../using/building-journeys/expression/journey-properties.md)** - Learn about Journey Properties and how to use them to build expressions, send alerts, and refine reporting.
