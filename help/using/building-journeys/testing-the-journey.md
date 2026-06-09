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
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/J9pg9Bw--ksizTh2itQnPu3uo54eoPj9ocgxwTgrLhE
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: c3f67a94-f1ff-4f5e-bf6f-bc22405930a3
    internal-label: Wait activity
  - id: d08afb72-92f6-4856-88e3-11ec34313c2f
    internal-label: Event configuration
  - id: ebd64fe4-362a-4a1c-9476-b2573ed12a95
    internal-label: Reaction events
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
---
	
# Test your journey{#testing_the_journey}

>[!CONTEXTUALHELP]
>id="ajo_journey_test"
>title="Test your journey"
>abstract="Test profiles let you test your journey before publishing it. This allows you to analyze how individuals flow in the journey and troubleshoot before publication."
>additional-url="https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-dry-run" text="Journey Dry run"

Once you have built your journey, you can test it before publishing. [!DNL Adobe Journey Optimizer] offers "Test mode" as a way to view test profiles as they move along the journey, detecting potential errors before activation. Running quick tests allows you to check that journeys operate correctly so that you can publish them with confidence.

Only test profiles can enter a journey in test mode. You can either create new test profiles or turn existing profiles into test profiles. Learn more about test profiles in [this section](../audience/creating-test-profiles.md). 

Adobe Journeys Optimizer offers two ways to test and validate your journey:

