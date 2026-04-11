---
title: Personalization recipes
description: Common personalization patterns and real-world examples for Adobe Journey Optimizer
feature: Personalization
topic: Personalization
role: Developer
level: Experienced
---
# Personalization recipes {#personalization-recipes}

This page provides ready-to-use personalization patterns for the most common use cases in Adobe Journey Optimizer. All examples use the personalization editor syntax and can be copied directly into email, SMS, or push content.

For a complete reference of available functions, see [Helper functions](functions/helpers.md), [Date/time functions](functions/dates.md), [String functions](functions/string.md), and [Array functions](functions/arrays-list.md).

## Date & time recipes {#date-time-recipes}

### Recipe 1 — Display the current date in a readable format {#recipe-current-date}

Use `formatDate` with `getCurrentZonedDateTime()` to render today's date in any format:

```sql
{%= formatDate(getCurrentZonedDateTime(), "MMMM dd, yyyy") %}
```

Output (example): `April 11, 2026`

**Common format patterns:**

| Pattern | Output example |
|---------|---------------|
| `"dd/MM/yyyy"` | `11/04/2026` |
| `"MM/dd/yyyy"` | `04/11/2026` |
| `"EEEE, MMMM dd"` | `Saturday, April 11` |
| `"yyyy-MM-dd"` | `2026-04-11` |

