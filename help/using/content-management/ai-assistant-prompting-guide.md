---
solution: Journey Optimizer
product: journey optimizer
title: AI Assistant content prompting guide
description: Learn how to craft effective prompts for AI-powered content generation using the CO-STAR framework to create high-converting, brand-aligned marketing content.
topic: Artificial Intelligence
role: User
level: Intermediate
---
# AI Assistant prompt best practices {#ai-assistant-prompting-guide}

>[!CONTEXTUALHELP]
>id="ajo_ai_assistant_prompt"
>title="Prompt examples"
>abstract="Explore Journey Optimizer documentation to learn how to create effective prompts that produce high-converting, on-brand marketing content."

This guide helps you structure your requests, communicate intent with clarity, and ensure the AI produces messaging that aligns with your brand guidelines, audience needs, and campaign goals.
Learn how to write effective prompts that enable AI Assistant to generate high-quality, on-brand marketing content tailored to your objectives. 

## Use the CO-STAR framework {#costar-framework}

For best results with AI Assistant, organize your prompts using the CO-STAR framework. This structured approach ensures AI understands exactly what you need.

| Component | What it means | Why it matters |
|-|-|-|
| **C - Context** | Background about your campaign, product, or situation | Helps AI understand the bigger picture |
| **O - Objective** | Your specific marketing goal | Drives what the content should achieve |
| **S - Style** | How you want to communicate | Sets the approach |
| **T - Tone** | Emotional style and voice | Shapes how your message feels |
| **A - Audience** | Audience you are targeting | Ensures the message resonates with the right people |
| **R - Requirements** | Specific constraints or must-haves | Defines boundaries and critical elements |

## AI prompts essentials {#key-takeaways}


### Do's and don'ts


<table style="table-layout: fixed; width: 100%; border: 0;">
<thead style="border: 0; background-color: #FFFFFF;">
<tr>
<th>Do</th>
<th>Don't</th>
</tr>
</thead>
<tbody>
<tr style="border: 0;">
<td>
<p>Use the CO-STAR framework for structure</p>
<p>Be explicit about fresh vs. existing content</p>
<p>Focus document usage with specific extraction guidance</p>
<p>Use dropdown selections for tone, strategy, and locale</p>
<p>Match marketing objectives to content type capabilities</p>
<p>Generate multiple variants for A/B testing</p>
</td>
<td>
<p>Ask for structural changes, styling, or image editing in prompts</p>
<p>Mention tone/strategy in prompts if available in dropdowns</p>
<p>Use vague objectives like "promote our product"</p>
<p>Request conditional element selections</p>
<p>Expect layout modifications through prompts</p>
</td>
</tr>
</tbody>
</table>

### Content not supported in prompts

>[!TIP]
>
>Use the **email editor** or **Adobe Express** for visual/image modifications.

These requests are not supported and should be handled through other tools:

<table style="table-layout: fixed; border: 0;">
<thead style="border: 0; background-color: #FFFFFF">
<tr>
<th>&#10005; Email structure modifications</th>
<th>&#10005; Visual styling changes</th>
<th>&#10005; Image editing operations</th>
</tr>
</thead>
<tbody>
<tr style="border: 0;">
<td>
<ul>
<li>Selecting specific sections to change</li>
<li>Deleting or cloning elements</li>
<li>Conditional selections</li>
<li>Adding or removing layout sections</li>
</ul>
</td>
<td>
<ul>
<li>Text formatting (bold, italic, font size)</li>
<li>Color modifications</li>
<li>Layout styling (borders, padding, margins)</li>
<li>Visual effects (shadows)</li>
</ul>
</td>
<td>
<ul>
<li>Background changes</li>
<li>Adding text overlays or logos</li>
<li>Images cropping or resizing</li>
<li>Color adjustments</li>
<li>Image replacement</li>
</ul>
</td>
</tr>
</tbody>
</table>

### Quality checklist {#quality-checklist}

Before generating content, ensure the following:

&check; **Clear objective**: Clearly states the action, product/service, value, and context.

&check; **Defined target audience**: Specifies the demographic, role, or segment.

&check; **Content type alignment**: Objective matches the selected channel or format.

&check; **Dropdown selections configured**: Tone, strategy, and locale are chosen, do not include them in the prompt.

