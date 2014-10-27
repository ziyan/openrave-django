mujin.namespace 'mujin.user', (exports) ->
  'use strict'

  mujin.app.User = DS.Model.extend
    username: DS.attr 'string'
    first_name: DS.attr 'string'
    last_name: DS.attr 'string'
    robots: DS.hasMany('robot', async: true)

  mujin.app.UserRoute = Ember.Route.extend
    model: (params) ->
      @store.find 'user', params.id

