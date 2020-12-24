import dbconfig

if __name__ == '__main__':
    user_id = input('user_id : ').split()
    try:
        cafe03_controller = dbconfig.MysqlController('110.10.130.118', 'lunaremote', 'lunaremote1014', 'lunatalk')
        user_info = ('id', 'user_status', 'db_ip', 'real_ip', 'process_ip', 'biztalk_db_ip', 'proxy_ip', 'proxy_port', 'lunatalk_flag', 'pay_plan')
        user_info_str = ','.join(user_info)
        query = """
                SELECT 
                    """ + user_info_str + """
                FROM 
                    lunatalk.users 
                WHERE 
                    user_id = %s
            """
        param = (user_id,)
        results = cafe03_controller.select_one(query, param)
        i = 0
        for result in results:
            print(f"{user_info[i]} : {result}")
            i += 1
    finally:
        cafe03_controller.conn.close()