&check; **Document focus specified**: Highlights which content or sections to reference.

&check; **Brand applied**: Appropriate brand guidelines are selected.

&check; **Realistic scope**: Avoid requests for layout changes, styling, or structural edits.

## Write effective marketing objectives {#marketing-objectives}

### Be specific and action-oriented

When crafting marketing objectives, make sure they are clear, actionable, and measurable. Avoid vague or generic statements.

**Examples of good objectives:**

&check; "Drive sign-ups for our free 30-day trial of the new AI-powered analytics dashboard"

&check; "Generate leads for our B2B webinar on 'Reducing Cloud Costs by 40%' happening March 15th"

&check; "Promote our limited-time 25% holiday discount on premium subscriptions, ending December 25th"

**Examples to avoid:**

&#10005; "Promote our product" (too vague)

&#10005; "Make people buy stuff" (unclear value)

&#10005; "Email about new features" (lacks purpose)

### Structure your objective

Always provide context and the value proposition so AI can generate relevant content.
Use this formula to help you write effective objectives: **Action + Product/Service + Value/Benefit + Urgency/Context**

**Examples of good objectives:**

&check; "Encourage downloads of our new mobile app that helps users track sustainable living habits with personalized eco-friendly recommendations"

&check; "Promote registration for our exclusive workshop on advanced data visualization techniques for marketing professionals"

&check; "Drive attendance to our product launch event showcasing the revolutionary AI writing assistant that saves 5+ hours per week"

**Examples to avoid:**

&#10005; "Announce new app" (missing value proposition and context)

&#10005; "Get people to sign up for workshop" (lacks specificity about audience and benefit)

&#10005; "Promote event" (no clear action, value, or urgency)

## Create new content vs. modify existing content {#new-vs-modify}

Clearly indicate if your request involves generating new content or updating existing material. This distinction is important because it guides the AI in selecting the appropriate approach and ensures a more accurate and useful outcome.

### Creating new content

Apply this strategy when you are launching marketing campaigns, unveiling new products, or initiating any kind of updated or refreshed communication. It ensures your message starts strong and aligns with your goals.

**How to prompt** &#10148; When creating new content, focus on your marketing objective without referencing existing content.

>[!BEGINSHADEBOX]

**Examples:**

* **SaaS trial**: "Launch our new CRM software to small business owners, highlighting 50% time savings, 90% faster lead qualification, and offering a 30-day free trial with personalized onboarding"
* **Feature announcement**: "Announce new API integration capabilities that reduce development time by 60% for enterprise customers, targeting technical decision-makers"
* **Event promotion**: "Drive registrations for our webinar on 'Digital Marketing Trends 2024' featuring experts from Google, Meta, and Adobe, emphasizing actionable insights and limited seats (500 max)"

>[!ENDSHADEBOX]

### Modifying existing content