>[!NOTE]
>
>Use lowercase `y` (calendar year) rather than `Y` (week-based year) to avoid unexpected results at year boundaries. See [pattern characters](functions/dates.md#pattern-characters) for the full reference.

### Recipe 2 — Countdown to an expiry or event date {#recipe-countdown}

Use `dateDiff` to compute the number of days remaining until a profile date attribute, then render it dynamically:

```handlebars
{% let daysLeft = dateDiff(stringToDate(profile.loyalty.expiryDate), getCurrentZonedDateTime()) %}
{% if daysLeft > 0 %}
Your reward points expire in {{daysLeft}} day{% if daysLeft > 1 %}s{% endif %}. Use them before they're gone!
{% else %}
Your reward points have expired.
{% endif %}
```

Output (example): `Your reward points expire in 7 days. Use them before they're gone!`

### Recipe 3 — X days before a dynamic end date {#recipe-days-before}

To compute a date that is X days before a profile attribute (e.g. to reference in content or subject lines), use `addDays` with a negative offset:

```sql
{%= formatDate(addDays(stringToDate(profile.subscription.endDate), -7), "MMMM dd, yyyy") %}
```

Output (example): `April 04, 2026` *(7 days before April 11)*

To also set a fixed time of day (e.g. 9 AM), combine with `setHours`:

```sql
{%= formatDate(setHours(addDays(stringToDate(profile.subscription.endDate), -7), 9), "dd/MM/yyyy HH:mm") %}
```

### Recipe 4 — Display current time as HH:MM only {#recipe-time-only}

Use `extractHours` and `extractMinutes` to show only the time portion, with a leading-zero guard for minutes:

```handlebars
{% let h = extractHours(getCurrentZonedDateTime()) %}
{% let m = extractMinutes(getCurrentZonedDateTime()) %}
Your appointment is at {{h}}:{% if m < 10 %}0{% endif %}{{m}}.
```

Output (example): `Your appointment is at 14:05.`

### Recipe 5 — Detect weekend vs. weekday {#recipe-weekend}

Use `dayOfWeek` to adapt content based on the day. The function returns 1 (Monday) through 7 (Sunday). Use the single `=` operator (PQL syntax, not `==`):

```handlebars
{% if dayOfWeek(getCurrentZonedDateTime()) = 6 or dayOfWeek(getCurrentZonedDateTime()) = 7 %}
We're closed on weekends — our team will follow up on the next business day.
{% else %}
Our team will get back to you within 24 hours.
{% endif %}
```

>[!NOTE]
>
>`dayOfWeek()` is for adapting **content** based on the day. For routing profiles differently in a journey based on the day of the week, use the built-in **Time condition → Day of the week** option in the journey Condition activity. [Learn more](../building-journeys/condition-activity.md#date_condition)

## Array & loop recipes {#array-recipes}

### Recipe 6 — List all items from a profile array {#recipe-list-items}

Use `{{#each}}` to iterate over a profile array and render each item. This is available in the personalization editor (email, SMS, push) only:

```handlebars
{{#each profile.purchases.recentItems}}
  - {{this.name}}: {{this.price}}&euro;
{{/each}}
```

Output (example):

```
- Running shoes: 89&euro;
- Water bottle: 15&euro;
- Gym bag: 45&euro;
```

>[!NOTE]
>
>`{{#each}}` is not supported in the journey condition activity. For array filtering in conditions, use [collection management functions](../building-journeys/expression/collection-management-functions.md).

### Recipe 7 — Show only the first N items from an array {#recipe-first-n}

Use `topN` to sort and retrieve the top N items, then loop with `{{#each}}`:

```handlebars
{{#each topN(profile.orders, price, 3)}}
  {{this.name}} — {{this.price}}&euro;
{{/each}}
```

Or use `head` to get only the single first item:

```sql
{%= head(profile.purchases.recentItems).name %}
```

### Recipe 8 — Render content conditionally per array item {#recipe-conditional-loop}

Use the PQL `{% if %}` block inside `{{#each}}` to render output only for matching items:

```handlebars
{{#each profile.orders}}
  {% if this.status = "pending" %}
  Order {{this.id}} is pending — we'll notify you when it ships.
  {% endif %}
{{/each}}
```

## String & formatting recipes {#string-recipes}

### Recipe 9 — Clean a string with replaceAll and reuse it {#recipe-replaceall-reuse}

`replaceAll` returns a new value — it does not modify the original. Use `{% let %}` to store the result and reference it multiple times without repeating the function call:

```handlebars
{% let cleanName = replaceAll(profile.person.name.firstName, "[^a-zA-Z]", "") %}
Hi {{cleanName}},
Your exclusive code is: WELCOME-{{upperCase(cleanName)}}
```

Output (example):

```
Hi John,
Your exclusive code is: WELCOME-JOHN
```

### Recipe 10 — Double-quote a value in JSON output {#recipe-json-quotes}

To include a literal double quote inside a string (e.g. generating JSON for a custom payload), escape it with a backslash (`\"`):

```handlebars
{ "greeting": "Hello \"{{profile.person.name.firstName}}\"" }
```

Output: `{ "greeting": "Hello \"John\"" }`

### Recipe 11 — Format a date component in uppercase {#recipe-uppercase-date}

Combine `formatDate` with `upperCase` to render month or day names in uppercase:

```sql
{%= upperCase(formatDate(getCurrentZonedDateTime(), "MMMM")) %}
```

Output (example): `APRIL`

For a full uppercase date string:

```sql
{%= upperCase(formatDate(profile.person.birthDateTime, "EEEE MMMM dd yyyy")) %}
```

Output (example): `WEDNESDAY JANUARY 01 2020`

## Conditional logic recipes {#conditional-recipes}

### Recipe 12 — IF/ELSEIF/ELSE in personalized content {#recipe-if-elseif}

Use `{% if %}`, `{% elseif %}`, and `{% else %}` for multi-branch conditional logic. This pattern works in email content and fragments:

```handlebars
{% if profile.loyalty.tier = "gold" %}
As a Gold member, enjoy free shipping on all orders.
{% elseif profile.loyalty.tier = "silver" %}
As a Silver member, enjoy free shipping on orders over &euro;50.
{% else %}
Join our loyalty program to unlock exclusive benefits.
{% endif %}
```

### Recipe 13 — Null-safe attribute display {#recipe-null-safe}

Use a conditional fallback to avoid rendering empty values when a profile attribute may be null or missing:

```handlebars
{% if profile.person.name.firstName %}
Hi {{profile.person.name.firstName}},
{% else %}
Hi there,
{% endif %}
```

Or inline with a ternary-style pattern using `isEmpty`:

```handlebars
Hi {% if isEmpty(profile.person.name.firstName) %}valued customer{% else %}{{profile.person.name.firstName}}{% endif %},
```

## PQL edge case recipes {#pql-edge-cases}

### Recipe 14 — Reference a hyphenated attribute key {#recipe-hyphenated-key}

If your XDM schema field name contains hyphens (e.g. `order-total`, `event-type`), wrap it in backticks to prevent the hyphen from being interpreted as a subtraction operator:

```handlebars
{{profile.commerce.`order-total`}}
```

```sql
{%= profile.events.`order-total` > 100 %}
```

Without backticks, the expression raises a PQL syntax error.

### Recipe 15 — Reference a numeric event ID in a context attribute {#recipe-numeric-event-id}

When using a journey context event whose ID is a numeric string (e.g. `1697323153`), wrap the ID in backticks and use `{% let %}` with `toDateTime()` and `formatDate()`:

```handlebars
{% let appointmentDate = formatDate(toDateTime(context.journey.events.`1697323153`.timestamp), "dd/MM/yyyy HH:mm") %}
Your appointment: {{appointmentDate}}
```

Output (example): `Your appointment: 18/03/2026 14:30`

>[!CAUTION]
>
>Using `{%= formatDate(toDateTime(context.journey.events.`1697323153`.timestamp), "dd/MM/yyyy") %}` inline (without `{% let %}`) causes a **"mismatched input '(' expecting \<EOF\>"** PQL error. Always use the `{% let %}` assignment pattern for this case.

### Recipe 16 — Type coercion: compare a string field to a number {#recipe-type-coercion}

PQL is strongly typed. When a profile field is stored as a string but you need to compare it numerically, convert it first with `stringToNumber()`:

```sql
{%= stringToNumber(profile.loyalty.pointsBalance) > 500 %}
```

For boolean fields stored as strings:

```sql
{%= toBool(profile.consents.email.val) = true %}
```
