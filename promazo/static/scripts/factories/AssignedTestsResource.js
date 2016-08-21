/**
 * Created by marc on 8/19/16.
 */
promazo.factory('AssignedTestsResource', function ($resource) {
    return $resource('/api/assignedtests/:id',{ id: '@_id' },{
        update: {method: 'PATCH'},
        role: {method: 'GET', url:'/api/assignedtests/:id/role/', isArray:true, params:{id:'@_id'}}
  });
});