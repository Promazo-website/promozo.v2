/**
 * Created by marc on 8/5/16.
 */
promazo.controller('TestsController',function( $scope,$log, TestsResource, QuestionResource, $mdDialog) {
    
    $scope.testsPage="tests";

    $scope.MyQuestionsList = QuestionResource.query({user:$scope.currentUser.id});
    $scope.PublicQuestions = QuestionResource.query({public:2});
    $scope.AllQuestions =QuestionResource.query({id:'all'});

    $scope.MyTestsList = TestsResource.query({user:$scope.currentUser.id});
    $scope.PublicTests = TestsResource.query({public:2});
    $scope.AllTests =TestsResource.query({id:'all'});

    $scope.showCreateTest=false;
    $scope.showCreateQuestion=false;
    
    $scope.newTest = new TestsResource({user:$scope.currentUser.id});
    $scope.newQuestion = new QuestionResource({user:$scope.currentUser.id});
    
    $scope.ConfirmDelete = $mdDialog.confirm()
        .title('Are you sure you want to Delete this item')
        .textContent('There is no undo, so please confirm before deletion')
        .ok("It's ok, Delete it")
        .cancel("'Oh no. don't do it");
    
    
    $scope.toggle_CreateTest = function(){
        if($scope.showCreateTest){
            $scope.showCreateTest=false;
        } else {
            $scope.showCreateTest=true;
        }
    };
    
        $scope.toggle_CreateQuestion = function(){
        if($scope.showCreateQuestion){
            $scope.showCreateQuestion=false;
        } else {
            $scope.showCreateQuestion=true;
        }
    };
    
    $scope.setTestsPage = function(data){
        $scope.testsPage=data;
    };
    
    $scope.CreateTest = function(){
      $scope.newTest.$save(function(data){
          $scope.openToast('test saved');
          $scope.newTest = new TestsResource({user:$scope.currentUser.id});
          $scope.MyTestsList = TestsResource.query({user:$scope.currentUser.id});
          $scope.showCreateTest=false;
      })  
    };
    
    $scope.CreateQuestion = function(){
      $scope.newQuestion.$save(function(data){
          $scope.openToast('test saved');
          $scope.newQuestion = new QuestionResource({user:$scope.currentUser.id});
          $scope.MyQuestionsList = QuestionResource.query({user:$scope.currentUser.id});
          $scope.showCreateQuestion=false;
      })  
    };
    
    $scope.EditTest = function(test){
        $scope.currentTest=test;
        $scope.testsPage="EditTest";
    };
    
     $scope.EditQuestion = function(question){
        $scope.currentQuestion=question;
        $scope.testsPage="EditQuestion";
    };
    
    
    $scope.UpdateTest = function(test) {
        test.$update({id:test.id},function(data){
            $scope.openToast('test updated');
            $scope.testsPage="tests";
        })
    };
    
    $scope.UpdateQuestion = function(question) {
        question.$update({id:question.id},function(data){
            $scope.openToast('question updated');
            $scope.testsPage="questions";
        })
    };

    $scope.DeleteTest = function(test){
        $mdDialog.show($scope.ConfirmDelete)
            .then(function(){
                test.$delete({id:test.id}, function (data) {
                        $scope.MyTestsList = TestsResource.query({user:$scope.currentUser.id});
                        $scope.PublicTests = TestsResource.query({public:2});

                })
            })

    };
    $scope.DeleteQuestion = function(question){
        $mdDialog.show($scope.ConfirmDelete)
            .then(function(){
                question.$delete({id:question.id}, function (data) {
                        $scope.MyQuestionsList = QuestionResource.query({user:$scope.currentUser.id});
                        $scope.PublicQuestions = QuestionResource.query({public:2});

                })
            })

    };
    
    
    
    
    $scope.TestsHelp = function() {
        $mdDialog.show(
            $mdDialog.alert()
                .clickOutsideToClose(true)
                .title('How to Make a test')
                .htmlContent('To make a test, first you must make the questions to go in the test.' +
                    'So hit the Create Question button and create a couple of questions.<br> When done' +
                    'Click the Create test button. This creates the Test container. You give your test ' +
                    'a name and select from the questions you have created to be in the test.' +
                    '<br>On the main Tests page, you can then edit a test, changing the questions within a test' +
                    'In the Questions page, you can select a question to edit.')
                .ok("Right, I'm ready")
        );
    };
});