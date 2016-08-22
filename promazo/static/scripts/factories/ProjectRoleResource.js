/**
 * Created by marc on 8/7/16.
 */
promazo.factory('ProjectRoleResource', function ($resource) {
    return $resource('/api/projectrole/:id',{ id: '@_id' },{
        update: {method: 'PATCH'},
        project: {method:'GET', isArray:true, url:'/api/projectrole/:id/project/',params:{id:'@_id'}}
  });
});