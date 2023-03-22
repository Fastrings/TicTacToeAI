from src.engine import PLAYERS, play
import psycopg2
from psycopg2.extras import execute_values
from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename) # read config from filename

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    
    return db # return parsed options

def get_player_id(player_name): # get player id, an int between 1 and 6 included. Player id 
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT id FROM "Robots" WHERE name = %s', (player_name, )) # execute query
        id = cur.fetchone() # fetch result of above query
    except (Exception, psycopg2.DatabaseError) as err:
        print(f'--{err}--')
    finally:
        if conn is not None:
            conn.commit()
            conn.close()
    
    return id

def repeated_battles(player1, player2, num, save):
    """
    This function is used to calculate statistics by plotting AIs against 
    each other any number num of times
    """

    cpt1, cpt2, cptD = 0, 0, 0
    conn = None
    player1_name, player1_algo = player1
    player2_name, player2_algo = player2
    values = [] # we prepare the values to send to the database
    id1 = get_player_id(player1_name) if save else None
    id2 = get_player_id(player2_name) if save else None

    for _ in range(num): # pitch 2 AIs against one another any num number of times
        result = play(player1_algo, player2_algo, notsilent=False)
        draw, winner = False, None
        if result == PLAYERS[0]:
            cpt1 += 1
            winner = id1
        elif result == PLAYERS[1]:
            cpt2 += 1
            winner = id2
        else:
            cptD += 1
            draw = True
        
        if save: # if we want to save to the database
            tup = (id1, id2, winner, draw)
            values.append(tup) # add current tally to list values to be sent to the database
    
    if save: # if we want to save to the database
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            execute_values(cur, 'INSERT INTO "results" VALUES %s', values) # only 1 call to the database because we prepared the values beforehand
            cur.close()
        except (Exception, psycopg2.DatabaseError) as err:
            print(f'--{err}--')
        finally:
            if conn is not None:
                conn.commit()
                conn.close()

    return [cpt1, cpt2, cptD]