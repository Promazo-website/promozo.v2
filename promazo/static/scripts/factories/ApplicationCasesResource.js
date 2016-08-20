/**
 * Created by marc on 8/19/16.
 */
promazo.factory('ApplicationCasesResource', function ($resource) {
    return $resource('/api/applicationcases/:id',{ id: '@_id' },{
        update: {method: 'PATCH'},
        role: {method: 'GET', url:'/api/applicationcases/:id/role/', isArray:true, params:{id:'@_id'}}
  });
});