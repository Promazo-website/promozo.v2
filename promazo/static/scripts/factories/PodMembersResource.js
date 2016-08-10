/**
 * Created by marc on 8/8/16.
 */
promazo.factory('PodMembersResource', function ($resource) {
    return $resource('/api/podmembers/:id',{ id: '@_id' },{
        update: {method: 'PATCH'},
        members: {method: 'GET', url:'/api/podmembers/:id/members/', isArray:true, params:{id:'@_id'}}
  });
});