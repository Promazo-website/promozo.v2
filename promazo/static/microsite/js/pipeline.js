// Project and Pipeline Filtering
var $target, val, $inp, idx;
var tagFilters = [];
var categoryFilters = [];
var search_value = $('#project-list-filter, #student-list-filter').val();
var projectDisplay = $('#project-display').clone();
var studentDisplay = $('#student-details-panel').clone();

// Sets the project status
function setProjectStatus(project_id, status){
    // Prepare the alert
    var alertBox = $("div#alert-pipeline");
    var alertBody = alertBox.find('.alert-body');
    var alertTitle = alertBox.find('.alert-title');
    alertBox.removeClass('alert-success').removeClass('alert-danger');

    $.ajax('/admin_board/projects/set_status/'+project_id+'/',{
        data:{'status':status},
        method:'POST',
        success:function(){
            alertBox.addClass('alert-success');
            alertBody.html("The current project now has the status <strong>"+status+"</strong> successfully set.");
            alertTitle.html('Success');
            alertBox.show();
            $('#project-detail-iframe').attr('src', $('#project-detail-iframe').attr('src'))
        },
        error:function(){
            alertBox.addClass('alert-danger');
            alertBody.html("An error happened and the project has not been modified.");
            alertTitle.html('ERROR');
            alertBox.show();
        }
    })
}

// Checkbox input
$('input:checkbox').prop('checked', false);

// Dropdown category and tag filtering
$('.dropdown-menu a').on('click', function(event){
    event.preventDefault();
    if($(event.currentTarget).attr('data-tag_title')){
        $target = $(event.currentTarget);
        val = $target.attr('data-tag_title');
        $inp = $target.find('input');

        if((idx = tagFilters.indexOf(val)) > -1 ){
            tagFilters.splice(idx, 1);
            setTimeout(function(){$inp.prop('checked', false)}, 0);
        }else{
            tagFilters.push(val);
            setTimeout(function(){ $inp.prop('checked', true)}, 0);
        }
        $(event.target).blur();
        console.log(tagFilters);
    }else if($(event.currentTarget).attr('data-corporation_category')){
        $target = $(event.currentTarget);
        val = $target.attr('data-corporation_category');
        $inp = $target.find('input');

        if((idx = categoryFilters.indexOf(val)) > -1 ){
            categoryFilters.splice(idx, 1);
            setTimeout(function(){$inp.prop('checked', false)}, 0);
        }else{
            categoryFilters.push(val);
            setTimeout(function(){ $inp.prop('checked', true)}, 0);
        }
        $(event.target).blur();
        console.log(categoryFilters);
    }

    var tagCount = tagFilters.length;
    var categoryCount = categoryFilters.length;
    var selectedFilters = {category_list:categoryFilters, tag_list:tagFilters, search_value:search_value};
    var tag = $('#tag').find('.dropdown-text');
    var category = $('#category').find('.dropdown-text');
    console.log(selectedFilters);
    console.log(tagCount, categoryCount);
    $.ajax({
        url:'/admin_board/pipeline_filter',
        data: selectedFilters,
        dataType:'html',
        success: function(data){
            $('#project-display').replaceWith(projectDisplay.clone());
            $('#project-list-container').html(data);

            tag.html('Tag');
            category.html('Category');
            if(tagCount == 1)
                tag.html(tagFilters[0]);
            else if(tagCount > 1)
                tag.html(tag.html() + ' (' + tagCount + ')');
            else
                tag.html('Tag');

            if(categoryCount == 1)
                category.html(categoryFilters[0]);
            else if(categoryCount > 1)
                category.html(category.html() + ' (' + categoryCount + ')');
            else
                category.html('Category');
        },
        error:function(){
            alert("Failed to filter projects!")
        }
    });
    return false;
});

