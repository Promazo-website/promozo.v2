/**
 * Created by marc on 7/29/16.
 */
promazo.factory('ApplicationTestsService', function ($http) {
    var atService = {};

    //list questions

    atService.list_questions =  function () {
      return $http.get('/api/question/')
          .then(function (data) {
              return data.data;
          })
    };

    //create questions

    atService.create_question = function(question_details) {
        payload=question_details;
        return $http.post('/api/question/',payload)
            .then(function (data) {
                return data.data;
            })
    };

    //delete question

    atService.delete_question = function (question) {
        return $http.delete('/api/question/'+question+'/')
            .then(function (data) {
                return data.data;
            })
    };

    //modify question

    atService.modify_question = function (question_details) {
        payload=question_details;
        return $http.patch('/api/question/'+question_details.id+'/', payload)
            .then(function (data) {
                return data.data;
            })
    };

    //list tests

    atService.list_tests =  function () {
      return $http.get('/api/tests/')
          .then(function (data) {
              return data.data;
          })
    };

    //create tests

    atService.create_test = function(question_details) {
        payload=question_details;
        return $http.post('/api/test/',payload)
            .then(function (data) {
                return data.data;
            })
    };

    //delete test

    atService.delete_test = function (question) {
        return $http.delete('/api/test/'+question+'/')
            .then(function (data) {
                return data.data;
            })
    };

    //modify test

    atService.modify_test = function (question_details) {
        payload=question_details;
        return $http.patch('/api/test/'+question_details.id+'/', payload)
            .then(function (data) {
                return data.data;
            })
    };

    //add question to test

    atService.add_question = function(test, question) {
        question_list=test.questions;
        found=false
        for(item in question_list){
            if(question_list[item]===question.id) {
                found=true;
            }
        }
        if(!found) {
            question_list.push(question.id);
            payload={questions:question_list};
            return $http.patch('/api/tests/'+test.id+'/',payload)
                .then(function (data) {
                    return data.data;
                })
        }
    };

    //remove question from test
    atService.add_question = function(test, question) {
        question_list=[];
        found=false
        for(item in test.questions){
            if(test.questions[item]===question.id) {
                question_list.push(test.questions[item]);
            }
        }
        payload={questions:question_list};
        return $http.patch('/api/tests/'+test.id+'/',payload)
            .then(function (data) {
                return data.data;
            })
    };



    return atService;
});