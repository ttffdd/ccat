# Services options check
# Input:
#        global dictionary with defined 'active_service' key inside global_params
#        config result dictionary
# Output:
#        updated result dictionary
#

def check(global_params):
    results_dict = {'Services':{}}
# 'should be enable' services section
    if 'password-encryption' in global_params['active_service']:
        results_dict['Services']['password encryption'] = [2, 'ENABLED']
    else:
        results_dict['Services']['password encryption'] = [0, 'DISABLED', 'Turn it on to encrypt passwords']

    if 'tcp-keepalives-in' in global_params['active_service']:
        results_dict['Services']['tcp keepalives in']   = [2, 'ENABLED']
    else:
        results_dict['Services']['tcp keepalives in']   = [1, 'DISABLED', 'You may need it to prevent stuck sessions']

    if 'tcp-keepalives-out' in global_params['active_service']:
        results_dict['Services']['tcp keepalives out']   = [2, 'ENABLED']
    else:
        results_dict['Services']['tcp keepalives out']   = [1, 'DISABLED', 'You may need it to prevent stuck sessions']

# 'should be disable' services section
    if 'pad' in global_params['disable_service']:
        results_dict['Services']['pad'] = [2, 'DISABLED']
    else:
        results_dict['Services']['pad'] = [0, 'ENABLED', 'Turn it off to prevent potential unauthorized access']

    if 'config' in global_params['active_service']:
        results_dict['Services']['config'] = [0, 'ENABLED', 'Turn it off to prevent autoloading configuration file '
                                                            'from a network server']
    else:
        results_dict['Services']['config'] = [2, 'DISABLED']

    if 'udp-small-servers' in global_params['active_service']:
        results_dict['Services']['udp small servers']   = [0, 'ENABLED', 'Turn it off to prevent potential information '
                                                                         'leak and DOS attack']
    else:
        results_dict['Services']['udp small servers']   = [2, 'DISABLED']

    if 'tcp-small-servers' in global_params['active_service']:
        results_dict['Services']['tcp small servers']   = [0, 'ENABLED', 'Turn it off to prevent potential information '
                                                                         'leak and DOS attack']
    else:
        results_dict['Services']['tcp small servers']   = [2, 'DISABLED']

    if 'vstack' in global_params['disable_service']:
        results_dict['Services']['smart install'] = [2, 'DISABLED']
    else:
        results_dict['Services']['smart install'] = [0, 'ENABLED', 'Turn it off or block 4786 port (if "vstack" option '
                                                            'unavailable) to disable smart install configuration']
    if float(global_params['version']) < 12.1:
        if 'finger' in global_params['disable_service']:
            results_dict['Services']['finger'] = [2, 'DISABLED']
        else:
            results_dict['Services']['finger'] = [0, 'ENABLED', 'Disable it to prevent user to view other active users']

    return results_dict
