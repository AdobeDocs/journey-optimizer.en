---
title: Deduplication of decision items in code-based implementations
description: This page shows how to apply deduplication to your decisioning requests in your Journey Optimizer code-based implementation.
feature: Code-based Experiences
topic: Content Management
role: Developer
level: Experienced
hide: yes
hidefromtoc: yes
exl-id: f9477611-b792-4b28-8ec2-6bbea2fa3328
---
# Decisioning in code-based experience implementations

When using Decisioning in code-based experiences, consider adding the following flags to your client implementation in the cases described below.

## Testing code-based experiences using decisions {#code-based-test-decisions}

Currently you cannot simulate content from the user interface in a [code-based experience](create-code-based.md) campaign or journey using decisions.

As a workaround, you can test decisioning after publishing your campaign by adding the `dryRun` flag into the XDM event `data` block in your client implementation:

    ```
    {
        "data": {
            "__adobe": {
                "ajo": {
                    "dryRun": true
                }
            }
        }
    }
    ```

>[!CAUTION]
>
>Adding the `dryRun` flag to your request will prevent feedback to be captured for reporting and frequency counters from being added to.

## Deduplication of decision items in code-based implementations {#code-based-decisioning-deduplication}

When using [decision policies](../experience-decisioning/create-decision.md) in your code-based experiences, learn how to apply deduplication to your decisioning requests in your client implementation.

Decisioning requests (through Konductor) accept the deduplication flag, which handles uniqueness of decision items in a single request comprised of multiple decision policies or placements.

### Deduplication logic {#deduplication-logic}

For any decisioning request, you can have one or more decision policies/placements based on setup.

* For a **single** decision policy and placement in a request, all items in the response are unique (by default). Two decision items cannot be the same in a single request.

* For **multiple** decision policies/placements in a request:

  * If `allowDuplicateDecisionItems` is set to `false`: all items in the response are unique (regardless of which message/decision policy/placement the item is for).

  * If `allowDuplicateDecisionItems` is set to `true` (default): items in the response can be duplicate (if multiple messages/decision policies/placements qualify for the same decision item for that request).

### Apply deduplication in a request {#deduplication-in-request}

By default, the deduplication flag is set to `true` (it is not passed).

In a Konductor request, you can pass the deduplication flag if you want unique elements in the response. In that case, set it to `false`.

```
{
    "data": {
        "__adobe": {
            "ajo": {
                "allowDuplicateDecisionItems": false
            }
        }
    }
}
```

+++Decisioning sample request

```
curl --location 'https://edge-int.adobedc.net/ee/v1/interact?configId=2f21d344-b69f-4a4f-98e8-000282fc9552' \
--header 'Content-Type: application/json' \
--data-raw '{
    "events": [
        {
            "query": {
                "personalization": {
                    "schemas": [
                        "https://ns.adobe.com/personalization/html-content-item"
                    ],
                    "surfaces": [
                        "https://www.adobe.com/san/placement/header",
                        "https://www.adobe.com/san/placement/footer"
                    ]
                }
            },
            "xdm": {
                "identityMap": {
                    "Email": [
                        {
                            "id": "cmk-exd-user01-deleted@adobe.com",
                            "primary": true
                        }
                    ]
                }
            },
            "data": {
                "__adobe":{
                    "ajo":{
                        "allowDuplicateDecisionItems": false
                    }
                }       
            }
        }
    ]
}'
```

+++

### Deduplication response {#deduplication-response}

Let's say you have the same decision policy with header and footer placement in a single request.

* Decisioning returns two propositions.

* If `itemId-X` is the single decision item that qualifies for both decision policy and placement combination:

  * If `allowDuplicateDecisionItems` is `true`(default): `itemId-X` is returned back for both propositions in a single response.

  * If `allowDuplicateDecisionItems` is `false`:

    * `itemId-X` is returned back for the first proposition.

    * The fallback decision item (also unique) or an empty decision item is passed for the second proposition.

