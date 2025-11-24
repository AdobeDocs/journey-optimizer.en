# Journey Entry and Exit Criteria - Content Enhancement Plan

## Executive Summary

Users find the community blog post "[Mastering Journey Entry and Exit Criteria](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer-blogs/mastering-journey-entry-and-exit-criteria-in-adobe-journey/ba-p/760958)" valuable because it provides:
- Real-world use case examples
- Business value explanations
- Practical best practices
- A unified view of both entry AND exit criteria

**Current State:** The official documentation has comprehensive technical information scattered across multiple files, but lacks the practical, business-focused approach that users find helpful.

## Gap Analysis

### What Exists
| File | Content | Strengths | Gaps |
|------|---------|-----------|------|
| `entry-management.md` | Profile entrance management, journey types, re-entrance rules | Technically comprehensive, covers processing rates | Missing real-world examples, business context |
| `journey-properties.md` | Exit criteria configuration | Good technical instructions | Only one use case, no best practices section |
| `end-journey.md` | How journeys close | Clear operational guidance | Doesn't connect to entry criteria |
| `journey-faq.md` | Q&A format with examples | Good practical examples in FAQ format | Scattered information |

### What Users Want (from blog post)
1. ✅ Real-world examples with context (Welcome Campaign, Abandoned Cart, Loyalty Program, Product Feedback)
2. ✅ "Why it matters" explanations (Relevance, Efficiency, Personalization, Compliance)
3. ✅ Best practices consolidated in one place
4. ✅ Unified coverage of entry + exit in one comprehensive guide
5. ✅ Accessible, less technical language

## Recommended Enhancements

### Option 1: Create a New Comprehensive Guide (RECOMMENDED)
**File:** `help/using/building-journeys/entry-exit-criteria-guide.md`

**Structure:**
```markdown
# Mastering Journey Entry and Exit Criteria

## Overview
- What are entry and exit criteria
- Why they matter (business value)

## Real-World Use Cases
1. Welcome Campaign for New Subscribers
2. Abandoned Cart Recovery
3. Loyalty Program Engagement
4. Product Feedback Collection
5. Time-Sensitive Promotions
6. Re-engagement Campaigns

## Configuring Entry Criteria
- Event-based triggers
- Audience-based entry
- Attribute filters
- Re-entrance rules
[Links to detailed technical docs]

## Configuring Exit Criteria
- Event-based exit
- Audience-based exit
- Goal achievement
- Timeout scenarios
[Links to detailed technical docs]

## Best Practices
- Clear definition and documentation
- Avoiding overlapping journeys
- Monitoring and optimization
- Frequency management
- Testing strategies

## Related Resources
[Links to technical documentation]
```

**Benefits:**
- Provides the unified, practical view users want
- Doesn't duplicate technical details (links to existing docs)
- Easy to find and understand
- Can be featured prominently in navigation

---

### Option 2: Enhance Existing Pages

#### A. Enhance `entry-management.md`

**Add after line 16:**

```markdown
## Why entry management matters

Properly configuring entry criteria ensures:

* **Relevance**: Only the right customers enter the journey, increasing engagement and conversion rates
* **Efficiency**: Prevents customers from entering irrelevant journeys, reducing unnecessary communication
* **Personalization**: Enables dynamic tailoring of experiences based on real-time data and behavior
* **Compliance**: Helps manage frequency capping and respect customer preferences

## Real-world entry scenarios

### Welcome Campaign for New Subscribers
**Entry condition:** Profiles enter when they subscribe to a newsletter  
**Journey type:** Unitary event journey  
**Re-entrance:** Usually disabled or with long wait period  
**Business benefit:** Ensures new subscribers receive timely onboarding

### Abandoned Cart Recovery
**Entry condition:** Profiles enter when they add items to cart but don't complete checkout within 24 hours  
**Journey type:** Event-triggered journey  
**Re-entrance:** Enabled with supplemental identifier for different cart sessions  
**Business benefit:** Drives conversions with timely reminders

### Loyalty Program Engagement
**Entry condition:** Profiles enter after reaching a loyalty points threshold  
**Journey type:** Audience qualification journey  
**Re-entrance:** Enabled for recurring rewards  
**Business benefit:** Keeps high-value customers engaged

### Product Feedback Collection
**Entry condition:** Profiles enter after receiving product delivery confirmation  
**Journey type:** Event-triggered journey  
**Re-entrance:** Per-product basis using supplemental identifiers  
**Business benefit:** Captures valuable feedback promptly
```

#### B. Enhance `journey-properties.md` Exit Criteria Section

**Add after line 273 (after the sample use case):**

