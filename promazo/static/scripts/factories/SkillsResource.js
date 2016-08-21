/**
 * Created by marc on 8/11/16.
 */
promazo.factory('SkillResource', function ($resource) {
    return $resource('/api/skills/resource/:id',{ id: '@_id' },{
        update: {method: 'PATCH'}
  });
});