+++Decisioning sample response (`allowDuplicateDecisionItems` = `true`)

```
{
    "requestId": "b40170e9-7d31-4242-adcc-18063d6b1d9e",
    "handle": [
        {
            "payload": [
                {
                    "id": "d97f102c-bdae-4ed7-aff6-622d73e3db3d",
                    "scope": "https://www.adobe.com/san/placement/header",
                    "scopeDetails": {
                        "decisionProvider": "AJO",
                        "correlationID": "3cc4ee00-bb76-4eaa-94b6-9b9be2c53e3a-0",
                        "characteristics": {
                            "eventToken": "eyJtZXNzYWdlRXhlY3V0aW9uIjp7Im1lc3NhZ2VFeGVjdXRpb25JRCI6IlVFOkluYm91bmQiLCJtZXNzYWdlSUQiOiJmYWM4YzVmZi1mYWNlLTRkOWItYmEzYi0yYzJjZTEyYzBjODYiLCJtZXNzYWdlUHVibGljYXRpb25JRCI6IjNjYzRlZTAwLWJiNzYtNGVhYS05NGI2LTliOWJlMmM1M2UzYSIsIm1lc3NhZ2VUeXBlIjoibWFya2V0aW5nIiwiY2FtcGFpZ25JRCI6ImUzYmJlZmZkLTZjYjItNGEwMy1iMjRhLTk1YzQ5ZjBkZjRlNCIsImNhbXBhaWduVmVyc2lvbklEIjoiZDlmMTMwNjAtZGVhNC00MTE1LTk5YzMtOGZjMTRjMWFiNTFiIiwiY2FtcGFpZ25BY3Rpb25JRCI6ImE1NmE0OTIxLWJjMjQtNGRjMC04Nzk3LTA2NmU4YzE0NTM5YiJ9LCJtZXNzYWdlUHJvZmlsZSI6eyJtZXNzYWdlUHJvZmlsZUlEIjoiYmQxMDEzNGMtNjBkMS00NjZiLWEwYWMtOWQ0MzdmNmY5YTczIiwiY2hhbm5lbCI6eyJfaWQiOiJodHRwczovL25zLmFkb2JlLmNvbS94ZG0vY2hhbm5lbHMvY29kZSIsIl90eXBlIjoiaHR0cHM6Ly9ucy5hZG9iZS5jb20veGRtL2NoYW5uZWwtdHlwZXMvY29kZSJ9fX0=",
                            "subPropositions": "W3siaWQiOiI4ZmMzMDBjYy1iMTg5LTQ2MTUtYmY0OC03NjIwMjZkMjlmMWYiLCJzY29wZSI6Imh0dHBzOi8vd3d3LmFkb2JlLmNvbS9zYW4vcGxhY2VtZW50L2hlYWRlciIsInNjb3BlRGV0YWlscyI6eyJkZWNpc2lvblByb3ZpZGVyIjoiRVhEIiwiY29ycmVsYXRpb25JRCI6IjNjYzRlZTAwLWJiNzYtNGVhYS05NGI2LTliOWJlMmM1M2UzYS0wIiwic3RyYXRlZ2llcyI6W3sic3RyYXRlZ3lJRCI6IjlhOTRjZjhjLTNkZjItNDE2NS1hMzRiLTIxNzBlMjg2YmUzMiIsInN0ZXAiOiJkZWNpc2lvblBvbGljeSJ9LHsic3RyYXRlZ3lJRCI6Imh0dHBzOi8vd3d3LmFkb2JlLmNvbS9zYW4vcGxhY2VtZW50L2hlYWRlciIsInN0ZXAiOiJwbGFjZW1lbnQifV0sInJhbmsiOjEsImFjdGl2aXR5Ijp7ImlkIjoiZTNiYmVmZmQtNmNiMi00YTAzLWIyNGEtOTVjNDlmMGRmNGU0I2E1NmE0OTIxLWJjMjQtNGRjMC04Nzk3LTA2NmU4YzE0NTM5YiIsInByaW9yaXR5IjowLCJtYXRjaGVkU3VyZmFjZXMiOlsiaHR0cHM6Ly93d3cuYWRvYmUuY29tL3Nhbi9wbGFjZW1lbnQvaGVhZGVyIl19fSwiaXRlbXMiOlt7ImlkIjoiZHBzOmM3MjI1YzNmYWMxNGUzMDBjYTNkZTlmY2I2ZDk4NTI0YjM5NTQ4YzFmYzFlYmQ2OToxOThkM2I5NDczZDRjYzQ3IiwiZXRhZyI6IjciLCJuYW1lIjoidGVzdFNhbi1tYW51YWxGYWxsYmFjay1vZmZlcjAxIiwic2NvcmUiOjExLjAsIml0ZW1TZWxlY3Rpb24iOnsic2VsZWN0aW9uRGV0YWlsIjp7InN0cmF0ZWd5SUQiOiJkcHM6c2VsZWN0aW9uLXN0cmF0ZWd5OjFhMGUzOTY4NzJlOWZiMWUiLCJzdHJhdGVneU5hbWUiOiJ0ZXN0U2FuLW1hbnVhbEZhbGxiYWNrLXN0cmF0ZWd5MTAwIiwic2VsZWN0aW9uVHlwZSI6InNlbGVjdGlvblN0cmF0ZWd5IiwidmVyc2lvbiI6Ijc0NUYzN0MzNUU0Qjc3NkUwQTQ5NDIxQkBBZG9iZU9yZzo2MzM5NzRmNC1lNTRlLTQyZjMtYjk3NC1mNGU1NGVjMmYzYmU6NThlNjE0MTItZTExOS00Mjg4LWJiZGEtYmQ1NGQ1MDgxNjVmIn0sInJhbmtpbmdEZXRhaWwiOnsic3RlcCI6InByaW9yaXR5In19LCJ0b2tlbiI6IitsckV1NWtHdnkrRXVYRFZ1K0VMWHcifV19XQ=="
                        },
                        "rank": 1,
                        "activity": {
                            "id": "e3bbeffd-6cb2-4a03-b24a-95c49f0df4e4#a56a4921-bc24-4dc0-8797-066e8c14539b",
                            "priority": 0,
                            "matchedSurfaces": [
                                "https://www.adobe.com/san/placement/header"
                            ]
                        }
                    },
                    "items": [
                        {
                            "id": "f37463f7-d23b-4ef1-b412-de1ac127efb9",
                            "schema": "https://ns.adobe.com/personalization/html-content-item",
                            "data": {
                                "content": "\nitemId: dps:c7225c3fac14e300ca3de9fcb6d98524b39548c1fc1ebd69:198d3b9473d4cc47\nitemName: testSan-manualFallback-offer01\ntrackingToken: +lrEu5kGvy+EuXDVu+ELXw\n"
                            }
                        }
                    ]
                },
                {
                    "id": "e1de0998-44d6-435d-8974-1d5175a845ea",
                    "scope": "https://www.adobe.com/san/placement/footer",
                    "scopeDetails": {
                        "decisionProvider": "AJO",
                        "correlationID": "3cc4ee00-bb76-4eaa-94b6-9b9be2c53e3a-0",
                        "characteristics": {
                            "eventToken": "eyJtZXNzYWdlRXhlY3V0aW9uIjp7Im1lc3NhZ2VFeGVjdXRpb25JRCI6IlVFOkluYm91bmQiLCJtZXNzYWdlSUQiOiJmYWM4YzVmZi1mYWNlLTRkOWItYmEzYi0yYzJjZTEyYzBjODYiLCJtZXNzYWdlUHVibGljYXRpb25JRCI6IjNjYzRlZTAwLWJiNzYtNGVhYS05NGI2LTliOWJlMmM1M2UzYSIsIm1lc3NhZ2VUeXBlIjoibWFya2V0aW5nIiwiY2FtcGFpZ25JRCI6ImUzYmJlZmZkLTZjYjItNGEwMy1iMjRhLTk1YzQ5ZjBkZjRlNCIsImNhbXBhaWduVmVyc2lvbklEIjoiZDlmMTMwNjAtZGVhNC00MTE1LTk5YzMtOGZjMTRjMWFiNTFiIiwiY2FtcGFpZ25BY3Rpb25JRCI6ImE1NmE0OTIxLWJjMjQtNGRjMC04Nzk3LTA2NmU4YzE0NTM5YiJ9LCJtZXNzYWdlUHJvZmlsZSI6eyJtZXNzYWdlUHJvZmlsZUlEIjoiMGI4NTYxMzAtNDZiNy00OTQ1LTgwYTAtZjM2MGUzMjhlMjllIiwiY2hhbm5lbCI6eyJfaWQiOiJodHRwczovL25zLmFkb2JlLmNvbS94ZG0vY2hhbm5lbHMvY29kZSIsIl90eXBlIjoiaHR0cHM6Ly9ucy5hZG9iZS5jb20veGRtL2NoYW5uZWwtdHlwZXMvY29kZSJ9fX0=",
                            "subPropositions": "W3siaWQiOiI1NzViZDY3My0yMTQ1LTQ2MzAtYjQ1Yy1iNDAwMGUxMzI1NmMiLCJzY29wZSI6Imh0dHBzOi8vd3d3LmFkb2JlLmNvbS9zYW4vcGxhY2VtZW50L2Zvb3RlciIsInNjb3BlRGV0YWlscyI6eyJkZWNpc2lvblByb3ZpZGVyIjoiRVhEIiwiY29ycmVsYXRpb25JRCI6IjNjYzRlZTAwLWJiNzYtNGVhYS05NGI2LTliOWJlMmM1M2UzYS0wIiwic3RyYXRlZ2llcyI6W3sic3RyYXRlZ3lJRCI6IjlhOTRjZjhjLTNkZjItNDE2NS1hMzRiLTIxNzBlMjg2YmUzMiIsInN0ZXAiOiJkZWNpc2lvblBvbGljeSJ9LHsic3RyYXRlZ3lJRCI6Imh0dHBzOi8vd3d3LmFkb2JlLmNvbS9zYW4vcGxhY2VtZW50L2Zvb3RlciIsInN0ZXAiOiJwbGFjZW1lbnQifV0sInJhbmsiOjEsImFjdGl2aXR5Ijp7ImlkIjoiZTNiYmVmZmQtNmNiMi00YTAzLWIyNGEtOTVjNDlmMGRmNGU0I2E1NmE0OTIxLWJjMjQtNGRjMC04Nzk3LTA2NmU4YzE0NTM5YiIsInByaW9yaXR5IjowLCJtYXRjaGVkU3VyZmFjZXMiOlsiaHR0cHM6Ly93d3cuYWRvYmUuY29tL3Nhbi9wbGFjZW1lbnQvZm9vdGVyIl19fSwiaXRlbXMiOltdfV0="
                        },
                        "rank": 1,
                        "activity": {
                            "id": "e3bbeffd-6cb2-4a03-b24a-95c49f0df4e4#a56a4921-bc24-4dc0-8797-066e8c14539b",
                            "priority": 0,
                            "matchedSurfaces": [
                                "https://www.adobe.com/san/placement/footer"
                            ]
                        }
                    },
                    "items": [
                        {
                            "id": "f37463f7-d23b-4ef1-b412-de1ac127efb9",
                            "schema": "https://ns.adobe.com/personalization/html-content-item",
                            "data": {
                                "content": "\nitemId: dps:c7225c3fac14e300ca3de9fcb6d98524b39548c1fc1ebd69:198d3b9473d4cc47\nitemName: testSan-manualFallback-offer01\ntrackingToken: +lrEu5kGvy+EuXDVu+ELXw\n"
                            }
                        }
                    ]
                }
            ],
            "type": "personalization:decisions",
            "eventIndex": 0
        }
    ]
}
```

