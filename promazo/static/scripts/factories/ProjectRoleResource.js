/**
 * Created by marc on 8/7/16.
 */
promazo.factory('projectRoleResource', function ($resource) {
    return $resource('/api/projectrole/:id',{ id: '@_id' },{
        update: {method: 'PATCH'}
  });
});