---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: Auto-optimization models
description: Learn more about auto-optimization models
badge: label="Legacy" type="Informative"
feature: Ranking, Decision Management
role: User
level: Experienced
exl-id: a85de6a9-ece2-43da-8789-e4f8b0e4a0e7
version: Journey Orchestration
---
# Auto-optimization models {#auto-optimization-model}

>[!TIP]
>
>Decisioning, [!DNL Adobe Journey Optimizer]'s new decisioning capability, is now available via the code-based experience and email channels! [Learn more](../../experience-decisioning/gs-experience-decisioning.md)

An Auto-optimization model aims to serve offers that maximize the return (KPIs) set by business clients. These KPIs could be in the form of conversion rates, revenue, etc. At this point, Auto-optimization focuses on optimizing offer clicks with offer conversion as our target. Auto-optimization is non-personalized and optimizes based on "global" performance of the offers.

## Dataset requirements

To train an auto-optimization model, the dataset must meet the following minimum requirements:

* At least 2 offers in the dataset must have at least 100 display events and 5 click events within the last 14 days.
* Offers with fewer than 100 displays and/or 5 click events within the last 14 days will be treated by the model as new offers, and are only eligible to be served by the exploration bandit.
* Offers with more than 100 displays and 5 click events within the last 14 days will be treated by the model as existing offers, and are eligible to be served by both exploration and exploitation bandits.

Until the first time an auto-optimization model is trained, offers within a selection strategy utilizing an auto-optimization model will be served at random.

## Limitations {#limitations}

The use of Auto-optimization models for decision management is subject to the limitations below:

* Auto-optimization models do not work with the Batch Decisioning API.
* Feedback needed to build model must be sent in as an experience event. It should not be sent in automatically in [!DNL Journey Optimizer] channels.

## Terminology {#terminology}

The following terms are useful when discussing Auto-optimization: 

* **Multi-armed bandit**: A [multi-armed bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit){target="_blank"} approach to optimization balances exploratory learning and exploitation of that learning.

