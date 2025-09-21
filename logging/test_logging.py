import logging

"""
logging
    root logger를 직접 사용

    # 기본 설정
    logging.StreamHandler() # 로그를 콘솔창에 출력함
    level=logging.WARNING  # WARNING 이상만 출력
    format='%(levelname)s:%(name)s:%(message)s'  # 간단한 형식

logger
    logger = logging.getLogger(__name__)  # 전용 로거 생성

basicConfig
    설정을 명시적으로 변경

    # 예시
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)  # 설정 변경
    logging.

"""

# # root logger 기본 설정 로깅
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# ----------------------------------------------------------

# # 로깅 설정: DEBUG 이상, 시간/레벨/메시지 출력
# logging.basicConfig(
#     level=logging.DEBUG, 
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# # 다양한 레벨의 로그 메시지 출력
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# ----------------------------------------------------------

# # 파일에 로그 저장
# logging.basicConfig(
#     filename='example.log',
#     level=logging.DEBUG, 
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# ----------------------------------------------------------

# custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set the log level to DEBUG to capture all types of log messages

# Create a console handler and set the level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Optionally, create a formatter
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s - %(message)s')

# Set the formatter for the console handler
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)

# Create a file handler, write logs to 'my_app.log'
file_handler = logging.FileHandler('my_app.log')
file_handler.setLevel(logging.DEBUG)

# Set the formatter for the file handler
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# example logging messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
