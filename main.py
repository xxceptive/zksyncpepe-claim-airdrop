from loguru import logger
from utils.addLogger import add_logger
from sdk.zksyncpepe import main_claim

with open('Data/wallets.txt') as apw:
    wallets = [row.strip() for row in apw]


if __name__ == '__main__':
    add_logger()

    logger.info('START')
    main_claim(wallets)
