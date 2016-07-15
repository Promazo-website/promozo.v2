/**
 * Created by dev on 10/28/14.
 */

/**
 Module to take care of the applications questions popup overlay window
 **/

var ApplyManager = (function () {
    "use strict";

    // Global apply list (id's only)
    var getApplyQuestions;
    var getRole;

    /**
     * Given a project_id and role_id fetch details and display them with the
     * popup overlay plugin.
     *
     * @param project_id
     * @param role_id
     */
    getApplyQuestions = function(project_id, role_id){
        $.get('/student/apply/'+project_id+'/'+role_id+'/', function(data){
            $("div#questions_display").html(data);
        });
    };

    getRole = function(project_id){
        $.get('/student/apply/'+project_id+'/', function(data){
            $("div#role_display").html(data);
        });
    };

    return {
        GetRole:getRole,
        GetApplyQuestions:getApplyQuestions
    };
}());