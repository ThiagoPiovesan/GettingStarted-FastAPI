# /*==========================================================*\
# |      /=============================================\       |
# |     ||  -    FastAPI Framework implementation    - ||      |
# |     ||  -      Adapted by: Thiago Piovesan       - ||      |
# |     ||  -         Versao atual: 1.0.0            - ||      |
# |      \=============================================/       |
# \*==========================================================*/

# Link do Github: https://github.com/ThiagoPiovesan

#==================================================================================================#
# Bibliotecas utilizadas:
import os
import databases
import sqlalchemy

# Setting database url
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
TEST_DATABASE = os.getenv('TEST_DATABASE', 'false') in ('true', 'yes')

# force_rollback doesn't let me write the data to the database when I'm testing it
database = databases.Database(DATABASE_URL, force_rollback=TEST_DATABASE) 
metadata = sqlalchemy.MetaData()
