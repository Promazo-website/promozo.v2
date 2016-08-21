/**
 * Created by marc on 8/11/16.
 */
promazo.factory('PodsRoleTypesResource', function ($resource) {
    return $resource('/api/roletypes/:id',{ id: '@_id' },{
        update: {method: 'PATCH'}
  });
});