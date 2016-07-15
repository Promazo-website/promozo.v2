/*global $:false */
/*Used by JSLin to not give errors with $ */

/**
 * Module to take care of the student form (on signup and edit profile)
 */
var StudentFormManager = (function () {
    "use strict";  // Don't forget to turn on strict checking!

    // Global project list (id's only)
    var initWizard,
        mainInit,
        validateWizardStep,
        handleFileSelect,
        validateField,
        fieldOk,
        formOK,
        fieldError,
        fetchUniv;

    var form_rules = {
            0: {
                "required": ["#id_first_name", "#id_last_name", "#id_mobile_number", "#id_addr_street", "#id_addr_city","#id_addr_state","#id_addr_zip"],
                "email":["#id_email"],
                "match":["#id_password","#id_confirm"]
            },
            1:{
                "required":["#id_university","#id_college","#id_major","#id_minor","#id_major_gpa","#id_grad_year","#id_overall_gpa"]
            }
        };
    var form_rules_match = {
        "#id_password":"#id_confirm",
        "#id_confirm":"#id_password"
    };

    // Will hold association field_id -> rule
    // Created during init and used for quick lookup
    var field_rules = {};

    validateField = function(field_id,type){
     // Apply different validation depending on what we are validating
            switch(type){
                case "required":
                    return ($(field_id).val());
                case "email":
                    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
                    return ($(field_id).val() && re.test($(field_id).val()));
                case "match":
                    return ($(field_id).val() && $(field_id).val() == $(form_rules_match[field_id]).val());

            }
        return false;

    };

    fieldOk = function(field_id){
        // If the field was a match we need to also decolor its related field
        if (field_rules[field_id] == "match"){
            $(form_rules_match[field_id]).removeClass('field_error');
        }
        $(field_id).removeClass('field_error');

        // Also removes the message if no more errors
        if (formOK())  $("#validation_message").hide();
    };

    fieldError = function(field_id){
        // If the field was a match we need to also color its related field
        if (field_rules[field_id] == "match"){
            $(form_rules_match[field_id]).addClass('field_error');
        }
        $(field_id).addClass('field_error');

        // Show the message no matter what
        $("#validation_message").show();
    };

    formOK = function(){
        return $("input.field_error, select.field_error").length == 0;
    };

    validateWizardStep = function(step){
        // Retrieve the current tab

        var currentIndex = $('#rootwizard').bootstrapWizard('currentIndex');

        // Override the current index if step passed
        if (!isNaN(parseFloat(step))) currentIndex = step;
        $.each(form_rules[currentIndex],function(idx,item){
            $.each(item, function(field_index,field_id){

                if (!validateField(field_id,idx)) fieldError(field_id);
            });
        });

        return formOK();
    };

    /**
     * Initialize the wizard for the student form.
     */
    initWizard = function () {
        var wizard = $('#rootwizard');

        // Create the wizard
        // Make sure that everytime we change tabs, we update the buttons (next,last)
        wizard.bootstrapWizard({
            'tabClass': 'nav nav-pills', onTabShow: function (tab, navigation, index) {

                var total = navigation.find('li').length;
                var current = index + 1;

                // If it's the last tab then hide the next
                if (current >= total) {
                    wizard.find('.wizard .next').hide();
                } else {
                    wizard.find('.wizard .next').show();
                }

                // If its the first tab then hide the previous
                if (current == 1) {
                    wizard.find('.wizard .previous').hide();
                } else {
                    wizard.find('.wizard .previous').show();
                }
            },
            onNext:validateWizardStep,
            onPrevious:validateWizardStep,
            onTabClick:validateWizardStep
        });


        // When click on the finish button, send the form
        $('div#rootwizard .finish').click(function () {
            if (!validateWizardStep(0) || !validateWizardStep(1) ) return false;
            $("form#userform").submit();
        });
    };

    /**
     * Handles the selection of new files for profile and background pictures.
     * Display them immediately.
     * @param evt
     */
    handleFileSelect = function (evt) {
        var files = evt.target.files; // FileList object

        // Loop through the FileList and render image files as thumbnails.
        for (var i = 0, f; f = files[i]; i++) {

            // Only process image files.
            if (!f.type.match('image.*')) {
                continue;
            }

            var reader = new FileReader();
            var inputFile = $(this);

            // Closure to capture the file information.
            reader.onload = (function (theFile) {
                return function (e) {
                    // Render thumbnail.
                    inputFile.parent().find('.preview').attr('src', e.target.result);
                };
            })(f);

            // Read in the image file as a data URL.
            reader.readAsDataURL(f);
        }
    };

    /**
     * Main Initialization:
     * - Initialize the bootstrap popover
     * - Fetch the currently selected university
     * - Register the change event of the university list
     */
    mainInit = function () {
        // Initialize the popovers
        $('button.pop').popover({html: true, container: 'body'});

        // Ftech the currently selected university
        fetchUniv($('select#id_university').val());

        // When a new university is selected => update the fields
        $('select#id_university').change(function () {
            if ($(this).val()) {
                fetchUniv($(this).val());
            } else {
                $("#univstreet").val("");
                $("#univcity").val("");
                $("#univzip").val("");
                $("#univstate").val("");
            }
        });

        // Initializes the field_rules that provides quickly access to the rule associated to a field
        $.each(form_rules,function(tab,rules){
            $.each(rules, function(rule,fields){
                $.each(fields,function(id,field){
                    field_rules[field] = rule;
                });
            });
        });


        // Display the pics when selected
        $('#id_profile_pic').change(handleFileSelect);
        $('#id_background_pic').change(handleFileSelect);

        // Init the validation

        $("input[type='text'], select, input[type='password']").change(function(){
            // Remove message if no element has the error class
            if ($('.field_error').length == 0)  $("#validation_message").hide();

            // Check if the field is still in errors
            // For that we need the rule first
            var id = "#"+$(this).attr('id');
            // No validation for this field
            if (!field_rules.hasOwnProperty(id)) return;

            // Look into our rules to discover which rule applies to our field
            if (validateField(id,field_rules[id])) {
                fieldOk(id);
            } else if(!$(this).hasClass('field_error')){
                fieldError(id);
            }
        });
    };

    /**
     * Called when a university is selected.
     * Updates the different input fields with the univ info
     *
     * @param univ_id ID of the university we need to fetch
     */
    fetchUniv = function (univ_id) {
        if (!univ_id){
            return;
        }
        $.ajax({
            type: "POST",
            url: '/university/',
            data: {university_id: univ_id},
            dataType: 'json',
            async: 'false',
            success: function (data) {
                // Fill the form
                $("#univstreet").val(data["street"]);
                $("#univcity").val(data["city"]);
                $("#univzip").val(data["zip"]);
                $("#univstate").val(data["state"]);
            }
        });
    };


    return {
        InitWizard: initWizard,
        MainInit: mainInit,
        FetchUniv: fetchUniv
    };

}());

$(document).ready(function () {
    StudentFormManager.MainInit();
    StudentFormManager.InitWizard();
});