from flask import Flask, jsonify, request, send_file
from Capture_Image import get_image_rtsp
from Sending_Image import send_image
import time
import threading
# Khởi tạo Flask app
app = Flask(__name__)


# Dữ liệu mẫu
data = [
    {'id': 1, 'name': 'Item 1', 'description': 'This is item 1'},
    {'id': 2, 'name': 'Item 2', 'description': 'This is item 2'},
]
rtsp_url_cam1 =  "rtsp://admin:S@ms@m00036@192.168.1.227:554/Streaming/Channels/101"
rtsp_url_cam2 =  "rtsp://admin:S@ms@m00036@192.168.1.223:554/Streaming/Channels/101"
rtsp_url_cam3 =  "rtsp://admin:S@ms@m00036@192.168.1.234:554/Streaming/Channels/101"
rtsp_url_cam4 =  "rtsp://admin:S@ms@m00036@192.168.1.226:554/Streaming/Channels/101"
rtsp_url_cam5 =  "rtsp://admin:S@ms@m00036@192.168.1.228:554/Streaming/Channels/101"
rtsp_url_cam6 =  "rtsp://admin:S@ms@m00036@192.168.1.229:554/Streaming/Channels/101"
rtsp_url_cam8 =  "rtsp://admin:S@ms@m00036@192.168.1.235:554/Streaming/Channels/101"
rtsp_url_cam9 =  "rtsp://admin:S@ms@m00036@192.168.1.231:554/Streaming/Channels/101"
def auto_send_image():
  
        # Lấy tên file ảnh đã lưu trong ổ cứng
    rtsp_url= "rtsp://admin:S@ms@m00036@192.168.1.227:554/Streaming/Channels/101"
    object_process_id = 3579
    ret_code, ret_string = get_image_rtsp(rtsp_url)

    if (ret_code == 1):
            # Đường dẫn tới ảnh
            #send_image("C:/Users/ADMINZ/Desktop/DemoSystem/RTSP_Image_Py3/601809.jpg")
            image_path = f"./{ret_string}"
            # Trả về file ảnh
            send_image(image_path,object_process_id)
          #  return send_file(image_path, mimetype='image/jpeg')
    else:
           print("Lỗi")
           
def auto_send_image_2():
      
        # Lấy tên file ảnh đã lưu trong ổ cứng
    rtsp_url= "rtsp://admin:S@ms@m00036@192.168.1.223:554/Streaming/Channels/101"
    object_process_id = 3582
    ret_code, ret_string = get_image_rtsp(rtsp_url)

    if (ret_code == 1):
            # Đường dẫn tới ảnh
            #send_image("C:/Users/ADMINZ/Desktop/DemoSystem/RTSP_Image_Py3/601809.jpg")
            image_path = f"./{ret_string}"
            # Trả về file ảnh
            send_image(image_path,object_process_id)
          #  return send_file(image_path, mimetype='image/jpeg')
    else:
           print("Lỗi")
def auto_send_image_3():
      
        # Lấy tên file ảnh đã lưu trong ổ cứng
    rtsp_url= "rtsp://admin:S@ms@m00036@192.168.1.234:554/Streaming/Channels/101"
    object_process_id = 3585
    ret_code, ret_string = get_image_rtsp(rtsp_url)

    if (ret_code == 1):
            # Đường dẫn tới ảnh
            #send_image("C:/Users/ADMINZ/Desktop/DemoSystem/RTSP_Image_Py3/601809.jpg")
            image_path = f"./{ret_string}"
            # Trả về file ảnh
            send_image(image_path,object_process_id)
          #  return send_file(image_path, mimetype='image/jpeg')
    else:
           print("Lỗi")
def auto_send_image_4():
      
        # Lấy tên file ảnh đã lưu trong ổ cứng
    rtsp_url= "rtsp://admin:S@ms@m00036@192.168.1.226:554/Streaming/Channels/101"
    object_process_id = 3588
    ret_code, ret_string = get_image_rtsp(rtsp_url)

    if (ret_code == 1):
            # Đường dẫn tới ảnh
            #send_image("C:/Users/ADMINZ/Desktop/DemoSystem/RTSP_Image_Py3/601809.jpg")
            image_path = f"./{ret_string}"
            # Trả về file ảnh
            send_image(image_path,object_process_id)
          #  return send_file(image_path, mimetype='image/jpeg')
    else:
           print("Lỗi")     #return jsonify({'error': ret_string}), 404
def auto_send_image_5():
      
        # Lấy tên file ảnh đã lưu trong ổ cứng
    rtsp_url= "rtsp://admin:S@ms@m00036@192.168.1.228:554/Streaming/Channels/101"
    object_process_id = 3588
    ret_code, ret_string = get_image_rtsp(rtsp_url)

    if (ret_code == 1):
            # Đường dẫn tới ảnh
            #send_image("C:/Users/ADMINZ/Desktop/DemoSystem/RTSP_Image_Py3/601809.jpg")
            image_path = f"./{ret_string}"
            # Trả về file ảnh
            send_image(image_path,object_process_id)
          #  return send_file(image_path, mimetype='image/jpeg')
    else:
           print("Lỗi")   
def auto_send_image_6():
      
        # Lấy tên file ảnh đã lưu trong ổ cứng
    rtsp_url= "rtsp://admin:S@ms@m00036@192.168.1.229:554/Streaming/Channels/101"
    object_process_id = 3588
    ret_code, ret_string = get_image_rtsp(rtsp_url)

    if (ret_code == 1):
            # Đường dẫn tới ảnh
            #send_image("C:/Users/ADMINZ/Desktop/DemoSystem/RTSP_Image_Py3/601809.jpg")
            image_path = f"./{ret_string}"
            # Trả về file ảnh
            send_image(image_path,object_process_id)
          #  return send_file(image_path, mimetype='image/jpeg')
    else:
           print("Lỗi")   
