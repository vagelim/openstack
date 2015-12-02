#!/usr/bin/env python
########################################
#    Required changes to nova.conf     #
########################################
# notification_driver=nova.openstack.common.notifier.rpc_notifier
# notification_topics = notifications
# notify_on_state_change = vm_and_task_state
# instance_usage_audit_period = hour
# instance_usage_audit = True
# default_notification_level = INFO
# notify_api_faults = true
###### Make sure you restart Nova#######

from kombu import Connection, Exchange, Queue
from pprint import pprint

nova_x = Exchange('nova', type='topic', durable=False)
info_q = Queue('notifications.info', exchange=nova_x, durable=False,
               routing_key='notifications.info')

def process_msg(body, message):
    print '='*80
    print body['event_type']
    print body['publisher_id']
    print body['timestamp']
    #pprint(body)
    message.ack()

#Change guest:guest and the hostname to match your configuration
with Connection('amqp://guest:guest@localhost//') as conn:
    with conn.Consumer(info_q, callbacks=[process_msg]):
        try:
            while True:
                conn.drain_events()
        except KeyboardInterrupt:
            exit()
