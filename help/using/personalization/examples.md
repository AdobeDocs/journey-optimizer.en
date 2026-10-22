```yaml
title: Examples of Template Personalization 
description: Journey Optimizer Personalization examples
feature: Personalization
topic: Personalization
role: Data Engineer
level: Experienced
```

# Personalization Examples{#examples}

## Plan-Prescriptions

**Use Case**

A profile contains plans, and each plan includes prescriptions. Prescriptions 
have various states, such as "ready," "recall," or "picked up." We will send a single email to the person, including all prescriptions that are either ready for pick up or recalled.

**Solution**

> [!BEGINTABS]

> [!Rendered Message!]

<div>
<p>Hi Anshul Chauhan,</p>
<p>Here are the prescriptions that are either ready for pick up or have been recalled:</p>

<h4>Health Plan A</h4>
<ul>

<li>
      <strong>Prescription ID:</strong> pres1<br>
      <strong>Name:</strong> Medication A<br>
      <strong>State:</strong> ready
   </li>

<li>
      <strong>Prescription ID:</strong> pres2<br>
      <strong>Name:</strong> Medication B<br>
      <strong>State:</strong> recall
   </li>

</ul>
<h4>Health Plan B</h4>
<ul>

<li>
      <strong>Prescription ID:</strong> pres4<br>
      <strong>Name:</strong> Medication D<br>
      <strong>State:</strong> ready
   </li>

</ul>
</div>

</div>

> [!HTML Template]

```html
<p>Hi {{profile.person.firstName}} {{profile.person.lastName}},</p>
<p>Here are the prescriptions that are either ready for pick up or have been recalled:</p>
{{#each profile.plans as |plan|}}
<h3>{{plan.name}}</h3>
<ul>
   {{#each plan.prescriptions as |prescription|}}
   {%#if prescription.state = "ready" or prescription.state = "recall"%}
   <li>
      <strong>Prescription ID:</strong> {{prescription.prescription_id}}<br>
      <strong>Name:</strong> {{prescription.name}}<br>
      <strong>State:</strong> {{prescription.state}}
   </li>
   {%/if%}
   {{/each}}
</ul>
{{/each}}
```

> [!Profile Data]

```javascript
{
  "profile": {
    "person": {
      "firstName": "Anshul",
      "lastName": "Chauhan"
    },
    "plans": [
      {
        "planId": "plan1",
        "name": "Health Plan A",
        "prescriptions": [
          {
            "prescription_id": "pres1",
            "name": "Medication A",
            "state": "ready"
          },
          {
            "prescription_id": "pres2",
            "name": "Medication B",
            "state": "recall"
          }
        ]
      },
      {
        "planId": "plan2",
        "name": "Health Plan B",
        "prescriptions": [
          {
            "prescription_id": "pres3",
            "name": "Medication C",
            "state": "picked up"
          },
          {
            "prescription_id": "pres4",
            "name": "Medication D",
            "state": "ready"
          }
        ]
      }
    ]
  }
}
```
