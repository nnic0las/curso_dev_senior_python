#tipos de eventos 
#1. DEBUG
#2. INFO
#3. WARNING
#4. ERROR
#5. CRITICAL

import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("mensaje de depuracion")