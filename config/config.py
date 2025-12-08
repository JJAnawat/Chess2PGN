from pathlib import Path

class Config:
    IMAGE_SIZE = (512, 512)
    IMAGE_DIR = Path("/home/anawat/JJ/Chula/Chess2PGN/data")

    # Chess board part configs
    BILATERAL_FILTER_D = 9
    BILATERAL_FILTER_SIGMA_COLOR = 75
    BILATERAL_FILTER_SIGMA_SPACE = 75
