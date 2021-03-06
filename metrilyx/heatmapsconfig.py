
from celery.schedules import crontab

from pprint import pprint

from metrilyxconfig import config
import celerytasks


def brokerHostStr(config):
    '''
    This converts the host array to a host:port string
    '''
    return ",".join(["%s:%s" %(h,config['port']) for h in config['host']])

CELERY_IMPORTS = config['celery']['tasks']
BROKER_URL = config['heatmaps']['transport']+\
    "://"+brokerHostStr(config['heatmaps']['broker'])+\
    "/"+str(config['heatmaps']['broker']['database'])

CELERY_RESULT_BACKEND = config['heatmaps']['transport']
CELERY_MONGODB_BACKEND_SETTINGS = config['heatmaps']['broker']
CELERY_ACCEPT_CONTENT = ['pickle', 'json']

## periodic tasks
CELERYBEAT_SCHEDULE = {}
if config["heatmaps"]["enabled"]:
    CELERYBEAT_SCHEDULE['heat-queries'] = {
        'task': 'metrilyx.celerytasks.run_heat_queries',
        'schedule': crontab(minute='*/1'),
        #'args': (1,2),
        #'options': { 'task_id': '' }
        }
        
if config["cache"]["enabled"]:
    CELERYBEAT_SCHEDULE['metric-cacher'] = {
        'task': 'metrilyx.celerytasks.cache_metrics',
        'schedule': crontab(minute=str("*/%d" %(config['cache']['interval'])))
    }
    ## TODO: re-work logic
    #CELERYBEAT_SCHEDULE['metric-cache-expirer'] = {
    #    'task': 'metrilyx.celerytasks.expire_metrics_cache',
    #    'schedule': crontab(minute=str("*/%d" %(config['cache']['retention_period'])))
    #}

