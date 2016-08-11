/**
 * Created by marc on 8/11/16.
 */
promazo.controller('PodRecordController',function( $scope,$log,PodsResource) {
    $scope.pod={};
    
    $scope.setPod = function(userid){
        $scope.pod=PodsResource.get({id:userid})
    }
});