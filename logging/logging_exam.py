import logging


# 비즈니스 로직 관련 정보 수집 예시
# * 사용자 관련 정보
logger = logging.getLogger(__name__)

def login(user_id, username, ip_address):
    logger.info(
        f"로그인 시도 - 사용자ID: {user_id}, "
        f"사용자명: {username}, IP: {ip_address}"
    )
    
    # 성공/실패 정보
    if authenticate(user_id):
        logger.info(
            f"로그인 성공 - 사용자ID: {user_id}, "
            f"세션ID: {generate_session_id()}"
        )
    else:
        logger.warning(
            f"로그인 실패 - 사용자ID: {user_id}, "
            f"실패 횟수: {get_fail_count(user_id)}"
        )

# * 요청 처리 관련 정보
def process_order(order_data, request_id=None):
    req_id = request_id or generate_request_id()
    
    logger.info(
        f"[{req_id}] 주문 처리 시작 - "
        f"사용자: {order_data['user_id']}, "
        f"상품수량: {len(order_data['items'])}, "
        f"총금액: {order_data['total_amount']}"
    )
    
    # 각 단계별 로깅
    logger.debug(f"[{req_id}] 재고 확인 중...")
    logger.debug(f"[{req_id}] 결제 처리 중...")
    logger.info(f"[{req_id}] 주문 완료 - 주문번호: {order_number}")


# * 리소스 사용량
def log_system_status():
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    logger.info(
        f"시스템 상태 - "
        f"CPU: {cpu_percent}%, "
        f"메모리: {memory.percent}%, "
        f"디스크: {disk.percent}%"
    )
    
    # 임계치 초과 시 경고
    if cpu_percent > 80:
        logger.warning(f"CPU 사용률 높음: {cpu_percent}%")
    
    if memory.percent > 85:
        logger.warning(f"메모리 사용률 높음: {memory.percent}%")


# * 외부 API 호출 정보
def call_external_api(url, data, timeout=30):
    logger.info(f"외부 API 호출 시작 - URL: {url}")
    
    start_time = time.time()
    
    try:
        response = requests.post(url, json=data, timeout=timeout)
        duration = round(time.time() - start_time, 3)
        
        logger.info(
            f"외부 API 응답 - "
            f"상태코드: {response.status_code}, "
            f"응답시간: {duration}초, "
            f"응답크기: {len(response.content)}바이트"
        )
        
        if response.status_code >= 400:
            logger.warning(f"API 오류 응답: {response.text[:200]}")
        
        return response
        
    except requests.Timeout:
        duration = round(time.time() - start_time, 3)
        logger.error(f"API 타임아웃 - {duration}초 경과")
        raise
        
    except Exception as e:
        duration = round(time.time() - start_time, 3)
        logger.error(f"API 호출 실패 - {duration}초, 오류: {e}")
        raise
