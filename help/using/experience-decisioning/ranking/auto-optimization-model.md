---
solution: Journey Optimizer
product: Journey Optimizer
title: Auto-optimization models
description: Learn more about auto-optimization models
feature: Ranking, Decisioning
role: User
level: Experienced
exl-id: 8a8b66cb-dd96-4373-bbe0-a67e0dc0b2c0
version: Journey Orchestration
---
# Auto-optimization models {#auto-optimization-model}

[!DNL Adobe Journey Optimizer]'s Auto-optimization model is a reinforcement learning model which maximizes offer click-through rate (CTR) by exploring all offers (or content), then ranking items based on predicted CTR, after eligibility rules and frequency caps are applied.

## Use cases and benefits {#use-cases-benefits}

Auto-optimization can be used any time you want quick and easy setup, want to find overall winning offers, and want to maximize offer clicks within a single channel. For example:

* Choose the best offers to insert on a web page to maximize offer clicks.
* Choose the best offers to insert in an email to maximize offer clicks.
* Choose the best offers to insert in a mobile app screen to maximize offer clicks.

Auto-optimization is a good choice when:

* Offers change over time or frequently: the Auto-optimization model is retrained every six hours.

## Requirements and limitations {#requirements-limitations}

Auto-optimization has the following requirements and limits:

* Auto-optimization requires a training dataset containing offer display events, offer click events, and the Experience Event - Proposition Interactions field group.
* Auto-optimization models cannot be utilized in requests to the Batch Decisioning API.
* Auto-optimization always optimizes for offer clicks. To maximize for an objective other than offer clicks, use the [Personalized optimization](personalized-optimization-model.md) model.
* Auto-optimization attempts to find overall winning offers and does not find a personalized ranking for each customer. To find personalized rankings for each customer, use the [Personalized optimization](personalized-optimization-model.md) model.

To train an auto-optimization model, the dataset must meet the following minimum requirements:

* At least 2 offers in the dataset must have at least 100 display events and 5 click events within the last 14 days.
* Offers with fewer than 100 displays and/or 5 click events within the last 14 days will be treated by the model as new offers, and are only eligible to be served by the exploration bandit.
* Offers with more than 100 displays and 5 click events within the last 14 days will be treated by the model as existing offers, and are eligible to be served by both exploration and exploitation bandits.

Until the first time an auto-optimization model is trained, offers within a selection strategy utilizing an auto-optimization model will be served at random.

## Balancing optimization with learning {#balancing-optimization-learning}

