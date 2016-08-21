/**
 * Created by marc on 8/19/16.
 */
promazo.factory('ApplicationNotesResource', function ($resource) {
    return $resource('/api/applicationnotes/:id',{ id: '@_id' },{
        update: {method: 'PATCH'},
        application: {method: 'GET', url:'/api/applicationnotes/:id/application/', isArray:true, params:{id:'@_id'}}
  });
});