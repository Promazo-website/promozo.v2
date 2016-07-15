/*global $:false */
/*Used by JSLin to not give errors with $ */

/**
 * Module to take care of the whole project listing page on the student side.
 */
var CompanyManager = (function () {
    "use strict";  // Don't forget to turn on strict checking!

     // All function declarations
    var getCompanyDetails,
        resizeDivs;


    /**
     * Given a project ID, fetch details and display them in the
     * big black box in the middle of the screen.
     *
     * @param company_id
     * @param elem the project div clicked
     */
    getCompanyDetails = function(company_id, elem)
    {
        $("div.selected").removeClass("selected");
        $(elem).addClass("selected");
        $.get( '/companies/'+company_id+'/',  function( data ) {
            $( "div#project_display" ).html( data );
            });


    };


    /**
     * Resize the project list and project details div to 90% of the viewport
     */
    resizeDivs = function(){
        var height = $(window).height(),
            ninetypc = (90 * height) / 100;

        ninetypc = parseInt(ninetypc,10) + 'px';
        $("#project_list").css('height',ninetypc);
    };



    return {
        ResizeDivs: resizeDivs,
        GetCompanyDetails:getCompanyDetails
    };

}());