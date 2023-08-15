from src.main.configs.app import app
from src.infra.config import DBConnectionHandler, Base
import os

# criando o banco de dados.
db_conn = DBConnectionHandler()
engine = db_conn.get_engine()
Base.metadata.create_all(engine)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=True)
