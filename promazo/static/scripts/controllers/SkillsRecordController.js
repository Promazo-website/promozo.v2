/**
 * Created by marc on 8/11/16.
 */
promazo.controller('SkillsRecordController',function( $scope,$log,SkillResource) {
    $scope.skill={};
    
    $scope.setskill = function(userid){
        $scope.skill=SkillResource.get({id:userid})
    }
});