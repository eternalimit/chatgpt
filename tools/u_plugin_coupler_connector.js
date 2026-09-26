'use strict';

/**
 * U Plugin Coupler Connector
 *
 * Couples U Authenticator to supported plugin/connector interfaces.
 * This is a routing and verification boundary. It does not install plugins,
 * create credentials, bypass provider authentication, or manufacture sessions.
 */

const SECRET_FIELDS = new Set([
  'password', 'private_key', 'seed_phrase', 'recovery_phrase',
  'pin', 'api_secret', 'access_token'
]);

function rejectSecrets(input = {}) {
  for (const key of Object.keys(input)) {
    if (SECRET_FIELDS.has(key.toLowerCase())) {
      throw new Error('SECRET_INPUT_REJECTED');
    }
  }
}

function couple(input = {}) {
  rejectSecrets(input);

  const provider = input.provider || null;
  const pluginSupported = input.plugin_supported === true;
  const authenticated = input.authenticated === true;
  const authorized = input.authorized === true;

  if (!provider) {
    return { state: 'HOLD', bit: 0, reason: 'PROVIDER_REQUIRED' };
  }
  if (!pluginSupported) {
    return { state: 'HOLD', bit: 0, provider, reason: 'PLUGIN_CONNECTOR_UNAVAILABLE' };
  }
  if (!authenticated) {
    return { state: 'HOLD', bit: 0, provider, reason: 'PROVIDER_AUTH_REQUIRED' };
  }
  if (!authorized) {
    return { state: 'HOLD', bit: 0, provider, reason: 'OPERATION_NOT_AUTHORIZED' };
  }

  return {
    state: 'PASS',
    bit: 1,
    provider,
    scope: input.scope || 'connection',
    route: 'U -> PLUGIN COUPLER -> CONNECTOR -> PROVIDER -> VERIFY'
  };
}

module.exports = { couple, rejectSecrets };
