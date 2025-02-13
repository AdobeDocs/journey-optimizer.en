---
solution: Journey Optimizer
product: journey optimizer
title: Test your journey
description: Learn how to test your journey
feature: Journeys, Test Profiles
topic: Content Management
role: User
level: Intermediate
keywords: test, journey, check, error, troubleshooting
exl-id: 9937d9b5-df5e-4686-83ac-573c4eba983a
---
# Test your journey{#testing_the_journey}

>[!CONTEXTUALHELP]
>id="ajo_journey_test"
>title="Test your journey"
>abstract="Use test profiles to test your journey before publishing it. This allows you to analyze how individuals flow in the journey and troubleshoot before publication."

Use test profiles to test your journey before publishing it. This mode allows you to run a test of your journey and identify issues using test profiles.

Only test profiles can enter a journey in test mode. You can either create new test profiles or turn existing profiles into test profiles. Learn more about test profiles in [this section](../audience/creating-test-profiles.md). 

>[!NOTE]
>
>Before testing your journey, you must resolve all errors if any. Learn how to check errors before testing in [this section](../building-journeys/troubleshooting.md#checking-for-errors-before-testing).

To use the test mode, follow these steps:

1. To activate the test mode, click the **[!UICONTROL Test mode]** button, located in the top right corner.

    ![](assets/journeytest1.png)

1. If the journey has at least one **Wait** activity, set the **[!UICONTROL Wait time]** parameter to define the time that each wait activity and event timeout will last in test mode. The default time is 10 seconds for waits and event timeouts. This will ensure that you get the test results quickly. 

    ![](assets/journeytest_wait.png)

    >[!NOTE]
    >
    >When a reaction event with a timeout is used in a journey, the wait time default and minimum value is 40 seconds. See [this section](../building-journeys/reaction-events.md).

1. Use the **[!UICONTROL Trigger an event]** button to configure and send events to the journey.

    ![](assets/journeyuctest1.png)

1. Configure the different fields expected. In the **Profile Identifier** field, enter the value of the field used to identify the test profile. It can be the email address, for example. Make sure to send events related to test profiles. See [this section](#firing_events).

    ![](assets/journeyuctest1-bis.png)

1. After the events are received, click the **[!UICONTROL Show log]** button to view the test result and verify them. See [this section](#viewing_logs).

    ![](assets/journeyuctest2.png)

1. If there is any error, deactivate the test mode, modify your journey and test it again. Once tests are done, you can publish your journey. See [this page](../building-journeys/publishing-the-journey.md).

## Important notes {#important_notes}

* In test mode, you can only fire events using the interface. Events cannot be fired from external systems using an API.
* Only individuals flagged as "test profiles" in the Real-time Customer Profile Service are allowed to enter the tested journey. Refer to this [section](../audience/creating-test-profiles.md). 
* The test mode is only available in draft journeys that use a namespace. Test mode needs to check if a person entering the journey is a test profile or not and thus must be able to reach Adobe Experience Platform.
* The maximum number of test profiles than can enter a journey during a test session is 100.
* When you disable the test mode, it empties the journeys from all people who entered it in the past or who are currently in it. It also clears the reporting.
* You can enable/disable the test mode as many times as needed.
* You cannot modify your journey when the test mode is activated. When in test mode, you can directly publish the journey, no need to deactivate the test mode before.
* When reaching a split, the top branch is always chosen. You can reorganize the position of the split branches if you want the test to choose a different path. 
* To optimize performance and prevent obsolete resource usage, all journeys in test mode that have not been triggered for a week will switch back to the **Draft** status.
* Events triggered by the test mode are stored in dedicated datasets. These datasets are labelled as follows: `JOtestmode - <schema of your event>`
* When testing journeys that include multiple events, you must trigger each event in sequence. Sending an event too early (before the first wait node finishes) or too late (after the configured timeout) will discard the event and send the profile to a timeout path. Always confirm any references to event payload fields remain valid by sending the payload within the defined window 


<!--
* Fields from related entities are hidden from the test mode.
-->

## Trigger your events {#firing_events}

>[!CONTEXTUALHELP]
>id="ajo_journey_test_configuration"
>title="Configure the test mode"
>abstract="If your journey contains several events, use the drop-down list to select an event. Then, for each event, configure the fields passed and the execution of the event sending."

Use the **[!UICONTROL Trigger an event]** button to configure an event that will make a person enter the journey.

>[!NOTE]
>
>* When you trigger an event in test mode, a real event is generated, meaning it will also hit other journey listening to this event.
>
>* Ensure that each event in test mode is triggered in the correct order and within the configured waiting window. For example, if there is a 60-second wait, the second event must be triggered only after that 60-second wait has elapsed and before the timeout limit expires.
>

As a prerequisite, you must know which profiles are flagged as test profiles in Adobe Experience Platform. Indeed, the test mode only allows these profiles in the journey and the event must contain an ID. The expected ID depends on the event configuration. It can be an ECID or an email address for example. The value of this key needs to be added in the **Profile Identifier** field. 


If your journey contains several events, use the drop-down list to select an event. Then, for each event, configure the fields passed and the execution of the event sending. The interface helps you pass the right information in the event payload and make sure the information type is correct. The test mode saves the last parameters used in a test session for later use.

![](assets/journeytest4.png)

The interface allows you to pass simple event parameters. If you want to pass collections or other advanced objects in the event, you can click on **[!UICONTROL Code View]** to see the entire code of the payload and modify it. For example, you can copy and paste event information prepared by a technical user.

![](assets/journeytest5.png)

A technical user can also use this interface to compose event payloads and trigger events without having to use a third-party tool.

When clicking the **[!UICONTROL Send]** button, the test begins. The progression of the individual in the journey is represented by a visual flow. The path progressively turns green as the individual moves across the journey. If an error occurs, a warning symbol is displayed on the corresponding step. You can place the cursor on it to display more information about the error and access full details (when available). 

![](assets/journeytest6.png)

When you select a different test profile in the event configuration screen and run the test again, the visual flow is cleared and shows the path of the new individual.

When opening a journey in test, the displayed path corresponds to the last test executed.

## Test mode for rule-based journeys {#test-rule-based}

The test mode is also available for journeys that use a rule-based event. For more information on rule-based events, refer to [this page](../event/about-events.md).

When triggering an event, the **Event configuration** screen allows you to define the event parameters to pass in the test. You can view the event ID condition by clicking the tooltip icon in the top right corner. A tooltip is also available next to each field that is part of the rule evaluation.

![](assets/jo-event8.png)

## Test mode for business events {#test-business}

When using a [business event](../event/about-events.md), use the test mode to trigger a single test profile entrance in the journey, simulate the event and pass the right profile ID. You have to pass the event parameters and the identifier of the test profile that will enter the journey in test. In test mode, there is no "Code view" mode available for journeys based on business events.

Note that when you first trigger a business event, you cannot change the business event definition in the same test session. You can only make the same individual or a different individual enter the journey passing the same or another identifier. If you want to change business event parameters, you must stop and start again test mode.

## View logs {#viewing_logs}

>[!CONTEXTUALHELP]
>id="ajo_journey_test_logs"
>title="Test mode logs"
>abstract="The **Show log** button displays test results in JSON format. These results display the number of individuals inside the journey and their status."

The **[!UICONTROL Show log]** button allows you to view the test results. This page displays the journey's current information in JSON format. A button allows you to copy entire nodes. You need to manually refresh the page to update the journey's test results.

![](assets/journeytest3.png)


>[!NOTE]
>
>In the test logs, in case of an error when calling a third-party system (data source or action), the error code and error response are displayed.

The number of individuals (technically they are called instances) currently inside the journey are displayed. Here is useful information that is displayed for each individual:

* _Id_: the individual's internal ID in the journey. This can be used for debugging purposes.
* _currentstep_: the step where the individual is at in the journey. We recommend adding labels to your activities to identify them more easily.
* _currentstep_ > phase: the status of the individual's journey (running, finished, error or timed out). See below for more information.
* _currentstep_ > _extraInfo_: description of the error and other contextual information.
* _currentstep_ > _fetchErrors_: information on fetch data errors that occurred during this step.
* _externalKeys_: the value for the key formula defined in the event.
* _enrichedData_: the data that the journey has retrieved if the journey uses data sources.
* _transitionHistory_: the list of steps that the individual followed. For events, the payload is displayed.
* _actionExecutionErrors_ : information on the errors that occurred.

Here are the different statuses of an individual's journey:

* _Running_: the individual is currently in the journey.
* _Finished_: the individual is at the end of the journey.
* _Error_: the individual is stopped in the journey because of an error.
* _Timed out_: the individual is stopped in the journey because of a step which took too much time.

When an event is triggered using the test mode, a dataset is automatically generated with the name of the source.

The test mode automatically creates an Experience Event and sends it to Adobe Experience Platform. The name of the source for this experience Event is "Journey Orchestration Test Events".