$(document).ready(function() {
    // Keyword Filter input textbox - Sends Category and Tag status when filtering
    $('#project-list-filter').keyup(function(){
        search_value = $(this).val();
        var selectedFilters = {category_list: categoryFilters, tag_list: tagFilters, search_value: search_value};
        $.ajax({
            cache: false,
            type: "GET",
            url: '/admin_board/pipeline_filter',
            data: selectedFilters,
            dataType: 'html',
            success: function(data){
                $('#project-display').replaceWith(projectDisplay.clone());
                $('#project-list-container').html(data);
            },
            error: function(){
                alert("Failed to search for projects!")
            }
        });
    });
    // End Project and Pipeline Filtering



    // when a student is clicked on make an ajax call to
    // show student details
    $('#student-list .student').click(function(){
        console.log("CAAAA");
        var student_id = $(this).data('id');
        console.log(student_id);
        var app_id = $(this).attr('data-app-id');
        window.location.href = '/admin_board/get_student_details?student_id='+student_id+'&application_id='+app_id;
        /*
        console.log(student_id);
        $.ajax({
            url:'../get_student_details',
            data: {student_id: student_id, application_id: app_id},
            success: function(data){
                var template = _.template($("#student-details-panel").html());
                $('#student-details').html(template(data));
                $('#student.selected').removeClass("selected");
                $(this).addClass("selected");
            },
            error: function(){
                alert("Failed to find the student!")
            }
        });*/
    });

    // Keyword Filter input textbox for student list
    $('#student-list-filter').keyup(function(){
        search_value = $(this).val();
        var role_id = $('.pipeline-nav').data('role_id');
        var phase_id = parseInt(getURLParameter('phase_id'));
        var selectedFilters = {role_id: role_id, phase_id: phase_id, search_value: search_value};
        console.log(selectedFilters);
        $.ajax({
            cache: false,
            type: "GET",
            url: '/admin_board/student_search_filter',
            data: selectedFilters,
            dataType: 'html',
            success: function(data){
                $('#student-details-panel').replaceWith(studentDisplay.clone());
                $('#student-list-container').html(data);
            },
            error: function(){
                alert("Failed to search for students!")
            }
        });
    });

    // Second tier phase filtering
    // Needs a view for the second tier filtering for th URL int he ajax call
    //$('#student-status-nav').click(function(){
    //    var role_id = $('.pipeline-nav').data('role_id');
    //    var phase_id = parseInt(getURLParameter('phase_id'));
    //    var selectedFilters = {role_id: role_id, phase_id: phase_id};
    //    console.log(selectedFilters);
    //    $.ajax({
    //        cache: false,
    //        type: "GET",
    //        url: '',
    //        data: selectedFilters,
    //        dataType: 'html',
    //        success: function(data){
    //            $('#student-details-panel').replaceWith(studentDisplay.clone());
    //            $('#student-list-container').html(data);
    //            $('.selected').removeClass('selected');
    //            $(this).addClass('.selected');
    //        },
    //        error: function(){
    //            alert("Failed to filter student list!");
    //        }
    //    })
    //});

    $(window).keydown(function(event){
        if(event.keyCode == 13) {
          event.preventDefault();
          return false;
        }
      });
});

