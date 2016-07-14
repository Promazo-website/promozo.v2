from django.shortcuts import render,render_to_response
from django.template.context import RequestContext



def Main(request):
    '''
    Render the main angular page
    '''
    return render_to_response('base.html',{}, context_instance=RequestContext(request))

def Verification(request,DateHash,UserHash):
    """
    Render an Angular Interface to validate a user and allow them to set their password
    """
    c={'initData':"callType='validate';DateHash='%s';UserHash='%s';" % (DateHash,UserHash)}
    return render_to_response('base.html',c, context_instance=RequestContext(request))