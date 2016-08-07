/**
 * Created by marc on 8/5/16.
 */
promazo.factory('QuestionResource', function ($resource) {
    return $resource('/api/questions/:id',{ id: '@_id' },{
        update: {method: 'PATCH'}
  });
});
