const test = require('node:test');
const assert = require('node:assert/strict');
const { sendConsentGatedBeacon } = require('./telemetry_beacon.js');

function createNavigator() {
  const calls = [];
  return {
    calls,
    sendBeacon(url, body) {
      calls.push({ url, body });
      return true;
    }
  };
}

test('does not send telemetry without explicit consent', () => {
  const navigatorObject = createNavigator();
  const sent = sendConsentGatedBeacon({
    consent: false,
    endpoint: '/analytics/collect',
    pageUrl: 'https://example.test/page',
    navigatorObject
  });
  assert.equal(sent, false);
  assert.equal(navigatorObject.calls.length, 0);
});

test('sends only a minimal pageview to a same-origin endpoint after consent', () => {
  const navigatorObject = createNavigator();
  const sent = sendConsentGatedBeacon({
    consent: true,
    endpoint: '/analytics/collect',
    pageUrl: 'https://example.test/page',
    navigatorObject
  });
  assert.equal(sent, true);
  assert.equal(navigatorObject.calls.length, 1);
  assert.equal(navigatorObject.calls[0].url, 'https://example.test/analytics/collect');
  assert.deepEqual(JSON.parse(navigatorObject.calls[0].body), { event: 'page_view' });
});

test('does not send data to a cross-origin endpoint', () => {
  const navigatorObject = createNavigator();
  const sent = sendConsentGatedBeacon({
    consent: true,
    endpoint: 'https://collector.example.net/collect',
    pageUrl: 'https://example.test/page',
    navigatorObject
  });
  assert.equal(sent, false);
  assert.equal(navigatorObject.calls.length, 0);
});
