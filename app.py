class LineDevice:
    def __init__(self, device_name):
        self.device_name = device_name


class BrakCamera(LineDevice):
    def inspect(self):
        print(f"[{self.device_name}] فحص الكاميرا: التأكد من وجود الغطاء والطباعة (Брак Check)")


class WeightSensor(LineDevice):
    def inspect(self):
        print(f"[{self.device_name}] فحص مستشعر الوزن: التأكد من دقة القياس (Weight Sensor Check)")


cam = BrakCamera("كاميرا الفحص")
sensor = WeightSensor("مستشعر الوزن")
for device in [cam, sensor]:
    device.inspect()