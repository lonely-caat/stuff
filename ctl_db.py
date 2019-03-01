from magic.db import LexDB, StatsdDB

# db = LexDB('lex-qa-db.llnw.com', 'lex', 'qa_lex', 'qa_lex')
# db = LexDB('uat-lex-db-rw.llnw.com', 'uat_lex', 'mbilichenko', 'test')


def update_pswd_sharedkey(username=None):
    """Set pasword=test for all users when username=None
    When no username specified only shared key is generated,
    otherwise mfa disabled, change password to 'test'"""
    db = LexDB('lex-qa-db.llnw.com', 'lex', 'qa_lex', 'qa_lex')
    if not username:
        db.run_query('update user_profile set '
                            ' password="098f6bcd4621d373cade4e832627b4f6",'
                            ' api_shared_key_enc="06275c6e8cb3441fa18dbc69968b390488ae5f734abfd8e7a03541c5dba3552d45c1ba80c850ddccb05e111feb8e57b544a41b7ea6d8d062789fda5d98deab91964aff2a855b32e1d1855f4f4466893c", '
                            ' mfa_status=0')
    else:
        db.run_query('update user_profile set '
                            ' password="098f6bcd4621d373cade4e832627b4f6",'
                            ' api_shared_key_enc="06275c6e8cb3441fa18dbc69968b390488ae5f734abfd8e7a03541c5dba3552d45c1ba80c850ddccb05e111feb8e57b544a41b7ea6d8d062789fda5d98deab91964aff2a855b32e1d1855f4f4466893c", '
                            ' mfa_status=0'
                            ' where username="%s";' % username)


def update_pswd_sharedkey_staging(username=None):
    """Set pasword=test for all users when username=None
    When no username specified only shared key is generated,
    otherwise change password to 'test' disable mfa"""
    db = LexDB('uat-lex-db-rw.llnw.com', 'uat_lex', 'mbilichenko', 'test')
    if not username:
        db.run_query('update user_profile set '
                            ' api_shared_key_enc="06275c6e8cb3441fa18dbc69968b390488ae5f734abfd8e7a03541c5dba3552d45c1ba80c850ddccb05e111feb8e57b544a41b7ea6d8d062789fda5d98deab91964aff2a855b32e1d1855f4f4466893c", '
                            ' mfa_status=0')
    else:
        db.run_query('update user_profile set '
                            ' password="098f6bcd4621d373cade4e832627b4f6",'
                            ' api_shared_key_enc="06275c6e8cb3441fa18dbc69968b390488ae5f734abfd8e7a03541c5dba3552d45c1ba80c850ddccb05e111feb8e57b544a41b7ea6d8d062789fda5d98deab91964aff2a855b32e1d1855f4f4466893c", '
                            ' mfa_status=0 '
                            ' where username="%s";' % username)


def insert_stream_data():
    db = StatsdDB('statsd-qa-db.llnw.com', 'statsd', 'qa_statsd', 'qa_statsd')
    db.insert_stream_data(stream_id=db.get_flash_stream_report_id('webcam'), date='2015-09-09 00:00:00')

# db.process_user('QATest', 'limelight')
# db.process_user('servicenowhack', 'llnw')
update_pswd_sharedkey('cont_super')
# update_pswd_sharedkey_staging('aautrand')
# process_uat_users()
# db.process_user('test_admin', 'bulkget', user_role='company_admin')

# res = db.get_data('select name, report_id from report;')
# from pprint import pprint
# pprint(len(dict(res)))

# insert_stream_data()