/**
 * Created by marc on 20/05/16.
 */
promazo.factory('ProfileService', function ($http) {
  var profileService = {};
    
    profileService.get_user_profile = function(){
        return $http.get('/api/user/profile/')
        .then( function(data){
            return data.data;
        });
        
    };

    profileService.get_user_score =  function () {
        return $http.get('/api/user/score/')
            .then( function(data){
                return data.data;
            })

    }
    
    profileService.update_profile = function (profiledata,type) {
        postdata = profiledata;
        delete postdata.avatarImage;
        if(type=='business') {
            profile_url = '/api/core/user/business/' + profiledata.id +'/';
        }
        else {
            profile_url = '/api/core/user/student/' +profiledata.id +'/';
        };
        return $http.put(profile_url, postdata)
              .then( function(data){
                  return data.data;
              });
    };
    
    profileService.get_profile = function(profileid){
        return $http.get('/api/profile/' + profileid + '/')
        .then( function(data){
            return data.data;
        });
        
    };
    
    profileService.search_profile = function (search_text) {
        return $http.get('/api/search/?search_text='+search_text)
            .then( function(data) {
                return data.data;
            })
    }
    


  return profileService;
});