+++

+++Decisioning sample response (`allowDuplicateDecisionItems` = `false`)

```
{
    "requestId": "b40170e9-7d31-4242-adcc-18063d6b1d9e",
    "handle": [
        {
            "payload": [
                {
                    "id": "d97f102c-bdae-4ed7-aff6-622d73e3db3d",
                    "scope": "https://www.adobe.com/san/placement/header",
                    "scopeDetails": {
                        "decisionProvider": "AJO",
                        "correlationID": "3cc4ee00-bb76-4eaa-94b6-9b9be2c53e3a-0",
                        "characteristics": {
                            "eventToken": "eyJtZXNzYWdlRXhlY3V0aW9uIjp7Im1lc3NhZ2VFeGVjdXRpb25JRCI6IlVFOkluYm91bmQiLCJtZXNzYWdlSUQiOiJmYWM4YzVmZi1mYWNlLTRkOWItYmEzYi0yYzJjZTEyYzBjODYiLCJtZXNzYWdlUHVibGljYXRpb25JRCI6IjNjYzRlZTAwLWJiNzYtNGVhYS05NGI2LTliOWJlMmM1M2UzYSIsIm1lc3NhZ2VUeXBlIjoibWFya2V0aW5nIiwiY2FtcGFpZ25JRCI6ImUzYmJlZmZkLTZjYjItNGEwMy1iMjRhLTk1YzQ5ZjBkZjRlNCIsImNhbXBhaWduVmVyc2lvbklEIjoiZDlmMTMwNjAtZGVhNC00MTE1LTk5YzMtOGZjMTRjMWFiNTFiIiwiY2FtcGFpZ25BY3Rpb25JRCI6ImE1NmE0OTIxLWJjMjQtNGRjMC04Nzk3LTA2NmU4YzE0NTM5YiJ9LCJtZXNzYWdlUHJvZmlsZSI6eyJtZXNzYWdlUHJvZmlsZUlEIjoiYmQxMDEzNGMtNjBkMS00NjZiLWEwYWMtOWQ0MzdmNmY5YTczIiwiY2hhbm5lbCI6eyJfaWQiOiJodHRwczovL25zLmFkb2JlLmNvbS94ZG0vY2hhbm5lbHMvY29kZSIsIl90eXBlIjoiaHR0cHM6Ly9ucy5hZG9iZS5jb20veGRtL2NoYW5uZWwtdHlwZXMvY29kZSJ9fX0=",
                            "subPropositions": "W3siaWQiOiI4ZmMzMDBjYy1iMTg5LTQ2MTUtYmY0OC03NjIwMjZkMjlmMWYiLCJzY29wZSI6Imh0dHBzOi8vd3d3LmFkb2JlLmNvbS9zYW4vcGxhY2VtZW50L2hlYWRlciIsInNjb3BlRGV0YWlscyI6eyJkZWNpc2lvblByb3ZpZGVyIjoiRVhEIiwiY29ycmVsYXRpb25JRCI6IjNjYzRlZTAwLWJiNzYtNGVhYS05NGI2LTliOWJlMmM1M2UzYS0wIiwic3RyYXRlZ2llcyI6W3sic3RyYXRlZ3lJRCI6IjlhOTRjZjhjLTNkZjItNDE2NS1hMzRiLTIxNzBlMjg2YmUzMiIsInN0ZXAiOiJkZWNpc2lvblBvbGljeSJ9LHsic3RyYXRlZ3lJRCI6Imh0dHBzOi8vd3d3LmFkb2JlLmNvbS9zYW4vcGxhY2VtZW50L2hlYWRlciIsInN0ZXAiOiJwbGFjZW1lbnQifV0sInJhbmsiOjEsImFjdGl2aXR5Ijp7ImlkIjoiZTNiYmVmZmQtNmNiMi00YTAzLWIyNGEtOTVjNDlmMGRmNGU0I2E1NmE0OTIxLWJjMjQtNGRjMC04Nzk3LTA2NmU4YzE0NTM5YiIsInByaW9yaXR5IjowLCJtYXRjaGVkU3VyZmFjZXMiOlsiaHR0cHM6Ly93d3cuYWRvYmUuY29tL3Nhbi9wbGFjZW1lbnQvaGVhZGVyIl19fSwiaXRlbXMiOlt7ImlkIjoiZHBzOmM3MjI1YzNmYWMxNGUzMDBjYTNkZTlmY2I2ZDk4NTI0YjM5NTQ4YzFmYzFlYmQ2OToxOThkM2I5NDczZDRjYzQ3IiwiZXRhZyI6IjciLCJuYW1lIjoidGVzdFNhbi1tYW51YWxGYWxsYmFjay1vZmZlcjAxIiwic2NvcmUiOjExLjAsIml0ZW1TZWxlY3Rpb24iOnsic2VsZWN0aW9uRGV0YWlsIjp7InN0cmF0ZWd5SUQiOiJkcHM6c2VsZWN0aW9uLXN0cmF0ZWd5OjFhMGUzOTY4NzJlOWZiMWUiLCJzdHJhdGVneU5hbWUiOiJ0ZXN0U2FuLW1hbnVhbEZhbGxiYWNrLXN0cmF0ZWd5MTAwIiwic2VsZWN0aW9uVHlwZSI6InNlbGVjdGlvblN0cmF0ZWd5IiwidmVyc2lvbiI6Ijc0NUYzN0MzNUU0Qjc3NkUwQTQ5NDIxQkBBZG9iZU9yZzo2MzM5NzRmNC1lNTRlLTQyZjMtYjk3NC1mNGU1NGVjMmYzYmU6NThlNjE0MTItZTExOS00Mjg4LWJiZGEtYmQ1NGQ1MDgxNjVmIn0sInJhbmtpbmdEZXRhaWwiOnsic3RlcCI6InByaW9yaXR5In19LCJ0b2tlbiI6IitsckV1NWtHdnkrRXVYRFZ1K0VMWHcifV19XQ=="
                        },
                        "rank": 1,
                        "activity": {
                            "id": "e3bbeffd-6cb2-4a03-b24a-95c49f0df4e4#a56a4921-bc24-4dc0-8797-066e8c14539b",
                            "priority": 0,
                            "matchedSurfaces": [
                                "https://www.adobe.com/san/placement/header"
                            ]
                        }
                    },
                    "items": [
                        {
                            "id": "f37463f7-d23b-4ef1-b412-de1ac127efb9",
                            "schema": "https://ns.adobe.com/personalization/html-content-item",
                            "data": {
                                "content": "\nitemId: dps:c7225c3fac14e300ca3de9fcb6d98524b39548c1fc1ebd69:198d3b9473d4cc47\nitemName: testSan-manualFallback-offer01\ntrackingToken: +lrEu5kGvy+EuXDVu+ELXw\n"
                            }
                        }
                    ]
                },
                {
                    "id": "e1de0998-44d6-435d-8974-1d5175a845ea",
                    "scope": "https://www.adobe.com/san/placement/footer",
                    "scopeDetails": {
                        "decisionProvider": "AJO",
                        "correlationID": "3cc4ee00-bb76-4eaa-94b6-9b9be2c53e3a-0",
                        "characteristics": {
                            "eventToken": "eyJtZXNzYWdlRXhlY3V0aW9uIjp7Im1lc3NhZ2VFeGVjdXRpb25JRCI6IlVFOkluYm91bmQiLCJtZXNzYWdlSUQiOiJmYWM4YzVmZi1mYWNlLTRkOWItYmEzYi0yYzJjZTEyYzBjODYiLCJtZXNzYWdlUHVibGljYXRpb25JRCI6IjNjYzRlZTAwLWJiNzYtNGVhYS05NGI2LTliOWJlMmM1M2UzYSIsIm1lc3NhZ2VUeXBlIjoibWFya2V0aW5nIiwiY2FtcGFpZ25JRCI6ImUzYmJlZmZkLTZjYjItNGEwMy1iMjRhLTk1YzQ5ZjBkZjRlNCIsImNhbXBhaWduVmVyc2lvbklEIjoiZDlmMTMwNjAtZGVhNC00MTE1LTk5YzMtOGZjMTRjMWFiNTFiIiwiY2FtcGFpZ25BY3Rpb25JRCI6ImE1NmE0OTIxLWJjMjQtNGRjMC04Nzk3LTA2NmU4YzE0NTM5YiJ9LCJtZXNzYWdlUHJvZmlsZSI6eyJtZXNzYWdlUHJvZmlsZUlEIjoiMGI4NTYxMzAtNDZiNy00OTQ1LTgwYTAtZjM2MGUzMjhlMjllIiwiY2hhbm5lbCI6eyJfaWQiOiJodHRwczovL25zLmFkb2JlLmNvbS94ZG0vY2hhbm5lbHMvY29kZSIsIl90eXBlIjoiaHR0cHM6Ly9ucy5hZG9iZS5jb20veGRtL2NoYW5uZWwtdHlwZXMvY29kZSJ9fX0=",
                            "subPropositions": "W3siaWQiOiI1NzViZDY3My0yMTQ1LTQ2MzAtYjQ1Yy1iNDAwMGUxMzI1NmMiLCJzY29wZSI6Imh0dHBzOi8vd3d3LmFkb2JlLmNvbS9zYW4vcGxhY2VtZW50L2Zvb3RlciIsInNjb3BlRGV0YWlscyI6eyJkZWNpc2lvblByb3ZpZGVyIjoiRVhEIiwiY29ycmVsYXRpb25JRCI6IjNjYzRlZTAwLWJiNzYtNGVhYS05NGI2LTliOWJlMmM1M2UzYS0wIiwic3RyYXRlZ2llcyI6W3sic3RyYXRlZ3lJRCI6IjlhOTRjZjhjLTNkZjItNDE2NS1hMzRiLTIxNzBlMjg2YmUzMiIsInN0ZXAiOiJkZWNpc2lvblBvbGljeSJ9LHsic3RyYXRlZ3lJRCI6Imh0dHBzOi8vd3d3LmFkb2JlLmNvbS9zYW4vcGxhY2VtZW50L2Zvb3RlciIsInN0ZXAiOiJwbGFjZW1lbnQifV0sInJhbmsiOjEsImFjdGl2aXR5Ijp7ImlkIjoiZTNiYmVmZmQtNmNiMi00YTAzLWIyNGEtOTVjNDlmMGRmNGU0I2E1NmE0OTIxLWJjMjQtNGRjMC04Nzk3LTA2NmU4YzE0NTM5YiIsInByaW9yaXR5IjowLCJtYXRjaGVkU3VyZmFjZXMiOlsiaHR0cHM6Ly93d3cuYWRvYmUuY29tL3Nhbi9wbGFjZW1lbnQvZm9vdGVyIl19fSwiaXRlbXMiOltdfV0="
                        },
                        "rank": 1,
                        "activity": {
                            "id": "e3bbeffd-6cb2-4a03-b24a-95c49f0df4e4#a56a4921-bc24-4dc0-8797-066e8c14539b",
                            "priority": 0,
                            "matchedSurfaces": [
                                "https://www.adobe.com/san/placement/footer"
                            ]
                        }
                    },
                    "items": [
                        {
                            "id": "3913a28e-d33b-475b-9737-9f6de3940799",
                            "schema": "https://ns.adobe.com/personalization/html-content-item",
                            "data": {
                                "content": ""
                            }
                        }
                    ]
                }
            ],
            "type": "personalization:decisions",
            "eventIndex": 0
        }       
    ]
}
```

+++
