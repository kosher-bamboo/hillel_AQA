import logging

logger = logging.getLogger('Registration test')
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler('input_data.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
