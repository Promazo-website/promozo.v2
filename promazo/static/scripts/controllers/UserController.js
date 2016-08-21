/**
 * Created by marc on 8/9/16.
 */
promazo.controller('UserController',function( $scope,$log,UserResource) {
    $scope.user={};
    
    $scope.setUser = function(userid){
        if(userid) {
            $scope.user = UserResource.get({id: userid})
        }
    }
});