def auto_send_image_8():
      
        # Lấy tên file ảnh đã lưu trong ổ cứng
    rtsp_url= "rtsp://admin:S@ms@m00036@192.168.1.235:554/Streaming/Channels/101"
    object_process_id = 3591
    ret_code, ret_string = get_image_rtsp(rtsp_url)

    if (ret_code == 1):
            # Đường dẫn tới ảnh
            #send_image("C:/Users/ADMINZ/Desktop/DemoSystem/RTSP_Image_Py3/601809.jpg")
            image_path = f"./{ret_string}"
            # Trả về file ảnh
            send_image(image_path,object_process_id)
          #  return send_file(image_path, mimetype='image/jpeg')
    else:
           print("Lỗi")  
def auto_send_image_9():
      
        # Lấy tên file ảnh đã lưu trong ổ cứng
    rtsp_url= "rtsp://admin:S@ms@m00036@192.168.1.231:554/Streaming/Channels/101"
    object_process_id = 3594
    ret_code, ret_string = get_image_rtsp(rtsp_url)

    if (ret_code == 1):
            # Đường dẫn tới ảnh
            #send_image("C:/Users/ADMINZ/Desktop/DemoSystem/RTSP_Image_Py3/601809.jpg")
            image_path = f"./{ret_string}"
            # Trả về file ảnh
            send_image(image_path,object_process_id)
          #  return send_file(image_path, mimetype='image/jpeg')
    else:
           print("Lỗi")  
class ThreadJob(threading.Thread):
    def __init__(self,callback,event,interval):
        '''runs the callback function after interval seconds

        :param callback:  callback function to invoke
        :param event: external event for controlling the update operation
        :param interval: time in seconds after which are required to fire the callback
        :type callback: function
        :type interval: int
        '''
        self.callback = callback
        self.event = event
        self.interval = interval
        super(ThreadJob,self).__init__()

    def run(self):
        while not self.event.wait(self.interval):
            self.callback()



event = threading.Event()
k1 = ThreadJob(auto_send_image,event,3600)
k2 = ThreadJob(auto_send_image_2,event,3600)
k3 = ThreadJob(auto_send_image_3,event,3600)
k4 = ThreadJob(auto_send_image_4,event,3600)
k5 = ThreadJob(auto_send_image_5,event,3600)
k6 = ThreadJob(auto_send_image_6,event,3600)
k8 = ThreadJob(auto_send_image_8,event,3600)
k9 = ThreadJob(auto_send_image_9,event,3600)
k1.start()
k2.start()
k3.start()
k4.start()
k5.start()
k6.start()
k8.start()
k9.start()
# def set_interval(func, sec):
#     def func_wrapper():
#         set_interval(func, sec)
#         func()
#     t = threading.Timer(sec, func_wrapper)
#     t.start()
#     time.sleep(10)
# def set_interval(func, interval):
#     stopped = threading.Event()

#     def run():
#         while not stopped.wait(interval):  # sẽ chờ trong khoảng thời gian 'interval'
#             func()

#     threading.Thread(target=run).start()
#     time.sleep(10)
#     return stopped.set  # trả về hàm để dừng lại
# def set_interval(func, interval):
#     def wrapper():
#         while True:
#             func()
#             time.sleep(interval)
#     thread = threading.Thread(target=wrapper)
#     thread.start()
# def set_interval(func, sec):
#     def func_wrapper():
#         set_interval(func, sec)
#         func()
#     t = threading.Timer(sec, func_wrapper)
#     t.start()
#     return t
# set_interval(auto_send_image,120) 
# set_interval(auto_send_image(rtsp_url_cam1,3579),120) 
# set_interval(auto_send_image(rtsp_url_cam2,3582), 3700) 
# set_interval(auto_send_image(rtsp_url_cam3,3585), 3800) 
# set_interval(auto_send_image(rtsp_url_cam4,3588), 3900)
# set_interval(auto_send_image(rtsp_url_cam5,3588), 4000)  
# set_interval(auto_send_image(rtsp_url_cam6,3588), 4100) 
# set_interval(auto_send_image(rtsp_url_cam8,3591), 4200) 
# set_interval(auto_send_image(rtsp_url_cam9,3594), 4300) 

@app.route('/rtspgetimage', methods=['GET'])
def get_image():
    try:
        #Bóc tách json data
        new_item = request.get_json()
        #rtsp_url = "rtsp://"+new_item["rtsp_user"]+":"+new_item["rtsp_pass"]+"@"+new_item["rtsp_ip_port"]+"/rtspgetimage"
        rtsp_url =  "rtsp://admin:S@ms@m00036@192.168.1.227:554/Streaming/Channels/101"
        # Lấy tên file ảnh đã lưu trong ổ cứng
        ret_code, ret_string = get_image_rtsp(rtsp_url)

        if (ret_code == 1):
            # Đường dẫn tới ảnh
            #send_image("C:/Users/ADMINZ/Desktop/DemoSystem/RTSP_Image_Py3/601809.jpg")
            image_path = f"./{ret_string}"
            # Trả về file ảnh
            send_image(image_path,3579)
            return send_file(image_path, mimetype='image/jpeg')
        else:
            return jsonify({'error': ret_string}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 404
# if __name__ == '__main__':
#     app.run(debug=True)