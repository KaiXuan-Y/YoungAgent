"""
全局日志配置模块
在项目启动时调用 setup_logging() 进行一次性配置
之后在任何模块中只需要 import logging; logger = logging.getLogger(__name__) 即可使用
"""

import logging
import sys
from pathlib import Path


def setup_logging(
    level=logging.INFO,
    log_file=None,
    log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    date_format='%Y-%m-%d %H:%M:%S'
):
    """
    配置全局日志
    
    Args:
        level: 日志级别，默认INFO
        log_file: 日志文件路径，如果为None则不写入文件
        log_format: 日志格式
        date_format: 时间格式
    """
    # 创建根logger配置
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    
    # 清除已有的handlers（避免重复配置）
    root_logger.handlers.clear()
    
    # 创建formatter
    formatter = logging.Formatter(log_format, datefmt=date_format)
    
    # 添加控制台handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)
    
    # 如果指定了日志文件，添加文件handler
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)
    
    # 设置第三方库的日志级别（避免过多输出）
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    logging.getLogger('httpx').setLevel(logging.WARNING)
    logging.getLogger('httpcore').setLevel(logging.WARNING)
    
    logging.info("日志系统初始化完成")


def get_logger(name):
    """
    获取logger的便捷方法
    
    Args:
        name: logger名称，通常使用 __name__
        
    Returns:
        logging.Logger对象
    """
    return logging.getLogger(name)

