/*global $:false */
/*Used by JSLin to not give errors with $ */

/**
 * Module to take care of the whole project listing page on the student side.
 */
var ProjectManager = (function () {
    "use strict";  // Don't forget to turn on strict checking!

    // Global project list (id's only)
    var resizeDivs;

    /**
     * Resize the project list and project details div to 90% of the viewport
     */
    resizeDivs = function () {
        var height = $(window).height(),
            ninetypc = (90 * height) / 100;

        ninetypc = parseInt(ninetypc, 10) + 'px';
        $("#project_list").css('height', ninetypc);
    };

    return {
        ResizeDivs: resizeDivs
    };

}());