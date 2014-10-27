debug.setLevel(9) if window.location.search is '?debug'

((window) ->
  'use strict'

  namespace = (target, name, block) ->
    [target, name, block] = [window, arguments...] if arguments.length < 3
    top = target
    target = target[item] or= {} for item in name.split '.'
    block target, top

  namespace 'mujin', (exports, top) ->
    exports.namespace =  namespace

)(window)

mujin.namespace 'mujin.settings', (exports) ->
  'use strict'

  $('div.js-settings div').each ->
    key = $(@).data('key')
    value =  $(@).data('value')
    return if not key
    exports[key] = value
    debug.setLevel(9) if key is 'DEBUG' and value
    debug.info 'mujin.settings.' + key, value
  $('div.js-settings').remove()


mujin.namespace 'mujin', (exports) ->
  'use strict'

  app = exports.app = Ember.Application.create()
  app.Router.reopen
    location: 'history'

  app.Router.map ->
    @resource 'about'
    @resource 'user',
      path: '/user/:id'
    @resource 'robot',
      path: '/robot/:id'

  app.ApplicationAdapter = DS.RESTAdapter.extend
    namespace: 'api'

  app.IndexRoute = Ember.Route.extend
    model: (params) ->
      @store.find 'robot'
