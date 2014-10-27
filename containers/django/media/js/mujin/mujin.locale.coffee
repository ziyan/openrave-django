mujin.namespace 'mujin.locale', (exports) ->
  'use strict'

  exports.set = (locale) ->
    return if locale == mujin.settings.LOCALE
    $.cookie 'locale', locale,
      expires: 365
    window.location.reload(true)
