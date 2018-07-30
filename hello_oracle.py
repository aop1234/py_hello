import cx_Oracle

db=cx_Oracle.connect('rzkf','BP1-ME6T=CZJ','133.2.15.40:1521/rzkf')
print(db.version)