from django.shortcuts import render

def results(request):
    prms = dict(request.GET)

    ex_a_notdetermined = not prms.has_key('a') or \
                        (prms.get('a')[0]=='')
    ex_a_notint = not(ex_a_notdetermined) and \
                  not(prms.get('a')[0].strip('-').isdecimal())
    ex_a_zero = not(ex_a_notdetermined) and \
                not(ex_a_notint) and (prms['a'][0]=='0')
    ex_b_notdetermined = not prms.has_key('b') or \
                        (prms.get('b')[0]=='')
    ex_b_notint = not(ex_b_notdetermined) and \
                  not(prms.get('b')[0].strip('-').isdecimal())
    ex_c_notdetermined = not prms.has_key('c') \
                         or (prms.get('c')[0]=='')
    ex_c_notint = not(ex_c_notdetermined) and \
                  not(prms.get('c')[0].strip('-').isdecimal())
    prms['ex_a_notdetermined'] = ex_a_notdetermined
    prms['ex_a_notint'] = ex_a_notint
    prms['ex_a_zero'] = ex_a_zero
    prms['ex_b_notdetermined'] = ex_b_notdetermined
    prms['ex_b_notint'] = ex_b_notint
    prms['ex_c_notdetermined'] = ex_c_notdetermined
    prms['ex_c_notint'] = ex_c_notint
    
    params_OK = not(ex_a_notdetermined) and not(ex_a_notint) and \
                not(ex_a_zero) and not(ex_b_notdetermined) and \
                not(ex_b_notint) and not(ex_c_notdetermined) and \
                not(ex_c_notint)
    prms['params_OK'] = params_OK
    if params_OK:
        a = int(prms.get('a')[0])
        b = int(prms.get('b')[0])
        c = int(prms.get('c')[0])
        d = int(b**2.0 - 4.0*a*c)
        prms['d'] = d
        prms['d_neg'] = d < 0 
        prms['d_pos'] = d > 0
        prms['d_zero'] = d == 0        
        if d>=0:
          x1 = (-b + d**(1/2.0)) / 2.0*a
          x2 = (-b - d**(1/2.0)) / 2.0*a
          prms['x1'] = x1
          prms['x2'] = x2

    return render(request, 'results.html', prms)
