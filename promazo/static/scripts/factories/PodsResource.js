/**
 * Created by marc on 8/8/16.
 */
promazo.factory('PodsResource', function ($resource) {
    return $resource('/api/pods/:id',{ id: '@_id' },{
        update: {method: 'PATCH'},
        permission: {method:'GET', url:'/api/pods/:id/permission/',params:{id:'@_id'}},
        mypods: {method:'GET', url:'/api/pods/mypods/',isArray:true},
        available_users: {method:'GET', url:'/api/pods/:id/available_users/',isArray:true,params:{id:'@_id'}},
  });
});