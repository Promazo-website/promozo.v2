/**
 * Created by marc on 8/9/16.
 */
promazo.controller('RoleController',function( $scope,$log,RoleResource) {
    $scope.role={};
    
    $scope.setRole = function(Roleid){
        if(Roleid){
            $scope.role=RoleResource.get({id:Roleid});
        }

    }
});