import psycopg2
import pandas as pd
from sqlalchemy import create_engine

def connect_posgresql():
    conf = {
        'user' : 'postgres',
        'password' : 'alienwarertx2070',
        'host' : 'localhost',
        'port' : '5432',
        'database' : 'postgres'
    }
    engine = create_engine(f'postgresql://{conf["user"]}:{conf["password"]}@{conf["host"]}:{conf["port"]}/{conf["database"]}')

    return engine


def main():

    datas = {
        '氏名':['山田太郎', '鈴木一郎', '佐藤花子', '田中次郎', '山本三郎'],
        '出席番号':[1, 2, 3, 4, 5],
        '数学':[90, 80, 70, 60, 50],
    }

    df = pd.DataFrame(datas).set_index('氏名')

    df.to_sql('test_table2', connect_posgresql(), if_exists='replace')


if __name__ == '__main__':
    main()
