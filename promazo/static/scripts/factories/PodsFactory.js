/**
 * Created by marc on 13/06/16.
 */
promazo.factory('PodService', function ($http) {
    var podService = {};

    podService.get_pods = function() {
        return $http.get('/api/pod/')
            .then(function(data){
                return data.data;
            })
    }    
    
    
    podService.get_pod_members = function(pod_id) {
        return $http.get('/api/pod/' + pod_id + '/')
            .then(function(data){
                return data.data;
            })
    }
    
    podService.get_user_pods = function() {
        return $http.get('/api/pod/user/')
            .then(function(data){
                return data.data;
            })
    }
    
    podService.has_permission = function(pod_id,permission) {
        return $http.get('/api/pod/permission/?pod=' + pod_id + '&permission='+ permission)
            .then(function(data){
                return data.data;
            })
    }


    return podService;
});