>[!TIP]
>
>For standard modifications such as elaborate, summarize, or simplify, use the **Refine** feature instead of writing custom prompts. [Learn more](generative-uc.md##refine)

Apply this when you need to update, refresh, or adapt your current marketing campaigns. This method supports incremental improvements, ensuring your messaging stays relevant without starting from scratch.

**How to prompt** &#10148; When modifying existing content, clearly specify what you want changed and how to change it.

>[!BEGINSHADEBOX]

**Examples:**

* **Campaign refresh**: "Modify the product launch email to focus on enterprise security features instead of general productivity benefits, targeting IT decision-makers with compliance certifications"
* **Audience pivot**: "Adapt our software demo invitation to target healthcare specifically, replacing generic examples with healthcare use cases and HIPAA compliance benefits"
* **Seasonal update**: "Update our Q3 promotional campaign for Q4 holiday shopping, changing focus from back-to-school to holiday gift giving with fast shipping emphasis"

>[!ENDSHADEBOX]

## Enhance your prompt with advanced settings {#personalize-prompt}

### Communication strategy types

>[!TIP]
>
>Use the Communication strategy dropdown from the Text settings menu instead of mentioning it in your prompt for specialized processing.

Your communication strategy determines how you present your message to maximize impact. Different strategies work better for different goals, whether you are building urgency, establishing trust, or driving immediate action. Choose the strategy that best aligns with your campaign objectives and audience mindset.

| **Strategy** | **Best For** | **Messaging Style** | **Examples** |
|--------------|--------------|------------------------|--------------|
| **Urgent** | Time-sensitive offers, deadlines, immediate action | Creates immediate pressure with time-based language | "Act now: Offer expires at midnight" <br> "Register today before spots fill up" <br> "48-hour flash sale starts now" |
| **FOMO (Fear of Missing Out)** | Limited offers, events, exclusive access | Uses urgency, scarcity, and time-pressure cues | "Only 24 hours left! Limited stock at 40% off" <br> "Last chance: Early bird pricing ends tomorrow" <br> "Only 100 beta spots remaining" |
| **Social Proof** | Trust-building, testimonials, popular products | Leverages others' experiences and validation | "Join 50,000+ satisfied customers" <br> "Rated 4.9/5 stars by industry professionals" <br> "Trusted by Fortune 500 companies" |
| **Scarcity** | Limited inventory, exclusive releases, high-demand items | Emphasizes limited availability and exclusiveness | "Only 5 left in stock" <br> "Limited edition: 100 units available" <br> "Exclusive release: First come, first served" |
| **Incentive** | Promotions, rewards programs, special offers | Highlights tangible benefits and rewards | "Get 20% off your first order" <br> "Earn double points this weekend" <br> "Free shipping on orders over $50" |
| **Exclusivity** | Premium products, VIP experiences, members-only offers | Uses premium positioning and special-access language | "Exclusive invitation to our private preview" <br> "Elite membership unlocks advanced analytics" <br> "Join select Fortune 500 companies already using us" |
| **Gamification** | Engagement campaigns, loyalty programs, interactive content | Uses game mechanics and achievement language | "Unlock your next reward level" <br> "Complete challenges to earn badges" <br> "Climb the leaderboard for exclusive prizes" |
| **Informative** | Education, research, complex products, thought leadership | Uses facts, data, insights, and explanation | "5 insights from analyzing 10,000+ interactions" <br> "New research reveals 3 breakthrough approaches" <br> "Complete guide to implementing AI in marketing" |
| **Education & Insights** | Learning content, industry trends, best practices | Provides valuable knowledge and actionable takeaways | "Master advanced techniques with our expert guide" <br> "Discover 7 strategies top marketers use" <br> "Learn how to optimize your workflow in 5 steps" |

### Set the right tone {#tone}

>[!TIP]
>
>Use the Tone dropdown from the Text settings menu rather than specifying it in your prompt. 

Tone shapes how your audience perceives and responds to your message. Always select a tone that aligns with your brand voice and the stage of the profile journey.

Use the table below to explore each tone in detail, including when it works best and examples of content that fit each style.

| Tonality | Best For | Content Example |
|-|-|-|
| Professional  | B2B communications, formal announcements | "We're pleased to announce our strategic partnership..." |
| Empathetic | Customer support, sensitive topics | "We understand how frustrating this must be for you..."|
| Humorous | Engaging campaigns, lighthearted content | "Warning: May cause serious productivity gains!"|
| Exciting | Product launches, event promotions | "This is the moment you've been waiting for!"|
| Inspirational | Motivational campaigns, brand purpose | "Together, we can make a difference in the world..."|
| Persuasive| Sales campaigns, conversions | "Don't miss this limited-time opportunity to..."      |
| Friendly | Customer engagement, welcome messages | "We're so glad you're here with us!"|
| Formal | Legal communications, official notices | "We hereby notify you of the following changes..."|
| Apologetic | Service recovery, issue resolution | "We sincerely apologize for any inconvenience caused..."|
| Assertive | Leadership content, authoritative messaging | "Here's what you need to do right now..."|
| Storytelling | Brand narratives, emotional connections | "It all started with a simple question..."|
| Conversational | Nurture campaigns, relationship building | "Let's talk about how this can help you..."|

### Optimize your brand assets {#brand-assets}

>[!TIP]
>
>If you have already uploaded a brand asset through the **Brand Assets** menu, you do not need to reference it in your prompt. The system automatically uses any selected documents.

Brand assets provide factual information that enriches your generated content with specific, accurate details.
When you upload broad documents such as product brochures, add to your prompt which parts to focus on:

* **Instead of** _"Use the product brochure"_ **you should use** _"Focus on the advanced security features and compliance certifications, specifically SOC 2 compliance and data encryption"_

* **Instead of** _"Reference the case studies"_ **you should use** _"Highlight ROI results from healthcare clients, specifically the 40% cost reduction at Regional Medical Center"_

* **Instead of** _"Include technical details"_ **you should use** _"Emphasize API integration capabilities and developer benefits, focusing on REST API endpoints and 99.9% uptime SLA"_

### Content Refinement

>[!TIP]
>
>Use the Refine feature instead of prompting when you want to elaborate, summarize, simplify, change tone, or translate existing content. [Learn more](generative-uc.md#refine)

Once content is generated, use the **Refine** feature to iterate and enhance it with the following options:

|**Action** | **Use Case** | **Prompt Example** |
|-|-|-|
| **Elaborate** | Add depth and detail to brief content | "Elaborate on the technical benefits of our security features" |
| **Summarize** | Condense lengthy content for different formats | "Summarize this product overview for a social media post" |
| **Simplify** | Make complex content more accessible | "Simplify this technical explanation for a general audience" |
| **Change Tone** | Adapt content for different audiences | "Change tone to more casual for younger demographic" |
| **Transcreate** | Cultural adaptation beyond translation | "Transcreate this campaign for the Japanese market" |

## Scenario-Based Prompt Examples

### Based on Content Type {#content-type-practices}

<table style="table-layout: fixed; border: 0;">
<thead>
<tr style="border: 0;background-color: #FFFFFF;">
<th>Channel</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Email</strong></td>
<td>"Nurture enterprise prospects by showcasing three customer success stories with detailed ROI metrics (IBM: 45% cost reduction, Accenture: 200% lead increase, Microsoft: 60% time savings), targeting IT directors at companies with 1000+ employees"</td>
</tr>
<tr>
<td><strong>SMS</strong></td>
<td>"Alert VIP customers about 4-hour flash sale on premium electronics with 40% discount, limited to first 100 customers"</td>
</tr>
<tr>
<td><strong>Push Notifications</strong></td>
<td>"Re-engage users who haven't opened the app in 7 days with personalized content recommendations based on their reading history"</td>
</tr>
<tr>
<td><strong>Landing Pages</strong></td>
<td>"Convert B2B visitors into qualified leads by demonstrating how our enterprise security solution prevents 99.9% of cyber attacks, with Fortune 500 testimonials and free security audit"</td>
</tr>
</tbody>
</table>

### Based on Industry-Specific Approaches {#industry-approaches}

<table style="table-layout: fixed; border-collapse: collapse; border: 0;">
<thead>
<tr style="border: 0;background-color: #FFFFFF;">
<th>Industry</th>
<th>Example Prompt</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>B2B Technology</strong></td>
<td>"Demonstrate ROI and technical specifications while addressing security concerns for IT decision-makers evaluating our cloud infrastructure solution, emphasizing 99.9% uptime SLA, SOC 2 compliance, and 40% cost savings."</td>
</tr>
<tr>
<td><strong>E-commerce Retail</strong></td>
<td>"Create urgency around limited-stock holiday items while highlighting free shipping and easy returns for last-minute shoppers, emphasizing limited quantities (less than 50 remaining) and 24-hour shipping cutoff."</td>
</tr>
<tr>
<td><strong>Financial Services</strong></td>
<td>"Educate clients about investment portfolio diversification strategies while maintaining regulatory compliance, featuring certified financial advisor insights and risk disclaimers."</td>
</tr>
<tr>
<td><strong>Healthcare & Wellness</strong></td>
<td>"Promote preventive care benefits and annual health screenings while maintaining medical accuracy, featuring board-certified physician recommendations and patient privacy assurances."</td>
</tr>
<tr>
<td><strong>Education & Training</strong></td>
<td>"Emphasize career advancement outcomes and industry certifications while showcasing instructor expertise, highlighting 92% job placement rate and project-based curriculum."</td>
</tr>
<tr>
<td><strong>SaaS Platforms</strong></td>
<td>"Highlight time savings and automation benefits with specific metrics while addressing integration concerns, featuring average 25-hour weekly time savings and integration with 200+ popular tools."</td>
</tr>
</tbody>
</table>
