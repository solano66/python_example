# 從模組 import 特定函式
from useMySql import SqlQuery

if __name__ == "__main__":
    my_train_titanic = SqlQuery("my_train_titanic")
    tables = my_train_titanic.show_table()

    print(tables)

    sql = """
            SELECT * FROM passengers;
        """
    data_list = my_train_titanic.query(sql)

    print(len(data_list))
    print(data_list[:5])

    for data in data_list:
        if data['age'] != None and data['sex'] == 'male' and data['age'] > 70:
            # print(data['name'])
            with open('passengers_data.txt', 'a') as f:
                f.write(data['name']+ '\n')
