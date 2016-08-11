/**
 * Created by marc on 8/7/16.
 */
promazo.controller('ProjectsController',function( $scope,$log,$mdDialog,ProjectResource,ProjectPlaceResource,
                                               ProjectTaskResource,SkillResource,
                                                  ProjectRoleResource,PodsResource,PodsRoleTypesResource) {
    

    $scope.ConfirmDelete = $mdDialog.confirm()
        .title('Are you sure you want to Delete this item')
        .textContent('There is no undo, so please confirm before deletion')
        .ok("It's ok, Delete it")
        .cancel("'Oh no. don't do it");

    $scope.SkillsList=SkillResource.query();
    $scope.RoleTypeList = PodsRoleTypesResource.query();
    $scope.PodList = PodsResource.mypods();
    $scope.fabMenu="false";
    $scope.projectsPage="Projects";

    $scope.setProjectPage = function(page) {
        $scope.projectsPage = page;
    }
    $scope.currentProject={};
    $scope.currentTask ={};
    $scope.currertRole ={};
    $scope.currentPlace={};
    
    $scope.showCreateProject=false;
    $scope.showCreateTask =false;
    $scope.showCreateRole=false;
    $scope.showCreatePlace=false;
    

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
    
    $scope.ShowProjects = function() {
        $scope.projectsPage="Projects";
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
        $scope.projectsPage="EditProject";
    };

    $scope.UpdateProject = function() {
        $scope.currentProject.$update({id:$scope.currentProject.id},function(){
            $scope.ProjectList =  ProjectResource.query({id:'all'});
            $scope.projectsPage="Projects";
            $scope.openToast('Project Updated');
        })
    };
    
    $scope.ShowTasks = function (project) {
        $scope.projectsPage="Tasks";
        $scope.newTask= new ProjectTaskResource({project:project.id,updated_by:$scope.currentUser.id});
        $scope.currentProject = project;
        $scope.TaskList = ProjectTaskResource.list({id:project.id});


    };

    $scope.EditTask = function (task) {
        $scope.currentTask=task;
        $scope.projectsPage="EditTask";
    };

    $scope.UpdateTask = function () {
        $scope.currentTask.$update({id:$scope.currentTask.id}, function(){
            $scope.TaskList = ProjectTaskResource.list({id:$scope.currentProject.id});
            $scope.projectsPage="Tasks";
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
        $scope.newRole= new ProjectRoleResource({project:project.id,updated_by:$scope.currentUser.id});
        $scope.RoleList = ProjectRoleResource.list({id:project.id});
        $scope.projectsPage='Roles';

    };

    $scope.EditRole = function (role) {
        $scope.currentRole=role;
        $scope.projectsPage="EditRole";

    };

    $scope.UpdateRole = function() {
        $scope.currentRole.$update({id:$scope.currentRole.id},function(){
            $scope.RolesList = ProjectRoleResource.list({id:$scope.currentProject.id});
            $scope.projectsPage="Roles";
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

    $scope.ShowPlaces = function (project) {
        $scope.currentProject=project;
        $scope.RoleList =  ProjectRoleResource.list({id:$scope.currentProject.id});
        $scope.newPlaces={number:0,role:null,start_date:null,end_date:null};
        $scope.PlacesList = ProjectPlaceResource.list({id:$scope.currentProject.id});
        $scope.projectsPage='Places';

    };

    $scope.EditPlace = function (place) {
        $scope.currentPlace = place;
        $scope.projectsPage="EditPlace";
    };

    $scope.UpdatePlace = function() {
        $scope.currentPlace.$update({id:$scope.currentPlace.id},function() {
            $scope.PlacesList = ProjectPlaceResource.list({id:$scope.currentProject.id});
            $scope.projectsPage="Places";
        })
    };

    $scope.CreatePlace = function(){
        var count =Number($scope.newPlaces.number);
        for(var i=0; i < count; i++) {
            newPlace = new ProjectPlaceResource({startdate:$scope.newPlaces.start_date,
                enddate:$scope.newPlaces.end_date,
                ProjectRole:$scope.newPlaces.role,
                updated_by:$scope.currentUser.id});
            newPlace.$save(function(){
                $scope.PlacesList = ProjectPlaceResource.list({id:$scope.currentProject.id});
                $scope.showCreatePlace=false;
                $scope.openToast('Places Created');
            });
            
        }

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
                    $scope.PlacesList =  ProjectPlaceResource.list({id:$scope.currentProject.id});
                })
            })
    };


});