* **[Simulation](simulate-journey.md#test-users)**: Set the journey to **[!UICONTROL Simulation]** and use simulated users (temporary profiles you create or generate on the fly without pre-created profiles in Adobe Experience Platform).

* **[Test mode](#test-profiles)**: Persistent profiles explicitly flagged as test profiles in Adobe Experience Platform. They can be reused across multiple test sessions. This method is recommended for testing with consistent, predefined profile data. [Learn how to create test profiles](../audience/creating-test-profiles.md).

>[!NOTE]
>
>Before testing your journey, you must resolve all errors if any. Learn how to check errors before testing in [this section](../building-journeys/troubleshooting.md). If test profiles fail to progress in test mode, see [troubleshooting test mode transitions](troubleshooting-execution.md#troubleshooting-test-transitions).

## Important notes {#important_notes}

Review these notes before running tests in your journey.

### General limitations

* **Test profiles only** - Only individuals flagged as "test profiles" in the Real-time Customer Profile Service can enter a journey in test mode. [Learn how to create test profiles](../audience/creating-test-profiles.md). 
* **Namespace requirement** - Test mode is available only for draft journeys that use a namespace. Test mode needs to check if a person entering the journey is a test profile or not and thus must be able to reach [!DNL Adobe Experience Platform].
* **Profile limit** - A maximum of 100 test profiles can enter a journey during a single test session.  
* **Event triggering** - Events can only be fired from the interface. Events cannot be fired from external systems using an API.
* **Custom upload audiences** - Journey test mode does not support [custom upload audience](../audience/custom-upload.md) attribute enrichment.

### Behavior during and after testing

* **Disabling test mode** - When you disable test mode, all profiles currently in or previously entered in the journey are removed, and reporting is cleared.  
* **Reactivation flexibility** - You can enable and disable test mode as many times as needed.  
* **Automatic deactivation** -  Journeys that remain inactive in test mode for **over a week** automatically revert to Draft status to optimize performance and prevent obsolete resource usage.
* **Editing and publishing** -  While test mode is active, you cannot modify the journey. You can, however, directly publish the journey, no need to deactivate the test mode before.  

### Execution

* **Split behavior** - When the journey reaches a split, the top branch is always selected. Reorder branches if you want a different path tested.  
* **Event timing** - If the journey includes multiple events, trigger each event in sequence. Sending an event too early (before the first wait node finishes) or too late (after the configured timeout) will discard the event. The profile will then be sent to a timeout path. Always confirm any references to event payload fields remain valid by sending the payload within the defined window. 
* **Active date window** -  Make sure the journey's configured [start and end dates/time](journey-properties.md#dates) window includes the current time when initiating test mode. Otherwise, triggered test events are silently discarded. Learn more about troubleshooting this issue [on this page](troubleshooting-execution.md#troubleshooting-test-transitions).
* **Reaction events** -  For reaction events with a timeout, the minimum and default wait time is 40 seconds.  
* **Test datasets** - Events triggered in test mode are stored in dedicated datasets labeled as follows: `JOtestmode - <schema of your event>`
* **Shared infrastructure** - Test Mode runs on the same infrastructure as production. During high traffic periods, you may notice delays in email sends or event processing. In this case, check platform traffic dashboards or retry your tests during off-peak hours.

<!--
* Fields from related entities are hidden from the test mode.
-->

## Activate the test mode

Use the **[!UICONTROL Test mode]** method when you want to test your journey with pre-existing test profiles that you have already created in Adobe Experience Platform.

1. To activate the test mode, click the **[!UICONTROL Simulate]** button, and select **[!UICONTROL Test mode]**.

    ![Test mode button in journey interface](assets/journeytest1.png)

1. If the journey has at least one **Wait** activity, set the **[!UICONTROL Wait time]** parameter to define the time that each wait activity and event timeout will last in test mode. The default time is 10 seconds for waits and event timeouts. This will ensure that you get the test results quickly. 

    ![Wait time parameter configuration in test mode](assets/journeytest_wait.png)

    >[!NOTE]
    >
    >When a reaction event with a timeout is used in a journey, the wait time default and minimum value is 40 seconds. See [this section](../building-journeys/reaction-events.md).

1. Use the **[!UICONTROL Trigger an event]** button to configure and send events to the journey.

    ![Trigger an event button in test mode](assets/journeyuctest1.png)

1. Configure the different fields expected. In the **Profile Identifier** field, enter the value of the field used to identify the test profile. It can be the email address, for example. Make sure to send events related to test profiles. See [this section](#firing_events).

    ![Event configuration fields with Profile Identifier input](assets/journeyuctest1-bis.png)

1. After the events are received, click the **[!UICONTROL Show log]** button to view the test result and verify them. See [this section](#viewing_logs).

    ![Show log button to view test results](assets/journeyuctest2.png)

1. If there is any error, deactivate the test mode, modify your journey and test it again. Once tests are done, you can publish your journey. See [this page](../building-journeys/publish-journey.md).

## Worked example: validate a simple journey {#test-walkthrough}

The following example walks through testing a journey that starts with a unitary event, sends an email, waits 10 minutes, then sends a push notification.

To validate the journey end to end:

1. Activate test mode by clicking **[!UICONTROL Test mode]** in the top-right corner. The canvas switches to test mode and a **[!UICONTROL Trigger an event]** button appears.
1. Set **[!UICONTROL Wait time]** to **10 seconds** so the wait node completes quickly during testing.
1. Click **[!UICONTROL Trigger an event]**, select your event, and enter a test profile identifier (for example, the email address of a profile flagged as a test profile in Adobe Experience Platform).
1. Click **[!UICONTROL Send]**. The visual flow appears on the canvas and turns green as the profile progresses through each step.
1. Click **[!UICONTROL Show log]** and confirm the following in the JSON output:
   * `currentstep` matches the activity you expect the profile to be at.
   * `phase` shows `running` while the profile is in a wait node, and `finished` when it reaches the end.
   * No `actionExecutionErrors` entries are present.
1. After 10 seconds, refresh the log. The profile should have advanced past the wait node and triggered the push action.
1. When all steps show `finished` and no errors are logged, deactivate test mode and publish the journey.

>[!TIP]
>
>If the profile does not appear in the log at all, check that:
>* The profile identifier you entered is flagged as a test profile in [!DNL Adobe Experience Platform].
>* The journey's configured start and end dates include the current time. Events triggered outside this window are silently discarded. [Learn more](troubleshooting-execution.md#troubleshooting-test-transitions).

## Trigger your events {#firing_events}

>[!CONTEXTUALHELP]
>id="ajo_journey_test_configuration"
>title="Configure the test mode"
>abstract="If a journey contains several events, the drop-down list is used to select an event. For each event, the fields passed and the execution of the event sending are configured."

Use the **[!UICONTROL Trigger an event]** button to configure an event that will make a person enter the journey.


### Prerequisites {#trigger-events-prerequisites}

As a prerequisite, you must know which profiles are flagged as test profiles in [!DNL Adobe Experience Platform]. Indeed, the test mode only allows these profiles in the journey.

The event must contain an ID. The expected ID depends on the event configuration. It can be an ECID or an email address for example. The value of this key needs to be added in the **Profile Identifier** field.  

If your journey fails to enable test mode with error `ERR_MODEL_RULES_16`, ensure the event used includes an [identity namespace](../audience/get-started-identity.md) when using a channel action.

The identity namespace is used to uniquely identify the test profiles. For example, if email is used to identify the test profiles, the identity namespace **Email** should be selected. If the unique identifier is the phone number, then the identity namespace **Phone** should be selected.

>[!NOTE]
>
>* When you trigger an event in test mode, a real event is generated, meaning it will also hit other journeys listening to this event.
>
>* Ensure that each event in test mode is triggered in the correct order and within the configured waiting window. For example, if there is a 60-second wait, the second event must be triggered only after that 60-second wait has elapsed and before the timeout limit expires.
>

### Event configuration {#trigger-events-configuration}

If your journey contains several events, use the drop-down list to select an event. Then, for each event, configure the fields passed and the execution of the event sending. The interface helps you pass the right information in the event payload and ensures the information type is correct. Test mode saves the last parameters used in a test session for later use.

![Event configuration interface with fields and drop-down for event selection](assets/journeytest4.png)

The interface allows you to pass simple event parameters. If you want to pass collections or other advanced objects in the event, you can select **[!UICONTROL Code View]** to see the entire code of the payload and modify it. For example, you can copy and paste event information prepared by a technical user.

![Code view of event payload in JSON format for advanced configuration](assets/journeytest5.png)

A technical user can also use this interface to compose event payloads and trigger events without having to use a third-party tool.

When clicking the **[!UICONTROL Send]** button, the test begins. The progression of the individual in the journey is represented by a visual flow. The path progressively turns green as the individual moves across the journey. If an error occurs, a warning symbol is displayed on the corresponding step. You can place the cursor on it to display more information about the error and access full details (when available). 

![Journey test visual flow showing profile progress and any errors](assets/journeytest6.png)

When you select a different test profile in the event configuration screen and run the test again, the visual flow is cleared and shows the path of the new individual.

When opening a journey in test, the displayed path corresponds to the last test executed.

## Test mode for rule-based journeys {#test-rule-based}

The test mode is also available for journeys that use a rule-based event. For more information on rule-based events, refer to [this page](../event/about-events.md).

When triggering an event, the **Event configuration** screen allows you to define the event parameters to pass in the test. You can view the event ID condition by clicking the tooltip icon in the top right corner. A tooltip is also available next to each field that is part of the rule evaluation.

![Event configuration screen with rule evaluation tooltips](assets/jo-event8.png)

## Test mode for business events {#test-business}

When using a [business event](../event/about-events.md), use the test mode to trigger a single test profile entrance in the journey, simulate the event and pass the right profile ID. You have to pass the event parameters and the identifier of the test profile that will enter the journey in test. In test mode, there is no "Code view" mode available for journeys based on business events.

Note that when you first trigger a business event, you cannot change the business event definition in the same test session. You can only make the same individual or a different individual enter the journey passing the same or another identifier. If you want to change business event parameters, you must stop and start again test mode.

## View logs {#viewing_logs}

>[!CONTEXTUALHELP]
>id="ajo_journey_test_logs"
>title="Test mode logs"
>abstract="The **Show log** button displays test results in JSON format. These results display the number of individuals inside the journey and their status."

The **[!UICONTROL Show log]** button allows you to view the test results. This page displays the journey's current information in JSON format. A button allows you to copy entire nodes. You need to manually refresh the page to update the journey's test results.

![Test logs displaying journey execution results in JSON format](assets/journeytest3.png)


>[!NOTE]
>
>In the test logs, in case of an error when calling a third-party system (data source or action), the error code and error response are displayed.

The number of individuals (technically called instances) currently inside the journey are displayed. The following information is displayed for each individual:

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

The test mode automatically creates an Experience Event and sends it to [!DNL Adobe Experience Platform]. The name of the source for this experience Event is "Journey Orchestration Test Events".

+++AI Assistant — Page context

- **TL;DR:** This page explains how to use Test mode in Adobe Journey Optimizer to validate a journey with persistent test profiles before publishing, including activating test mode, triggering events, reading logs, and handling business and rule-based events.

**Intents:**
- Activate Test mode on a draft journey to validate it with pre-existing AEP test profiles
- Configure and trigger events for test profiles using the Trigger an event interface
- Override Wait activity durations in test mode to accelerate journey progression
- Read and interpret the Show log JSON output to verify profile progression and identify errors
- Test rule-based journeys and business event journeys in test mode
- Understand the limitations and behavioral differences of Test mode compared to Simulation

**Glossary:**
- **Test mode**: A journey validation state that allows persistent AEP test profiles to traverse a draft journey before it is published *(product-specific)*
- **Test profiles**: Profiles explicitly flagged as test profiles in the Adobe Experience Platform Real-time Customer Profile Service; the only profile type permitted to enter a journey in test mode *(product-specific)*
- **Visual flow**: The canvas representation that turns green to show the path a test profile has followed through the journey
- **Show log**: A test mode feature that displays journey execution state in JSON format for each test profile instance *(product-specific)*
- **Journey Orchestration Test Events**: The source name under which test mode experience events are stored in Adobe Experience Platform

**Guardrails:**
- Only profiles flagged as test profiles in AEP can enter a journey in test mode
- Test mode requires the journey to use a namespace to verify test profile identity
- Maximum 100 test profiles per single test session
- Events can only be triggered from the test mode UI; external API triggering is not supported
- Custom upload audience attribute enrichment is not supported in test mode
- Journeys inactive in test mode for over a week automatically revert to Draft status
- Journey edits are blocked while test mode is active, but direct publishing is allowed
- At a split, the top branch is always selected; reorder branches to test different paths
- Reaction event timeout minimum and default wait time is 40 seconds
- Events sent outside the journey's configured start/end date window are silently discarded
- Disabling test mode removes all profiles from the journey and clears reporting

**Terminology:**
- Canonical name: Test mode — Acronym: none — variants: test mode, journey test mode
- Canonical name: Test profiles — Acronym: none — variants: test users (Simulation UI label only)
- Synonyms: "Show log" = test results log; "visual flow" = canvas path visualization
- Do not confuse: "Test mode" ≠ "Simulation" — Test mode uses persistent AEP test profiles; Simulation uses temporary simulated users generated on the fly

**FAQ:**
- **Q: Who can enter a journey in test mode?** — Only profiles explicitly flagged as test profiles in the Adobe Experience Platform Real-time Customer Profile Service.
- **Q: How many test profiles can run in a single test session?** — A maximum of 100 test profiles per test session.
- **Q: What happens when I disable test mode?** — All profiles currently in or previously entered in the journey are removed and reporting is cleared.
- **Q: Can I edit a journey while test mode is active?** — No. The journey cannot be modified while test mode is active, but you can publish it directly without deactivating test mode first.
- **Q: Why are my test events being silently discarded?** — Events triggered outside the journey's configured active date/time window are silently discarded. Verify the journey start and end dates include the current time.
- **Q: What does the phase field in the test log indicate?** — It shows the profile's current status: running (active in journey), finished (reached end), error (stopped due to error), or timed out (stopped due to timeout).

+++
