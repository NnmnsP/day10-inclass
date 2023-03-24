import logging
import psycopg2

def main():
    # connect to the PostgreSQL server
    logging.info('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="superpass15_22")
    logging.info('Connected.')

    # create table players
    logging.info('Creating table...')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS products')
    cur.execute('CREATE TABLE products (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, price float NOT NULL)')

    # insert a new player
    logging.info('Inserting data...')
    cur.execute("INSERT INTO products (name, price) VALUES ('Phone One', 300.00)")
    cur.execute("INSERT INTO products (name, price) VALUES ('Phone Two', 520.00)")
    conn.commit()

    # close the communication with the PostgreSQL
    cur.close()
    conn.close()
    logging.info('Done.')

if __name__ == "__main__":
    format = "SRV: %(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%F-%H-%M-%S")

    main()