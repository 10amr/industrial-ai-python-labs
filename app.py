"""
Industrial AI Lab - Quality Inspection System
Module: OOP & Inheritance for Production Line Sensors and Vision Cameras
"""

class Sensor:
    def __init__(self, line_num: int):
        self.line_num = line_num

    def status(self) -> None:
        print(f"[STATUS] Sensor active on Production Line {self.line_num}")


class BrakCamera(Sensor):
    def detect_brak(self, is_defective: bool) -> None:
        if is_defective:
            print(f"[ALERT] إنذار للـ Наладчик (خط {self.line_num}): تم رصد Брак!")
        else:
            print(f"[OK] Line {self.line_num}: Product passed inspection.")


if __name__ == "__main__":
    cam1 = BrakCamera(line_num=3)
    cam1.status()
    cam1.detect_brak(is_defective=True)