```markdown
### Additional exit criteria use cases

#### Welcome Campaign
**Exit trigger:** Profile completes first purchase  
**Benefit:** Stops welcome messaging once goal is achieved, preventing message fatigue

#### Abandoned Cart Recovery
**Exit trigger:** Purchase completed event  
**Benefit:** Immediately removes profiles from recovery journey once they convert

#### Loyalty Program Engagement  
**Exit trigger:** Rewards redeemed OR 60 days of inactivity  
**Benefit:** Keeps communications relevant to active, engaged members only

#### Product Feedback Collection
**Exit trigger:** Feedback submitted OR 10 days elapsed  
**Benefit:** Stops requests once feedback received, respecting customer time

## Best practices for entry and exit criteria

### Planning and documentation
* **Document your logic:** Clearly map entry triggers and exit conditions before building
* **Align teams:** Ensure marketing and analytics teams understand the criteria
* **Use clear naming:** Label entry/exit criteria descriptively for easy maintenance

### Avoiding conflicts
* **Prevent overlapping journeys:** Ensure profiles aren't in conflicting journeys simultaneously
* **Use exit criteria to resolve conflicts:** Exit profiles from lower-priority journeys when they enter higher-priority ones
* **Leverage journey prioritization:** Configure priority scores in conflict management

### Optimization and monitoring
* **Monitor performance:** Track how entry/exit criteria affect journey metrics
* **A/B test criteria:** Experiment with different entry timing and exit triggers
* **Adjust based on data:** Refine criteria based on engagement and conversion data
* **Review regularly:** Audit active journeys quarterly for outdated criteria

### Frequency management
* **Respect frequency caps:** Configure criteria to limit journey entries per profile
* **Set appropriate re-entrance wait periods:** Balance persistence with message fatigue
* **Use exit criteria to limit exposure:** Remove profiles after a set number of communications
* **Consider cross-journey frequency:** Coordinate with global capping rules
```

#### C. Create Cross-Reference Section

**Add to end of `entry-management.md`:**

```markdown
## Related topics

* [Configure exit criteria](journey-properties.md#exit-criteria) - Define when profiles should leave your journey
* [End a journey](end-journey.md) - Understand how journeys close and finish
* [Best practices for entry and exit](journey-properties.md#best-practices-entry-exit) - Optimize your journey criteria
* [Journey use cases](jo-use-cases.md) - See complete examples with entry and exit configurations
```

**Add to `journey-properties.md` exit criteria section:**

```markdown
## Related topics

* [Profile entrance management](entry-management.md) - Configure how profiles enter journeys
* [Re-entrance rules](entry-management.md#entry-unitary) - Control repeated journey entries
* [How journeys end](end-journey.md) - Understand natural journey completion
* [Journey use cases](jo-use-cases.md) - See complete examples
```

---

### Option 3: Create a Dedicated Use Cases Page

**File:** `help/using/building-journeys/entry-exit-use-cases.md`

This would contain only the real-world examples with detailed configurations for each scenario, linking to technical documentation for implementation details.

---

## Implementation Recommendation

### Recommended Approach: Combination Strategy

1. **Create new comprehensive guide** (Option 1)
   - Provides the unified, accessible content users want
   - Timeline: 1-2 days

2. **Add best practices sections** to existing pages (Option 2B)
   - Enhances discoverability for users already on those pages
   - Timeline: 1 day

3. **Add cross-references** (Option 2C)
   - Improves navigation between related topics
   - Timeline: 30 minutes

4. **Update TOC and navigation**
   - Feature the new comprehensive guide prominently
   - Timeline: 30 minutes

### Priority Order

**Phase 1 (Week 1):**
- ✅ Create comprehensive guide with use cases and best practices
- ✅ Add cross-references between existing pages
- ✅ Update navigation/TOC

**Phase 2 (Week 2):**
- ✅ Enhance existing pages with additional use cases
- ✅ Add best practices sections to technical docs
- ✅ Review and test all links

**Phase 3 (Week 3):**
- ✅ Gather feedback from users
- ✅ Iterate based on analytics and user comments
- ✅ Consider creating video walkthrough

---

## Content Style Guidelines

Based on what makes the blog post effective:

### Do:
✅ Start with business value before technical details  
✅ Use concrete, relatable examples  
✅ Provide "Entry → Journey → Exit" complete scenarios  
✅ Include "Why" and "Benefit" for each use case  
✅ Use clear, accessible language  
✅ Break complex topics into digestible sections  
✅ Add visual diagrams where helpful  

### Don't:
❌ Lead with technical specifications  
❌ Use only abstract examples  
❌ Separate entry and exit into different contexts  
❌ Skip the business rationale  
❌ Use overly technical jargon without context  
❌ Create walls of text  

---

## Metrics for Success

Track these to measure if enhancements are working:

1. **Page views** on new comprehensive guide
2. **Time on page** (should increase with better content)
3. **Bounce rate** (should decrease)
4. **Internal link clicks** between entry/exit topics
5. **Search queries** - monitor if users still search for "entry criteria examples"
6. **Feedback/ratings** on documentation pages
7. **Community posts** - are users still asking these questions?

---

## Next Steps

1. **Review and approve** this enhancement plan
2. **Choose approach** (Recommended: Combination Strategy)
3. **Assign resources** for content creation
4. **Create content** following the structures above
5. **Review and edit** for consistency
6. **Publish and monitor** user engagement
7. **Iterate** based on feedback

---

## Quick Win: Add to jo-use-cases.md

While planning larger enhancements, you can make an immediate improvement:

**In `jo-use-cases.md`, line 192** already references the blog. Consider adding a note:

```markdown
<p><a href="https://experienceleaguecommunities.adobe.com/t5/journey-optimizer-blogs/mastering-journey-entry-and-exit-criteria-in-adobe-journey/ba-p/760958" target="_blank">Use Case: Journey Entry and Exit Criteria</a> - Learn how to effectively configure when profiles enter and exit journeys, with real-world examples and best practices. See also our <a href="entry-management.md">entry management</a> and <a href="journey-properties.md#exit-criteria">exit criteria</a> documentation.</p>
```

This creates a bridge between the popular blog post and the official documentation.

