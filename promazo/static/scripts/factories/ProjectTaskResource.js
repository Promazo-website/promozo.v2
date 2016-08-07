/**
 * Created by marc on 8/7/16.
 */
promazo.factory('ProjectTaskResource', function ($resource) {
    return $resource('/api/projecttask/:id',{ id: '@_id' },{
        update: {method: 'PATCH'}
  });
});