Auto-optimization is a [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning){target="_blank"} model which learns about the click-through performance of offers based on real-world customer behavior. Reinforcement learning models seek to maximize an objective by choosing actions with better predicted outcomes. However, a model that always presented every customer with the item(s) with the best predicted outcome would never learn about the performance of new items introduced over time (the so-called "cold start problem"), nor would it learn about changes in the performance of other existing items resulting from changes in the behavior of customers over time. Reinforcement learning models must therefore manage what is commonly called the [explore-exploit tradeoff](https://en.wikipedia.org/wiki/Exploration%E2%80%93exploitation_dilemma){target="_blank"}, i.e. balance optimization with learning.

Auto-optimization uses a common approach called a [multi-armed bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit){target="_blank"} to manage the tradeoff. The multi-armed bandit makes ranking decisions based on:

* the predicted click-through rate of each item
* the differences in the predicted click-through rate of each item
* the model's degree of uncertainty about its predictions for each item.

Multi-armed bandits utilize this information, along with random variability, to choose the actions to take. Auto-optimization is an [ensemble algorithm](https://en.wikipedia.org/wiki/Ensemble_learning){target="_blank"} which contains multiple multi-armed bandits in order to ensure all offers are adequately explored while maximizing overall performance.

When responding to a ranking request, a "supervising" multi-armed bandit first makes a choice of whether this request should be biased towards exploration or biased towards exploitation. This decision is made using an "epsilon-greedy" approach.

The second layer of ranking is performed by one of two [Thompson sampling](https://en.wikipedia.org/wiki/Thompson_sampling){target="_blank"} bandits:

* 10% of traffic is allocated towards an exploration-focused bandit which is more likely to recommend new offers or those with limited data, under the assumption that the model would benefit from learning more about customer behavior in response to these offers.
* 90% of traffic is allocated towards an exploitation-focused bandit which is more likely to consistently recommend high-performing offers over time, under the assumption that new or low-data offers are more likely to underperform until proven otherwise.

In a technical sense, these assumptions are parameters of the prior probability distribution, also referred to as [priors](https://en.wikipedia.org/wiki/Prior_probability){target="_blank"}. As offers gather more display and click data, the influence of the chosen priors becomes lower, and the predictions made by the two bandits tend to converge over time.

Our approach of combining multiple bandits and allocating some dedicated traffic for exploration provides several benefits:

* the model learns most quickly about the newest offers with the least data
* the model continues to learn about all offers and responds to changes in customer behavior over time
* the model does not overfit by aggressively favoring offers with higher apparent CTR but few observations, or aggressively disfavoring offers with lower apparent CTR but few observations
* the model is robust to handling traffic allocation decisions across hundreds of offers with sparse click data and with very different amounts of historical data

## Thompson sampling {#thompson-sampling}

[Thompson sampling](https://en.wikipedia.org/wiki/Thompson_sampling){target="_blank"}, or Bayesian bandits, is a Bayesian approach to the multi-armed bandit problem. The model treats average reward 𝛍 from each offer as a random variable and uses the data we have collected so far to update our "belief" about the average reward. This "belief" is represented mathematically by a posterior probability distribution – essentially a range of values for the average reward, along with the plausibility (or probability) that the reward has that value for each offer. Then, for every decision, we will sample a point from each of these posterior reward distributions and select the offer whose sampled reward had the highest value.

This process is illustrated in the figure below, where we have 3 different offers. Initially we have no evidence from the data, and we assume all offers have a uniform posterior reward distribution. We draw a sample from each offer's posterior reward distribution. The sample selected from Offer 2's distribution has the highest value. This is an example of exploration. After showing Offer 2, we collect any potential reward (for example conversion/no-conversion) and update the posterior distribution of Offer 2 using Bayes Theorem as explained below. We continue this process and update the posterior distributions each time an offer is shown and the reward is collected. In the second figure, Offer 3 is selected – despite Offer 1 having the highest average reward (its posterior reward distribution is furthest to the right), the process of sampling from each distribution has led to us choosing an apparently suboptimal Offer 3. In doing so, we give ourselves the opportunity to learn more about Offer 3's true reward distribution.

As more samples are collected, the confidence increases, and a more accurate estimate of the possible reward is obtained (corresponding to narrower reward distributions). This process of updating our beliefs as more evidence becomes available is known as **Bayesian Inference**.

Eventually, if one offer (e.g. Offer 1) is a clear winner, its posterior reward distribution will be separated from others. At this point, for each decision, the sampled reward from Offer 1 is likely to be the highest, and we will choose it with a higher probability. This is exploitation – we have a strong belief that Offer 1 is the best, and so it's being chosen to maximize rewards.

![](../assets/ai-ranking-thompson-sampling.png)

**Figure 1**: *For every decision, we sample a point from the posterior reward distributions. The offer with highest sample value (conversion rate) will be chosen. In the initial phase, all offers have uniform distribution since we do not have any evidence about the conversion rates of the offers from the data. As we collect more samples, the posterior distributions get narrower and more accurate. Ultimately, the offer with highest conversion rate will be chosen every time.*

+++ Calculation details

To calculate/update distributions, we use **Bayes' Theorem**. For each offer ***i***, we want to calculate their ***P(𝛍i | data)***, i.e. for each offer ***i***, how likely a reward value **𝛍i** is, given the data we have collected so far for that offer.

From Bayes Theorem:

***Posterior = Likelihood * Prior***

The **prior probability** is the initial guess about the probability for producing an output. The probability, after some evidence has been collected, is known as the **posterior probability**.

Auto-optimization is designed to consider binary rewards (click/no-click). In this case, the likelihood represents the number of successes from N trials and is modeled by a binomial distribution. For some likelihood functions, if you choose a certain prior, the posterior ends up being in the same distribution as the prior. Such a prior then is called a **conjugate prior**. This kind of prior makes the calculation of posterior distribution very simple. The [Beta distribution](https://en.wikipedia.org/wiki/Beta_distribution){target="_blank"} is a conjugate prior to the binomial likelihood (binary rewards), and so is a convenient and sensible choice for the prior and posterior probability distributions. The Beta distribution takes two parameters, ***α*** and ***β***. These parameters can be thought of as the count of successes and failures and the mean value given by:

![](../assets/ai-ranking-beta-distribution.png)

The Likelihood function as explained above is modeled by a Binomial distribution, with s successes (conversions) and f failures (no-conversions) and q is a random variable with a Beta distribution.

The prior is modeled by Beta distribution and the posterior distribution takes the following form:

![](../assets/ai-ranking-posterior-distribution.svg)

+++

### Exploration bias and exploitation bias {#exploration-exploitation-bias}

An initial value must be chosen for the parameters ***α***, ***β***. Auto-optimization includes both an exploration-biased Thompson sampling bandit and an exploitation-biased Thompson sampling bandit which utilize different initial ***α***, ***β*** priors in their beta distributions.

In a general Thompson sampling approach, the posterior is calculated by simply adding the number of successes and failures to the existing parameters ***α***, ***β***. Auto-optimization utilizes different weighting factors for new successes and failures to modify the impact of new data vs. prior data in both the exploration-biased and exploitation-biased bandits.

## References {#references}

For a deeper dive on Thompson sampling bandits, refer to the following research papers:

* [An Empirical Evaluation of Thompson Sampling](https://proceedings.neurips.cc/paper/2011/file/e53a0a2978c28872a4505bdb51db06dc-Paper.pdf){target="_blank"}
* [Analysis of Thompson Sampling for the Multi-armed Bandit Problem](https://proceedings.mlr.press/v23/agrawal12/agrawal12.pdf){target="_blank"}
