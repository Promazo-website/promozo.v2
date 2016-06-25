/**
 * Created by marc on 22/05/16.
 */
promazo.factory('OrgService', function ($http) {
    var OrgService = {};
    
    OrgService.findOrganisation = function(Email){
        return $http.get('/api/core/user/registration/organisation/?email='+ Email)
          .then(function(data){
                return data.data;
          });
    };
    
    OrgService.createUniversity = function (name) {
        return $http.post('/api/core/university/',{name: name})
            .then(function(data){
                return data.data;
            });
    };
    
    OrgService.createBusiness= function (name) {
        return $http.post('/api/core/business/',{name: name})
            .then(function(data){
                return data.data;
            });
    };
  return OrgService;
});