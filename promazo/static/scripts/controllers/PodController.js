/**
 * Created by marc on 8/7/16.
 */
promazo.controller('PodController',function( $scope,$log,$mdDialog,PodsResource,PodMembersResource,
                                             PodsRolesResource,PodsPermissionsResource) {


    $scope.ConfirmDelete = $mdDialog.confirm()
        .title('Are you sure you want to Delete this item')
        .textContent('There is no undo, so please confirm before deletion')
        .ok("It's ok, Delete it")
        .cancel("'Oh no. don't do it");

    function toggleVal(val){
        if(val){
            return false;
        }else{
            return true;
        }
    }

    $scope.RoleList =  PodsRolesResource.query();

    $scope.PodsPage="Pods";
    
    $scope.ViewPods = function(){
      $scope.PodsPage="Pods";  
    };
    
    //list my pods

    $scope.PodList = PodsResource.mypods();

    //show create pod form

    $scope.showCreatePod=false;
    $scope.newPod= new PodsResource({updated_by:$scope.currentUser.id});

    $scope.toggle_CreatePod = function(){
        $scope.showCreatePod=toggleVal($scope.showCreatePod);
    };

    //create pod

    $scope.CreatePod = function() {
        $scope.newPod.$save(function(data){

            newMember= new PodMembersResource({pod:data.id,member:$scope.currentUser.id});
            newMember.$save(function () {
                $scope.PodList = PodsResource.mypods();
                $scope.showCreatePod=false;
            });
            $scope.openToast('New Pod Created')
        })
    };

    //open Modify Pod

    $scope.currentPod={};

    $scope.EditPod = function(pod) {
        $scope.currentPod=pod;
        $scope.PodsPage="EditPod";
    };
    //modify pod
    $scope.UpdatePod = function() {
        $scope.currentPod.$update({id:$scope.currentPod.id, updated_by:$scope.currentUser.id},
        function(data){
            $scope.PodList = PodsResource.mypods();
            $scope.PodsPage="Pods";
        })
    };

    //delete pod

    $scope.DeletePod = function(pod) {
        $mdDialog.show($scope.ConfirmDelete)
            .then(function () {
                pod.$delete({id: pod.id}, function () {
                    $scope.PodList = PodsResource.mypods();
                })
            })
    };

    //view Pod Members
    $scope.PodMembers=[];

    $scope.ViewPodMembers = function(pod){
        $scope.currentPod=pod;
        $scope.PodMembers = PodMembersResource.members({id:pod.id});
        $scope.PodsPage='Members';

    };

    //Add Pod Member
    $scope.showAddMember = false;

    $scope.toggle_AddMember = function() {
        $scope.available_users =PodsResource.available_users({id:$scope.currentPod.id});
        $scope.showAddMember = toggleVal($scope.showAddMember);
        $scope.newMember = new PodMembersResource({pod:$scope.currentPod.id});
    };
    
    $scope.AddMember = function() {
        $scope.newMember.$save(function(){
            $scope.PodMembers =  PodMembersResource.members();
            $scope.openToast('Member Added');
            $scope.showAddMember = false;
            $scope.PodMembers = PodMembersResource.members({id:$scope.currentPod.id});
        })
        
    };

    //remove Pod Member
    
    $scope.DeleteMember = function(member) {
        $mdDialog.show($scope.ConfirmDelete)
            .then(function(){
                member.$delete({id:member.id}, function(){
                    $scope.PodMembers =  PodMembersResource.members();
                })
            });

    };
    
});