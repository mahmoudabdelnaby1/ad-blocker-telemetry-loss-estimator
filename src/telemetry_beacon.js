/*
 * Minimal consent-gated pageview beacon.
 * No identifiers, fingerprinting, blocker detection, or third-party requests.
 * The host page must set window.__analyticsConsent = true and provide a
 * same-origin data-telemetry-endpoint on its root element.
 */
(function (root) {
  'use strict';

  function sendConsentGatedBeacon(options) {
    const opts = options || {};
    if (opts.consent !== true || !opts.endpoint || !opts.pageUrl) return false;
    if (!opts.navigatorObject || typeof opts.navigatorObject.sendBeacon !== 'function') return false;

    let target;
    let page;
    try {
      page = new URL(opts.pageUrl);
      target = new URL(opts.endpoint, page);
    } catch (_error) {
      return false;
    }
    if (target.origin !== page.origin) return false;

    const payload = JSON.stringify({ event: 'page_view' });
    return opts.navigatorObject.sendBeacon(target.href, payload) === true;
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { sendConsentGatedBeacon };
    return;
  }

  if (!root || !root.document || !root.navigator || !root.location) return;
  const endpoint = root.document.documentElement &&
    root.document.documentElement.getAttribute('data-telemetry-endpoint');
  sendConsentGatedBeacon({
    consent: root.__analyticsConsent === true,
    endpoint,
    pageUrl: root.location.href,
    navigatorObject: root.navigator
  });
})(typeof window !== 'undefined' ? window : null);
