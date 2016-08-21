/**
 * Created by marc on 8/19/16.
 */
promazo.factory('ApplicationCaseResultsResource', function ($resource) {
    return $resource('/api/applicationcaseresults/:id',{ id: '@_id' },{
        update: {method: 'PATCH'},
        application: {method: 'GET', url:'/api/applicationcaseresults/:id/application/', isArray:true, params:{id:'@_id'}},
        case: {method: 'GET', url:'/api/applicationcaseresults/:id/case/', isArray:true, params:{id:'@_id'}}

  });
});