// when a project title in project details is clicked on
// show role list
function loadPhaseTable(){
    var role_id = parseInt(getURLParameter('role_id'));
    var project_id = parseInt(getURLParameter('project_id'));
    var phase_id = parseInt(getURLParameter('phase_id'));
    var roleSourceKeys = {role_id: role_id, project_id: project_id, phase_id: phase_id};
    var studentListKeys = {role_id: role_id, phase_id: phase_id};
    console.log(roleSourceKeys);
    console.log(studentListKeys);
    // Loads Phase Table on page load
    $.ajax({
        url: '/admin_board/role_source_detail',
        data: roleSourceKeys,
        success: function(data){
            console.log(data);
            var template = _.template($('#role-table').html());
            // var template_content = _.template($('#role-content').html());
            $('#role-nav').html(template(data));
            // $('#role-content-panel').html(template_content(data));
            // Must load click events after template loads
            // collapseButton();
            loadPhaseButtonEvents();
        },
        error: function(){
            alert("Failed to find the roles!");
        }
    });
}
// When the phase is clicked in role_details, the filtered student list is loaded
function loadPhaseButtonEvents(){
    //$('.bottom:first-child').addClass('selected');
    $($('[data-phase_id="'+phase_id+'"]')[1]).addClass('selected');
    $('.phase-filter').click(function(){
        var selectedPhase = $(this);
        var role_id = $('.page-header').data('role_id');
        var phase_id = $(this).data('phase_id');
        var selectedFilters = {role_id: role_id, phase_id: phase_id};

        console.log(selectedFilters);
        $.ajax({
            url: '/admin_board/student_phase_filter',
            data: selectedFilters,
            dataType: 'html',
            success: function(data){
                $('#student-list-container').html(data);
                changeUrlParam ('phase_id', phase_id);
                $('.selected').removeClass('selected');
                selectedPhase.addClass('selected');
            },
            error: function(){
                alert("Failed to filter student list by phase.");
            }
        });
    });
}

// Go back button functions
function goBack() {
    window.history.back();
}

// Get parameters rom URL
function getURLParameter(name){
    return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null
}

// Change URL parameters
function changeUrlParam (param, value) {
    var currentURL = window.location.href+'&';
    var change = new RegExp('('+param+')=(.*)&', 'g');
    var newURL = currentURL.replace(change, '$1='+value+'&');

    if (getURLParameter(param) !== null){
        try {
            window.history.replaceState('', '', newURL.slice(0, - 1) );
        } catch (e) {
            console.log(e);
        }
    } else {
        var currURL = window.location.href;
        if (currURL.indexOf("?") !== -1){
            window.history.replaceState('', '', currentURL.slice(0, - 1) + '&' + param + '=' + value);
        } else {
            window.history.replaceState('', '', currentURL.slice(0, - 1) + '?' + param + '=' + value);
        }
    }
}

// Collapse Student List button event - recursive
function collapseButton(){
    $('#collapse-student-list').click(function(){
        var studentListPanel = $('#student-list-panel');
        var collapseStudentList = $('#collapse-student-list');
        var defaultStudentListPanel = $(studentListPanel).clone();
        var collapseStudentListButton = $(collapseStudentList).css('float', 'left');
        var collapsedStudentListPanel = $(studentListPanel).css({
            'width' : '24px',
            'height' : '23px',
            'position' : 'fixed',
            'top' : '210px',
            'left' : '35px'
        }).html(collapseStudentListButton);

        $(studentListPanel).replaceWith(collapsedStudentListPanel);

        $(collapseStudentList).click(function(){
            $('#student-list-panel').replaceWith(defaultStudentListPanel);
            collapseButton();
        });
    });
}

// When project list is loaded, call this to activate the clicks.
function projectDetailLoad() {
  $('.selected-project').click(function(){
      $('div.selected').removeClass("selected");
      $(this).addClass("selected");

      var url = $(this).data('url');
      console.log(url);
      $('#project-display').css('display', 'none');
      $('#project-detail-iframe').attr('src', url);
      $('#project-detail-iframe').css('display', 'block');
  });

  // $('#tag_filter ').click(function() {
  //     $('div.selected').removeClass("selected");
  //     $('#project-display').css('display', 'block');
  //     $('#project-detail-iframe').css('display', 'none');
  // });

  $('#project-list-filter').keyup(function() {
      $('div.selected').removeClass("selected");
      $('#project-display').css('display', 'block');
      $('#project-detail-iframe').css('display', 'none');
  });
}


//Make background white instead of uploaded student background
$(document).ready(function(){
    $("body").css("background" , "#FFFFFF");
    $('span[rel="nav_link"]').each(function(){
            $(this).click(function(){
                    window.location.href = $(this).attr('href');
            });
    });
});
