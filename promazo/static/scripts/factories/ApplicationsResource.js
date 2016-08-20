/**
 * Created by marc on 8/19/16.
 */
promazo.factory('ApplicationsResource', function ($resource) {
    return $resource('/api/applications/:id',{ id: '@_id' },{
        update: {method: 'PATCH'},
        role: {method: 'GET', url:'/api/applications/:id/role/', isArray:true, params:{id:'@_id'}}
  });
});