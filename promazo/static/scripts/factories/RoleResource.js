/**
 * Created by marc on 8/9/16.
 */
promazo.factory('RoleResource', function ($resource) {
    return $resource('/api/podroles/:id',{ id: '@_id' },{
  });
});