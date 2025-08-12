---
solution: Journey Optimizer
product: Journey Optimizer
title: Helper functions list
description: Helper functions list
redpen-status: CREATED_||_2025-08-12_00-34-42
---
# Helper functions list{#section-overview}

Helper functions in Adobe Journey Optimizer empower you to personalize experiences with precision and efficiency by manipulating data, performing calculations, and formatting content—all within the personalization editor. Whether you need to summarize data, create dynamic content, or fine-tune logic, these functions are your toolkit. From Aggregation and Math to String and Date-Time functions, each category offers specialized tools for unique tasks like filtering arrays, formatting dates, or applying conditional logic. Explore how these functions, operators, and helpers work together to help you craft tailored, data-driven customer journeys effortlessly.

## Helper Functions List

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 20px;">
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-circle-play -->
                <path d="M0,256a256,256,0,1,1,512,0A256,256,0,1,1,0,256zM188.3,147.1c-7.6 4.2 -12.3 12.3 -12.3 20.9l0,176c0,8.7,4.7,16.7,12.3,20.9s16.8,4.1,24.3 -.5l144 -88c7.1 -4.4 11.5 -12.1 11.5 -20.5s-4.4 -16.1 -11.5 -20.5l-144 -88c-7.4 -4.5 -16.7 -4.7 -24.3 -.5z"/>
            </svg>
            Get Started with Helper Functions
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn how to use helper functions for data manipulation and personalization in Adobe Journey Optimizer.</p>
        <a href="../using/personalization/functions/functions.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore Helper Functions</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-list-check -->
                <path d="M152.1,38.2c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,113C-2.3 103.6 -2.3 88.4,7,79s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zm0,160c9.9,8.9,10.7,24,1.8,33.9l-72 80c-4.4 4.9 -10.6 7.8 -17.2 7.9s-12.9 -2.4 -17.6 -7L7,273c-9.4 -9.4 -9.4 -24.6 0 -33.9s24.6 -9.4 33.9,0l22.1,22.1,55.1 -61.2c8.9 -9.9 24 -10.7 33.9 -1.8zM224,96c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zm0,160c0 -17.7 14.3 -32 32 -32l224,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-224 0c-17.7 0 -32 -14.3 -32 -32zM160,416c0 -17.7 14.3 -32 32 -32l288,0c17.7,0,32,14.3,32,32s-14.3 32 -32 32l-288 0c-17.7 0 -32 -14.3 -32 -32zM48,368a48,48,0,1,1,0,96,48,48,0,1,1,0 -96z"/>
            </svg>
            Aggregation Functions Library
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Discover functions to summarize multiple values into a single value for personalization.</p>
        <a href="../using/personalization/functions/aggregation.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn About Aggregation Functions</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            Arithmetic Functions Library
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Explore how arithmetic functions perform calculations like addition, subtraction, and more.</p>
        <a href="../using/personalization/functions/arithmetic-functions.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Dive into Arithmetic Functions</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            Array and List Functions Reference
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn to manipulate arrays and lists with functions like counting, retrieving distinct values, and more.</p>
        <a href="../using/personalization/functions/arrays-list.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore Array & List Functions</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-calendar-alt -->
                <path d="M0,64C0,28.7,28.7,0,64,0L224,0l0,128c0,17.7,14.3,32,32,32l128,0,0,144 -208 0c-35.3 0 -64 28.7 -64 64l0,144 -48 0c-35.3 0 -64 -28.7 -64 -64L0,64zm384,64l-128 0L256,0,384,128zM200,352l16,0c22.1,0,40,17.9,40,40l0,8c0,8.8 -7.2 16 -16 16s-16 -7.2 -16 -16l0 -8c0 -4.4 -3.6 -8 -8 -8l-16 0c-4.4 0 -8 3.6 -8 8l0,80c0,4.4,3.6,8,8,8l16,0c4.4,0,8 -3.6 8 -8l0 -8c0 -8.8 7.2 -16 16 -16s16,7.2,16,16l0,8c0,22.1 -17.9 40 -40 40l-16 0c-22.1 0 -40 -17.9 -40 -40l0 -80c0 -22.1 17.9 -40 40 -40zm133.1,0l34.9,0c8.8,0,16,7.2,16,16s-7.2 16 -16 16l-34.9 0c-7.2 0 -13.1 5.9 -13.1 13.1c0,5.2,3,9.9,7.8,12l37.4,16.6c16.3,7.2,26.8,23.4,26.8,41.2c0,24.9 -20.2 45.1 -45.1 45.1L304,512c-8.8 0 -16 -7.2 -16 -16s7.2 -16 16 -16l42.9,0c7.2,0,13.1 -5.9 13.1 -13.1c0 -5.2 -3 -9.9 -7.8 -12l-37.4 -16.6c-16.3 -7.2 -26.8 -23.4 -26.8 -41.2c0 -24.9 20.2 -45.1 45.1 -45.1zm98.9,0c8.8,0,16,7.2,16,16l0,31.6c0,23,5.5,45.6,16,66c10.5 -20.3 16 -42.9 16 -66l0 -31.6c0 -8.8 7.2 -16 16 -16s16,7.2,16,16l0,31.6c0,34.7 -10.3 68.7 -29.6 97.6l-5.1 7.7c-3 4.5 -8 7.1 -13.3 7.1s-10.3 -2.7 -13.3 -7.1l-5.1 -7.7c-19.3 -28.9 -29.6 -62.9 -29.6 -97.6l0 -31.6c0 -8.8 7.2 -16 16 -16z"/>
            </svg>
            Date and Time Functions Library
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Use date and time functions to manipulate and format dates for personalization workflows.</p>
        <a href="../using/personalization/functions/dates.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn About Date Functions</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            Boolean & Comparison Functions Library
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Implement Boolean logic and comparison operations for dynamic personalization workflows.</p>
        <a href="../using/personalization/functions/operators.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore Boolean & Comparison Functions</a>
    </div>
</div>

## Additional Resources

- **[Helper Functions for Personalization](../using/personalization/functions/helpers.md)** - Learn about conditional evaluations, iteration, and variable assignments for dynamic personalization.
- **[Map Functions Library](../using/personalization/functions/maps.md)** - Utilize map functions to interact with key-value pairs for personalization workflows.
- **[Comprehensive Math Functions Reference](../using/personalization/functions/math.md)** - Perform numerical operations and formatting using advanced math functions.
- **[Object Functions Library for Personalization](../using/personalization/functions/objects.md)** - Check object references with functions like `isNull` and `isNotNull` for personalization workflows.
- **[String Functions Library](../using/personalization/functions/string.md)** - Manipulate and analyze strings with functions like `concat`, `substring`, and more.
