"""
YoungAgent 项目初始化
在这里进行全局配置，包括日志系统
"""

from .utils.logger import setup_logging
import logging

setup_logging(
    level=logging.INFO,
    log_file='logs/app.log',  # 可选：写入文件
)

