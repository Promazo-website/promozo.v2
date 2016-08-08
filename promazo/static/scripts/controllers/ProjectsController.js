/**
 * Created by marc on 8/7/16.
 */
promazo.controller('TestsController',function( $scope,$log,$mdDialog,ProjectResource,ProjectPlaceResource,
                                               ProjectTaskResource,ProjectRoleResource) {
    

    $scope.ConfirmDelete = $mdDialog.confirm()
        .title('Are you sure you want to Delete this item')
        .textContent('There is no undo, so please confirm before deletion')
        .ok("It's ok, Delete it")
        .cancel("'Oh no. don't do it");

    $scope.projectsPage="projects";
    $scope.currentProject={};
    $scope.currentTask ={};
    $scope.currertRole ={};
    $scope.currentPlace={};
    
    $scope.showCreateProject=false;
    $scope.showCreateTask =false;
    $scope.showCreateRole=false;
    $scope.showCreatePlace=false;
    
    $scope.showEditProject=false;
    $scope.showEditTask=false;
    $scope.showEditRole=false;
    $scope.showEditPlace=false;
    
    
    $scope.ProjectList =  ProjectResource.query({id:'all'});
    $scope.TaskList=[];
    $scope.RoleList=[];
    $scope.PlaceList=[];
    
    $scope.newProject = new ProjectResource();

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
    
    $scope.toggle_CreateProject = function(){
        $scope.showCreateProject=toggleVal($scope.showCreateProject);
    };
    
    $scope.toggle_CreateTask = function(){
        $scope.showCreateTask=toggleVal($scope.showCreateTask);
    };
    
    $scope.toggle_CreateRole = function(){
        $scope.showCreateRole=toggleVal($scope.showCreateRole);
    };
    
    $scope.toggle_CreatePlace = function(){
        $scope.showCreatePlace = toggleVal($scope.showCreatePlace);
    };

    $scope.CreateProject = function(){
        $scope.newProject.$save(function(data){
            $scope.ProjectList =  ProjectResource.query({id:'all'});
            $scope.showCreateProject=false;
            $scope.openToast('Project Created');
        })
    };

    $scope.EditProject = function(project){
        $scope.currentProject=project;
        $scope.showEditProject=true;
    };

    $scope.UpdateProject = function() {
        $scope.currentProject.$update(function(){
            $scope.ProjectList =  ProjectResource.query({id:'all'});
            $scope.showEditProject=false;
            $scope.openToast('Project Updated');
        })
    };
    
    $scope.ShowTasks = function (project) {
        $scope.newTask= new ProjectTaskResource({project:project.id});
        $scope.currentProject = project;
        $scope.TaskList = ProjectTaskResource.list({id:project.id});
        $scope.projectsPage='tasks';

    };

    $scope.EditTask = function (task) {
        $scope.currentTask=task;
        $scope.showEditTask=true;
    };

    $scope.UpdateTask = function () {
        $scope.currentTask.$update( function(){
            $scope.TaskList = ProjectTaskResource.list({id:project.id});
            $scope.showEditTask=false;
        })
    };

    $scope.CreateTask = function(){
        $scope.newTask.$save(function(data){
            $scope.TaskList =  ProjectTaskResource.list({id:$scope.currentProject.id});
            $scope.showCreateTask=false;
            $scope.openToast('Task Created');
        })
    };

    $scope.ShowRoles = function (project) {
        $scope.currentProject = project;
        $scope.newRole= new ProjectRoleResource({project:project.id});
        $scope.RolesList = ProjectRoleResource.list({id:project.id});
        $scope.projectsPage='roles';

    };

    $scope.EditRole = function (role) {
        $scope.currentRole=role;
        $scope.showEditRole=true;

    };

    $scope.UpdateRole = function() {
        $scope.currentRole.$update(function(){
            $scope.RolesList = ProjectRoleResource.list({id:project.id});
            $scope.showEditRole=false;
            $scope.openToast('Role Updated')
        })
    };

    $scope.CreateRole = function(){
        $scope.newRole.$save(function(data){
            $scope.RoleList =  ProjectRoleResource.list({id:$scope.currentProject.id});
            $scope.showCreateRole=false;
            $scope.openToast('Role Created');
        })
    };

    $scope.ShowPlaces = function (role) {
        $scope.currentRole = role;
        $scope.newPlace = new ProjectPlaceResource({ProjectRole: role.id});
        $scope.PlacesList = ProjectPlaceResource.list({id:role.id});
        $scope.projectsPage='places';

    };

    $scope.EditPlace = function (place) {
        $scope.currentPlace = place;
        $scope.showEditPlace=true;
    };

    $scope.UpdatePlace = function() {
        $scope.currentPlace.$update(function() {
            $scope.PlacesList = ProjectPlaceResource.list({id:$scope.currentRole.id});
            $scope.showEditPlace=false;
        })
    };

    $scope.CreatePlace = function(){
        $scope.newPlace.$save(function(data){
            $scope.PlaceList =  ProjectRoleResource.list({id:$scope.currentRole.id});
            $scope.showCreatePlace=false;
            $scope.openToast('Place Created');
        })
    };

    $scope.DeleteProject = function(project){
        $mdDialog.show($scope.ConfirmDelete)
            .then(function(){
                project.$delete({id:project.id}, function(){
                    $scope.ProjectList =  ProjectResource.query({id:'all'});
                })
            })
    };

    $scope.DeleteTask = function(task){
        $mdDialog.show($scope.ConfirmDelete)
            .then(function(){
                task.$delete({id:task.id}, function(){
                    $scope.TaskList =  ProjectTaskResource.list({id:$scope.currentProject.id});
                })
            })
    };

    $scope.DeleteRole = function(role){
        $mdDialog.show($scope.ConfirmDelete)
            .then(function(){
                role.$delete({id:role.id}, function(){
                    $scope.RoleList =  ProjectRoleResource.list({id:$scope.currentProject.id});
                })
            })
    };

    $scope.DeletePlace = function(place){
        $mdDialog.show($scope.ConfirmDelete)
            .then(function(){
                place.$delete({id:place.id}, function(){
                    $scope.PlaceList =  ProjectPlaceResource.list({id:$scope.currentRole.id});
                })
            })
    };
});