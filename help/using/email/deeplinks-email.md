---
solution: Journey Optimizer
product: journey optimizer
title: Use deeplinks in email messages
description: Learn how to add deeplinks to email content and how to implement deep link handling in iOS and Android apps.
feature: Email
topic: Content Management
role: User, Developer
level: Intermediate
keywords: deeplink, deep link, universal links, app links, email
exl-id: 9c2c1e7b-31bf-4a5d-b8d4-7c4c4f2f1b21
---
 
# Use deeplinks in email messages {#email-deeplinks}
 
Deeplinks in emails help you take recipients from an email to a specific screen or piece of content in your mobile app. It helps bring people straight to the intended in-app experience, without routing them through a web browser or an app store, so the journey stays relevant and on-brand.

This page covers:
 
* Journey Optimizer configuration prerequisites - how to configure deeplinks for emails
* How your mobile app team can implement deeplink handling for iOS and Android
 
>[!NOTE]
>
>To successfully open in-app content, deeplinks require **both**:
>
>* A deeplink URL added in the email content
>* A mobile app implementation that recognizes and routes that deeplink URL
 
## Configure prerequisites and add deeplink URLs in email content {#ajo-prerequisites-and-authoring}
 
### Before you start {#before-you-start}
 
Make sure you have:
 
* **A defined deeplink format**: decide what your emails will use (for example, `myapp://...` custom scheme, or `https://example.com/...` handled via universal links / app links).
* **Mobile app readiness**: your mobile app must be configured to handle the deeplink format you plan to use. See [Mobile app implementation](#mobile-implementation).
* **The destination mapping**: define how each deeplink maps to in-app content (screen name, route, parameters, etc.).
 
>[!IMPORTANT]
>
>If you use **universal links (iOS)** and/or **app links (Android)**, hosting and validating the site association files is a prerequisite. Some steps are not self-service and require support assistance. See [Host and validate the association files](#host-and-validate-association-files).

>[!IMPORTANT]
>
>Journey Optimizer can insert deeplink URLs in email content, but it does not implement app-side routing. If the app does not recognize the deeplink, the click may fail or open a fallback destination depending on your link strategy (see [Troubleshooting and FAQ](#troubleshooting-faq)).
 
### Host and validate the association files (universal links / app links) {#host-and-validate-association-files}

This section applies when you use **universal links (iOS)** and **app links (Android)** (HTTPS-based deeplinks).

>[!NOTE]
>
>If you use **custom URI schemes** (not recommended), you can skip the hosting and validation steps below.

#### Step 1: Delegate a subdomain {#delegate-subdomain}

Delegate the subdomain where deeplinking is enabled (self-service).

#### Step 2: Request hosting of the association file(s) {#request-hosting-association-files}

Contact Adobe Client Care with the details below.

* **For iOS (AASA)**:
  * Delegated subdomain
  * App bundle ID
* **For Android (`assetlinks.json`)**:
  * Delegated subdomain
  * App bundle ID
  * SHA-256 certificate fingerprint

#### Step 3: Validate the configuration {#validate-association-files}

Validate the URLs below and ensure the content matches the expected format.

* **For iOS (AASA)**: `https://data.<delegated_subdomain>/.well-known/apple-app-site-association`

The file should look like the example below. Other than `appID`, other values remain the same for all customers.

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": "<app_bundle_id>",
        "paths": [
          "NOT /ee/v1/click/*",
          "/ee/v1/mclick/*"
        ]
      }
    ]
  }
}
```

* **For Android (`assetlinks.json`)**: `https://data.<delegated_subdomain>/.well-known/assetlinks.json`

The file should look like the example below. Other than the app identifiers, other values remain the same for all customers.

```json
[
  {
    "relation": ["delegate_permission/common.handle_all_urls"],
    "target": {
      "namespace": "android_app",
      "package_name": "<app_bundle_id>",
      "sha256_cert_fingerprints": [
        "12:34:56:78:90:AB:CD:EF:12:34:56:78:90:AB:CD:EF:12:34:56:78:90:AB:CD:EF:12:34"
      ]
    }
  }
]
```

### Add a deeplink in the Email Designer {#add-deeplink-in-email-designer}
 
To add a deeplink in an email:
 
1. In the Email Designer, select the element you want to link (text, button, or image).
1. Click **[!UICONTROL Insert link]** in the contextual toolbar.
1. In the link type selector, choose **[!UICONTROL Deeplink]**.
1. Enter your deeplink URL.
1. Save your changes.
 
