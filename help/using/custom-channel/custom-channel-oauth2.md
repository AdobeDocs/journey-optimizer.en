---
title: Configure OAuth 2.0 authentication for custom channels
description: Learn how to configure the OAuth 2.0 token request, credential paths, and token settings for custom channels in Adobe Journey Optimizer.
feature: Channel Configuration
topic: Content Management
role: Admin
level: Experienced
---

# Configure OAuth 2.0 authentication {#custom-channel-oauth2}

>[!BEGINSHADEBOX]

**On this page:** Learn how to configure OAuth 2.0 authentication for custom channels in Adobe Journey Optimizer, including the token request payload, credential paths, token extraction, and token location in delivery requests.

>[!ENDSHADEBOX]

When you select **[!UICONTROL OAuth 2.0]** as the authentication type while [creating a custom channel](create-custom-channel.md#authentication-settings), configure the token request that Adobe Journey Optimizer uses to retrieve an access token from your authorization server.

Journey Optimizer sends the token request using the `endpoint`, `method`, `request`, and `policy` configuration. It then extracts the access token from the response using `tokenPath` and adds it to the delivery request using `locationConfig`.

The OAuth 2.0 authentication payload configures the request to the **token endpoint**. It is separate from the [message payload](create-custom-channel.md#payload-configuration) sent to your custom channel delivery endpoint.

## Configure the token request {#token-request}

Use the following examples to configure your token request. Replace the example endpoint and credential values with those required by your authorization server. The `headers` and `queryParams` entries in the examples are optional: remove them if your token endpoint does not require them, and remove the matching entries from `credentialPaths`.

### Form body example {#form-body-example}

Use a `form` payload when the token endpoint expects form fields such as `grant_type`, `client_id`, or `client_secret`.

```json
{
  "type": "oauth2",
  "endpoint": {
    "uri": "https://auth.example.com/oauth/token"
  },
  "method": "post",
  "request": {
    "headers": [
      {
        "key": "sampleHeaderKey",
        "value": "sampleHeaderValue"
      }
    ],
    "queryParams": [
      {
        "key": "sampleQueryParamKey",
        "value": "sampleQueryParamValue"
      }
    ],
    "payload": {
      "type": "form",
      "content": [
        {
          "key": "grant_type",
          "value": "client_credentials"
        },
        {
          "key": "client_id",
          "value": "your-client-id"
        },
        {
          "key": "client_secret",
          "value": "your-client-secret"
        }
      ],
      "includeNullValues": false
    }
  },
  "response": {
    "type": "json"
  },
  "policy": {
    "timeoutInMilliseconds": 30000,
    "cache": {
      "enabled": true,
      "ttlInSeconds": 300
    },
    "retry": {
      "enabled": false,
      "maxRetryCount": 3
    }
  },
  "credentialPaths": [
    "header.sampleHeaderKey",
    "queryParam.sampleQueryParamKey",
    "payload.client_id",
    "payload.client_secret"
  ],
  "tokenPath": "access_token",
  "locationConfig": {
    "key": "Authorization",
    "location": "header"
  }
}
```

For a `form` payload, each credential path uses the form field key, for example, `payload.client_secret`. Do not include `content` or array indexes in the credential path.

### JSON body example {#json-body-example}

Use a `json` payload when the token endpoint expects a JSON request body.

```json
{
  "type": "oauth2",
  "endpoint": {
    "uri": "https://auth.example.com/oauth/token"
  },
  "method": "post",
  "request": {
    "headers": [
      {
        "key": "sampleHeaderKey",
        "value": "sampleHeaderValue"
      }
    ],
    "queryParams": [
      {
        "key": "sampleQueryParamKey",
        "value": "sampleQueryParamValue"
      }
    ],
    "payload": {
      "type": "json",
      "content": {
        "grant_type": "client_credentials",
        "client_id": "your-client-id",
        "client_secret": "your-client-secret"
      },
      "includeNullValues": false
    }
  },
  "response": {
    "type": "json"
  },
  "policy": {
    "timeoutInMilliseconds": 30000,
    "cache": {
      "enabled": true,
      "ttlInSeconds": 300
    },
    "retry": {
      "enabled": false,
      "maxRetryCount": 3
    }
  },
  "credentialPaths": [
    "header.sampleHeaderKey",
    "queryParam.sampleQueryParamKey",
    "payload.client_id",
    "payload.client_secret"
  ],
  "tokenPath": "access_token",
  "locationConfig": {
    "key": "Authorization",
    "location": "header"
  }
}
```

### OAuth 2.0 fields {#oauth2-fields}

| Field | Description |
| --- | --- |
| `type` | Must be `oauth2`. |
| `endpoint.uri` | HTTPS URL of the OAuth 2.0 token endpoint. |
| `method` | HTTP method used to call the token endpoint. Use `post` for token requests. |
| `request.headers` | Optional headers sent to the token endpoint. |
| `request.queryParams` | Optional query parameters appended to the token endpoint URL. |
| `request.payload` | Token request body. Supports `form` and `json` payloads. |
| `request.payload.includeNullValues` | Defines whether fields with a null value are included in the token request body. |
| `response.type` | Response format. Use `json` when the token endpoint returns a JSON response. |
| `policy.timeoutInMilliseconds` | Maximum time to wait for the token endpoint response. |
| `policy.cache` | Defines whether the OAuth token is cached and for how long. |
| `policy.retry` | Optional retry configuration for token endpoint failures. |
| `credentialPaths` | Paths to request fields that contain credentials. These fields are treated as credentials and can be managed securely. |
| `tokenPath` | Dot-separated path to the access token in the OAuth response, for example, `access_token` or `data.access_token`. |
| `locationConfig` | Defines where the retrieved token is added to the delivery request. |
| `locationConfig.key` | Name of the header or query parameter that carries the token, for example, `Authorization`. |
| `locationConfig.location` | Where the token is added: `header` or `queryParam`. |

When token caching is enabled, Journey Optimizer reuses the OAuth token for the configured cache duration instead of calling the token endpoint for every delivery request.

## Identify credential fields {#credential-paths}

Use `credentialPaths` to identify which request fields contain credentials. If a header or query parameter contains a credential, include its path as well as any credential paths in the request body. The examples above identify the sample header and query parameter values as credentials; adjust this list to match your request.

| Prefix | Used for | Example |
| --- | --- | --- |
| `header.` | Credential passed in request headers. | `header.sampleHeaderKey` |
| `queryParam.` | Credential passed in query parameters. | `queryParam.sampleQueryParamKey` |
| `payload.` | Credential passed in the request body. | `payload.client_secret` |

Apply the following rules:

* Paths must start with `header`, `queryParam`, or `payload` and use dots as separators.
* For `form` payloads, use `payload.<formFieldKey>`.
* For `json` payloads, use the JSON object path, such as `payload.client_id` or `payload.credentials.client_secret`. Do not include `content` in the path.
* Empty path segments are not supported. For example, `payload..client_id` is invalid.

For a nested JSON body, use dot notation as shown in this configuration excerpt:

```json
{
  "request": {
    "payload": {
      "type": "json",
      "content": {
        "credentials": {
          "client_id": "your-client-id",
          "client_secret": "your-client-secret"
        }
      },
      "includeNullValues": false
    }
  },
  "credentialPaths": [
    "payload.credentials.client_id",
    "payload.credentials.client_secret"
  ]
}
```

## Extract the access token {#token-path}

`tokenPath` defines where the access token is located in the OAuth 2.0 token response.

For the following response, set `tokenPath` to `access_token`:

```json
{
  "access_token": "example-access-token",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

For a nested response, set `tokenPath` to `data.access_token`:

```json
{
  "data": {
    "access_token": "example-access-token"
  }
}
```

## Add the token to delivery requests {#token-location}

`locationConfig` defines where Journey Optimizer adds the retrieved token when calling the custom channel delivery endpoint.

To send the token in the `Authorization` header, use:

```json
{
  "locationConfig": {
    "key": "Authorization",
    "location": "header"
  }
}
```

| Location | Description |
| --- | --- |
| `header` | Adds the token as an HTTP header. |
| `queryParam` | Adds the token as a query parameter. |

## Limits and validation rules {#limits}

| Field | Limit |
| --- | --- |
| `endpoint.uri` | Must be an absolute HTTPS URL with a non-empty host. Maximum length: 2048 characters. |
| `policy.timeoutInMilliseconds` | Minimum: 300 ms. Maximum: 60000 ms. |
| `policy.cache.ttlInSeconds` | Applies when cache is enabled. Minimum: 300 seconds. Maximum: 3600 seconds. |
| `request.headers` | Maximum 50 headers. Header key length: 1-100 characters. Header value maximum: 8192 characters. |
| `request.queryParams` | Maximum 50 query parameters. Query parameter key length: 1-100 characters. Query parameter value maximum: 8192 characters. |
| `request.payload.type=form` | Maximum 50 form fields. Form key length: 1-100 characters. Duplicate form keys are not allowed. |
| Credential values | 1-1024 characters. |
| `tokenPath` | Must be a valid dot-separated path. An empty value is allowed only when the entire response is the token. |
| `credentialPaths` | Must start with `header`, `queryParam`, or `payload` and use dots as separators. |

## Next steps {#next-steps}

* [Test the connection and activate your custom channel](create-custom-channel.md#test-activate).
* [Manage API credentials for your custom channel](custom-channel-api-credentials.md).

{{$include /help/_includes/do-not-localize/custom-channel/ai-augmented-custom-channel-oauth2.md}}
