/**
 * Created by marc on 8/9/16.
 */
promazo.factory('UserResource', function ($resource) {
    return $resource('/api/user/:id',{ id: '@_id' },{
  });
});