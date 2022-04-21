import requests
import random
import json
import time
import datetime
import pytz
import os

with open('settings.json') as file:
    data = json.load(file)
channel = os.getenv('CHANNEL')
token = os.getenv('TOKEN')
    #sucvat = data["sucvat"]
def sendTime():
    timeSend = datetime.datetime.now(tz=pytz.timezone("Asia/Bangkok"))
    return timeSend.strftime("%d %b %Y %H:%M:%S")

def sendMessage(token, channel, message):
    data = {"content": message}
    url = 'https://discord.com/api/v8/channels/{}/messages'.format(channel)
    headers = {"authorization": token}
    
    requests.post(url, data=data, headers=headers)
    print(f"{sendTime()} [SENT] " + message)
    
while True:
    try:
        messages = ["Trời đất dung hoa, vạn vật sinh sôi", "Con mẹ mày lôi thôi, đầu xanh mỏ đỏ", "Gặm cỏ thay cơm, đầu tóc bờm xờm", "Khạc đờm tung tóe, tao địt con mẹ mày", "Như lồn trâu lồn chó, lồn bó xi măng", "Lồn chằng mạng nhện mà lồn bện là khoai", "Lồn quai lá mít, lồn đít lồn cơm", "Lồn tơm lồn đậm, lồn đười ươi nó địt", "Lồn con vịt nó phang, lồn giang mai lồn ỉa chảy", "Lồn nhảy hiphop, lồn hàng xốp làm hàng hiệu", "Lồn hàng triệu con súc vật, mà tao địt con đĩ mẹ mày", "Đứng từ trên cao, mà lao đầu xuống đất", "Địt lất phất như mưa rơi, địt tơi bởi như bom đạn", "Địt lãng mạn như Romeo và Juliet", "Địt khoét cái lỗ sâu, địt khắp cái lỗ bướm", "Địt đứng tim phổi, địt cặp mắt nai", "Mà địt chai lỗ đít, địt khít cái lỗ lồn", "Con đĩ mẹ mày, mà tao địt con đĩ mẹ mày", "Như gà mái mổ giun, như chó càn cắn dậu", "Thằng cậu mày hiếp dâm, tao bật cái cánh cửa", "Cho con mẹ mày nằm ngửa, bửa nát tử cung", "Khai thông buồng trứng, hứng full tinh trùng", "Địt bồi hồi cảm xúc, địt như bánh đúc ra lò", "Địt như mấy con phò bên hồ Hoàn Kiếm", "Địt như mấy con điếm bên chợ Đồng Xuân", "Địt đằng chân mà lên đằng đầu", "Địt sập cầu sập cống", "Địt con mẹ mày sống", "Địt con mẹ mày chết", "Cho con mẹ mày AIDS" ,"Cho con mẹ mày sida", "Mà tao địt từ Nga, mà qua tới Pháp", "Tao lại địt về Việt Nam mà ra hàng Cỏ", "Và một trăm thằng da đỏ, một nghìn thằng da đen", "Nó lại bem vào cái lỗ lồn con đĩ mẹ mày", "Địt vô đầu gối", "Địt thối màng trinh", "Địt bất thình lình", "Địt kiểu âu tướng", "Địt hướng mặt trời", "Địt chơi địt bời", "Địt ra kiểu mới", "Địt tới địt lui", "Địt búi cả đầu", "Địt đâu cũng chết", "Địt bết cả lồn", "Địt kiểu teo kiểu héo", "Kiểu ngang kiểu dọc", "Kiểu không cần khoa học", "Cũng chọc thủng lồn con đĩ mẹ mày", "Cái thằng đâm cha chém chú", "Bóp vú chị dâu", "Cạo đầu em nhỏ", "Bắn bỏ em trai", "Kì lồn em gái", "Đái ỉa ra sông", "Như công xỉa cánh", "Như đánh chó hoang", "Đập đầu chó thiến", "Chiềng hàng chiềng trại", "Bắn hại chim non", "Đập đầu chim cú", "Bú lồn chim sẻ", "Bẻ lồn chim ri", "Kì lồn chim cắt", "Và đút lồn vào chim trâu", "Địt cái lồn mẹ mày", "Đi với phật thì mặc áo cà sa", "Đi với mà thì mặc áo giấy", "Mà cái lồn con đĩ mẹ mày không đầy chấy thì cũng đầy ve mà giữa cái hột le lại đầy ghẻ mới đẻ ra thằng như mày đúng ko, địt lồn mẹ mày cái thằng súc vật","MỘT VÒNG NỮA NÈ CON CHÓ"]
        for i in messages:
            sendMessage(token, channel, (f"<@{sucvat}>" + " " + i ))
            #sendMessage(token, channel, i)
            time.sleep(random.randint(5, 10))
    except Exception as e:
        print("An error occurred!")
