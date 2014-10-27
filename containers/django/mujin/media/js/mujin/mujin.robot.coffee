mujin.namespace 'mujin.robot', (exports) ->
  'use strict'

  mujin.app.Robot = DS.Model.extend
    name: DS.attr 'string'
    description: DS.attr 'string'
    user: DS.belongsTo('user', async: true)
    dof: DS.attr 'number'

  mujin.app.RobotRoute = Ember.Route.extend
    model: (params) ->
      @store.find 'robot', params.id

