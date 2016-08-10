/**
 * Created by marc on 8/7/16.
 */
promazo.factory('ProjectResource', function ($resource) {
    return $resource('/api/project/:id',{ id: '@_id' },{
        update: {method: 'PATCH'},
        available_users: {method:'GET', url:'/api/pods/:id/available_users/',isArray:true,params:{id:'@_id'}}
  });
});