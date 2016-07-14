/**
 * Created by marc on 19/05/16.
 */
promazo.factory('SkillsService', function ($http) {
  var skillService = {};


    skillService.list = function () {
        return $http
            .get('/api/skills/skills/')
            .then(function (data) {
                  return data.data;
            });
    };

    skillService.new = function (details) {
        return $http
            .post('/api/skills/skills/', details)
            .then(function (data) {
                return data.data;
            });
    };
    skillService.assign =  function(details) {
        return $http
            .post('/api/skills/user/', {skills: [details.id]})
            .then( function(data) {
                return data.data;
            });
    };
    
    skillService.unassign =  function(details) {
        return $http.delete('/api/skills/user/', {skills: [details.id]})
            .then( function(data) {
                return data.data;
            });
    };
    
    skillService.assigned = function() {
        return $http.get('/api/skills/user/simple/')
            .then( function(data) {
                return data.data;
            });
    };


    skillService.assignedFull = function() {
        return $http.get('/api/skills/user/')
            .then( function(data) {
                return data.data;
            });
    };
    
    skillService.getLoginQuestion =  function() {
        return $http.get('/api/skills/questions/')
            .then(function (data) {
                return data.data;
                
            });
    };
    skillService.answerQuestion = function (Userid, UserAnswer) {
        postdata={user:Userid,answer: UserAnswer};
        return $http.post('/api/skills/questions/', postdata)
            .then(function (data) {
                return data.data;
                
            });
    };
    
    skillService.deleteAnswer = function(answerid) {
        return $http.delete('/api/skills/answer/' + answerid + '/')
            .then(function (data) {
                return data.data;

            });
    };
    
    skillService.listUserAnswers = function () {
        return $http.get('/api/skills/answer/')
            .then(function (data) {
                return data.data;
                
            });
        
    };

    return skillService;
});


