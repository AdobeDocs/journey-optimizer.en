---
solution: Journey Optimizer
product: journey optimizer
title: Exclusions list
description: Learn more on exclusions occuring during sending
feature: Reporting
topic: Content Management
role: User
level: Intermediate
exl-id: a34ba1a8-87d5-4f9c-a181-2f49e74e8f09
---
# Exclusion reasons {#exclusion-list}

|Exclusion reason | Error code | Channel | Explanation |
|-|-|-|-|
| RuntimeDispatchError | 050301 | All Channels | Generic exclusion event for any Runtime dispatch error.|
| RuntimeRenderingError | 050302 | All Channels | Generic exclusion event for any Runtime rendering error. |
| NamespaceErrorForExperimentation | 050017 | All Channels | An exclusion event is generated when Namespace in Experiment is different from the namespace of the profile. |
| ExperimentationHoldoutExclusion | 050018 | All Channels | This exclusion event is generated when the qualified Treatment for an Experiment is "Holdout". |
| ExcludedForControlRules | 050002 | All Channels | This exclusion event is generated when delivery of the current message results in violation of control rules, e.g. the number of emails allowed in one month. |
| DirectMailNoVariantDefined | 050062 | DirectMail | An exclusion event is generated when in direct mail variant is not defined. |
| DirectMailNoMessageFoundForTreatment | 050061 | DirectMail  | An exclusion event is generated when the experiment is enabled for the message and no message is found for the qualified treatment. |
| EmailNoConsent | 050101 | Email | An exclusion event is generated when the user has opted out of receiving Marketing emails. |
| Suppressed | 050107 | Email | Exclusion due to one of the Suppression reasons. |
| EmailSuppressed | 050102 | Email | An exclusion event is generated when the target email is suppressed. |
| DomainSuppressed | 050105 | Email | An exclusion event is generated when the domain of the targeted email is suppressed. |
| NotAllowed | 050108 | Email  | An exclusion event is generated when the allowed list is enabled and the targeted email is excluded from the allowed list. |
| EmailNotAllowed | 050103 | Email | An exclusion event is generated when the allowed list is enabled and the targeted email is excluded from the allowed list. |
| DomainNotAllowed | 050106 | Email | An exclusion event is generated when the allowed list is enabled and the domain of the targeted email is excluded from the allowed list.|
| EmailNoSubscriberIdFoundInProfile | 050025 | Email  | An exclusion event is generated when subscriberId is not found in the profile for a subscription email. |
| EmailNoAddressFoundInProfile | 050020 | Email | An exclusion event is generated when the email address is not found in the execution address. |
| EmailNoAddressDefinedInPreset | 050021 | Email | An exclusion event is generated when the execution address is not defined in the configuration. |
| EmailNoVariantDefined | 050026 | Email  | An exclusion event is generated when no variant is defined in the email message. |
| EmailNoMessageFoundForTreatment | 050027 | Email | An exclusion event is generated when the experiment is enabled for the message and no message is found for the qualified treatment. |
| EmailMalformedAddress | 050024 | Email | An exclusion event is generated when the email contains a malformed address. |
| InAppNoVariantDefined | 050041 | InApp | An exclusion event is generated when no variant is defined for InApp message. |
| InAppNoMessageFoundForTreatment | 050042 | InApp | An exclusion event is generated when the experiment is enabled for the message and no message is found for the qualified treatment. |
| PushNoTokenFoundInProfile | 050030 | Push | An exclusion event is generated when the profile does not have push tokens. |
| PushNoValidTokenFoundForApps | 050031 | Push | An exclusion event is generated when no valid token is found for the targeted apps in the configuration. |
| PushMalformedProfile | 050034 | Push | An exclusion event is generated when pushNotificationDetails in the profile is malformed. |
| PushNoConsent | 050111 | Push  | An exclusion event is generated when the user has opted out of marketing push notifications. |
| PushNoApplicationDefinedInPreset | 050033 | Push  | An exclusion event is generated when the configuration does not contain any application to target. |
| PushNoVariantDefined | 050035 | Push  | An exclusion event is generated when no variant is defined. |
| PushNoMessageFoundForTreatment | 050036 | Push | An exclusion event is generated when the experiment is enabled for the message and no message is found for the qualified treatment. |
| SMSNoConsent | 050104 | SMS | An exclusion event is generated when the user has opted out of marketing SMS. |
|SMSFromNumberNotDefinedInPreset| 050152 | SMS  | An exclusion event is generated when "FromNumber" is not defined in the configuration. |
| SMSNoToNumberDefinedInProfile | 050153 | SMS | An exclusion event is generated when "ToNumber" is not defined in the configuration. |
| SMSNoVariantDefined | 050154 | SMS  | An exclusion event is generated when no variant is defined. |
| SMSNoMessageFoundForTreatment | 050155 | SMS | An exclusion event is generated when the experiment is enabled for the message and no message is found for the qualified treatment. |
| WebNoVariantDefined | 050041 | Web | An exclusion event is generated when no variant is defined for a web message. |
| WebNoMessageFoundForTreatment | 050042 | Web | An exclusion event is generated when the experiment is enabled for the message and no message is found for the qualified treatment. |
