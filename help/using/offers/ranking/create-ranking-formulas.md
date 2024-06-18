---
title: Ranking formulas
description: Learn how to create formulas to rank offers
feature: Ranking, Decision Management
topic: Integrations
role: User
level: Intermediate
exl-id: 8bc808da-4796-4767-9433-71f1f2f0a432
---
# Ranking formulas {#create-ranking-formulas}

## About ranking formulas {#about-ranking-formulas}

**Ranking formulas** allow you to define rules that will determine which offer should be presented first for a given placement, rather than taking into account the offers' priority scores.

Ranking formulas are expressed in **PQL syntax** and can leverage profile attributes, context data and offer attributes. For more on how to use the PQL syntax, refer to the [dedicated documentation](https://experienceleague.adobe.com/docs/experience-platform/segmentation/pql/overview.html).

Once a ranking formula has been created, you can assign it to a placement in a decision. For more on this, see [Configure offers selection in decisions](../offer-activities/configure-offer-selection.md).

## Create a ranking formula {#create-ranking-formula}

To create a ranking formula, follow the steps below:

1. Access the **[!UICONTROL Components]** menu, then select the **[!UICONTROL Ranking]** tab. The **[!UICONTROL Formulas]** tab is selected by default. The list of previously created formulas is displayed.

    ![](../assets/rankings-list.png)

1. Click **[!UICONTROL Create ranking]** to create a new ranking formula.

    ![](../assets/ranking-create-formula.png)

1. Specify the formula name, description, and formula. 

    In this example, we want to boost the priority of all offers with the "hot" attribute if the actual weather is hot. To do this, the **contextData.weather=hot** was passed in the decisioning call.

    ![](../assets/ranking-syntax.png)

    >[!IMPORTANT]
    >
    >When creating a ranking formula, looking back into a previous period of time is not supported. For instance, if you specify an experience event that occurred within the last month as a component of the formula. Any attempt to include a lookback period during formula creation will trigger an error when saving it.

1. Click **[!UICONTROL Save]**. Your ranking formula is created, you can select it from the list to get details and edit or delete it.

    It is now ready to be used in a decision to rank eligible offers for a placement (see [Configure offers selection in decisions](../offer-activities/configure-offer-selection.md)).

    ![](../assets/ranking-formula-created.png)

## Ranking formula examples {#ranking-formula-examples}

You can create many different ranking formulas according to your needs. Below are some examples.

<!--
Boost by offer ID

Boost the priority of an offer with the offer ID *xcore:personalized-offer:13d213cd4cb328ec* by 5.

**Ranking formula:**

```
if( offer._id = "xcore:personalized-offer:13d213cd4cb328ec", offer.rank.priority + 5, offer.rank.priority)
```

Change the offer priority based on a certain profile attribute

Set the offer priority to 30 for offer *xcore:personalized-offer:13d213cd4cb328ec* if the user lives in the city of Bondi.

**Ranking formula:**

```
if( offer._id = "xcore:personalized-offer:13d213cd4cb328ec" and homeAddress.city.equals("Bondi", false), 30, offer.rank.priority)
```

Boost multiple offers by offer ID based on the presence of a profile's audience membership

Boost the priority of offers based on whether the user is a member of a priority audience, which is configured as an attribute in the offer.

**Ranking formula:**

```
if( segmentMembership.get("ups").get(offer.characteristics.get("prioritySegmentId")).status in (["realized","existing"]), offer.rank.priority + 10, offer.rank.priority)
```
-->

### Boost offers with certain offer attribute based on profile attribute

If the profile lives in the city corresponding to the offer, then double the priority for all offers in that city.

**Ranking formula:**

```
if( offer.characteristics.get("city") = homeAddress.city, offer.rank.priority * 2, offer.rank.priority)
```

### Boost offers where the end date is less than 24 hours from now

**Ranking formula:**

```
if( offer.selectionConstraint.endDate occurs <= 24 hours after now, offer.rank.priority * 3, offer.rank.priority)
```

### Boost offers with certain offer attribute based on context data

Boost certain offers based on the context data being passed in the decisioning call. For example, if the `contextData.weather=hot` is passed in the decisioning call, the priority of all offers with `attribute=hot` must be boosted.

**Ranking formula:**

```
if (@{_xdm.context.additionalParameters;version=1}.weather.isNotNull()
and offer.characteristics.get("weather")=@{_xdm.context.additionalParameters;version=1}.weather, offer.rank.priority + 5, offer.rank.priority)
```

Note that when using the decisioning API, the context data is added to the profile element in the request body, such as in the example below.

**Snippet from request body:**

```
"xdm:profiles": [
{
    "xdm:identityMap": {
        "crmid": [
            {
            "xdm:id": "CRMID1"
            }
        ]
    },
    "xdm:contextData": [
        {
            "@type":"_xdm.context.additionalParameters;version=1",
            "xdm:data":{
                "xdm:weather":"hot"
            }
        }
    ]
 }],
```

### Boost offers based on the customers propensity to purchase the product being offered

You can boost the score for an offer based on a customer propensity score.

In this example, the instance tenant is *_salesvelocity* and the profile schema contains a range of scores stored in an array:

![](../assets/ranking-example-schema.png)

Given this, for a profile such as:

```
{"_salesvelocity": {"individualScoring": [
                    {"core": {
                            "category":"insurance",
                            "propensityScore": 96.9
                        }},
                    {"core": {
                            "category":"personalLoan",
                            "propensityScore": 45.3
                        }},
                    {"core": {
                            "category":"creditCard",
                            "propensityScore": 78.1
                        }}
                    ]}
}
```

The offers would contain an attribute for *propensityType* which matches the category from the scores:

![](../assets/ranking-example-propensityType.png)

Your ranking formula can then set the priority of each offer to equal the customers *propensityScore* for that *propensityType*. If no score is found, use the static priority set on the offer:

```
let score = (select _Individual_Scoring1 from _salesvelocity.individualScoring
             where _Individual_Scoring1.core.category.equals(offer.characteristics.get("propensityType"), false)).head().core.propensityScore
in if(score.isNotNull(), score, offer.rank.priority)
```
