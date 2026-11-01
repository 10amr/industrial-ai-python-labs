"""
Industrial AI Lab - Quality Inspection System
Module: OOP Polymorphism with Production Line Sensors and Cameras
"""

class BrakCamera:
    def inspect(self) -> None:
        print("كاميرا الفحص: فحص وجود الغطاء والطباعة (Брак Check)")

class WeightSensor:
    def inspect(self) -> None:
        print("حساس الوزن: فحص جرامات العبوة على السير (Weight Check)")

def run_inspection(device) -> None:
    device.inspect()

if __name__ == "__main__":
    cam = BrakCamera()
    sensor = WeightSensor()

    devices = [cam, sensor]
    for dev in devices:
        run_inspection(dev)