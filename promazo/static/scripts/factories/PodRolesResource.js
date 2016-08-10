/**
 * Created by marc on 8/8/16.
 */
promazo.factory('PodsRolesResource', function ($resource) {
    return $resource('/api/podroles/:id',{ id: '@_id' },{
        update: {method: 'PATCH'}
  });
});