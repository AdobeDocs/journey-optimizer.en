---
solution: Journey Optimizer
product: Journey Optimizer
title: Date
description: Date
redpen-status: CREATED_||_2025-08-11_20-14-40
---
# Date{#section-overview}

The Date functions in Adobe Journey Optimizer empower you to work seamlessly with time-related data, helping you create dynamic expressions based on the current time, past intervals, or future projections. Whether you need to evaluate if an event occurred within specific hours, days, or years, or adjust time zones and set custom date components, these tools offer precise control over temporal data. Each function, like 'currentTimeInMillis,' 'inLastDays,' or 'updateTimeZone,' serves a unique purpose, enabling you to build personalized journeys and automate decisions with confidence. Explore the subtopics to discover their distinct roles and how they fit together to streamline your workflows.

## Date Functions in Adobe Journey Optimizer

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 20px;">
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            currentTimeInMillis Function Reference
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn how to use the 'currentTimeInMillis' function to retrieve the current time in epoch milliseconds.</p>
        <a href="../using/building-journeys/functions/functioncurrenttimeinmillis.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Read about currentTimeInMillis</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            inLastDays Function
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Understand the 'inLastDays' function, which checks if a given date falls within a specified number of days before today.</p>
        <a href="../using/building-journeys/functions/functioninlastdays.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn about inLastDays</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            Using the inLastHours Function
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Explore the 'inLastHours' function to determine if a date-time falls within the last specified number of hours.</p>
        <a href="../using/building-journeys/functions/functioninlasthours.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Read about inLastHours</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            Using the inLastMonths Function
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Check if a date falls within a specified range of months using 'inLastMonths' in Adobe Journey Optimizer.</p>
        <a href="../using/building-journeys/functions/functioninlastmonths.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn about inLastMonths</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            Using the inLastYears Function
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn how to use the 'inLastYears' function to evaluate if a date is within a specified number of years before now.</p>
        <a href="../using/building-journeys/functions/functioninlastyears.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore inLastYears</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            inNextDays Function
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn how to check if a date falls within a specified range of days from today using the 'inNextDays' function.</p>
        <a href="../using/building-journeys/functions/functioninnextdays.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Discover inNextDays</a>
    </div>
</div>

## Additional Resources

- **[inNextHours Function](../using/building-journeys/functions/functioninnexthours.md)** - Understand how to use the 'inNextHours' function to evaluate if a date-time is within the next specified hours.
- **[inNextMonths Function Reference](../using/building-journeys/functions/functioninnextmonths.md)** - Explore the 'inNextMonths' function to check if a date is within the next specified range of months.
- **[inNextYears Function](../using/building-journeys/functions/functioninnextyears.md)** - Determine if a date falls within a specified range of years in the future using the 'inNextYears' function.
- **[Using the 'now' Function](../using/building-journeys/functions/functionnow.md)** - Learn about the 'now' function to retrieve the current date and time, with optional time zone support.
- **[Using the nowWithDelta Function](../using/building-journeys/functions/functionnowwithdelta.md)** - Explore the 'nowWithDelta' function to calculate the current date-time with an offset.
- **[setHours Function](../using/building-journeys/functions/functionsethours.md)** - Modify the hour component of a date-time value using the 'setHours' function.
- **[setDays Function](../using/building-journeys/functions/functionsetdays.md)** - Learn how to change the day component of a date-time object using the 'setDays' function.
- **[updateTimeZone Function](../using/building-journeys/functions/functionupdatetimezone.md)** - Adjust a date-time value to a new time zone with the 'updateTimeZone' function.
