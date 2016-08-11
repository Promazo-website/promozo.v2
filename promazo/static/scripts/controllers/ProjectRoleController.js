/**
 * Created by marc on 8/11/16.
 */
promazo.controller('ProjectRoleController',function( $scope,$log,ProjectRoleResource) {
    $scope.role={};
    
    $scope.setRole = function(Roleid){
        if(Roleid){
            $scope.role=ProjectRoleResource.get({id:Roleid});
        }

    }
});