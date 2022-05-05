class GlobalConstant:
    BASE_URL_PROD = 'https://service.raganetwork.com:8801'
    BASE_URL_DEV = 'https://service.raganetwork.com:8802'

    LOCATION_NAME = "测试地点"
    
    DUTY_ATTENDANCE = 1
    TASK_ATTENDANCE = 0

    WORK_ON = 1
    WORK_OFF=0

    OUT_OF_BOUND = 1
    IN_BOUND = 0

    CONTENT_TYPE_FORMDATA = "multipart/form-data"
    CONTENT_TYPE_JSON = "application/json"
    CONTENT_TYPE_COMMON_FORM = "application/x-www-form-urlencoded"

    IMAGES_FOLDER = '.'

    ATTENDANCE_PHOTO_CONTENT_TEMPLATE = 'attendance_photo;time:{}'