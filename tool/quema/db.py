import sqlite3

CREATE_SQL = 'CREATE TABLE {} ({})'
INSERT_SQL = 'INSERT INTO {} VALUES ({})'
SELECT_SQL = 'SELECT {} FROM {} WHERE %s=?'
PAI_SHAN_TABLE = 'qm_pai_shan'
TABLE_MAP = {
    PAI_SHAN_TABLE: ['sha256', 'ps_data'],
}


def generate_sql(field_map):
    tb_map = {}
    for t_name, fields in field_map.items():
        tb_map.update({
            t_name: [
                CREATE_SQL.format(t_name, ','.join(fields)),
                INSERT_SQL.format(t_name, ','.join(['?' for _ in fields])),
                SELECT_SQL.format(','.join(fields), t_name)
            ]
        })
    return tb_map


TABLE_SQL = generate_sql(TABLE_MAP)


class DataBase:
    def __init__(self, filename, init=False):
        self.con = sqlite3.connect(filename)
        self.cur = self.con.cursor()
        if init:
            for tb_sqls in TABLE_SQL.values():
                self.con.execute(tb_sqls[0])
            self.con.commit()

    def save_data(self, datas, table_name=PAI_SHAN_TABLE):
        self.cur.executemany(TABLE_SQL[table_name][1], datas)
        return self.con.commit()

    def get_data(self, value, field='sha256', table_name=PAI_SHAN_TABLE):
        self.cur.execute(TABLE_SQL[table_name][2] % field, (value,))
        return self.cur.fetchall()

    def close(self):
        self.con.close()
