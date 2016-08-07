/**
 * Created by marc on 8/5/16.
 */

promazo.factory('TestsResource', function ($resource) {
    return $resource('/api/tests/:id',{ id: '@_id' },{
        update: {method: 'PATCH'}
  });
});