#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

import config

try:
    APP_ID = config("APP_ID", default=18990697, cast=int)
    API_HASH = config("API_HASH", default="f4815b9a16cb03c2f5eabe8db1cb0903")
    BOT_TOKEN = config("6574755955:AAFr3tBM_bnzpBVWTNFysU1MV5RyKGe_kck")
    DEV = 6651534688
    OWNER = config("6651534688")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset ultrafast -c:v libx265 -crf 27 -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? "{}"',
    )
    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/bdc936caa8040f7645c0c.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
