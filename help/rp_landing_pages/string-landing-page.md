---
solution: Journey Optimizer
product: Journey Optimizer
title: String
description: String
redpen-status: CREATED_||_2025-08-11_20-18-34
---

# String{#section-overview}

Strings are the building blocks of text-based data, and Adobe Journey Optimizer's string functions give you powerful tools to manage and transform them effortlessly. Whether you need to combine values, check for patterns, extract parts of a string, or format data for personalized journeys, these functions are here to help. Each function has a specific purpose—from finding patterns with `matchRegExp` to generating unique identifiers with `uuid`. You'll also explore how functions like `concat`, `split`, and `replace` work together to help you manipulate strings dynamically. Dive in to discover practical examples and see how these tools simplify data handling in your campaigns.

## String Functions Overview

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 20px;">
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            concat Function Reference
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn how to combine strings or a list of strings using the 'concat' function.</p>
        <a href="../using/building-journeys/functions/functionconcat.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore concat function</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            Using the 'contain' Function
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Discover how to check for the presence of a string within another string.</p>
        <a href="../using/building-journeys/functions/functioncontain.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn about contain function</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            containIgnoreCase Function
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Understand how to perform case-insensitive string containment checks.</p>
        <a href="../using/building-journeys/functions/functioncontainwithignorecase.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore containIgnoreCase function</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            endWith Function Reference
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Learn to check if a string ends with a specific suffix.</p>
        <a href="../using/building-journeys/functions/functionendwith.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn about endWith function</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            endWithIgnoreCase Function
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Check if a string ends with a suffix, ignoring case sensitivity.</p>
        <a href="../using/building-journeys/functions/functionendwithignorecase.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Explore endWithIgnoreCase function</a>
    </div>
    <!-- Card -->
    <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left; background-color: #f7f7f7;">
        <h4 style="margin: 0; color: #3a4f63; display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" style="fill: currentColor;">
                <!-- fa-code-branch -->
                <path d="M112,104a24,24,0,1,0,0 -48 24,24,0,1,0,0,48zm80 -24c0,32.8 -19.7 61 -48 73.3l0,87.8c18.8 -10.9 40.7 -17.1 64 -17.1l96,0c35.3,0,64 -28.7 64 -64l0 -6.7C339.7,141,320,112.8,320,80c0 -44.2 35.8 -80 80 -80s80,35.8,80,80c0,32.8 -19.7 61 -48 73.3l0,6.7c0,70.7 -57.3 128 -128 128l-96 0c-35.3 0 -64 28.7 -64 64l0,6.7c28.3,12.3,48,40.5,48,73.3c0,44.2 -35.8 80 -80 80s-80 -35.8 -80 -80c0 -32.8 19.7 -61 48 -73.3l0 -6.7 0 -198.7C51.7,141,32,112.8,32,80C32,35.8,67.8,0,112,0s80,35.8,80,80zm232,0a24,24,0,1,0 -48 0,24,24,0,1,0,48,0zM112,456a24,24,0,1,0,0 -48 24,24,0,1,0,0,48z"/>
            </svg>
            equalIgnoreCase Function Reference
        </h4>
        <p style="color: #666666; font-size: 14px; margin-top: 12px;">Compare strings case-insensitively to determine equality.</p>
        <a href="../using/building-journeys/functions/functionequalignorecase.md" style="color: #007BFF; font-weight: bold; text-decoration: none;">Learn about equalIgnoreCase function</a>
    </div>
</div>

## Additional Resources

- **[indexOf Function Overview](../using/building-journeys/functions/functionindexof.md)** - Find the position of a substring within a string.
- **[isEmpty Function Reference](../using/building-journeys/functions/functionisempty.md)** - Determine if a string is empty using the 'isEmpty' function.
- **[isNotEmpty Function Reference](../using/building-journeys/functions/functionisnotempty.md)** - Check if a string is not empty using the 'isNotEmpty' function.
- **[lastIndexOf Function](../using/building-journeys/functions/functionlastindexof.md)** - Locate the position of the last occurrence of a substring.
- **[Length Function Overview](../using/building-journeys/functions/functionlength.md)** - Calculate the number of characters in a string.
- **[Using the 'lower' Function](../using/building-journeys/functions/functionlower.md)** - Convert strings to lowercase using the 'lower' function.
- **[matchRegExp Function Reference](../using/building-journeys/functions/functionmatchregexp.md)** - Check if a string matches a regular expression.
- **[notEqualIgnoreCase Function](../using/building-journeys/functions/functionnotequalignorecase.md)** - Determine if strings are different, ignoring case sensitivity.
- **[replace Function Overview](../using/building-journeys/functions/functionreplace.md)** - Replace the first occurrence of a string or pattern with another string.
- **[replaceAll Function](../using/building-journeys/functions/functionreplaceall.md)** - Replace all occurrences of a string or pattern with another string.
- **[split Function Usage](../using/building-journeys/functions/functionsplit.md)** - Split a string into tokens using the 'split' function.
- **[startWith Function Reference](../using/building-journeys/functions/functionstartwith.md)** - Check if a string starts with a specified prefix.
- **[startWithIgnoreCase Function](../using/building-journeys/functions/functionstartwithignorecase.md)** - Evaluate if a string starts with a prefix, case-insensitively.
- **[substr Function Overview](../using/building-journeys/functions/functionsubstr.md)** - Extract substrings using start and end indices.
- **[Trim Function Reference](../using/building-journeys/functions/functiontrim.md)** - Remove leading and trailing spaces from strings.
- **[Upper Function Overview](../using/building-journeys/functions/functionupper.md)** - Transform strings to uppercase using the 'upper' function.
- **[uuid Function Reference](../using/building-journeys/functions/functionuuid.md)** - Generate random Universal Unique Identifiers (UUIDs).
