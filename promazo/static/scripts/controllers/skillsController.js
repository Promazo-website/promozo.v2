/**
 * Created by marc on 05/06/16.
 */
promazo.controller('skillsController',function( $scope,$http,$mdToast,$timeout,SkillsService) {
    
    $scope.loginQuestion={Question:null,Answers:null,UserAnswer:null};
    $scope.nextQuestion=false;
    
    
    $scope.newQuestion = function() {
        SkillsService.getLoginQuestion()
            .then(function (data) {
                $scope.loginQuestion.Question=data;
                $scope.loginQuestion.Answers=data.answers;
                $scope.loginQuestion.UserAnswer=null;
                $scope.nextQuestion=false;
                $scope.setCurrentPage('login_question');
            },
                function() {
                    if ($scope.nextQuestion==true) {
                        $scope.setCurrentPage('no_questions');
                    } else {
                        $scope.setCurrentPage("home");
                    };

                }
            );
    };

    $scope.skillsQuestion = function () {
        $scope.nextQuestion=true;
        $scope.newQuestion();
    };

    $scope.answerQuestion =  function(answer) {
        SkillsService.answerQuestion($scope.currentUser.id, answer)
            .then(function(data) {
                $scope.nextQuestion=true;
            });
    };

    $scope.endQuestions = function() {
        $scope.setCurrentPage("home");
    };
    
    if($scope.currentScore < 10) {
        $scope.newQuestion();
    };



});