Learn more on inserting links in [this section](message-tracking.md#insert-links).
 
### Recommended practices for deeplink URLs {#deeplink-best-practices}
 
* **Use stable paths**: prefer routes that are resilient to app UI changes (for example `/account/orders` instead of `/tab/3/view/2`).
* **Keep parameters predictable**: define a consistent parameter scheme (for example `?orderId=12345`).
* **Avoid sensitive data in URLs**: do not put secrets or personal data directly into the deeplink URL.
 
### Test your deeplinks {#test-deeplinks}
 
* Send a proof and click the deeplink on a device where the app is installed.
* If the deeplink does not open the expected screen, validate the app-side routing and the URL format (scheme/host/path/query encoding).
 
## B. Mobile app implementation (iOS and Android) {#mobile-implementation}
 
This section provides common implementation patterns for deep links. Your exact setup depends on your app architecture and routing framework.
 
### Choose a deeplink strategy {#choose-strategy}
 
Most apps use one (or both) of these strategies:
 
* **Custom URL schemes** (example: `myapp://product/123`)
  * Pros: easy to set up
  * Cons: no standard web fallback; if the app is not installed, the click may fail depending on the client/device behavior
 
* **Universal Links (iOS) / App Links (Android)** using HTTPS URLs (example: `https://links.example.com/product/123`)
  * Pros: can fall back to a website when the app is not installed; more consistent handling
  * Cons: requires domain association configuration
 
>[!NOTE]
>
>If you want a predictable fallback experience when the app is not installed, prefer an HTTPS-based approach (universal links / app links) with a web destination.
 
### iOS implementation {#ios-implementation}
 
#### Option 1: Custom URL scheme {#ios-custom-scheme}
 
1. Register a URL type (scheme) in your app's configuration (for example in Xcode project settings / `Info.plist` via URL Types).
1. Handle incoming URLs and route them within your app.
 
Example (Swift, routing URL opens):
 
```swift
// AppDelegate.swift
func application(_ app: UIApplication,
                 open url: URL,
                 options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    DeepLinkRouter.shared.route(url)
    return true
}
```
 
```swift
final class DeepLinkRouter {
    static let shared = DeepLinkRouter()
 
    func route(_ url: URL) {
        // Example: myapp://product/123?ref=email
        // Parse host/path/query and navigate accordingly.
    }
}
```
 
#### Option 2: Universal Links (recommended for HTTPS links) {#ios-universal-links}
 
1. Configure Associated Domains in your app (for example `applinks:links.example.com`).
1. Host the Apple App Site Association (AASA) file on your domain.
1. Handle universal link navigation via `NSUserActivity`.
 
Example (Swift, universal link handling):
 
```swift
// AppDelegate.swift
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
          let url = userActivity.webpageURL else {
        return false
    }
 
    DeepLinkRouter.shared.route(url)
    return true
}
```
 
### Android implementation {#android-implementation}
 
#### Option 1: Intent filter (custom scheme or HTTPS) {#android-intent-filter}
 
1. Add an `intent-filter` to the Activity that should receive deep links.
1. Parse the incoming intent data and route inside the app.
 
Example (AndroidManifest.xml, HTTPS App Link-style filter):
 
```xml
<activity android:name=".DeepLinkActivity">
  <intent-filter android:autoVerify="true">
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
    <data
      android:scheme="https"
      android:host="links.example.com"
      android:pathPrefix="/product" />
  </intent-filter>
</activity>
```
 
Example (Kotlin, reading the deeplink URL):
 
```kotlin
class DeepLinkActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
 
        val url = intent?.data
        if (url != null) {
            DeepLinkRouter.route(url)
        }
 
        finish()
    }
}
 
object DeepLinkRouter {
    fun route(uri: Uri) {
        // Example: https://links.example.com/product/123?ref=email
        // Parse path/query and navigate accordingly.
    }
}
```
 
#### Option 2: Android App Links verification {#android-app-links}
 
If you use HTTPS App Links and want Android to open your app directly:
 
1. Configure `android:autoVerify="true"` on your intent filter.
1. Host `assetlinks.json` under `https://<your-domain>/.well-known/assetlinks.json`.
1. Ensure the asset links file matches your app package and signing configuration.
 
## Troubleshooting and FAQ {#troubleshooting-faq}
 
### The app doesn't open when I tap the deeplink {#faq-app-doesnt-open}
 
* Verify the deeplink format matches what the app is registered to handle (scheme/host/path).
* For iOS universal links and Android app links, confirm domain association (AASA / `assetlinks.json`) is correctly configured and reachable.
* Test on a real device (simulators/emulators can behave differently for link association).
 
### The app opens but doesn't navigate to the expected screen {#faq-app-opens-wrong-screen}
 
* Confirm the app-side router correctly parses the URL path/query.
* Check URL encoding: reserved characters should be URL-encoded.
* Validate parameter names and values match what the router expects.
 
### What happens if the app is not installed? {#faq-app-not-installed}
 
* With **custom URL schemes**, behavior varies by platform/client; the click may fail or do nothing.
* With **HTTPS universal links / app links**, you can provide a web fallback destination so the click still lands somewhere useful.
 
### How do I safely include special characters in parameters? {#faq-url-encoding}
 
URL-encode query parameter values. This reduces delivery and rendering issues and helps prevent parsing errors in your app.
 
### How should we test end-to-end? {#faq-testing}
 
* Create a proof with a deeplink, click it on iOS and Android devices (installed and not installed scenarios).
* Validate:
  * The email link value (scheme/host/path/query)
  * The OS-level association (if using universal links / app links)
  * The in-app routing outcome

