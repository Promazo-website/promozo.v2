/**
 * Created by marc on 8/8/16.
 */
/**
 * Created by marc on 8/8/16.
 */
promazo.factory('PodsPermissionsResource', function ($resource) {
    return $resource('/api/podpermissions/:id',{ id: '@_id' },{
        update: {method: 'PATCH'}
  });
});