/**
 * Created by marc on 8/7/16.
 */
promazo.factory('ProjectPlaceResource', function ($resource) {
    return $resource('/api/projectplace/:id',{ id: '@_id' },{
        update: {method: 'PATCH'}
  });
});