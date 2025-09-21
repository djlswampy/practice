import logging

"""
%(asctime)s: 로그가 생성된 시간
%(name)s: 로거 이름 (보통 모듈명)
%(lineno)d: 로그가 호출된 코드의 줄 번호
%(levelname)s: 로그 레벨 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
%(message)s: 실제 로그 메시지
datefmt='%Y-%m-%d %H:%M:%S': 시간 형식 지정
"""
# 포메터 예시 ---------------------
# 상세 포메터
detailed_formatter = logging.Formatter(
    '%(asctime)s | %(name)s:%(lineno)d | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# 간단 포메터
simple_formatter = logging.Formatter(
    '%(levelname)s:%(name)s:%(message)s'
)


# 기본 메타데이터 포맷 --------------
# * 시간 정보
formatter1 = logging.Formatter(
    '%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'  # 2025-09-21 14:30:15
)

formatter2 = logging.Formatter(
    '%(asctime)s - %(message)s',
    datefmt='%Y/%m/%d %I:%M:%S %p'  # 2025/09/21 02:30:15 PM
)

formatter3 = logging.Formatter(
    '%(asctime)s.%(msecs)03d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'  # 2025-09-21 14:30:15.123  (밀리초까지 포함)
)

# * 위치 정보
# 파일과 위치 정보
formatter = logging.Formatter(
    '%(pathname)s:%(lineno)d | %(funcName)s() | %(message)s'
)

# 출력 예시:
# /Users/myproject/services/user_service.py:25 | create_user() | 사용자 생성 시작

# 간단한 파일명만
formatter = logging.Formatter(
    '%(filename)s:%(lineno)d | %(message)s'
)

# 출력 예시:
# user_service.py:25 | 사용자 생성 시작

# * 프로세스/스레드 정보
# 멀티프로세싱/멀티스레딩 환경에서 유용
formatter = logging.Formatter(
    '%(asctime)s | PID:%(process)d | TID:%(thread)d | %(message)s'
)

