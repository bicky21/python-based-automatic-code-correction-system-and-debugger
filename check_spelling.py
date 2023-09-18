import itertools
import time
import sqlite3

database = sqlite3.connect('clang.db')
user = database.cursor()
error = 0

def find_and_replace(to_replace):
    user.execute("SELECT keyword FROM keys")
    
    data = user.fetchall()
    corrected_value = to_replace
    
    for row in data:
        from_replace = row[0]
        from_replace_data = [''.join(p) for p in itertools.permutations(from_replace)]
        
        for from_str in from_replace_data:
            if from_str in corrected_value:
                corrected_value = corrected_value.replace(from_str, from_replace)
                global error
                error += 1
                break
    
    return corrected_value

def error_count():
    return error
