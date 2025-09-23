---
title: Statistical calculations used in the Experimentation report
description: Learn more about A/B testing vs multi-armed bandit
feature: A/B Testing, Experimentation
role: User
level: Experienced
---
# A/B vs Multi-armed bandit experiments {#mab-vs-ab}

<!--
>[!CONTEXTUALHELP]
>id="ajo_ab_test_mab"
>title="Experiment type"
>abstract="Experiment type determines how traffic is allocated between treatments during your test. Choose the method that best aligns with your goals:</br>
>
>* **A/B Experiment**: Splits traffic as you define between treatments and measures performance until results are statistically significant. Best for learning which treatment performs better in a controlled comparison.
>
>* **Multi-armed Bandit**: Shifts traffic toward higher-performing treatments as data is collected, balancing speed and optimization. Useful when you want to maximize conversions during the experiment.
>
>* **Bring your own Multi-armed Bandit**: Use your own algorithm to decide traffic allocation, giving you flexibility if you have a custom model or strategy."
-->

This page provides a detailed comparison of **A/B** and **Multi-Armed Bandit** experiments, explaining their respective strengths, limitations, and the scenarios in which each approach is most effective. 

## A/B {#ab-test}

Traditional A/B experiment involves splitting traffic equally across treatments and maintaining this allocation until the experiment concludes. Once statistical significance is reached, the winning treatment is identified and subsequently scaled.

### Advantages

The key strengths of traditional A/B experiment are:

* **Statistical Rigor**

    The fixed design provides well-defined error rates and confidence intervals.

    Hypothesis testing frameworks, e.g. 95% confidence, are easier to apply and interpret.

    Properly powered experiments reduce the likelihood of false positives.

* **Simplicity**

    The methodology is straightforward to design and execute.

    Results can be communicated clearly to non-technical stakeholders.

* **Comprehensive Data Collection**

    Each treatment receives adequate exposure, enabling analysis not only of the winning variant but also of underperforming alternatives.

    This additional information can inform long-term strategic decisions.

* **Bias Control**

    Fixed allocation reduces susceptibility to biases such as the "winner's curse" or regression to the mean.

### Limitations

The main limitations of traditional A/B experiment are:

* **Opportunity Cost**

    A substantial proportion of traffic is directed toward inferior treatments, potentially reducing conversions or revenue during the test.

    The winning treatment cannot be implemented until the experiment concludes.

* **Fixed Duration Requirement**

    Tests must generally run for their pre-specified horizon, even if external conditions, e.g. seasonality, market shifts, change mid-way.

    Adaptation during the experiment is limited.

## Multi-armed bandit {#mab-experiment}

Multi-armed bandit algorithms use adaptive allocation: as evidence accumulates, more traffic is directed toward better-performing treatments. The objective is to maximize cumulative reward during the experiment rather than focus solely on the final result.

### Advantages

The key strengths of Multi-armed bandit methods are:

* **Faster Optimization**
    
    Promising treatments are prioritized earlier, improving overall performance during the test.

* **Adaptivity**

    Allocations update continuously as data is collected, making Multi-armed bandit suitable for dynamic environments.

* **Reduced Opportunity Cost**
    
    Poor treatments are phased out quickly, minimizing wasted traffic.

* **Suitability for Continuous Testing**

    Effective for ongoing experimentation or contexts where traffic is costly.

### Limitations

The main limitations of Multi-armed bandit methods are:

* **Weaker Statistical Guarantees**

    Traditional hypothesis testing is harder to apply, and stopping rules are less clear.

* **Reduced Transparency**

    Adaptive allocation can be difficult to explain to stakeholders.

* **Limited Information on Underperforming Treatments**

    Weak treatments receive little exposure, limiting diagnostic insight.

* **Implementation Complexity**

    Requires advanced algorithms and infrastructure, with greater potential for misconfiguration.

## When to use A/B vs Multi-armed bandit

|Scenario | Recommended Method |
|-|-|
| You are running exploratory or research-driven tests | A/B  |
| You are running always-on campaigns, e.g. ads, recommendations | Multi-Armed Bandit |
| You want to maximize conversions during the test | Multi-Armed Bandit |
| You want clear, confident insights | A/B |
| You need to adapt quickly, e.g. seasonal shifts | Multi-Armed Bandit |
| You have limited traffic and want to optimize Return on Investement quickly | Multi-Armed Bandit |
| You have high traffic and can afford slower learning | A/B |
| Stakeholders need clear decision points | A/B |