* **Thomson sampling**: Thompson sampling is an algorithm for online decision problems where actions are taken sequentially in a manner that must balance between exploiting what is known to maximize immediate performance and investing to accumulate new information that may improve future performance. [Learn more](#thompson-sampling)

* [**Beta distribution**](https://en.wikipedia.org/wiki/Beta_distribution){target="_blank"}: Set of continuous [probability distributions](https://en.wikipedia.org/wiki/Probability_distribution){target="_blank"} defined on the interval [0, 1] [parameterized](https://en.wikipedia.org/wiki/Statistical_parameter){target="_blank"} by two positive [shape parameters](https://en.wikipedia.org/wiki/Shape_parameter){target="_blank"}. 

## Thompson Sampling {#thompson-sampling}

The algorithm that underlies Auto-optimization is **Thompson sampling**. In this section, we discuss the intuition behind Thompson sampling.

[Thompson sampling](https://en.wikipedia.org/wiki/Thompson_sampling){target="_blank"}, or Bayesian bandits, is a Bayesian approach to the multi-armed bandit problem.  The basic idea is to treat the average reward 𝛍 from each offer as a **random variable** and use the data we have collected so far, to update our "belief" about the average reward. This "belief" is represented mathematically by a **posterior probability distribution** – essentially a range of values for the average reward, along with the plausibility (or probability) that the reward has that value for each offer. Then, for every decision, we will **sample a point from each of these posterior reward distributions** and select the offer whose sampled reward had the highest value.  

This process is illustrated in the figure below, where we have 3 different offers. Initially we have no evidence from the data and we assume all offers have a uniform posterior reward distribution. We draw a sample from each offer's posterior reward distribution. The sample selected from Offer 2's distribution has the highest value. This is an example of **exploration**. After showing Offer 2, we collect any potential reward (for example conversion/no-conversion) and update the posterior distribution of Offer 2 using Bayes Theorem as explained below.  We continue this process and update the posterior distributions each time an offer is shown and the reward is collected. In the second figure, Offer 3 is selected – despite Offer 1 having the highest average reward (its posterior reward distribution is furthest to the right), the process of sampling from each distribution has led to us choosing an apparently suboptimal Offer 3. In doing so, we give ourself the opportunity to learn more about Offer 3's true reward distribution. 

As more samples are collected, the confidence increases, and a more accurate estimate of the possible reward is obtained (corresponding to narrower reward distributions). This process of updating our beliefs as more evidence becomes available is known as **Bayesian Inference**. 

Eventually, if one offer (e.g. Offer 1) is a clear winner, its posterior reward distribution will be separated from others. At this point, for each decision, the sampled reward from Offer 1 is likely to be the highest, and we will choose it with a higher probability. This is **exploitation** – we have a strong belief that Offer 1 is the best, and so it's being chosen to maximize rewards.

![](../assets/ai-ranking-thompson-sampling.png)

**Figure 1**: *For every decision, we sample a point from the posterior reward distributions. The offer with highest sample value (conversion rate) will be chosen. In the initial phase, all offers have uniform distribution since we do not have any evidence about the conversion rates of the offers from the data. As we collect more samples, the posterior distributions get narrower and more accurate. Ultimately, the offer with highest conversion rate will be chosen every time.*


<!--
![](../assets/ai-ranking-thompson-sampling-initial.png)
![](../assets/ai-ranking-thompson-sampling-intermediate.png)
![](../assets/ai-ranking-thompson-sampling-ultimate.png)
-->


+++**Technical Details**

To calculate/update distributions, we use **Bayes Theorem**. For each offer ***i***, we want to calculate their ***P(𝛍i | data)***, i.e. for each offer ***i***, how likely a reward value **𝛍i** is, given the data we have collected so far for that offer.

From Bayes Theorem:

***Posterior = Likelihood * Prior***

The **prior probability** is the initial guess about the probability for producing an output. The probability, after some evidence has been collected, is known as the **posterior probability**.  

Auto-optimization is designed to consider binary rewards (click/no-click). In this case, the likelihood represents the number of successes from N trials and is modeled by a **Binomial distribution**. For some likelihood functions, if you choose a certain prior, the posterior ends up being in the same distribution as the prior. Such a prior then is called a **conjugate prior**. This kind of prior makes the calculation of posterior distribution very simple. The **Beta distribution** is a conjugate prior to the binomial likelihood (binary rewards), and so is a convenient and sensible choice for the prior and posterior probability distributions.The Beta distribution takes two parameters, ***α*** and ***β***. These parameters can be thought of as the count of successes and failures and the mean value given by: 

![](../assets/ai-ranking-beta-distribution.png)

The Likelihood function as we explained above is modeled by a Binomial distribution, with s successes (conversions) and f failures (no-conversions) and q is a [random variable](https://en.wikipedia.org/wiki/Random_variable){target="_blank"} with a [beta distribution](https://en.wikipedia.org/wiki/Beta_distribution){target="_blank"}.

The prior is modeled by Beta distribution and the posterior distribution takes the following form:

![](../assets/ai-ranking-posterior-distribution.svg)

The posterior is calculated by simply adding the number of successes and failures to the existing parameters ***α***, ***β***.  

For Auto-optimization, as shown in the example above, we start with a prior distribution ***Beta(1, 1)*** (uniform distribution) for all offers and after getting s successes and f failures for a given offer, the posterior becomes a Beta distribution with parameters ***(s+α, f+β)*** for that offer.
+++

**Related topics**:

For a deeper dive on Thompson sampling, read the following research papers:

* [An Empirical Evaluation of Thompson Sampling](https://proceedings.neurips.cc/paper/2011/file/e53a0a2978c28872a4505bdb51db06dc-Paper.pdf){target="_blank"}
* [Analysis of Thompson Sampling for the Multi-armed Bandit Problem](https://proceedings.mlr.press/v23/agrawal12/agrawal12.pdf){target="_blank"}

## Cold-start problem {#cold-start}

The "cold-start" problem occurs when a new offer is added to a campaign, and there is no data available about the new offer's conversion rate. During this period, we have to come up with a strategy regarding how often this new offer is chosen so that the performance drop is minimized, while we collect information about conversion rate of this new offer. There are multiple solutions available to tackle this problem. The key is to find a balance between the exploration of this new offer while we do not sacrifice the exploitation much. Currently we use "uniform distribution" as our initial guess about the new offer's conversion rate (prior distribution). Basically we give all conversion rate values equal probability of occurrence. 


![](../assets/ai-ranking-cold-start-strategies.png)

**Figure 2**: *Consider a campaign with 3 offers. While the campaign is live, Offer 4 is added to the campaign. Initially we have no data about the conversion rate of the Offer 4 and we have to deal with the cold-start problem. We use uniform distribution as our initial guess about conversion rate of Offer 4, while we collect data for this new offer. As explained in the [Thompson sampling](#thompson-sampling) section, to choose which offer is going to be shown to a user, we sample points from the posterior rewards distributions of the offers and select the offer with the highest sample value. In the example above, Offer 4 is chosen and later based on the reward collected, the posterior distribution of this offer is updated as explained in the [Thompson sampling](#thompson-sampling) section.*

## Lift Measurement {#lift}

"Lift" is the metric used to measure the performance of any strategy deployed in ranking service, in comparison with baseline strategy (serving offers just randomly). 

For example, if we're interested in measuring the performance of a Thompson Sampling (TS) strategy used in ranking service, and the KPI is conversion rate (CVR), the "lift" of the TS strategy against baseline strategy is defined as:

![](../assets/ai-ranking-lift.png)
