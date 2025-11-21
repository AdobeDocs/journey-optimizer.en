# Screenshots Needed for Weekday Email Use Case

## Instructions

Download the following screenshots from the blog post at:
https://experienceleaguecommunities.adobe.com/t5/journey-optimizer-blogs/how-to-send-emails-only-on-weekdays-in-adobe-journey-optimizer/ba-p/760400

Save them in this folder (`help/using/building-journeys/assets/`) with the exact filenames listed below.

## Required Screenshots

### 1. weekday-email-uc-properties.png
**Description:** Journey properties configuration screen showing the name and description setup
**Should show:** The journey properties panel with fields filled in

### 2. weekday-email-uc-canvas.png
**Description:** Journey canvas with Read Audience activity as the starting point
**Should show:** The initial journey canvas with a Read Audience or Event activity

### 3. weekday-email-uc-add-condition.png
**Description:** Adding a Condition activity to the journey
**Should show:** The journey canvas with a Condition activity being added or already placed

### 4. weekday-email-uc-condition-expression.png
**Description:** Expression editor showing the Saturday condition
**Should show:** The advanced expression editor with the dayOfWeek condition:
```
dayOfWeek(now()) == 7
```
for Saturday, or 
```
dayOfWeek(now()) == 1
```
for Sunday

### 5. weekday-email-uc-paths.png
**Description:** Journey with three condition paths - Saturday, Sunday, and Weekdays
**Should show:** The condition activity split into three paths:
- Path 1: Saturday (dayOfWeek = 7)
- Path 2: Sunday (dayOfWeek = 1)
- Path 3: Otherwise (weekdays)

### 6. weekday-email-uc-complete-journey.png
**Description:** Complete weekday email journey with all activities
**Should show:** The full journey from start to finish including:
- Read Audience/Event
- Condition activity with 3 paths
- Wait activity on Saturday path (with formula for 2-day delay)
- Wait activity on Sunday path (with formula for 1-day delay)
- Direct path for weekdays (no Wait)
- All paths merging to Email action
- End activity

### 7. weekday-email-uc-test-mode.png
**Description:** Testing the journey with test mode enabled
**Should show:** The test mode interface with test profiles or logs

### Additional Screenshots (Optional but Recommended)

#### weekday-email-uc-wait-formula-saturday.png
**Description:** Wait activity configuration for Saturday with custom formula
**Should show:** The Wait activity settings with the custom formula:
```
setHours(nowWithDelta(2, "days"), 9)
```
Showing X=2 for Saturday (2 days forward to Monday) and H=9 for 9 AM delivery

#### weekday-email-uc-wait-formula-sunday.png
**Description:** Wait activity configuration for Sunday with custom formula
**Should show:** The Wait activity settings with the custom formula:
```
setHours(nowWithDelta(1, "days"), 9)
```
Showing X=1 for Sunday (1 day forward to Monday) and H=9 for 9 AM delivery

## Image Requirements

- **Format:** PNG (preferred) or JPG
- **Naming:** Use exact filenames as listed above (lowercase, with hyphens)
- **Size:** Optimize for web (recommended max width: 1200px)
- **Quality:** High enough to see text and UI elements clearly
- **Annotations:** If the blog screenshots have annotations/highlights, keep them

## After Adding Screenshots

1. Verify all 7 screenshots are saved in the assets folder
2. Check that filenames match exactly (case-sensitive)
3. Delete this instruction file (weekday-email-screenshots-instructions.md)
4. Test the markdown file to ensure images display correctly

## Alternative: Use Existing Similar Screenshots

If specific screenshots from the blog are not available or sufficient, you can:

1. Create new screenshots following the journey building steps in the documentation
2. Use similar screenshots from other use cases and relabel them (if permitted)
3. Request the blog author to provide high-resolution images

## Contact

If you have questions about these screenshots, refer to the blog post or contact the documentation team.

