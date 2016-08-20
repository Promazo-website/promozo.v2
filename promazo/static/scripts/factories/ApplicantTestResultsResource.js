/**
 * Created by marc on 8/19/16.
 */
promazo.factory('ApplicantTestResultsResource', function ($resource) {
    return $resource('/api/applicanttestresults/:id',{ id: '@_id' },{
        update: {method: 'PATCH'},
        application: {method: 'GET', url:'/api/applicanttestresults/:id/application/', isArray:true, params:{id:'@_id'}}
  });
});