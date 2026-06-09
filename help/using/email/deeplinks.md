---
solution: Journey Optimizer
product: journey optimizer
title: Use and configure deep links in email and SMS messages
description: Learn how to add deep links to email and SMS content and how to implement deep link handling in iOS and Android apps.
feature: Email, SMS
topic: Content Management
role: User, Developer
level: Intermediate
keywords: deeplink, deep link, universal links, app links, email, sms
feature_v2: []
subfeature_v2: []
---
 
# Use and configure deep links in emails and SMS {#deeplinks}
 
Deep links help you take recipients from an email or SMS message to a specific screen or piece of content in your mobile app. It helps bring people straight to the intended in-app experience, without routing them through a web browser or an app store, so the journey stays relevant and on-brand.

When your recipients click the deep link, they are taken directly to the intended in-app content - **provided you have completed**:

* the [configuration steps](#configuration) in Journey Optimizer;

* the [mobile app implementation](#mobile-implementation) steps for iOS and Android in your mobile app.

>[!NOTE]
>
>[!DNL Adobe Journey Optimizer] supports deep linking for both iOS and Android using tracked URLs (`/ee/v1/mclick/*`) to ensure compatibility and click tracking.  

## Authoring deep links {#authoring}

>[!CAUTION]
>
>Deep links will not work unless you have completed the [configuration](#configuration) and [mobile app implementation](#mobile-implementation) steps on this page.

### Email {#authoring-email}

For email messages, you have two options to insert a deep link:

* **Email Designer**: Make sure [link tracking is enabled](message-tracking.md#enable-tracking). Select the element you want to link (text, button, or image), click **[!UICONTROL Insert link]** in the contextual toolbar, and choose **[!UICONTROL Deeplink]** to enter your deep link URL. [Learn more on inserting links](message-tracking.md#insert-links)

* **Personalization editor (code)**: Insert the deep link directly into the HTML using the following snippet:

    ```html
    <a class="arc-link" data-nl-type="DEEPLINK" href="<<deeplink_url>>" id="acr-link-7821368" style="text-decoration:underline;" target="_blank" data-tracking-type="DEEPLINK">Click Here</a>
    ```

    >[!TIP]
    >
    >Replace `<<deeplink_url>>` with your actual deep link URL and use a unique `id` for each block to avoid conflicts.


### SMS {#authoring-sms}

For SMS, deep links are authored using the [Url](../personalization/functions/helpers.md#url) helper function in the personalization editor. Learn how to add links to SMS content in [this section](../mobile/design-mobile.md#sms-content).

To insert deep links in SMS content, use the following syntax:

```
{{url originalUrl='<<url>>' type='DEEPLINK' action='CLICK'}}
```

>[!TIP]
>
>Replace `<<url>>` with your actual deep link URL.

## Configuration in Journey Optimizer {#configuration}

To be able to use deep links in emails and SMS for your mobile apps, complete the configuration steps below.

>[!NOTE]
>
>This section applies when you use **universal links (iOS)** and **app links (Android)** (HTTPS-based deep links).

1. In Journey Optimizer, delegate the subdomain where deep linking is enabled. [Learn more](../configuration/delegate-subdomain.md)

1. Host the AASA file for iOS and the assetLinks.json file for Android on your subdomain. Contact [Adobe Customer Care](https://helpx.adobe.com/enterprise/admin-guide.html/enterprise/using/support-for-experience-cloud.ug.html){target="_blank"} or your Adobe representative with the details below:

    * **For iOS (AASA)**:
      * Delegated subdomain
      * App bundle ID
    * **For Android (assetLinks.json)**:
      * Delegated subdomain
      * App bundle ID
      * SHA-256 certificate fingerprint

>[!IMPORTANT]
>
>Deep linking through Adobe infrastructure applies when link tracking is enabled for your message — in the[ email tracking settings](message-tracking.md#enable-tracking) or in the **[!UICONTROL Actions tracking]** section for SMS campaigns. Tracked deep link clicks use URLs under `/ee/v1/mclick/*`, which Adobe hosts and resolves.
>
>For **non-tracked** links, the URL is not rewritten through Adobe systems. You must configure universal links or app links on your own domains and hosting so those links open your app as intended.

## Mobile app implementation {#mobile-implementation}
 
This section explains how to implement mobile deep links with [!DNL Adobe Journey Optimizer] so that, in a typical **HTTPS** setup (universal links and app links), a single URL can:
 
* Open a specific screen inside your mobile app when the app is installed, or
* Open your website as a fallback when the app is not installed.
 
When link tracking is enabled for your message, [!DNL Journey Optimizer] continues to track these clicks, includes them in reporting, and can use them in [content experiments](../content-management/content-experiment.md) if you run them on the message.
 
This section provides common implementation patterns for deep links. Your exact setup depends on your app architecture and routing framework.
 
### iOS (Universal Links) {#ios-implementation}

1. In Xcode, select your target through **[!UICONTROL Signing & Capabilities]** > **[!UICONTROL + Capability]** > **[!UICONTROL Associated Domains]**.
1. Add entries for your delegated subdomains, for example:

    ```text
    applinks:www.mybusiness.com
    applinks:data.email.mybusiness.com
    ```

1. Handle Universal Links in the app and get the original link from the response header.

    +++ Example: iOS 13+ with scenes

    ```swift
    class SceneDelegate: UIResponder, UIWindowSceneDelegate {

        func scene(_ scene: UIScene,
                  continue userActivity: NSUserActivity) {
            guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
                  let incomingURL = userActivity.webpageURL else {
                return
            }

            handleUniversalLink(url: incomingURL)
        }

        private func handleUniversalLink(url: URL) {
            // Only handle AJO tracked mobile clicks
            guard url.host == "data.email.mybusiness.com",
                  url.path.hasPrefix("/ee/v1/mclick") else {
                // Could also handle direct www.mybusiness.com links here
                return
            }

            resolveTrackedUrlAndRoute(url)
        }

        private func resolveTrackedUrlAndRoute(_ trackedUrl: URL) {
            var request = URLRequest(url: trackedUrl)
            request.httpMethod = "GET"

            URLSession.shared.dataTask(with: request) { _, response, error in
                guard error == nil,
                      let httpResponse = response as? HTTPURLResponse,
                      let locationValue = httpResponse.allHeaderFields["Location"] as? String,
                      let finalUrl = URL(string: locationValue) else {
                    return
                }

                DispatchQueue.main.async {
                    self.routeToDestination(finalUrl)
                }
            }.resume()
        }

        private func routeToDestination(_ url: URL) {
            // Example: map URL paths to screens
            // https://www.mybusiness.com/dashboard/offers/coupons
            // → OffersViewController for Coupons
        }
    }
    ```

    +++

>[!IMPORTANT]
>
>The app must perform a **GET** on the `mclick` URL and read the **`Location`** header, then route based on the **final** URL.
>
>Do not simply open the `mclick` URL in Safari; that defeats the purpose of deep linking.

### Android (App Links) {#android-implementation}

1. Add App Link intent filter in your Android app.

    ```xml
    <activity
        android:name=".DeepLinkActivity"
        android:exported="true">

        <intent-filter android:autoVerify="true">
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.DEFAULT" />
            <category android:name="android.intent.category.BROWSABLE" />

            <data
                android:scheme="https"
                android:host="data.email.mybusiness.com"
                android:pathPrefix="/ee/v1/mclick" />
        </intent-filter>

    </activity>
    ```

1. Implement the deep link handler.

    +++ In Kotlin:

    ```kotlin
    class DeepLinkActivity : AppCompatActivity() {

        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)

            val trackedUri = intent?.data
            if (trackedUri == null ||
                trackedUri.host != "data.email.mybusiness.com" ||
                !trackedUri.path.orEmpty().startsWith("/ee/v1/mclick")) {
                finish()
                return
            }

            resolveTrackedUrlAndRoute(trackedUri)
        }

        private fun resolveTrackedUrlAndRoute(trackedUri: Uri) {
            lifecycleScope.launch(Dispatchers.IO) {
                try {
                    val finalUrl = followRedirect(trackedUri.toString())
                    withContext(Dispatchers.Main) {
                        routeToDestination(finalUrl)
                        finish()
                    }
                } catch (e: Exception) {
                    // Optionally log error, fallback to browser
                    finish()
                }
            }
        }

        private fun followRedirect(trackedUrl: String): Uri {
            val client = OkHttpClient.Builder()
                .followRedirects(false) // We want to read Location ourselves
                .build()

            val request = Request.Builder()
                .url(trackedUrl)
                .get()
                .build()

            client.newCall(request).execute().use { response ->
                val location = response.header("Location")
                    ?: throw IllegalStateException("Missing Location header")
                return Uri.parse(location)
            }
        }

        private fun routeToDestination(finalUri: Uri) {
            // Example: interpret https://www.mybusiness.com/dashboard/offers/coupons
            // and open the correct Activity / Fragment
        }
    }
    ```

    +++
  
>[!IMPORTANT]
>
>Like iOS, the app must call the `mclick` URL and use the **`Location`** header to determine the final destination.
>
>Use `followRedirects(false)` so you control redirect handling and can log analytics accurately if needed.
>
>Routing logic is app‑specific; define a clear mapping from URLs to screens.

## Recommended practices {#deeplink-best-practices}
 
* **Use stable paths**: Prefer routes that are resilient to app UI changes (for example `/account/orders` instead of `/tab/3/view/2`).
* **Account for tracked paths**: When link tracking is enabled, the clicked link may use tracked path patterns (for example `/ee/v1/mclick/`). Make sure your router can parse the final URL after resolving the tracked link.
* **Keep parameters predictable**: Define a consistent parameter scheme (for example `?orderId=12345`).
* **Avoid sensitive data in URLs**: Do not put secrets or personal data directly into the deep link URL.
* **Test your deep link**: Send a proof and click the deep link on a device where the app is installed.
* **Validate on real devices**: Universal links and tracked-link resolution behaviors are more reliable to validate on physical devices rather than simulators.
* **Validate the app-side routing**: If the deep link does not open the expected screen, validate the app-side routing and the URL format (host/path/query and URL encoding).
* **Keep app initialization in mind**: App Links / Universal Links behavior is most reliable after the app has been installed and opened at least once.
 
## Troubleshooting and FAQ {#troubleshooting-faq}
 
+++ The app doesn't open when I tap the deep link.
 
* Verify the URL matches the host and path patterns your app is registered to handle, including tracked click paths when link tracking is enabled (for example paths under `/ee/v1/mclick/`).
* For iOS universal links and Android app links, confirm domain association (AASA / `assetlinks.json`) is correctly configured and reachable.
* Test on a real device (simulators/emulators can behave differently for link association).
 
+++
 
+++ The app opens but doesn't navigate to the expected screen.
 
* Confirm the app-side router correctly parses the URL path/query.
* Check URL encoding: reserved characters should be URL-encoded.
* Validate parameter names and values match what the router expects.
 
+++
 
+++ What happens if the app is not installed?
 
* If the same HTTPS URL can be served by your website, the link can open a web page as a fallback when the app is not installed (configure your web destination and routing accordingly).
 
+++
 
+++ How do I safely include special characters in parameters?
 
URL-encode query parameter values. This reduces delivery and rendering issues and helps prevent parsing errors in your app.
 
+++
 
+++ How should we test end-to-end?
 
* Create a proof with a deep link, click it on iOS and Android devices (installed and not installed scenarios).
* Validate:
  * The final email or SMS link value (host/path/query)
  * The OS-level association (if using universal links / app links)
  * The in-app routing outcome
 
+++
 
+++ I have one app but different subdomains for the organization. Should I request AASA and assetLinks.json to be created for each subdomain?

Yes. If you want deep linking on every delegated subdomain, request AASA and `assetlinks.json` configuration for each subdomain that should support the feature.

+++

+++ Should the URL I configure use a deep linking format (for example `appname://path`)?

You can use a custom URL scheme (for example `appname://path`), but the recommended approach is a universal link or app link (`https://`), which matches the HTTPS-based setup in the configuration and implementation sections on this page.

+++
 
+++ Will UTM parameters on the URL be available in the mobile app for analytics?

Yes. UTM parameters you configure in [!DNL Journey Optimizer] are included in the final URL returned in the `Location` header when your app performs a GET on the `mclick` URL, so you can use them for in-app analytics.

+++
 
+++ What is the user experience for `/ee/v1/click/` URLs?

The link opens in the device's default web browser (standard click tracking behavior), rather than being handled as an app deep link through the `mclick` flow described on this page.

+++

