/**
 * Created by marc on 8/7/16.
 */
promazo.factory('RoleTypeResource', function ($resource) {
    return $resource('/api/roletype/:id',{ id: '@_id' },{
        update: {method: 'PATCH'}
  });
});